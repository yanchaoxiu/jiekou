# coding:utf-8
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
class Blog():
    def __init__(self, s):
        self.s = s
    def login(self):
        url = "https://passport.cnblogs.com/user/signin"
        header = {
            "Cookie":"xxx已省略",
            "X-Requested-With":"XMLHttpRequest",
        }
        json_data = {"input1":"账号",
                     "input2":"密码",
                     "remember": False}
        res = self.s.post(url, headers=header, json=json_data, verify=False)
        result1 = res.content
        print result1
        return res.json()
    def save(self, title, body):
        url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
        d = {"__VIEWSTATE": "",
             "__VIEWSTATEGENERATOR":"FE27D343",
             "Editor$Edit$txbTitle":title,
             "Editor$Edit$EditorBody":"<p>%s</p>" % body,
             "Editor$Edit$Advanced$ckbPublished":"on",
             "Editor$Edit$Advanced$chkDisplayHomePage":"on",
             "Editor$Edit$Advanced$chkComments":"on",
             "Editor$Edit$Advanced$chkMainSyndication":"on",
             "Editor$Edit$lkbDraft":"存为草稿",
             }

        r2 = self.s.post(url2, data=d, verify=False)
        print r2.url
        return r2.url
    def get_postid(self, r2_url):
        import re
        postid = re.findall(r"postid=(.+?)&", r2_url)
        print postid
        print postid[0]
        return postid[0]
    def del_tie(self, postid):
        del_json = {"postId": postid}
        del_url = "https://i.cnblogs.com/post/delete"
        r3 = self.s.post(del_url, json=del_json, verify=False)
        print r3.json()["isSuccess"]
        return r3.json()
if __name__ == "__main__":
    s = requests.session()
    Blog(s).login()
