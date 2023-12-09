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

    def get_text(self, locator):
        return self.find_element(*locator).text

    def send_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def search_element_in_dom(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def get_element_text(self, *locator):
        return self.find_element(locator).text
