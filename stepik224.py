from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
   link = "http://suninjuly.github.io/execute_script.html"
   browser = webdriver.Chrome()
   browser.get(link)
   x = browser.find_element_by_css_selector("#input_value").text
   y = calc(x)
   input1 = browser.find_element_by_css_selector("#answer")
   input1.send_keys(y)

   option1 = browser.find_element_by_css_selector("#robotCheckbox")
   option1.click()


   option2 = browser.find_element_by_css_selector("#robotsRule")
   browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
   option2.click()
   button = browser.find_element_by_css_selector("button.btn")
   button.click()
   button = browser.find_element_by_tag_name("button")
   browser.execute_script("return arguments[0].scrollIntoView(true);", button)
   button.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
