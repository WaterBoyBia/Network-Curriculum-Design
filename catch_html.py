import os
import time
from IP import IP_Pool
from selenium import webdriver














def get_html(user_id):

    class DoubanUserSpider:
        def __init__(self):
            self.driver_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe'
            self.options = webdriver.EdgeOptions()
            self.options.add_argument('headless')  # 无界面模式
            self.options.add_argument('user-data-dir=C:\\Users\\10766\AppData\Local\Microsoft\Edge\\User Data')


            #
            # # todo IP池模式：会直接封
            # IP = IP_Pool()
            # print(IP)
            # self.options.add_argument("--proxy-server=http://{}".format(IP))
            # #
            #



            self.browser = webdriver.Edge(executable_path=self.driver_path, options=self.options)

        def get_page_source(self, user_id):
            url = f'https://www.douban.com/people/{user_id}'



            try:
                self.browser.get(url)
            except:
                self.browser.get(url)


            page_source = self.browser.page_source
            return page_source

    # if __name__ == '__main__':

    # spider = DoubanUserSpider()
    # for user_id in range(1000001, 1000011):
    #     page_source = spider.get_page_source(user_id)
    #     with open(f'douban_user_{user_id}.txt', 'w', encoding='utf-8') as f:
    #         f.write(page_source)
    # spider.browser.quit()
    #
    spider = DoubanUserSpider()
    # user_id = 'ruo1996'
    page_source = spider.get_page_source(user_id)
    with open(f'douban_user.txt', 'w', encoding='utf-8') as f:
        f.write(page_source)
    spider.browser.quit()

    # # 将txt转换为html
    # # 加载文本文件
    # doc = aw.Document('douban_user.txt')
    # # 将文本保存为 HTML
    # doc.save("1.html")
    #
    # a = 0  # 定义一个数文件数量的变量
    # b = 0
    # for root, dirs, files in os.walk('D:\\University\\大创\\爬虫'):  # D:\\masked\\Annotations可以改成自己想要的路径
    #     for name in files:  # for循环删除文件
    #         if name.endswith(".jpeg"):  # .jpg可以换成另一种你想删除的文件后缀名
    #             a += 1
    #             os.remove(os.path.join(root, name))  # 删除后缀为.jpeg的文件
    #     for name in files:  # for循环删除文件
    #         if name.endswith(".png"):  # .jpg可以换成另一种你想删除的文件后缀名
    #             b += 1
    #             os.remove(os.path.join(root, name))  # 删除后缀为.png的文件

    # 删除指定的文件
    for filename in os.listdir():
        if filename.startswith('douban_user'):
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            if '<title>登录豆瓣</title>' in content or '<title>页面不存在</title>' in content or\
                    '<html><head><title>Error: Access denied</title></head>' in content or \
                    '该用户已经主动注销帐号。<br>' in content or '已被永久停用' in content:
                for i in range(10):
                    try:
                        os.remove(filename)
                        print(f'{filename} 删除成功')
                        break
                    except PermissionError:
                        print(f'{filename} 正在被占用，等待 1 秒后重试')
                        time.sleep(1)
                else:
                    print(f'{filename} 删除失败')

    if os.path.exists('douban_user.txt'):
        os.rename(r"D:\University\大二\计算机网络\课程设计\爬虫\douban_user.txt", r"D:\University\大二\计算机网络\课程设计\爬虫\1.html")
