from selenium import webdriver

def firefox_browser():
    driver = webdriver.Firefox(executable_path="D:\\Class practice\\tools\\geckodriver.exe")

    driver.get("https://www.xnxx.com/")

    driver.close()

firefox_browser()