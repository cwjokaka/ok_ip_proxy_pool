from setting import DB
from src.database.abs_database import AbsDatabase
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.entity.proxy_entity import ProxyEntity


class SqliteOpt(AbsDatabase):

    def __init__(self) -> None:
        engine = create_engine(f'sqlite:///{DB["db_name"]}?check_same_thread=False', echo=True)
        self._DBSession = sessionmaker(bind=engine)

    def set(self, proxy):
        session = self._DBSession()
        session.add(proxy)

        # 提交即保存到数据库:
        session.commit()
        # 关闭session:
        session.close()

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)

    def init_db(self):
        conn = self._get_connect()
        cursor = conn.cursor()
        try:
            cursor.execute(f"""
            create table {DB["table_name"]}(id INTEGER NOT NULL primary key AUTOINCREMENT, 
            ip varchar(20) not null,
            port varchar(5) not null, 
            source varchar(16), supplier varchar(32),
            proxy_type tinyint(3), proxy_cover tinyint(3), check_count int(10), region varchar(20), 
            last_check_time text,
            create_time text default (datetime(CURRENT_TIMESTAMP,'localtime'))
            )
            """)
        except sqlite3.OperationalError as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def _get_connect():
        return sqlite3.connect(DB['db_name'])
        # return conn.cursor()


sqlite_db = SqliteOpt()
