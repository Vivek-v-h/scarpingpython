from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

e=driver.find_elements(By.TAG_NAME,"h3")
st=""
for item in e:
    print(item.text)
    st+=f"{item.text}\n"

with open("results.txt","w",encoding="utf-8")as f:
    f.write(st)
assert "No results found." not in driver.page_source
a=input()
driver.close()