import requests
import urllib3


class BaseApi:

    def __init__(self):
        urllib3.disable_warnings()
        self.s = requests.Session()
        self.url = "https://qyapi.weixin.qq.com"
        self.s.params["access_token"] = self.get_token()

    def get_token(self, corpid=None, corpsecret=None):
        if corpid is None:
            corpid = "wwf455935108d79648"
        if corpsecret is None:
            corpsecret = "tbLnjwlgSgaeiL8dKhXDE-_qGdpEJ3feP7yjO362b-c"
        url = self.url + "/cgi-bin/gettoken"
        data = {"corpid": corpid,
                "corpsecret": corpsecret}

        res = self.s.get(url, params=data, verify=False)
        return res.json().get("access_token")


if __name__ == '__main__':
    a = BaseApi()
    print(a.get_token())
