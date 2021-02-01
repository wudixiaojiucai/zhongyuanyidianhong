import pytest

from wechat_api.api.member_api import MemeberApi


class TestGetMember:

    def setup_class(self):
        self.mb = MemeberApi()
        self.mb.add_member()

    @pytest.mark.parametrize("tmp", range(50))
    def test_get_member(self, tmp):
        res = self.mb.get_member_info("1111115")
        assert res.get("userid") == "1111115"

    def teardown_class(self):
        self.mb.del_member("1111115")
