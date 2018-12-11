from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote


browser = webdriver.chrome()
wait = WebDriverWait(browser, 10)
KEYWORD = 'ipad'
