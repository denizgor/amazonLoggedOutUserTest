from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    SEARCH_RESULT_BAR = (By.CSS_SELECTOR, "[data-component-id='15']")