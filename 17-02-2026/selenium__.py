# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://www.scrapethissite.com/pages/forms/")
# assert "Hockey Teams" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("Boston Bruins")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# time.sleep(6)
# driver.close()



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# query = "laptop"
file = 0

for i in range(1, 20):
    driver.get("https://www.scrapethissite.com/pages/forms/")

    elem = driver.find_elements("div", "container")
    print(f"{len(elem)} items found")
    for elem in elem:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
            file += 1
    # print(elem.text)

    time.sleep(60)
driver.close()
