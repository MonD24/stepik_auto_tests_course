from selenium import webdriver
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("//body/div[1]/form[1]/div[1]/input[1]")
    input1.send_keys("Testovich")

    input2 = browser.find_element_by_xpath("//body/div[1]/form[1]/div[1]/input[2]")
    input2.send_keys("Test")

    input3 = browser.find_element_by_xpath("//body/div[1]/form[1]/div[1]/input[3]")
    input3.send_keys("Testov@test.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
    with open("test.txt", "w") as file:
        content = file.write("automationbypython")  # create test.txt file
    element = browser.find_element_by_xpath("//input[@id='file']").send_keys(file_path)

   #with open("test.txt", "w") as file:
   #    content = file.write("automationbypython")  # create test.txt file
   #element = browser.find_element_by_xpath("//input[@id='file']").send_keys(file_path)

    click = browser.find_element_by_tag_name("button").click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()