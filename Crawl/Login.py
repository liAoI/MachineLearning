"""
20181119
liao
get mail from 163 mail
"""
import requests
import lxml
from bs4 import BeautifulSoup
import re
name = ""
pwd = ""
url = "http://mail.163.com/"
urlSID = "https://mail.163.com/entry/cgi/ntesdoor?df=mail163_letter&from=web&funcid=loginone&iframe=1&language=-1&passtype=1&product=mail163&net=t&style=-1&race=-2_42_-2_hz"

headers = {
    'Host': "mail.163.com", 'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'Accept-Language': "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3", 'Accept-Encoding': "gzip, deflate, br",
    'Referer': "http://mail.163.com/", 'Connection': "keep-alive"
           }

postData = {
    'savelogin':"0",
    'url2':"http://mail.163.com/errorpage/error163.htm",
    "username":name,
    "password":pwd
}
#https://mail.163.com/app/jifen/wel_js6.jsp?sid=TBjyazFDLCKmQNFtRsDDspPPkdBUePgF&uid=m13659512310@163.com&host=mail.163.com&ver=js6&fontface=yahei&style=1&lang=undefined&skin=skyblue&color=064977&callback=netease.mail.base.Ajax.padding187389375527
response = requests.post(urlSID,postData,headers=headers)
cookies = response.cookies

html = response.content
soup = BeautifulSoup(html,'lxml')

SIDpattern = re.compile('sid=(.*?)&',re.S)
result = re.search(SIDpattern,html.decode('utf-8'))


SID = result.group(1)

MailUrl = "http://mail.163.com/js6/s?sid=%s&func=mbox:listMessages&TopTabReaderShow=1&TopTabLofterShow=1&welcome_welcomemodule_mailrecom_click=1&LeftNavfolder1Click=1&mbox_folder_enter=1"%SID

MailHeaders = { 'Host':"mail.163.com", 'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0", 'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 'Accept-Language':"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3", 'Accept-Encoding':"gzip, deflate, br", 'Referer':"http://mail.163.com/js6/main.jsp?sid=%s&df=mail163_letter"%SID, 'Connection':"keep-alive" }

postData = {
    'savelogin':"0",
    'url2':"http://mail.163.com/",
    "username":name,
    "password":pwd
}
ResponseNow = requests.post(MailUrl,MailHeaders,cookies = cookies)

soup = BeautifulSoup(ResponseNow.content,'lxml')
print(soup)