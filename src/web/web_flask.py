from flask import Flask, jsonify

from src.database.sqlite_opt import sqlite_opt

app = Flask(__name__)


@app.route('/')
def index():
    """主页
    """
    return '''
    <h1>Welcome to Home Page😄</h1>
    <h2>APIS:</h2>
    <h3>Get a useable proxy:</h3>
    <p>/get</p>
    <h3>Get all useable proxies:</h3>
    <p>/get_all</p>
    '''


@app.route('/get')
def get_proxy():
    """获取单个代理
    """
    proxy = sqlite_opt.get_one_in_page()
    if proxy:
        return jsonify({
            'code': 200,
            'proxy': proxy.url
        })
    else:
        return jsonify({'code': 500, 'msg': 'server error'})


@app.route('/get_all')
def get_all_proxy():
    """获取全部(可用的)代理
    """
    proxy_list = sqlite_opt.get_all_in_page()
    if proxy_list:
        return jsonify({
            'code': 200,
            'proxies': [proxy.url for proxy in proxy_list]
        })
    else:
        return jsonify({'code': 500, 'msg': 'server error'})
