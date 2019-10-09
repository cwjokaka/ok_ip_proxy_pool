from sqlalchemy.exc import IntegrityError

from setting import DB
from src.database.abs_database import AbsDatabase
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from src.entity.proxy_entity import ProxyEntity
from src.enum.common import ProxyCoverEnum
from src.log.logger import logger
import sqlite3

class SqliteOpt(AbsDatabase):

    def __init__(self) -> None:
        engine = create_engine(f'sqlite:///{DB["db_name"]}?check_same_thread=False', echo=True)
        self._DBSession = sessionmaker(bind=engine)

    def add_proxy(self, proxy):
        session = self._DBSession()
        session.add(proxy)
        result = 0
        # 提交即保存到数据库:
        try:
            session.commit()
            result = 1
        except IntegrityError as e:
            logger.info(f'ip: {proxy.url} 已存在')
        finally:
            # 关闭session:
            session.close()
        return result

    def get_all_proxies(self):
        session = self._DBSession()
        try:
            return session.query(ProxyEntity).all()
        except Exception as e:
            logger.exception(e)
        finally:
            session.close()
        return []

    def get_unknown_anonymity_proxies(self):
        session = self._DBSession()
        try:
            return (session.query(ProxyEntity)
                    .filter(ProxyEntity.reliability > 0)
                    .filter(ProxyEntity.proxy_cover == ProxyCoverEnum.UNKNOWN.value)
                    .all())
        except Exception as e:
            logger.exception(e)
        finally:
            session.close()
        return []

    def increase_reliability(self, url):
        conn = self._get_connect()
        cursor = conn.cursor()
        try:
            cursor.execute(f"""
            UPDATE {DB["table_name"]} SET reliability = reliability + 1, 
            last_check_time=datetime(CURRENT_TIMESTAMP,'localtime'),
            check_count = check_count + 1
            WHERE url='{url}'
            """)
            conn.commit()
        except Exception as e:
            pass
            # logger.exception(e)
        finally:
            cursor.close()
            conn.close()

    def reduce_reliability(self, url):
        conn = self._get_connect()
        cursor = conn.cursor()
        try:
            cursor.execute(f"""
            UPDATE {DB["table_name"]} SET reliability = reliability - 1, 
            last_check_time=datetime(CURRENT_TIMESTAMP, 'localtime'),
            check_count = check_count + 1
            WHERE url='{url}'
            """)
            conn.commit()
        except Exception as e:
            pass
            # logger.exception(e)
        finally:
            cursor.close()
            conn.close()

    def remove(self, key):
        return super().remove(key)

    def update_anonymity(self, url, value):
        conn = self._get_connect()
        cursor = conn.cursor()
        try:
            cursor.execute(f"""
            UPDATE {DB["table_name"]} SET proxy_cover = {value}
            WHERE url='{url}'
            """)
            conn.commit()
        except Exception as e:
            logger.exception(e)
        finally:
            cursor.close()
            conn.close()

    def init_db(self):
        conn = self._get_connect()
        cursor = conn.cursor()
        try:
            cursor.execute(f"""
            create table {DB["table_name"]}(
            url varchar(36) not null,
            source varchar(16), 
            supplier varchar(32),
            proxy_type tinyint(3), 
            proxy_cover tinyint(3), 
            check_count int(10), 
            region varchar(36), 
            last_check_time text,
            create_time text default (datetime(CURRENT_TIMESTAMP,'localtime')),
            reliability integer not null default 0 check(reliability >= 0) check(reliability <= 15),
            PRIMARY KEY ("url")
            )
            """)
        except sqlite3.OperationalError as e:
            logger.warn(e)
        finally:
            cursor.close()
            conn.close()

    def clean(self):
        conn = self._get_connect()
        cursor = conn.cursor()
        try:
            cursor.execute(f'DELETE FROM {DB["table_name"]}')
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def get_one_in_page(self):
        session = self._DBSession()
        try:
            return session.query(ProxyEntity).order_by(desc(ProxyEntity.reliability)).first()
        except Exception as e:
            logger.exception(e)
        finally:
            session.close()
        return None

    def get_all_in_page(self):
        session = self._DBSession()
        try:
            return session.query(ProxyEntity).filter(ProxyEntity.reliability > 0).all()
        except Exception as e:
            logger.exception(e)
        finally:
            session.close()
        return None

    def remove_all_zero_reliability(self):
        conn = self._get_connect()
        cursor = conn.cursor()
        try:
            cursor.execute(f"""
            DELETE FROM {DB["table_name"]}
            WHERE reliability = 0
            """)
            conn.commit()
        except sqlite3.OperationalError as e:
            logger.warn(e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def _get_connect():
        return sqlite3.connect(DB['db_name'])


sqlite_opt = SqliteOpt()
