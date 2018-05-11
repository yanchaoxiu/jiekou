# # coding:utf-8
# import requests
# r=requests.get('http://www.cnblogs.com/yoyoketang/')
#
# print r.status_code
# print r.text

# # coding:utf-8
# import requests
# par={"Keywords":"yoyoketang"}
# r=requests.get('http://zzk.cnblogs.com/s/blogpost',params=par)
#
# print r.status_code
# print r.text

# # coding:utf-8
# import requests
# r=requests.get('https://www.baidu.com')
#
# print r.url
# print r.encoding
# print r.content
# print r.headers
# print r.cookies

# # coding:utf-8
# import requests
# payload={"yoyo":"hello world",
#      "python":"123456"}
# r=requests.get('http://httpbin.org/post',data=payload)
# print r.text

# # coding:utf-8
# import requests
# url = "https://passport.cnblogs.com/user/signin"
# headers = {
#             "Connection": "keep-alive",
#             "Accept":" application/json, text/javascript, */*; q=0.01",
#             "X-Requested-With": "XMLHttpRequest",
#             "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
#             "Content-Type":"application/json; charset=UTF-8",
#             "Accept-Encoding":"gzip, deflate, br",
#             "Accept-Language":"zh-CN,zh;q=0.9",
#             "Content-Length": "555",
#             "Cookie":"ga=GA1.2.2112917921.1524644257; _gid=GA1.2.2121126762.1524644257; __gads=ID=a815c22a6b679da8:T=1524707820:S=ALNI_MaPWJT7SZJvvOYKE7V5tPQpa60OgQ; _gat=1; SERVERID=34e1ee01aa40e94e2474dffd938824db|1524732993|1524729409; ASP.NET_SessionId=wdu2iripu4pkl3olt3grsygk",
#             }
# payload = {"input1":"U3FhXYsTpgkw4M2vx25nqx5aRk6LVUff//IItucjIOzUPUrLBMD8YeTrblCqbFD3mFCe6odeUZtde+gG221HjwtcmzfVajl02ayrMWXNHVAkK/rUU8ouS2xY8b7kUJWQOyjZHCZgO1bm5zV5DEpVPVpRhmRlyZEMC1Se838jiZk=",
#            "input2":"xxssuJs4K9bqBSyix7xxdM2LFy6ZwFDoX7jT1wsb5OTldp2FAuJ02JwQq6JMPJLNevNAxg8HnKSqBWMm5Tcghejvbz2JT2Jf5K5EAf25KQ7dDhK55TLyGRSyWSbfGDjSjTn9w3duiJYUytvVQsovDtSj9b5ywKI237yz01oMcyY=",
#            "remember":"false",
#            "geetest_challenge":"370f7dac87c63bd842542d1947f37acc",
#            "geetest_validate":"8d1e4e9347d59addbfacdb28437dd6f2",
#            "geetest_seccode":"8d1e4e9347d59addbfacdb28437dd6f2|jordan"
#            }
# r = requests.post(url, json=payload, headers=headers,verify=False)
# print r.json()

# # coding:utf-8
# import requests
# url = "http://localhost:8080/jenkins/j_acegi_security_check"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
# }
# d = {"from": "",
#      "j_password": "f7bcd85ebab14e2fbb6d76cc99bc5c6a",
#      "j_username": "admin",
#      "Jenkins-Crumb": "e677c237181756818cbbccd4296d44f1",
#      "json": {"j_username": "admin",
#               "j_password": "f7bcd85ebab14e2fbb6d76cc99bc5c6a",
#               "remember_me": True,
#               "from": "",
#               "Jenkins-Crumb": "e677c237181756818cbbccd4296d44f1"},
#      "remember_me": "on",
#      "Submit": u"登录"
#      }
# s = requests.session()
# r = s.post(url, headers=headers, data=d)
# print r.content


# # coding:utf-8
# import requests
# # 先打开登录首页，获取部分cookie
# url = "http://localhost:8080/jenkins/j_acegi_security_check"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
# }
# d = {"from": "",
#      "j_password": "123qwe...",
#      "j_username": "yanchaoxiu",
#      "Jenkins-Crumb": "ae38d5c02952195c795b45966497d67d",
#      "json": {"j_username": "yanchaoxiu",
#               "j_password": "123qwe...",
#               "remember_me": True,
#               "from": "",
#               "Jenkins-Crumb": "ae38d5c02952195c795b45966497d67d"},
#      "remember_me": "on",
#      "Submit": u"登录"
#      }
# s = requests.session()
# r = s.post(url, headers=headers, data=d)
# import re
# t = re.findall(r'<b>(.+?)</b>', r.content)
# print t[0]
# print t[1]


# # coding:utf-8
# import requests
# r=requests.get("https://passport.cnblogs.com/user/signin")
# print(r.status_code)


