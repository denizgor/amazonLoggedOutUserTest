from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from pages.home_page import HomePage


class TestAmazonLoggedOutUserJourney(BaseTest):

    search_keys = "bluetooth kulaklık"

    #Go to mainpage and click "reject cookies"
    def test_amazon_logged_out_user(self):
        home_page = HomePage(self.driver)
        home_page.click_reject_cookies_link()
        home_page.enter_search_term(self.search_keys)
        home_page.click_search_icon()


    #Click the search bar and search for a product


    #Assert that you are in the serch results page for the product searched


    #click on a product and go to product page

    # assert that product name is the same with the clicked product name

    #assert that the product card has: name, brand, star rating and icon, comments, and price

    #store product name and price in a variable

    #add product to the cart and check that minicart updated

    #click on the cart icon and go to cart

    #check that product is in the cart

    #check that product price is the same with the price on the product page

    #delete the product from the cart

    #check that the prdoduct is removed from the cart