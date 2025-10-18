from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    # Locators
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[type='text']")
    GRID_ITEMS = (By.XPATH, "//div[@class='grid grid-cols-3 gap-4']//div")
    NO_RESULT = (By.XPATH, "//div[text()='No results found.']")

    def search(self, text):
        self.enter_text(self.SEARCH_INPUT, text)
        self.temp_sleep()

    def get_result_count(self):
        items = self.find_all(self.GRID_ITEMS)
        return len(items)

    def get_error_message(self):
        text = self.find(self.NO_RESULT).text
        return text