# # coding:utf-8
# import requests
# url = "https://passport.cnblogs.com/user/signin"
# headers = {
#             "Connection": "keep-alive",
#             "Accept":" application/json, text/javascript, */*; q=0.01",
#             "X-Requested-With": "XMLHttpRequest",
#             "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
#             "Content-Type":"application/json; charset=UTF-8",
#             "Accept-Encoding":"gzip, deflate, br",
#             "Accept-Language":"zh-CN,zh;q=0.9",
#             "Content-Length": "555",
#             "Cookie":"ga=GA1.2.2112917921.1524644257; _gid=GA1.2.2121126762.1524644257; __gads=ID=a815c22a6b679da8:T=1524707820:S=ALNI_MaPWJT7SZJvvOYKE7V5tPQpa60OgQ; _gat=1; SERVERID=34e1ee01aa40e94e2474dffd938824db|1524732993|1524729409; ASP.NET_SessionId=wdu2iripu4pkl3olt3grsygk",
#             }
# payload = {"input1":"U3FhXYsTpgkw4M2vx25nqx5aRk6LVUff//IItucjIOzUPUrLBMD8YeTrblCqbFD3mFCe6odeUZtde+gG221HjwtcmzfVajl02ayrMWXNHVAkK/rUU8ouS2xY8b7kUJWQOyjZHCZgO1bm5zV5DEpVPVpRhmRlyZEMC1Se838jiZk=",
#            "input2":"xxssuJs4K9bqBSyix7xxdM2LFy6ZwFDoX7jT1wsb5OTldp2FAuJ02JwQq6JMPJLNevNAxg8HnKSqBWMm5Tcghejvbz2JT2Jf5K5EAf25KQ7dDhK55TLyGRSyWSbfGDjSjTn9w3duiJYUytvVQsovDtSj9b5ywKI237yz01oMcyY=",
#            "remember":"false",
#            "geetest_challenge":"370f7dac87c63bd842542d1947f37acc",
#            "geetest_validate":"8d1e4e9347d59addbfacdb28437dd6f2",
#            "geetest_seccode":"8d1e4e9347d59addbfacdb28437dd6f2|jordan"
#            }
# # r = requests.post(url, json=payload, headers=headers,verify=False)
# # 修改后如下
# s = requests.session()
# r = s.post(url, json=payload, headers=headers)
# print r.json()
#
#
# ur12="https://i.cnblogs.com/EditPosts.aspx?opt=1"
# body = {"__VIEWSTATE": "",
#         "__VIEWSTATEGENERATOR":"FE27D343",
#         "Editor$Edit$txbTitle":"这是我的标题：上海-悠悠",
#         "Editor$Edit$EditorBody":"<p>这里是中文内容：http://www.cnblogs.com/yoyoketang/</p>",
#         "Editor$Edit$Advanced$ckbPublished":"on",
#         "Editor$Edit$Advanced$chkDisplayHomePage":"on",
#         "Editor$Edit$Advanced$chkComments":"on",
#         "Editor$Edit$Advanced$chkMainSyndication":"on",
#         "Editor$Edit$lkbDraft":"存为草稿",
# }
# r2=s.post(ur12,data=body)
# print r.content


# # coding:utf-8
# import requests
# # 先打开登录首页，获取部分cookie
# url = "https://passport.cnblogs.com/user/signin"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
# }
# s = requests.session()
# r = s.get(url, headers=headers,verify=False)
# print s.cookies
# c = requests.cookies.RequestsCookieJar()
# c.set('.CNBlogsCookie', 'F676305594D619B9DB501715765D82EFCE04ED20D7BDF554C70AC02AE091318DF5C1ABE109B24D5B26EC2581EF549E7BA18654A287E750AD711BA5575FA352BEE5B03A8E7A3F732823FF417C67B1BD8BF633F59A')
# c.set('.Cnblogs.AspNetCore.Cookies','CfDJ8Gf3jjv4cttDnEy2UYRcGZ3LjQahJARMHF59tcz5BJR9JAbo07pyup8tYSMw9uTG0uoXc6S2YBjZ-q5klYdRuarZaH25RecVzBqdIdlOvtRWXEWICHhggU6u9KH5ZHSUMvFYNbMclEQMf1uYK_kcq9Uy2N78uHEuyTyjndHpFiYoLYoCJzu0NNLFJx40l9BUoGxUgA1BGY1-o05t63xbsakDryn1yo5GsqsCZfdfjl5ibZ4EV98KfUyu07R4saT8gP7bcNg1nlhNSXrpv66wteAv2I8hz0AKrUwa7BVNmQXF')
# c.set('AlwaysCreateItemsAsActive',"True")
# c.set('AdminCookieAlwaysExpandAdvanced',"True")
# s.cookies.update(c)
# print s.cookies
# r1 = s.get("https://i.cnblogs.com/EditPosts.aspx?opt=1", headers=headers, verify=False)
# url2= "https://i.cnblogs.com/EditPosts.aspx?opt=1"
# body = {"__VIEWSTATE": "",
#         "__VIEWSTATEGENERATOR":"FE27D343",
#         "Editor$Edit$txbTitle":"这是博客主题：上海-悠悠",
#         "Editor$Edit$EditorBody":"<p>这里正文内容：http://www.cnblogs.com/yoyoketang/</p>",
#         "Editor$Edit$Advanced$ckbPublished":"on",
#         "Editor$Edit$Advanced$chkDisplayHomePage":"on",
#         "Editor$Edit$Advanced$chkComments":"on",
#         "Editor$Edit$Advanced$chkMainSyndication":"on",
#         "Editor$Edit$Advanced$txbEntryName":"",
#         "Editor$Edit$Advanced$txbExcerpt":"",
#         "Editor$Edit$Advanced$tbEnryPassword":"",
#         "Editor$Edit$lkbDraft":"存为草稿",
#         }
# r2 =s.post(url2, data=body, verify=False)
# print r.content


# # coding:utf-8
# import requests
# import json
# payload={"yoyo":True,"json":False,"python":"226296743",}
# print type(payload)
# data_json=json.dumps(payload)
# print type(data_json)
# print data_json

# # coding:utf-8
# import requests
# url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
# }
# s = requests.session()
# r = s.get(url, headers=headers,verify=False)
# result = r.json()
# data = result["data"]
# print data
# print data[0]
# get_result = data[0]['context']
# print get_result
# if u"已签收" in get_result:
#     print "快递单已签收成功"
# else:
#     print "未签收"


# # coding:utf-8
# import requests
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
# }
# s=requests.session()
# r=s.get('https://i.cnblogs.com/EditPosts.aspx?opt=1',headers=headers,allow_redirects=False,verify=False)
# print r.status_code

# # coding:utf-8
# import requests
# headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
# }
# s=requests.session()
# r=s.get('https://i.cnblogs.com/EditPosts.aspx?opt=1',headers=headers,allow_redirects=False,verify=False)
# print r.status_code
# new_url=r.headers["Location"]
# print new_url


