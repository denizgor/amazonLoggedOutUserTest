from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CartPage(BasePage):
    PRODUCT_NAME = (By.CLASS_NAME, "a-truncate-cut")