from selenium import webdriver
from time import sleep

# selecting Firefox as the browser
# in order to select Chrome
# webdriver.Chrome() will be used
driver = webdriver.Chrome(
    executable_path='E:\chromedriver_win32\chromedriver.exe')

# URL of the website
url = "https://randomwordgenerator.com/sentence.php"

# opening link in the browser
driver.get(url)
# sleep(5)

inputVal = driver.find_element_by_id("qty")
inputVal.clear()
inputVal.send_keys("50")

sleep(2)

formSubmit = driver.find_element_by_id("btn_submit_generator")
formSubmit.click()

sentencesPulled = driver.find_elements_by_class_name("support-sentence")

with open("Random_sentences.txt", "w") as f:
    for i in sentencesPulled:
        f.write(i.text + "\n")
