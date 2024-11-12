from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "https://www.youtube.com/watch?v=UNfwFfZdEw0";
no_of_views = 100;
duration = 10;
print("");
for i in range(0, no_of_views):
    browser = webdriver.Chrome();
    browser.get(url);
    time.sleep(duration);
    print(str(i + 1) + " iterations done");
    browser.quit()