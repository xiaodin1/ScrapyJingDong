# -*- coding:utf-8 -*-

from . import api
from flask import jsonify
from datetime import datetime

@api.app_errorhandler(404)
def page_not_found(e):
    return jsonify({'error':str('404')})

@api.route('/',methods=['GET'])
def test_api():
    return jsonify({'status':'successful','time':str(datetime.now())})

@api.route('/scrapyd/',methods=['POST'])
def start_scrapyd(host):
    pass