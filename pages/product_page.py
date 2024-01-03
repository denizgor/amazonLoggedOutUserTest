from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    PRODUCT_TITLE = (By.ID, "productTitle")
    PRODUCT_BRAND = (By.ID, "bylineInfo")
    PRODUCT_STAR_POINTS = (By.ID, "averageCustomerReviews")
    PRODUCT_COMMENTS = (By.ID, "acrCustomerReviewText")
    PRODUCT_PRICE = (By.ID, "corePriceDisplay_desktop_feature_div")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    GO_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-csa-c-slot-id='sw-gtc']")
    MINICART_ITEM_COUNT = (By.ID, "nav-cart-count")


    def get_product_title(self):
        product_title = self.get_element_text(*self.PRODUCT_TITLE)

        return product_title

    def extract_product_price(self):
        return self.get_product_price(*self.PRODUCT_PRICE)

    def click_add_to_cart_button(self):
        self.click_element(*self.ADD_TO_CART_BUTTON)

    def click_go_to_cart_button(self):
        self.click_element(*self.GO_TO_CART_BUTTON)

    def get_minicart_count(self):
        return int(self.get_element_text(*self.MINICART_ITEM_COUNT))