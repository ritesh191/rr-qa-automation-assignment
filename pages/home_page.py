from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from resources.testData import CATEGORIES

class HomePage(BasePage):
    # Locators
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[type='text']")
    GRID_ITEMS = (By.XPATH, "//div[@class='grid grid-cols-3 gap-4']//div")
    NO_RESULT = (By.XPATH, "//div[text()='No results found.']")
    POPULAR_lINK = (By.LINK_TEXT, "Popular")
    TREND_LINK = (By.LINK_TEXT, "Trend")
    NEWEST_LINK = (By.LINK_TEXT, "Newest")
    TOPRATED_LINK = (By.LINK_TEXT, "Top rated")
    TYPE_DROPDOWN = (By.XPATH, "//div[contains(@class,'css-1hwfws3')]")
    TYPE_DROPDOWN_TV = (By.XPATH, "//div[contains(text(),'TV Shows')]")
    TYPE_DROPDOWN_MOVIE = (By.XPATH, "//div[contains(text(),'Movie')]")

    def search(self, text):
        self.enter_text(self.SEARCH_INPUT, text)
        self.temp_sleep()

    def get_result_count(self):
        items = self.find_all(self.GRID_ITEMS)
        return len(items)

    def get_error_message(self):
        text = self.find(self.NO_RESULT).text
        return text

    def select_category(self, category_name):
        # categories in demo app are links
        if category_name in CATEGORIES.keys():
            LINK_TEXT = CATEGORIES.get(category_name)
        locator = getattr(self, LINK_TEXT)
        self.click(locator)
        self.temp_sleep()

    def select_type(self, option):
        self.find(self.TYPE_DROPDOWN).click()
        if option == "TV":
            self.click(self.TYPE_DROPDOWN_TV)
            self.temp_sleep()
        elif option == "Movie":
            self.click(self.TYPE_DROPDOWN_MOVIE)
            self.temp_sleep()