# # coding:utf-8
# import requests
# url = "https://passport.cnblogs.com/user/signin"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
# }
# s = requests.session()
# r = s.get(url, headers=headers,verify=False)
# print s.cookies
# # 添加登录需要的两个cookie
# c = requests.cookies.RequestsCookieJar()
# c.set('.CNBlogsCookie', 'F676305594D619B9DB501715765D82EFCE04ED20D7BDF554C70AC02AE091318DF5C1ABE109B24D5B26EC2581EF549E7BA18654A287E750AD711BA5575FA352BEE5B03A8E7A3F732823FF417C67B1BD8BF633F59A')
# c.set('.Cnblogs.AspNetCore.Cookies','CfDJ8Gf3jjv4cttDnEy2UYRcGZ3LjQahJARMHF59tcz5BJR9JAbo07pyup8tYSMw9uTG0uoXc6S2YBjZ-q5klYdRuarZaH25RecVzBqdIdlOvtRWXEWICHhggU6u9KH5ZHSUMvFYNbMclEQMf1uYK_kcq9Uy2N78uHEuyTyjndHpFiYoLYoCJzu0NNLFJx40l9BUoGxUgA1BGY1-o05t63xbsakDryn1yo5GsqsCZfdfjl5ibZ4EV98KfUyu07R4saT8gP7bcNg1nlhNSXrpv66wteAv2I8hz0AKrUwa7BVNmQXF')
# c.set('AlwaysCreateItemsAsActive',"True")
# c.set('AdminCookieAlwaysExpandAdvanced',"True")
# s.cookies.update(c)
# print s.cookies
# # -----------登录全部走cookie登录---
# # 第二步：保存草稿
# url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
# body = {"__VIEWSTATE": "",
#         "__VIEWSTATEGENERATOR":"FE27D343",
#         "Editor$Edit$txbTitle":"这是博客主题：上海-悠悠1",
#         "Editor$Edit$EditorBody":"<p>这里正文内容：http://www.cnblogs.com/yoyoketang/</p>",
#         "Editor$Edit$Advanced$ckbPublished":"on",
#         "Editor$Edit$Advanced$chkDisplayHomePage":"on",
#         "Editor$Edit$Advanced$chkComments":"on",
#         "Editor$Edit$Advanced$chkMainSyndication":"on",
#         "Editor$Edit$Advanced$txbEntryName":"",
#         "Editor$Edit$Advanced$txbExcerpt":"",
#         "Editor$Edit$Advanced$tbEnryPassword":"",
#         "Editor$Edit$lkbDraft":"存为草稿",
#         }
# r2 = s.post(url2, data=body, verify=False)
# # 获取当前url地址
# print r2.url
# # 第三步：正则提取需要的参数值
# import re
# postid = re.findall(r"postid=(.+?)&", r2.url)
# print postid
# # 提取为字符串
# print postid[0]
# # 第四步：删除草稿箱
# url3 = "https://i.cnblogs.com/post/delete"
# json3 = {"postId": postid[0]}
# r3 = s.post(url3, json=json3, verify=False)
# print r3.json()


# # coding:utf-8
# import requests
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
#     "Accept": "*/*",
#     "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
#     "Accept-Encoding": "gzip, deflate",
#     "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#     "X-Requested-With": "XMLHttpRequest",
#     "Content-Length": "423",
#     "Connection": "keep-alive"
# }
# body = {"key1": "value1",
#         "key2": "value2"}
# s = requests.session()
# login_url = "http://xxx.login"
# login_ret = s.post(login_url, headers=header, data=body)
# # 这里token在返回的json里，可以直接提取
# token = login_ret.json()["token"]
# # 这是登录后发的一个post请求
# post_url = "http://xxx"
# # 添加token到请求头
# header["token"] = token
# # 如果这个post请求的头部其它参数变了，也可以直接更新
# header["Content-Length"]="9"
# body1 = {
#  "key": "value"
# }
# post_ret = s.post(post_url, headers=header, data=body1)
# print post_ret.content

# # coding:utf-8
# import requests
# # 优惠券列表
# url = 'http://xxx/xxx/coupon/list'
# h = {
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
# "Accept":
# "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
# "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
# "Accept-Encoding": "gzip, deflate",
# "Cookie": "csrfToken=xxx(复制抓包的信息); JSESSIONID=xxx(复制抓包的信息); businessUsername=（用户名）",
# "Connection": "keep-alive"
# }
# r = requests.get(url, headers=h)
# print r.content


# # coding:utf-8
# import requests
# # 主要是post请求后重定向，cookie丢失，所以回到登录页面了
# # 解决办法，禁止重定向，获取重定向的url后，重新发重定向的url地址请求就行了
# # 三个主要参数
# csrfToken = '获取到的csrftoken，一般有有效期的'
# jsessionId = '获取到的jsessionid'
# userName = '用户名'
# url = 'http://xxx/xxxx/update'
# h1 = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#     "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
#     "Accept-Encoding": "gzip, deflate",
#     "Cookie": "csrfToken=%s; JSESSIONID=%s; businessUsername=%s" %(csrfToken, jsessionId, userName),
#     "Connection": "keep-alive",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Content-Length": "115"
# }
# body = {"instantMessageId":"56",
#         "name": u"哈哈1",
#         "order": "",
#         "csrfToken": csrfToken,
#         "type": "qq",
#         "account": "1001"}
# s = requests.session()
# r1 = s.post(url, headers=h1, data=body, allow_redirects=False)
# print r1.status_code
# # 获取重定向的url地址
# redirect_url = r1.headers["Location"]
# print redirect_url
# h2 = {
# "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
# "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
# "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
# "Accept-Encoding": "gzip, deflate",
# "Cookie": "csrfToken=%s; JSESSIONID=%s; businessUsername=%s" % (csrfToken, jsessionId, userName),
# "Connection": "keep-alive"
# }
# r2 = s.get(redirect_url, headers=h2)
# print r2.content


