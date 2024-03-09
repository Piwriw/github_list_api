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
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        user = query_params.get('user', [None])[0]  # 获取'user'参数的值，如果不存在则默认为None
        
        data = getdata(user) if user else {"error": "User parameter not provided"}
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return
