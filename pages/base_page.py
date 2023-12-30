from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains



class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)
        self.actions = ActionChains(self.driver)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, index, *element):
        return self.driver.find_elements(*element)[index]

    def click_element(self, *locator):
        self.find_element(*locator).click()

    def wait_element(self, method, message=""):
        return self.wait.until(EC.presence_of_element_located(method), message)

    def hover_element(self, *locator):
        self.actions.move_to_element(self.find_element(*locator)).perform()


    def send_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def search_element_in_dom(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def get_element_text(self, *locator, index=None):
        if index is not None:
            return self.find_elements(index, *locator).text
        else:
            return self.find_element(*locator).text

    def get_product_price(self, *locator):
        raw_price = self.driver.find_element(*locator).text

        # Split the data based on whitespace and newline characters
        price_tokens = raw_price.split()

        # Join the numeric tokens to form a numeric string
        numeric_string = ''.join(token for token in price_tokens if token.replace('.', '').isdigit())

        # Convert the numeric string to a float
        if numeric_string:
            extracted_price = float(numeric_string.replace(',', '.'))
            return extracted_price
        else:
            print("Price not found in the given data.")