# # coding:utf-8
# import requests
# from requests_toolbelt import MultipartEncoder
# host = 'http://127.0.0.1:81'
# loginUrl = host+"/zentao/user-login.html"
# user="admin"
# psw="e10adc3949ba59abbe56e057f20f883e"
# def login(s,user,psw):
#     h = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#         "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
#         "Accept-Encoding": "gzip, deflate",
#         "Referer": host+"/zentao/user-login.html",
#         "Connection": "keep-alive",
#         "Content-Type": "application/x-www-form-urlencoded",
#     }
#     body = {"account": user,
#             "password": psw,
#             "keepLogin[]": "on",
#             "referer": host+"/zentao/my/"
#             }
#     try:
#         r = s.post(loginUrl, data=body, headers=h)
#         print(r.content)
#         if "/zentao/my/" in r.content:
#             print("登录成功！")
#             return True
#         else:
#             print("登录失败：%s" % r.content)
#             return False
#     except Exception as msg:
#         print("登录失败:%s"%str(msg))
#         return False
# def upload_jpg(s):
#     url1 = host+"/zentao/file-ajaxUpload-5a26aca290b59.html?dir=image"
#     m = MultipartEncoder(fields={"localUrl": (None, "1.png"),"imgFile": ("1.png", open("d:\\1.png", "rb"), "image/png")})
#     try:
#         r1 = s.post(url1, data=m, headers={'Content-Type': m.content_type})
#         jpg_url = r1.json()["url"]
#         return jpg_url
#     except Exception as msg:
#         print("上传失败：%s"%str(msg))
#         return ""
# def submit_bug(s,jpg_url,title="yoyoketang-这是一个带附件的内容"):
#     url2 = host+"/zentao/bug-create-1-0-moduleID=0.html"
#     m = MultipartEncoder(
#         fields = [
#             ("product", "1"),
#             ("module","0"),
#             ("project", ""),
#             ("openedBuild[]", "trunk"),
#             ("assignedTo", "admin"),
#             ("type", "codeerror"),
#             ("os", "all"),
#             ("browser", "all"),
#             ("color", ""),
#             ("title", title),
#             ("severity", "3"),
#             ("pri", "0"),
#             ("steps", u'<p>[步骤]</p>\
#                     <p>1、第一步点</p>\
#                     <p>2、第二步点</p>\
#                     <p>3、点三步点</p>\
#                     <p>[结果]</p>\
#                     <p><img src="%s" alt="" /></p>\
#                     <p>[期望]</p>' % jpg_url),
#             ("story", "0"),
#             ("task", "0"),
#             ("mailto[]", ""),
#             ("keywords", ""),
#             ("files[]", ("1.png", open("d:\\1.png", "rb"), "image/png")),
#             ("labels[]", "tu1"),
#             ("files[]", ("2.png", open("d:\\2.png", "rb"), "image/png")),
#             ("labels[]", "tu2"),
#             ("uid", "5a2955c884f98"),
#             ("case", "0"),
#             ("caseVersion", "0"),
#             ("result", "0"),
#             ("testtask", "0")])
#     try:
#         r2 = s.post(url2, data=m, headers={'Content-Type': m.content_type})
#         print(r2.content)
#     except Exception as msg:
#         print("提交BUG失败：%s" % str(msg))
# if __name__ == "__main__":
#     s = requests.session()
#     login(s, user, psw)
#     jpg = upload_jpg(s)
#     submit_bug(s, jpg, title="yoyoketang-这是一个带附件的内容")



# import unittest
#
#
# class IntegerArithmeticTestCase(unittest.TestCase):
#     def testAdd(self):  ## test method names begin 'test*'
#         self.assertEqual((1 + 2), 3)
#         self.assertEqual(0 + 1, 1)
#
#     def testMultiply(self):
#         self.assertEqual((0 * 10), 0)
#         self.assertEqual((5 * 8), 40)
#
#     def testMinus(self):
#         result=6-5
#         hope=1
#         self.assertEqual(result,hope)
#
#     def testDivide(self):
#         result = 7/2
#         hope = 3.5
#         self.assertEqual(result, hope)
#
# if __name__ == '__main__':
#     unittest.main()
#

# # coding:utf-8
# import unittest
# class Test(unittest.TestCase):
#     def test01(self):
#         a = 1
#         b = 1
#         self.assertEqual(a, b)
#     def test02(self):
#         a = "hello"
#         b = "hello world!"
#         self.assertIn(a, b)
#     def test03(self):
#         a = True
#         self.assertTrue(a)
#     def test04(self):
#         a = "上海-悠悠"
#         b = "yoyo"
#         self.assertEqual(a, b,msg="失败原因：%s !=%s"%(a,b))
# if __name__ == "__main__":
#     unittest.main()

# # coding:utf-8
# import unittest
# import requests
# class Test_Kuaidi(unittest.TestCase):
#     def setUp(self):
#         self.headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
#         }
#     def test_yunda(self):
#         danhao = '1202247993797'
#         kd = 'yunda'
#         self.url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html" %(danhao, kd)
#         print(self.url)
#         r = requests.get(self.url, headers=self.headers, verify=False)
#         result = r.json()
#         print(result['company'])
#         data = result["data"]
#         print(data[0])
#         get_result = data[0]['context']
#         print(get_result)
#         self.assertEqual(u"韵达快递", result['company'])
#         self.assertIn(u"已签收", get_result)
#     def test_tiantian(self):
#         danhao = '631963354105'
#         kd = 'zhongtong'
#         self.url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html" %(danhao,kd)
#         print(self.url)
#         r = requests.get(self.url, headers=self.headers, verify=False)
#         result = r.json()
#         print(result['company'])
#         data = result["data"]
#         print(data[0])
#         get_result = data[0]['context']
#         print(get_result)
#         self.assertEqual(u"中通快递", result['company'])
#         self.assertIn(u"签收", get_result)
# if __name__ == "__main__":
#     unittest.main()


