from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_xpath("//span[@id='num1']").text
    y = browser.find_element_by_xpath("//span[@id='num2']").text
    x1 = int(x)
    y1 = int(y)
    z = str(x1 + y1)

    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector(f"[value='{z}']").click()
    browser.find_element_by_tag_name('button').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()
