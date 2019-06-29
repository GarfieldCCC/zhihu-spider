import requests, json, time, random
from bs4 import BeautifulSoup


class zhihuspider:

    def __init__(self, Start, api):
        self.user = []
        self.headers = {
            'User-Agent': 'ozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
            'Referer': 'https://www.zhihu.com',
            'Cookie': 'tgw_l7_route=6936aeaa581e37ec1db11b7e1aef240e; _zap=12b849f1-2a10-4347-b0e4-e45b52a9f912; _xsrf=mVWY6fjE7Noale8GFbNCFXE5ubfaMLIS; d_c0="AKCtie7Zmg-PTuvAdGEggxrY0_IVl0ZeYs0=|1560869932"; capsion_ticket="2|1:0|10:1560869933|14:capsion_ticket|44:NTVmMWJiNTY0NTQwNGI3OThlNzYxNjhhYWFlY2FiMTY=|286aa8976d49462a19c319d14591ea6d0ed40e5f04eb2f499e055e9dab711a50"; z_c0="2|1:0|10:1560869935|4:z_c0|92:Mi4xVjVoeUF3QUFBQUFBb0sySjd0bWFEeVlBQUFCZ0FsVk5MMHIyWFFEV3JJMWZTRzZKWGFaajFCeThodUpma21lN3dB|330c6a2bea600b930e3e59eb026694fa5bedb99ef8402426aff365dbcee4c088"; tst=r'}

        self.info = Start
        self.start_json_url = "https://www.zhihu.com/api/v4/members/" + api
        self.info_url = "https://www.zhihu.com/api/v4/members/"
        self.aim_path = "zhihu.txt"

        self.proxies_pool = [{"http": "http:// 125.67.75.8:9000"}, {"http": "http://115.218.218.193:9000"},
                             {"http": "http://182.129.240.115:9000"}, {"http": "http://117.90.7.33:9000"},
                             {"http": "http://121.232.144.223:9000"}, {"http": "http://117.90.3.206:9000"},
                             {"http": "http://115.223.255.11	:9000"}, {"http": "http://182.129.241.45	:9000"},
                             {"http": "http://121.232.144.223:9000"}, {"http": "http://115.223.238.73:9000"},
                             {"http": "http://121.232.194.198:9000"}, {"http": "http://59.62.6.40:9000"},
                             {"http": "http://115.218.125.218:9000"}, {"http": "http://117.90.2.153:9000"},
                             {"http": "http://115.223.243.65:9000"}, {"http": "http://115.223.202.251:9000"},
                             {"http": "http://115.223.254.201:9000"}, {"http": "http://121.31.148.34:8123"},
                             {"http": "http://115.218.122.24:9000"}, {"http": "http://119.164.20.193:8118"},
                             {"http": "http://119.162.188.198:8818"}, {"http": "http://115.196.149.164:61202"},
                             {"http": "http://121.62.50.35:61234"}, {"http": "http://110.73.53.140:8123"},
                             {"http": "http://110.73.52.110:8123"}, {"http": "http://61.185.10.167:61202"},
                             {"http": "http://113.138.178.241:61202"}, {"http": "http://113.200.88.237:61202"},
                             {"http": "http://122.114.31.177:808"}, {"http": "http://61.135.217.7:80"},
                             {"http": "http://112.255.192.54:61202"}, {"http": "http://112.230.190.27:61202"},
                             {"http": "http://110.73.51.78:8123"}, {"http": "http://115.58.129.226:8118"},
                             {"http": "http://110.73.11.116:8123"}, {"http": "http://123.53.132.208:61234"},
                             {"http": "http://182.91.237.16:8118"}, {"http": "http://218.93.134.135:6666"},
                             {"http": "http://183.33.131.183:9999"}, {"http": "http://101.132.121.157:9000"},
                             {"http": "http://122.72.18.34:80"}, {"http": "http://180.173.149.144:9797"},
                             {"http": "http://118.212.137.135:31288"}, {"http": "http://122.72.18.35:80"},
                             {"http": "http://59.67.152.230:3128"}, {"http": "http://61.135.217.7:80"},
                             {"http": "http://112.255.192.54:61202"}, {"http": "http://110.73.11.116:8123"},
                             {"http": "123.53.132.208:61234"}, {"http": "http://221.237.136.30:8118"},
                             {"http": "http://122.241.208.119:61202"}, {"http": "http://111.124.22.186:61202"},
                             {"http": "http://116.30.120.3:9000"}, {"http": "http://113.14.43.169:61202"},
                             {"http": "http://139.212.251.131:61202"}, {"http": "http://203.174.112.13:3128"},
                             {"http": "http://58.252.6.165:9000"}, {"http": "http://1.197.72.245:61234"},
                             {"http": "http://119.183.35.75:61202"}, {"http": "http://182.247.56.69:61202"},
                             {"http": "http://222.188.247.178:6666"}, {"http": "http://218.6.145.11:9797"},
                             {"http": "http://122.114.31.177:808"}, {"http": "http://180.173.149.144:9797"}]

    def user_is_valid(self, info):
        return False if list(info.items())[0][0] == 'error' else True

    def get_numbers(self, URL, isFollowers=True):
        "返回关注者或关注了的人数"
        proxies = self.proxies_pool[random.randint(0, 63)]
        r = requests.get(URL, headers=self.headers, proxies=proxies)
        text = r.text
        soup = BeautifulSoup(text, 'html.parser')
        if isFollowers == True:
            return soup.find_all('strong', class_='NumberBoard-itemValue')[1].text
        else:
            return soup.find_all('strong', class_='NumberBoard-itemValue')[0].text

    def get_json_data(self, URL, Type):
        "获取json格式"
        proxies = self.proxies_pool[random.randint(0, 63)]
        l = []

        url = URL + Type + "?limit=20&offset=0"
        r = requests.get(url, headers=self.headers, proxies=proxies)
        text = r.text
        jo = json.loads(text)
        for data in jo['data']:
            l.append(data)
        return l

    def get_all_list(self, List):
        "返回url_token列表"
        l = []
        for item in List:
            l.append(item['url_token'])
        return l

    def delete_repeat(self, list1, list2):
        "合并去重排序"
        self.user = list(set(self.user + list1 + list2))
        return self.user
        # return list(set(list1 + list2))

    def get_infos(self, url):
        proxies = self.proxies_pool[random.randint(0, 63)]
        Dic = {}
        r = requests.get(url, headers=self.headers, proxies=proxies)
        text = r.text
        jo = json.loads(text)
        if int(str(r)[11:14]) != 200:
            # print("已注销用户的信息: : ", jo)
            return jo
        Dic['name'] = jo['name']
        Dic['gender'] = jo['gender']
        Dic['headline'] = jo['headline']
        Dic['url_token'] = jo['url_token']
        return Dic

    def get_url_token(self, URL):
        "返回关注和被关注的url_token列表, 这个函数会更新self.user列表(因为delete_repeat)"
        following = self.get_json_data(URL, Type='/followees')
        followers = self.get_json_data(URL, Type='/followers')
        return list(self.delete_repeat(self.get_all_list(following), self.get_all_list(followers)))

    def Iteration(self, Max, base_url, file_path):
        G = ['女', '男', '未知']
        index = -1

        while len(self.user) < Max:
            print(len(self.user))
            index += 1
            item = self.user[index]
            url = base_url + str(item)
            following = self.get_json_data(url, Type='/followees')
            followers = self.get_json_data(url, Type='/followers')
            self.user = list(set(self.user + self.get_all_list(following) + self.get_all_list(followers)))
        for item in self.user:
            url = base_url + str(item)
            information = self.get_infos(url)
            if self.user_is_valid(information):
                name = information['name']
                gender = G[information['gender']]
                signature = information['headline']
                url_token = information['url_token']
                sentence = "标识: " + url_token + " 昵称: " + name + ", 性别: " + gender + ", 个性签名: " + signature + "\n"
                print("昵称: ", name, ", 性别: ", gender, ", 个性签名: ", signature)
                with open(file_path, 'a', encoding='utf-8') as f:
                    f.write(sentence)
                # time.sleep(round(random.random(), 1))


if __name__ == '__main__':
    username = "Garfield"
    userurl = "garfield-21-38"
    Max = 2048

    spider = zhihuspider(username, userurl)

    print("\n从“", username, "”开始获取知乎用户信息\n")
    List = spider.get_url_token(spider.start_json_url)
    spider.user = List
    spider.Iteration(Max, spider.info_url, spider.aim_path)