# # coding:utf-8
# import unittest
# import requests
# class Test_Kuaidi(unittest.TestCase):
#     def setUp(self):
#         self.headers = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
#         }
#     def chaxun_kuaidi(self, danhao, kd, kd_name):
#         self.url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html" %(danhao, kd)
#         print(self.url)
#         r = requests.get(self.url, headers=self.headers, verify=False)
#         result = r.json()
#         print(result['company'])
#         data = result["data"]
#         print(data[0])
#         get_result = data[0]['context']
#         print(get_result)
#         self.assertEqual(kd_name, result['company'])
#         self.assertIn(u"签收", get_result)
#     def test_yunda(self):
#         danhao = '1202247993797'
#         kd = 'yunda'
#         kd_name = u"韵达快递"
#         self.chaxun_kuaidi(danhao, kd, kd_name)
#     def test_tiantian(self):
#         danhao = '631963354105'
#         kd = 'zhongtong'
#         kd_name =u"中通快递"
#         self.chaxun_kuaidi(danhao, kd, kd_name)
#
# if __name__ == "__main__":
#     unittest.main()


# # coding:utf-8
# import unittest
# import requests
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# username="yanchaoxiu"
# psw="123qwe..."
# reme=True
# class Blog_login(unittest.TestCase):
#
#     def login(self, username, psw, reme=True):
#         url = "https://passport.cnblogs.com/user/signin"
#         header = {
#             "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
#             "Cookie": "_ga=GA1.2.2112917921.1524644257; __gads=ID=a815c22a6b679da8:T=1524707820:S=ALNI_MaPWJT7SZJvvOYKE7V5tPQpa60OgQ; ASP.NET_SessionId=qegr1uixfuf0g4a31uzwch1w; SERVERID=34e1ee01aa40e94e2474dffd938824db|1524883234|1524883233",
#             "X-Requested-With": "XMLHttpRequest",
#             "Connection": "keep-alive",
#             "Content-Length": "557"
#         }
#         json_data = {"input1": username,
#                      "input2": psw,
#                      "remember": reme}
#         res = requests.post(url, headers=header, json=json_data, verify=False)
#         result1 = res.content
#         print result1
#         return res.json()
#     def test_login1(self):
#         # username = "NfFJYEkzpmK0ex+GDD88OZneHAchG2/pZJE5WF3UgtrIEi1Sn4N4Ix/WsDPjKZCiGLDrn+4C1qiKTXdAEFjcYHC/fdU+N/lRlk5MzQfFoywRyaq0ibAfsVUdiXLEvvpwvp+0PPikuMk3eq9bOvSBHP8821GT5wJz11UxFnQmyUY="
#         # psw = "xQam1r8J9qNkzO08REX5mBH+6c4EJugD39VqEG0jXgiHnSJ/Tx4i9btE7LyOaQe3EVTHOa1AvbCYYAsjjLZNzttzIVXbtHt7XOuO8hPFKA5gQ0JMc17hZu9ygVk2TO8iyE23J6kNuwOATPtkh+Nz3e6qVEUz0d1lh6O3QS0JjyM="
#         result = self.login(username, psw)
#         self.assertEqual(result["success"], True)
#     def test_login2(self):
#         username = "正确账号"
#         psw = "xxx错误密码"
#         result = self.login(username, psw)
#         self.assertEqual(result["success"], False)
# if __name__ == "__main__":
#     unittest.main()


# # coding:utf-8
# import unittest
# def all_case():
#     case_dir = "D:\\test\\yoyotest\\case"
#     testcase = unittest.TestSuite()
#     discover = unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)
#     testcase.addTests(discover)
#     print(testcase)
#     return testcase
# if __name__ == "__main__":
#     runner = unittest.TextTestRunner()
#     runner.run(all_case())

# # coding:utf-8
# import requests
# def login(s, url, payload):
#     headers = {"Accept": "application/json, text/javascript, */*; q=0.01",
#                "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
#                "Accept-Encoding": "gzip, deflate, br",
#                "Content-Type": "application/json; charset=utf-8",
#                "X-Requested-With": "XMLHttpRequest",
#                "Connection": "keep-alive",
#                "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
#                "Cookie":"_ga=GA1.2.2112917921.1524644257; __gads=ID=a815c22a6b679da8:T=1524707820:S=ALNI_MaPWJT7SZJvvOYKE7V5tPQpa60OgQ; ASP.NET_SessionId=qegr1uixfuf0g4a31uzwch1w; SERVERID=34e1ee01aa40e94e2474dffd938824db|1524883234|1524883233",
#                "Content-Length": "557"
#                }
#     r = s.post(url, json=payload, headers=headers, verify=False)
#     result = r.json()
#     print result
#     return result['success']
# def save_box(s, url2, title, body_data):
#     body = {"__VIEWSTATE": "",
#             "__VIEWSTATEGENERATOR": "FE27D343",
#             "Editor$Edit$txbTitle": title,
#             "Editor$Edit$EditorBody": "<p>"+body_data+"</p>",
#             "Editor$Edit$Advanced$ckbPublished": "on",
#             "Editor$Edit$Advanced$chkDisplayHomePage": "on",
#             "Editor$Edit$Advanced$chkComments": "on",
#             "Editor$Edit$Advanced$chkMainSyndication": "on",
#             "Editor$Edit$lkbDraft": "存为草稿",
#             }
#     r2 = s.post(url2, data=body, verify=False)
#     print r2.url
#     return r2.url
# def get_postid(u):
#     import re
#     postid = re.findall(r"postid=(.+?)&", u)
#     print postid
#     if len(postid) < 1:
#         return ''
#     else:
#         return postid[0]
# def delete_box(s,url3, postid):
#     json3 = {"postId": postid}
#     r3 = s.post(url3, json=json3, verify=False)
#     print r3.json()
# if __name__ == "__main__":
#     url = "https://passport.cnblogs.com/user/signin"
#     payload = {
#         "input1": "xxx",
#         "input2": "xxx",
#         "remember": True
#     }
#     s = requests.session()
#     login(s, url, payload)
#     url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
#     u = save_box(s, url2, "标题", "正文内容")
#     postid = get_postid(u)
#     url3 = "https://i.cnblogs.com/post/delete"
#     delete_box(s, url3, postid)


