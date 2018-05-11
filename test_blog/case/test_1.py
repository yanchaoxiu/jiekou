# coding:utf-8
import unittest
import requests
from test_blog.blog.login import Blog
class Test(unittest.TestCase):
    def setUp(self):
        s = requests.session()
        self.blog = Blog(s)
    def test_login(self):
        result = self.blog.login()
        print result
        print type(result)
        print result["success"]
        self.assertEqual(result["success"] , True)
    def test_del(self):
        self.blog.login()
        r2_url = self.blog.save(title="12121", body="WQASDAS")
        pid = self.blog.get_postid(r2_url)
        result = self.blog.del_tie(pid)
        self.assertEqual(result["isSuccess"], True)
if __name__ == "__main__":
    unittest.main()
