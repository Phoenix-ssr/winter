from flask import render_template
from app import app
import requests
import re
url = 'https://www.hqu.edu.cn/hdxw.htm'
response = requests.get(url)
response.encoding ='utf-8'
html = response.text
content = re.findall(r'<tr id="line_u15_0">.*?<span id="section_u15_24" style="display:none;">',html,re.S)[0]
content2_url= re.findall(r'href="(.*?)" ',content,re.S)
content_title=re.findall(r'<font color="">(.*?)<',content,re.S)
post=[]
a=0
for content2_url in content2_url:
     post.append({'url':'https://www.hqu.edu.cn/%s' % content2_url,'title':content_title[a]})
     a=a+1
    
@app.route('/')
def index():
	return render_template('index.html',post=post)