# # coding:utf-8
# from bs4 import BeautifulSoup
# import requests
# r = requests.get("http://www.cnblogs.com/yoyoketang/")
# # 请求首页后获取整个html界面
# blog = r.content
# # print blog
# # 用html.parser解析html
# soup = BeautifulSoup(blog, "html.parser")
# # 获取所有的class属性为dayTitle，返回Tag类
# times = soup.find_all(class_="dayTitle")
# # for i in times:
# #     print i.a.string  # 获取a标签的文本
# title = soup.find_all(class_="postTitle")
# # for i in title:
# #     print i.a.string
# # 读取摘要内容
# descs = soup.find_all(class_="postCon")
# # for i in descs:
# #     # tag的 .contents 属性可以将tag的子节点以列表的方式输出
# #     c = i.div.contents[0]  # 取第一个
# #     print c
# for i, j, k in zip(times,title,descs):
#     print i.a.string
#     print j.a.string
#     print k.div.contents[0]
#     print ""

# # coding:utf-8
# from bs4 import BeautifulSoup
# y=open("1.html")
# print y.read()

# # coding:utf-8
# from bs4 import BeautifulSoup
# y=open("1.html")
# soup=BeautifulSoup(y,"html.parser")
# print soup.prettify()


# # coding:utf-8
# from bs4 import BeautifulSoup
# y=open("1.html")
# soup=BeautifulSoup(y,"html.parser")
# print soup.prettify()
# print type(soup)
# tag=soup.title
# print type(tag)
# string=tag.string
# print type(string)
# comment=soup.b.string
# print type(comment)


# # coding:utf-8
# from bs4 import BeautifulSoup
# y=open("1.html")
# soup=BeautifulSoup(y,"html.parser")
# tag1=soup.head
# print type(tag1)
# tag2=soup.title
# print tag2
# tag3=soup.a
# print tag3

# # coding:utf-8
# from bs4 import BeautifulSoup
# y=open("1.html")
# soup=BeautifulSoup(y,"html.parser")
# tag1=soup.head
# print tag1.name
# tag2=soup.title
# print tag2.name
# tag3=soup.a
# print tag3.name

# # coding:utf-8
# from bs4 import BeautifulSoup
# import requests
# r = requests.get("https://www.qiushibaike.com/")
# qiubai = r.content
# soup = BeautifulSoup(qiubai, "html.parser")
# duanzi = soup.find_all(class_="content")
# for i in duanzi:
#     duan = i.span.contents[0]
#     print duan

# from bs4 import BeautifulSoup
# import requests
# import os
# r = requests.get("http://699pic.com/sousuo-218808-13-1.html")
# fengjing = r.content
# soup = BeautifulSoup(fengjing, "html.parser")
# # 找出所有的标签
# images = soup.find_all(class_="lazy")
# # print images # 返回list对象
# for i in images:
#     jpg_rl = i["data-original"]
#     title = i["title"]
#     print title
#     print jpg_rl
#     print ""

# # coding:utf-8
# from bs4 import BeautifulSoup
# import requests
# import os
# r = requests.get("http://699pic.com/sousuo-218808-13-1.html")
# fengjing = r.content
# soup = BeautifulSoup(fengjing, "html.parser")
# # 找出所有的标签
# images = soup.find_all(class_="lazy")
# # print images # 返回list对象
# for i in images:
#     try:
#         jpg_rl = i["data-original"]
#         title = i["title"]
#         print title
#         print jpg_rl
#         print ""
#         with open(os.getcwd()+"\\jpg\\"+title+'.jpg', "wb") as f:
#             f.write(requests.get(jpg_rl).content)
#     except:
#         pass

# # coding:utf-8
# from bs4 import BeautifulSoup
# import requests
# r = requests.get("http://www.cnblogs.com/yoyoketang/")
# # 请求首页后获取整个html界面
# blog = r.content
# # 用html.parser解析html
# soup = BeautifulSoup(blog, "html.parser")
# # find方法查找页面上第一个属性匹配的tag对象
# tag_soup = soup.find(class_="c_b_p_desc")
# # len函数获取子节点的个数
# print len(tag_soup.contents)
# for i in tag_soup.contents:
#     print i
# print tag_soup.contents[0]
# print tag_soup.contents[1]


# # coding:utf-8
# from bs4 import BeautifulSoup
# import requests
# r = requests.get("http://www.cnblogs.com/yoyoketang/")
# # 请求首页后获取整个html界面
# blog = r.content
# # 用html.parser解析html
# soup = BeautifulSoup(blog, "html.parser")
# # find方法查找页面上第一个属性匹配的tag对象
# tag_soup = soup.find(class_="c_b_p_desc")
# print tag_soup.children
# for i in tag_soup.children:
#     print i

# # coding:utf-8
# from bs4 import BeautifulSoup
# import requests
# r = requests.get("http://www.cnblogs.com/yoyoketang/")
# # 请求首页后获取整个html界面
# blog = r.content
# # 用html.parser解析html
# soup = BeautifulSoup(blog, "html.parser")
# # find方法查找页面上第一个属性匹配的tag对象
# tag_soup = soup.find(class_="c_b_p_desc")
# # len函数获取子节点的个数
# print len(list(tag_soup.children))
# # 获取子孙节点的个数
# print len(list(tag_soup.descendants))
# for i in tag_soup.descendants:
#     print i



