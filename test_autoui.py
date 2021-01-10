import pytest

from time import sleep
from selenium import webdriver

def test_main():
    # 创建webdriver实例对象
    wd = webdriver.Chrome(r'd:\chromedriver.exe')
    wd.maximize_window()
    wd.implicitly_wait(5)
    wd.get('http://web4tst.dogotsn.cn/supplier/pages/login.html')
    sleep(1)
    wd.find_element_by_name('username').send_keys('13611011011')
    wd.find_element_by_name('password').send_keys('12345678')
    wd.find_element_by_id('loginSub').click()
    sleep(4)
    wd.find_element_by_xpath('//*[@id="side-menu"]/li[2]').click()
    sleep(1)
    wd.find_element_by_link_text('全部订单').click()
    sleep(1)
    wd.switch_to.frame('iframe1')  # 切换右侧frame
    # page_id = wd.page_source
    # print(page_id)
    # page_text = wd.find_element_by_id('tb_departments').text
    # print(page_text)
    # title = wd.find_element_by_class_name('panel-heading').text
    # print(title)
    # assert u'全部订单列表' in title  # 判断是否打开全部订单页
    wd.find_element_by_id('orderNo').send_keys('5201228141913619936')
    wd.find_element_by_id('queryBtn').click()
    content = wd.find_element_by_xpath('//*[@id="tb_departments"]/tbody/tr/td[13]').text
    print(content)

    assert u'全部退款' in content , 'aaaaaaaaa' # 判断是否打开全部订单页

if __name__ == '__main__':

    pytest.main(['-s','test_autoui.py','--html=./report/result.html'])

