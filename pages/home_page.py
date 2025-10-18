from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    # Locators
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[type='text']")
    GRID_ITEMS = (By.XPATH, "//div[@class='grid grid-cols-3 gap-4']//div")

    def search(self, text):
        search_box = self.find(self.SEARCH_INPUT)
        search_box.clear()
        search_box.send_keys(text)