# # coding:utf-8
# from bs4 import BeautifulSoup
# import requests
# r = requests.get("http://www.cnblogs.com/yoyoketang/mvc/blog/sidecolumn.aspx?blogApp=yoyoketang")
# # 请求首页后获取整个html界面
# blog = r.content
# # 用html.parser解析html
# soup = BeautifulSoup(blog, "html.parser")
# tag_soup = soup.find(class_="catListTag")
# # print body.prettify()
# ul_soup = tag_soup.find_all("a")
# print ul_soup
# for i in ul_soup:
#     print i.string



# # coding:utf-8
# import xlrd
# data = xlrd.open_workbook('test.xlsx')
# # table = data.sheets()[0]
# # table = data.sheet_by_index(0)
# table = data.sheet_by_name(u'Sheet1')
# nrows = table.nrows
# ncols = table.ncols
# print table.row_values(0)
# print table.col_values(0)


# # coding:utf-8
# import xlrd
# class ExcelUtil():
#     def __init__(self, excelPath, sheetName):
#         self.data = xlrd.open_workbook(excelPath)
#         self.table = self.data.sheet_by_name(sheetName)
#         self.keys = self.table.row_values(0)
#         self.rowNum = self.table.nrows
#         self.colNum = self.table.ncols
#     def dict_data(self):
#         if self.rowNum <= 1:
#             print("总行数小于1")
#         else:
#             r = []
#             j=1
#             for i in range(self.rowNum-1):
#                 s = {}
#                 values = self.table.row_values(j)
#                 for x in range(self.colNum):
#                     s[self.keys[x]] = values[x]
#                     r.append(s)
#                     j+=1
#                     return r
# if __name__ == "__main__":
#     # filepath = "D:\\test1\\web-project\\5ke\\testdata.xlsx"
#     filepath = "test.xlsx"
#     sheetName = "Sheet1"
#     data = ExcelUtil(filepath, sheetName)
#     print data.dict_data()



# # coding:utf-8
# import logging, time, os
# # 这个是日志保存本地的路径
# # log_path = "D:\\test\\newp\\report"
# log_path = "D:\\jiekouzidonghua\\report"
# class Log:
#     def __init__(self):
#         self.logname = os.path.join(log_path, '%s.log'%time.strftime('%Y_%m_%d'))
#         self.logger = logging.getLogger()
#         self.logger.setLevel(logging.DEBUG)
#         self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')
#     def __console(self, level, message):
#         fh = logging.FileHandler(self.logname, 'a')
#         fh.setLevel(logging.DEBUG)
#         fh.setFormatter(self.formatter)
#         self.logger.addHandler(fh)
#         ch = logging.StreamHandler()
#         ch.setLevel(logging.DEBUG)
#         ch.setFormatter(self.formatter)
#         self.logger.addHandler(ch)
#         if level == 'info':
#             self.logger.info(message)
#         elif level == 'debug':
#             self.logger.debug(message)
#         elif level == 'warning':
#             self.logger.warning(message)
#         elif level == 'error':
#             self.logger.error(message)
#             self.logger.removeHandler(ch)
#             self.logger.removeHandler(fh)
#             fh.close()
#     def debug(self, message):
#             self.__console('debug', message)
#     def info(self, message):
#             self.__console('info', message)
#     def warning(self, message):
#             self.__console('warning', message)
#     def error(self, message):
#             self.__console('error', message)
# if __name__ == "__main__":
#     log = Log()
#     log.info("---测试开始----")
#     log.info("输入密码")
#     log.warning("----测试结束----")


# # coding:utf-8
# import smtplib
# from email.mime.text import MIMEText
# # ----------1.跟发件相关的参数------
# smtpserver = "smtp.163.com"
# port = 0
# sender = "yanchaoxiu@163.com"
# psw = "123qwe"
# receiver = "yanchaoxiu@163.com"
# # ----------2.编辑邮件的内容------
# subject = "主题yanchaoxiu"
# body = '<p>woaini</p>'
# msg = MIMEText(body, "html", "utf-8")
# msg['from'] = sender
# msg['to'] = "yanchaoxiu@163.com"
# msg['subject'] = subject
# # ----------3.发送邮件------
# smtp = smtplib.SMTP()
# smtp.connect(smtpserver)
# smtp.login(sender, psw)
# smtp.sendmail(sender, receiver, msg.as_string())
# smtp.quit()


# # coding:utf-8
# import smtplib
# from email.mime.text import MIMEText
# # ----------1.跟发件相关的参数------
# smtpserver = "smtp.qq.com"
# port = 465
# sender = "1822107818@qq.com"
# psw = "wzoaohvxgfsjfdfj"
# receiver = "1822107818@qq.com"
# # ----------2.编辑邮件的内容------
# subject = "这个是主题QQ"
# body = '<p>这个是发送的QQ邮件</p>'
# msg = MIMEText(body, "html", "utf-8")
# msg['from'] = sender
# msg['to'] = "1822107818@qq.com"
# msg['subject'] = subject
# smtp = smtplib.SMTP_SSL(smtpserver, port)
# smtp.login(sender, psw)
# smtp.sendmail(sender, receiver, msg.as_string())
# smtp.quit()


# # coding:utf-8
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# # ----------1.跟发件相关的参数------
# smtpserver = "smtp.163.com"
# port = 0
# sender = "yanchaoxiu@163.com"
# psw = "123qwe"
# receiver = "1822107818@qq.com"
# # ----------2.编辑邮件的内容------
# # 读文件
# file_path = "1.html"
# with open(file_path, "rb") as fp:
#     mail_body = fp.read()
#     msg = MIMEMultipart()
#     msg["from"] = sender
#     msg["to"] = receiver
#     msg["subject"] = "这个我的主题"
#     body = MIMEText(mail_body, "html", "utf-8")
#     msg.attach(body)
#     att = MIMEText(mail_body, "base64", "utf-8")
#     att["Content-Type"] = "application/octet-stream"
#     att["Content-Disposition"] = 'attachment; filename="test_report.html"'
#     msg.attach(att)
# # ----------3.发送邮件------
# try:
#     smtp = smtplib.SMTP()
#     smtp.connect(smtpserver)
#     smtp.login(sender, psw)
# except:
#     smtp = smtplib.SMTP_SSL(smtpserver, port)
#     smtp.login(sender, psw)
# smtp.sendmail(sender, receiver, msg.as_string())
# smtp.quit()



