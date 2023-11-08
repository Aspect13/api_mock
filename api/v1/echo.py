from flask import request

from pylon.core.tools import log
from tools import api_tools, auth, config as c
import random
from time import sleep



class API(api_tools.APIBase):
    url_params = [
        '<int:project_id>',
    ]

    def get(self, project_id: int, **kwargs):
        tts = request.args.get('sleep')
        sc = request.args.get('status_code', 200)
        if tts:
            try:
                sleep(min({float(tts), 10}))
            except ValueError:
                ...
        return {'args': dict(request.args)}, sc

    def post(self, project_id: int, **kwargs):
        tts = request.json.get('sleep')
        sc = request.json.get('status_code', 200)
        if tts:
            try:
                sleep(min({float(tts), 10}))
            except ValueError:
                ...
        return {'args': dict(request.args), 'json': dict(request.json)}, sc

    def put(self, project_id: int, **kwargs):
        tts = request.json.get('sleep')
        sc = request.json.get('status_code', 200)
        if tts:
            try:
                sleep(min({float(tts), 10}))
            except ValueError:
                ...
        return {'args': dict(request.args), 'json': dict(request.json)}, sc

    def delete(self, project_id: int, **kwargs):
        tts = request.json.get('sleep')
        sc = request.json.get('status_code', 200)
        if tts:
            try:
                sleep(min({float(tts), 10}))
            except ValueError:
                ...
        return {'args': dict(request.args), 'json': dict(request.json)}, sc
