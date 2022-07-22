import unittest
import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.options import Options

class BasePage():
    def __init__(self, browser , url):
        self.browser = browser
        self.url = url
    
    def open(self):
        self.browser.get(self.url)
