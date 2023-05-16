import pytest
from suds.client import Client


@pytest.mark.rmb
class WebServices(object):
    WSDL_ADDRESS = 'http://www.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx?wsdl'

    def __init__(self):
        self.web_service = Client(self.WSDL_ADDRESS)

    def get_version_time(self):
        return self.web_service.service.getVersionTime()

    def get_contry_city_by_ip(self, ip):
        return self.web_service.service.getCountryCityByIp(ip)


class TestWebServices:
    def test_version_time(self):
        assert WebServices().get_version_time() == "IP地址数据库，及时更新"

    @pytest.mark.parametrize('ip, expected', [('10.10.10.10', '10.10.10.10')])
    def test_get_contry_city_by_ip(self):
        assert expected in str(WebServices().get_contry_city_by_ip(ip))


if __name__ == '__main__':
    pytest.main(["-m", "rmb", "-s", "-v"])
