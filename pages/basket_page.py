import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.options import Options
from .base_page import BasePage
from .locators import BasketPageLocators, MainPageLocators
from .login_page import LoginPage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasketPageLocators.MESSAGE_ALERT), \
       "Items are in the cart"
    
    def should_not_be_success_disappered(self):
        assert self.is_disappeared(*BasketPageLocators.MESSAGE_ALERT), \
       "The message didn't disappear"

    def should_be_succes_empty_cart(self):
        text_empty = self.browser.find_element(*BasketPageLocators.EMPTY_CART).text
        text_cart = self.browser.find_element(*BasketPageLocators.MESSAGE_CART).text
        assert text_empty in text_cart , "No empty text in the text cart"
