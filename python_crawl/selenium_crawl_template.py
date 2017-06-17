# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

# 模拟登陆
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
now_handle = driver.current_window_handle  # 获取当前窗口句柄

# driver = webdriver.Firefox()
# 暂停10秒手动输入网址
time.sleep(3)

# 用户名 密码
driver.get("xxxxxxxxxxx")
elem_user = driver.find_element_by_id("account")
elem_user.send_keys("******")
elem_pwd = driver.find_element_by_id("pwd")
elem_pwd.send_keys("******")
elem_pwd.send_keys(Keys.RETURN)
# 暂定60秒扫二维码 跳转到定向页面
time.sleep(60)

# 登录用户管理 获取相关标签
print driver.current_url
elem_user = driver.find_elements_by_xpath("//td[@class='table_cell user']/div/a[1]")
now_handle = driver.current_window_handle  # 获取当前窗口句柄
print now_handle  # 输出当前获取的窗口句柄

# 单击操作
for elem in elem_user:
    print '########################################'
    print elem.text
    # 点击进入查看详细用户
    elem.click()

    """ 
    NoSuchElementException: Message: no such element 
    因为总是获取当前句柄 故找不到相关的界面，需要窗口句柄转换 
    """
    all_handles = driver.window_handles  # 获取所有窗口句柄
    for handle in all_handles:
        if handle != now_handle:
            # 输出待选择的窗口句柄
            print handle
            driver.switch_to_window(handle)
            time.sleep(1)

            # 点击"图文消息"
            elem_tw = driver.find_element_by_xpath("//li[@class='tab_nav tab_appmsg width5']/a")
            # elem_tw = driver.find_element_by_xpath("//div[@class='tab_navs_wrp']/ul/li/a")

            print elem_tw.text
            print elem_tw.get_attribute("href")
            elem_tw.click()
            time.sleep(1)

            # 点击 '从素材库中选择'按钮
            elem_sc = driver.find_element_by_xpath("//span[@class='create_access']/a")
            print elem_sc.text
            print elem_sc.get_attribute("href")
            elem_sc.click()
            time.sleep(1)

            # 点击素材 '11-14 星期二中奖名单' 注意是id
            # elem_dj = driver.find_element_by_xpath("//div[@class='edit_mask appmsg_mask']")
            # elem_dj = driver.find_element_by_xpath("//div[@id='appmsg503811334']/div/div[2]")
            elem_dj = driver.find_element_by_xpath("//div[@id='appmsg503811334']")
            print elem_dj.text
            print elem_dj.get_attribute("href")
            elem_dj.click()
            time.sleep(1)

            # SyntaxError: Failed to execute 'evaluate' on 'Document': The string
            # '//div[@class='appmsg503811334']/div/' is not a valid XPath expression.

            # WebDriverException: Message: unknown error: Element is not clickable
            # at point (473, 361). Other element would receive the click:
            # <div class="appmsg_content">...</div>

            # 获取'确定按钮'
            elem_bt = driver.find_element_by_xpath("//div[@class='dialog_ft']/span[1]/button")
            print elem_bt.text
            print elem_bt.get_attribute("class")
            elem_bt.click()
            time.sleep(1)

            # 点击 '发送'
            elem_fs = driver.find_element_by_xpath("//span[@id='js_submit']/button")
            print elem_fs.text
            print elem_fs.get_attribute("class")
            elem_fs.click()
            time.sleep(1)

            # 关闭当前窗口
            driver.close()


            # 输出主窗口句柄
    print now_handle
    driver.switch_to_window(now_handle)  # 返回主窗口
    # break

    print '\n\n'

# 暂停换页
# 登录用户管理 获取相关标签
print '********************************************'
print '********************************************'
print u'换页操作1'
# elem_next = driver.find_elements_by_xpath("//a[@class='btn page_next']")
# elem_next.click()

time.sleep(10)
elem_user = driver.find_elements_by_xpath("//td[@class='table_cell user']/div/a[1]")
now_handle = driver.current_window_handle  # 获取当前窗口句柄
print now_handle  # 输出当前获取的窗口句柄

# 单击操作
for elem in elem_user:
    print '########################################'
    print elem.text
    # 点击进入查看详细用户
    elem.click()

    all_handles = driver.window_handles  # 获取所有窗口句柄
    for handle in all_handles:
        if handle != now_handle:
            # 输出待选择的窗口句柄
            print handle
            driver.switch_to_window(handle)
            time.sleep(1)

            # 点击"图文消息"
            elem_tw = driver.find_element_by_xpath("//li[@class='tab_nav tab_appmsg width5']/a")
            print elem_tw.text
            print elem_tw.get_attribute("href")
            elem_tw.click()
            time.sleep(1)

            # 点击 '从素材库中选择'按钮
            elem_sc = driver.find_element_by_xpath("//span[@class='create_access']/a")
            print elem_sc.text
            print elem_sc.get_attribute("href")
            elem_sc.click()
            time.sleep(1)

            # 点击素材 注意是id
            elem_dj = driver.find_element_by_xpath("//div[@id='appmsg503811334']")
            print elem_dj.text
            print elem_dj.get_attribute("href")
            elem_dj.click()
            time.sleep(1)

            # 获取'确定按钮'
            elem_bt = driver.find_element_by_xpath("//div[@class='dialog_ft']/span[1]/button")
            print elem_bt.text
            print elem_bt.get_attribute("class")
            elem_bt.click()
            time.sleep(1)

            # 点击 '发送'
            elem_fs = driver.find_element_by_xpath("//span[@id='js_submit']/button")
            print elem_fs.text
            print elem_fs.get_attribute("class")
            elem_fs.click()
            time.sleep(1)

            driver.close()  # 关闭当前窗口

    # 输出主窗口句柄
    print now_handle
    driver.switch_to_window(now_handle)  # 返回主窗口
    # break
    print '\n\n'