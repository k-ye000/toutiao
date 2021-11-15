from selenium.webdriver import Chrome, ChromeOptions


class toutiaoSignature(object):
    # 改变token或max_behot_time获得的_signature参数不同
    # max_behot_time参数为0则只请求最新数据，每次请求会返回max_behot_time作为下一次请求的参数
    def __init__(self, token=None, max_behot_time=0) -> None:
        super().__init__()
        self.option = ChromeOptions()
        self.option.add_argument('--headless')
        self.option.add_argument('--no-sandbox')
        self.option.add_argument('--disable-gpu')
        self.browser = Chrome(
            executable_path='./chromedriver', options=self.option)
        self.browser.get(url='http://127.0.0.1:5001/')
        self.token = token
        if not self.token:
            raise('token value error')
        self.max_behot_time = max_behot_time

    def sign(self):
        # 加密后的完整url格式为：https://www.toutiao.com/api/pc/list/feed?category=profile_all&token=MS4wLjABAAAAvazHMceCo3MeM9IJbll231AC8GkJDcrd__iZFw2hi4o&max_behot_time=0&_signature=_02B4Z6wo00d01yKT3VgAAIDDSBGkzJ1pV6sit9nAAKk-a5
        js = '''
            n = '/api/pc/list/feed?category=profile_all&token=%s&max_behot_time=%s'
            var _signature = I(n);
            return _signature
            ''' % (self.token, self.max_behot_time)
        _signature = self.browser.execute_script(js)

        print(_signature)


if __name__ == '__main__':
    # 需要使用头条新闻的搜索功能与获取首页新闻只需改变token与js的url相关代码即可
    token = 'MS4wLjABAAAAZ-7_bvIhGk-tKa7Z4B3GUSA0d-6Rc3qMsEsMEPPUQig'
    max_behot_time = 0
    ttS = toutiaoSignature(token=token, max_behot_time=max_behot_time)
    ttS.sign()
