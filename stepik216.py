from selenium import webdriver
import time

def calc(x):
    return int(x+z)



try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("h2")
    z_element = browser.find_element_by_css_selector("h2")
    x = x_element.get_attribute("#num1")
    z = z_element.get_attribute("#num2")
    y = calc(x)

    print(y)

    #from selenium.webdriver.support.ui import Select
#
    #select = Select(browser.find_element_by_tag_name("select"))
    #select.select_by_value("1")  # ищем элемент с текстом "Python"
   # input1 = browser.find_element_by_css_selector("#answer")
   # input1.send_keys(y)
#
   # option1 = browser.find_element_by_css_selector("#robotCheckbox")
   # option1.click()
#
   # option2 = browser.find_element_by_css_selector("#robotsRule")
   # option2.click()
#
   # button = browser.find_element_by_css_selector("button.btn")
   # button.click()
#
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
