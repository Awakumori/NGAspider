import time
import json
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://bbs.nga.cn/thread.php?fid=-7")

time.sleep(40)

with open('cookies.txt', 'w') as cookiefile:
    # 将cookies保存为json格式
    cookiefile.write(json.dumps(driver.get_cookies()))

time.sleep(1)
driver.quit()
