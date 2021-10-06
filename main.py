import time
import json
import pandas as pd
from selenium import webdriver

from items import Topic

StopWords = '停用词库.txt'

driver = webdriver.Chrome()
driver_user = webdriver.Chrome()

driver.get("https://bbs.nga.cn/thread.php?fid=-7")
driver_user.get('https://bbs.nga.cn/nuke.php?func=ucp&uid=36587915')

driver.delete_all_cookies()
driver_user.delete_all_cookies()


def is_ElementExist(ddriver, xpath):
    try:
        ddriver.find_element_by_xpath(xpath)
        return True
    except:
        return False


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


def now_time():
    return time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())


with open('cookies.txt', 'r') as cookief:
    cookieslist = json.load(cookief)
    for cookie in cookieslist:
        driver.add_cookie(cookie)
        driver_user.add_cookie(cookie)

print('cookies加载完成')

driver.refresh()
content = []
time.sleep(1)
for i in range(5):
    if not is_ElementExist(driver, '//a[@title="继续访问艾泽拉斯国家地理"]'):
        row_list = driver.find_elements_by_xpath('//*[@class="row1 topicrow"]')
        row_list.extend(driver.find_elements_by_xpath('//*[@class="row2 topicrow"]'))
        for row in row_list:
            try:
                link = str(row.find_element_by_class_name('replies').get_attribute('href'))
                tid = link[32:]
                title = row.find_element_by_class_name('topic').text
                if title == '帖子发布或回复时间超过限制':
                    continue
                poster_id = str(row.find_element_by_class_name('author').get_attribute('title'))[5:]
                post_time = str(row.find_element_by_class_name('silver.postdate').get_attribute('title'))
                poster_name = row.find_element_by_class_name('author').text
                re_num = row.find_element_by_class_name('replies').text
                partition = '水区'
                if is_ElementExist(row, './td[@class="c2"]/span[@class="titleadd2"]/a[@class="silver"]'):
                    partition = row.find_element_by_xpath(
                        './td[@class="c2"]/span[@class="titleadd2"]/a[@class="silver"]').text
                sampling_time = now_time()

                user_history_re_num = ''
                user_prestige = ''
                user_group = ''
                user_reg_date = ''
                # 查询楼主成分
                if is_number(poster_id):
                    driver_user.get('https://bbs.nga.cn/nuke.php?func=ucp&uid=' + poster_id)
                    user_group = driver_user.find_element_by_xpath('//label[contains(text(), "用户组")]/../span/span').text
                    user_reg_date = driver_user.find_element_by_xpath(
                        '//label[contains(text(), "注册日期")]/../span/span').text
                    if is_ElementExist(driver_user, '//label[contains(text(), "威望")]/../span'):
                        user_prestige = (driver_user.find_element_by_xpath(
                            '//label[contains(text(), "威望")]/../span').text)[2:]
                    if is_ElementExist(driver_user, '//label[contains(text(), "发帖数")]/../span'):
                        user_history_re_num = (driver_user.find_element_by_xpath(
                            '//label[contains(text(), "发帖数")]/../span').text)[2:]

                # 写入字典
                item = {'tid': tid,
                        'title': title,
                        'reply_num': re_num,
                        'partition': partition,
                        'post_time': post_time,
                        'poster_id': poster_id,
                        'poster_name': poster_name,
                        'poster_history_re_num': user_history_re_num,
                        'poster_prestige': user_prestige,
                        'poster_group': user_group,
                        'poster_reg_date': user_reg_date,
                        'sampling_time': sampling_time}
                print(item)
                content.append(item)
            except:
                continue
        continue_link = driver.find_element_by_xpath('//a[@title="加载下一页"]')
        continue_link.click()
        driver.refresh()

    else:
        time.sleep(3)
        skip_link = driver.find_element_by_xpath('//a[@title="继续访问艾泽拉斯国家地理"]')
        skip_link.click()

data = pd.DataFrame(content)
data.to_csv("ngaData" + str(now_time()) + ".csv", index=False, sep=',')

time.sleep(5)
driver.quit()
driver_user.quit()
