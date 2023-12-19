from pages.base_page import BasePage
from pages.product_page import ProductPage
from selenium.webdriver.common.by import By
import random


class SearchResultsPage(BasePage):
    SEARCH_RESULT_BAR = (By.CSS_SELECTOR, "[data-component-id='15']")
    PRODUCT_CARD_ARRAY = (By.CLASS_NAME, "a-size-base-plus.a-text-normal")

    index = random.randint(0, 59)
    def get_picked_element_text(self):
        element_text = self.get_element_text(*self.PRODUCT_CARD_ARRAY, index=self.index)

        return element_text

    def click_picked_product(self):
        self.find_elements(self.index, *self.PRODUCT_CARD_ARRAY).click()

        return ProductPage(self.driver)

