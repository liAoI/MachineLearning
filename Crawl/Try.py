# import requests
# from lxml import etree
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"}
# response = requests.get("https://www.baidu.com",headers = headers)
# response.encoding = "utf-8"
# print(response.text)
#
#
#
# html = etree.HTML(response.text,etree.HTMLParser())
# headFlag = html.xpath("//a[@]")
#
# for head in headFlag:
#     print(head.get('href'))
#     print(head.text)

# result = etree.tostring(html)
#
# print(result)


# print(response.content)