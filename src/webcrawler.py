from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
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
time.sleep(15)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(15)

html_text = driver.page_source

soup = BeautifulSoup(html_text, "lxml")
allAnchors = soup.find_all("a", class_ = False)

print("===================================================================================================================================================")
print("===================================================================================================================================================")

cnnLinksForDatabase = []
for tag in allAnchors:
    href = tag["href"]

    if href[0] == "/":
        href = "https://www.cnn.com" + href

    if (href.startswith("https://www.cnn.com") and (href.endswith("index.html") or href.endswith(".cnn") or href.endswith("CNNUnderscoredHPcontainer") or href[20:25] == "audio")):
        cnnLinksForDatabase.append(href)
        print(href)
        print()


print("Collected " + str(len(allAnchors)) + " links.")
print()

driver.close()
driver.quit()

################
# Serializing json
################
cnnLinks = json.dumps(cnnLinksForDatabase, indent=4)

############################
# Writing to cnn-links.json
############################
with open('src\cnn-links.json', "w") as outfile:
    outfile.write(cnnLinks)