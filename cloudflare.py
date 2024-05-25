from undetected_chromedriver import Chrome
import time

chrome = Chrome()

chrome.get("https://nabildzr.xyz")

time.sleep(100)

chrome.close()
