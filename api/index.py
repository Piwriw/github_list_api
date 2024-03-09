# -*- coding: UTF-8 -*-
import requests
import re
import json
from http.server import BaseHTTPRequestHandler
from bs4 import BeautifulSoup

def github_json(user,repo,branch):
    if user =='':
        result = 'The user cannot be none!'
    else:
        try:
            if repo =='':
                repo = 'friends'
            if branch =='':
                branch = 'master'
            requests_path = 'https://github.com/' + user + '/' +repo + '/blob/'+branch+'/friendlist.json'
            r = requests.get(requests_path)
            r.encoding = 'utf-8'
            gitpage = r.text
            soup = BeautifulSoup(gitpage, 'html.parser')
            main_content = soup.find('td',id = 'LC1').text
            result = json.loads(main_content)
        except:
            result = 'Incorrect user parameter!Please check!'
    return result
    
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 2024-02-21 固定用户名 https://github.com/Zfour/python_github_calendar_api/issues/20
        # path = self.path
        # user = path.split('?')[1]
        user = 'piwriw'
        data = getdata(user)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return
