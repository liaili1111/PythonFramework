from suds.client import Client

if __name__ == '__main__':
    url = 'http://www.webxml.com.cn/WebServices/IpAddressSearchWebService.asmx?wsdl'
    # 初始化
    client = Client(url)
#   打印出所有可用的方法
    print(client)

#   使用client.service调用所支持的方法
    print('使用client.service调用所支持的方法')
    print(client.service.getVersionTime())
    print(client.service.getCountryCityByIp('192.168.0.1'))