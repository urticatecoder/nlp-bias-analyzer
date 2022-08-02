from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup



####################
# Set up webdriver
####################
DRIVER_PATH = "F:/Downloads/chromedriver_win32/chromedriver.exe"

options = Options()
#options.headless = True
options.add_argument("start-maximized")

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)


#########################################
# Use webdriver to collect CNN articles
#########################################
driver.get("https://www.cnn.com")
driver.implicitly_wait(10000)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.implicitly_wait(10000)

# html_text = driver.page_source

# soup = BeautifulSoup(html_text, "lxml")
# anchors = soup.find_all("a", class_ = False)

# print("===================================================================================================================================================")
# print("===================================================================================================================================================")

# for tag in anchors:
#     href = tag["href"]

#     if href[0] == "/":
#         href = "https://www.cnn.com" + href

#     if href.startswith("https://www.cnn.com"):
#         print(href)
#         print()


# print(len(anchors))


anchors = driver.find_elements(By.TAG_NAME, "a")

print("===================================================================================================================================================")
print("===================================================================================================================================================")
for tag in anchors:
    print(tag)
    print()

driver.quit()