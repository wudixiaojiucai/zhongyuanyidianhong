from wechat_api.api.base_api import BaseApi


class MemeberApi(BaseApi):

    def add_member(self, userid="1111115", name="asaf", mobile="19923445555", department=[1]):
        url = self.url + "/cgi-bin/user/create"
        data = {"userid": userid,
                "name": name,
                "mobile": mobile,
                "department": department}
        res = self.s.post(url, json=data, verify=False)
        return res.json()

    def get_member_info(self, userid: str):
        url = self.url + "/cgi-bin/user/get"
        data = {"userid": userid}
        res = self.s.get(url, params=data, verify=False)
        return res.json()

    def del_member(self, userid: str):
        url = self.url + "/cgi-bin/user/delete"
        data = {"userid": userid}
        res = self.s.get(url, params=data, verify=False)
        return res.json()


if __name__ == '__main__':
    a = MemeberApi()
    b = a.add_member("1111115", "asaf", "19923445555", [1])
    # b = a.del_member("1111115")
    # b = a.get_member_info("1111115")
    print(b)
