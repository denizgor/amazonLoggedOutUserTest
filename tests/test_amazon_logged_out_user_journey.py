from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from tests.base_test import BaseTest
from pages.home_page import HomePage


class TestAmazonLoggedOutUserJourney(BaseTest):
    PRODUCT_BRAND = (By.ID, "bylineInfo")
    search_keys = "bluetooth kulaklık"

    # Go to mainpage and click "reject cookies"
    def test_amazon_logged_out_user(self):
        home_page = HomePage(self.driver)
        home_page.click_reject_cookies_link()

        # Search for a product
        home_page.enter_search_term(self.search_keys)
        search_results_page = home_page.click_search_icon()

        # Assert that you are in the search results page for the product searched
        self.assertIn(self.search_keys, self.driver.title)
        self.assertTrue(
            self.driver.find_element(By.CLASS_NAME, "a-color-state").text == '"{}"'.format(self.search_keys))

        # pick a random product & click on it and go to product page
        picked_element_text = search_results_page.get_picked_element_text()
        self.assertTrue(picked_element_text != "")

        product_page = search_results_page.click_picked_product()
        clicked_product_title = product_page.get_product_title()
        print("Picked Element Text: ", picked_element_text)
        print("Clicked Product Title: ", clicked_product_title)

        # assert that product name is the same with the clicked product name
        self.assertEqual(picked_element_text, clicked_product_title, "Error! This isn't the picked product!")

        # assert that the product card has: name, brand, star rating and icon, comments, and price
        self.assertTrue(EC.presence_of_element_located(product_page.PRODUCT_TITLE),
                        "Error! Product name is not present.")
        self.assertTrue(EC.presence_of_element_located(product_page.PRODUCT_BRAND),
                        "Error! Product brand is not present.")
        self.assertTrue(EC.presence_of_element_located(product_page.PRODUCT_STAR_POINTS),
                        "Error! Product star points not present.")
        self.assertTrue(EC.presence_of_element_located(product_page.PRODUCT_PRICE),
                        "Error! Product price is not present.")
        self.assertTrue(EC.presence_of_element_located(product_page.PRODUCT_COMMENTS),
                        "Error! Comments are not present.")

        # store product name and price in a variable
        product_price = product_page.extract_product_price()
        print(product_price)

        print("Test")

    # add product to the cart and check that minicart updated

    # click on the cart icon and go to cart

    # check that product is in the cart

    # check that product price is the same with the price on the product page

    # delete the product from the cart

    # check that the prdoduct is removed from the cart

    print("Finished Test")
