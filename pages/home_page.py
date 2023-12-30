from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.search_results_page import SearchResultsPage

class HomePage(BasePage):

    #LOCATORS
    REJECT_COOKIES = (By.ID, "sp-cc-rejectall-link")
    #Searchbox-Dropdown $("#searchDropdownBox")
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_ICON = (By.ID, "nav-search-submit-button")
    LOCATION_ICON = (By.ID, "nav-global-location-data-modal-action")
    AMZN_LOGO = (By.ID, "nav-logo-sprites")



    def click_reject_cookies_link(self):
        self.click_element(*self.REJECT_COOKIES)

    def enter_search_term(self, text):
        self.send_text(text, *self.SEARCH_BOX)

    def click_search_icon(self):
        self.click_element(*self.SEARCH_ICON)

        return SearchResultsPage(self.driver)

