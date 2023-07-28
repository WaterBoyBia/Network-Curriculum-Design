from selenium import webdriver
from IP import IP_Pool

driver_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe'
options = webdriver.EdgeOptions()

IP = IP_Pool()
options.add_argument("--proxy-server=http://{}".format(IP))
options.add_experimental_option("detach", True)
browser = webdriver.Edge(executable_path=driver_path, options=options)
url = 'https://qifu.baidu.com/?activeKey=SEARCH_IP&trace=apistore_ip_aladdin&activeId=SEARCH_IP_ADDRESS&ip='
print(IP)


browser.get(url)