# # coding:utf-8
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# # ----------1.跟发件相关的参数------
# smtpserver = "smtp.163.com"
# port = 0
# sender = "yanchaoxiu@163.com"
# psw = "123qwe"
# receiver = ["1126492944@qq.com","1822107818@qq.com"]
# file_path = "D:\\test1\\yoyotest\\report\\result.html"
# with open(file_path, "rb") as fp:
#     mail_body = fp.read()
#     msg = MIMEMultipart()
#     msg["from"] = sender
#     msg["to"] = ";".join(receiver)
#     msg["subject"] = "严朝秀我爱你"
#     body = MIMEText(mail_body, "html", "utf-8")
#     msg.attach(body)
#     att = MIMEText(mail_body, "base64", "utf-8")
#     att["Content-Type"] = "application/octet-stream"
#     att["Content-Disposition"] = 'attachment; filename="ttt_report.html"'
#     msg.attach(att)
# try:
#     smtp = smtplib.SMTP()
#     smtp.connect(smtpserver)
#     smtp.login(sender, psw)
# except:
#     smtp = smtplib.SMTP_SSL(smtpserver, port)
#     smtp.login(sender, psw)
# smtp.sendmail(sender, receiver, msg.as_string())
# smtp.quit()


# # coding:utf-8
# import logging, time
# import os
# cur_path = os.path.dirname(os.path.realpath(__file__))
# log_path = os.path.join(os.path.dirname(cur_path), 'D:\\jiekouzidonghua\\logs')
#
# def mkdir(path):
#     path = path.strip()
#     path = path.rstrip("\\")
#     isExists = os.path.exists(path)
#     if not isExists:
#         os.makedirs(path)
#         print path + ' 创建成功'
#         return True
#     else:
#         print path + ' 目录已存在'
#         return False
# mkdir(log_path)
# # mkpath = "d:\\qttc\\web\\"
# # mkdir(mkpath)
# # if not os.path.exists(log_path):
# #     os.mkdir(log_path)
# class Log():
#     def __init__(self):
#         self.logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
#         self.logger = logging.getLogger()
#         self.logger.setLevel(logging.DEBUG)
#         self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')
#     def __console(self, level, message):
#         fh = logging.FileHandler(self.logname, 'a')
#         fh.setLevel(logging.DEBUG)
#         fh.setFormatter(self.formatter)
#         self.logger.addHandler(fh)
#         ch = logging.StreamHandler()
#         ch.setLevel(logging.DEBUG)
#         ch.setFormatter(self.formatter)
#         self.logger.addHandler(ch)
#         if level == 'info':
#             self.logger.info(message)
#         elif level == 'debug':
#             self.logger.debug(message)
#         elif level == 'warning':
#             self.logger.warning(message)
#         elif level == 'error':
#             self.logger.error(message)
#             self.logger.removeHandler(ch)
#             self.logger.removeHandler(fh)
#             fh.close()
#     def debug(self, message):
#         self.__console('debug', message)
#     def info(self, message):
#         self.__console('info', message)
#     def warning(self, message):
#         self.__console('warning', message)
#     def error(self, message):
#         self.__console('error', message)
# if __name__ == "__main__":
#     log = Log()
#     log.info("---测试开始----")
#     log.info("操作步骤1,2,3")
#     log.warning("----测试结束----")



# coding:utf-8
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time
# firefox浏览器配置文件地址
profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\h6b7grdr.default'
s = requests.session()
url = "https://home.cnblogs.com/u/yoyoketang"
def get_cookies(url):
    try:
        profile = webdriver.FirefoxProfile(profile_directory)
        driver = webdriver.Firefox(profile)
        driver.get(url+"/followers")
        time.sleep(3)
        cookies = driver.get_cookies()
        print(cookies)
        driver.quit()
        return cookies
    except Exception as msg:
        print(u"启动浏览器报错了：%s" %str(msg))
def add_cookies(cookies):
    try:
        c = requests.cookies.RequestsCookieJar()
        for i in cookies:
            c.set(i["name"], i['value'])
            s.cookies.update(c)
    except Exception as msg:
        print(u"添加cookies的时候报错了：%s" % str(msg))
def get_ye_nub(url):
    try:
        r1 = s.get(url+"/relation/followers")
        soup = BeautifulSoup(r1.content, "html.parser")
        fensinub = soup.find_all(class_="current_nav")
        print(fensinub[0].string)
        num = re.findall(u"我的粉丝\((.+?)\)", fensinub[0].string)
        print len(num)
        print(u"我的粉丝数量：%s"%str(num[0]))
        ye = int(int(num[0])/45)+1
        print len(ye)
        print(u"总共分页数：%s"%str(ye))
        return ye
    except Exception as msg:
        print(u"获取粉丝页数报错了，默认返回数量1 ：%s"%str(msg))
        return 1
def save_name(nub):
    try:
        if nub <= 1:
            url_page = url+"/relation/followers"
        else:
            url_page = url+"/relation/followers?page=%s" % str(nub)
            print(u"正在抓取的页面：%s" %url_page)
            r2 = s.get(url_page, verify=False)
            soup = BeautifulSoup(r2.content, "html.parser")
            fensi = soup.find_all(class_="avatar_name")
            for i in fensi:
                name = i.string.replace("\n", "").replace(" ","")
                print(name)
                with open("name.txt", "a") as f:
                    f.write(name.encode("utf-8")+"\n")
    except Exception as msg:
        print(u"抓取粉丝名称过程中报错了 ：%s"%str(msg))
if __name__ == "__main__":
    cookies = get_cookies(url)
    add_cookies(cookies)
    n = get_ye_nub(url)
    for i in list(range(1, n+1)):
        save_name(i)
