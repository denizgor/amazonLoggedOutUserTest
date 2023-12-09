from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.product_page import ProductPage
import random


class SearchResultsPage(BasePage):
    SEARCH_RESULT_BAR = (By.CSS_SELECTOR, "[data-component-id='15']")
    PRODUCT_CARD_ARRAY = (By.CLASS_NAME, "puis-card-container")

    index = random.randint(0, 59)
    def get_picked_element_text(self):
        element_text = self.get_element_text(self.find_elements(self.index, *self.PRODUCT_CARD_ARRAY))

        return element_text

    def click_picked_product(self):
        self.click_element(self.find_elements(self.index, *self.PRODUCT_CARD_ARRAY))

        return ProductPage(self.driver)
