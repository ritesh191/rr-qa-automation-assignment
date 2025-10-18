import random
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from resources.testData import CATEGORIES, GENRE_CATEGORIES

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
    GENRE_DROPDOWN = (By.XPATH, "//div[contains(@class, 'css-2b097c-container')][2]//div[contains(@class, 'css-1hwfws3')]")
    YEAR_DROPDOWN_FROM = (By.XPATH, "//div[contains(@class, 'flex items-center')]//div[@class='w-24 css-2b097c-container'][1]")
    YEAR_DROPDOWN_TO = (By.XPATH, "//div[contains(@class, 'flex items-center')]//div[@class='w-24 css-2b097c-container'][2]")
    HALF_STAR = "//div[@class='rc-rate-star-first']"
    FULL_STAR = "//div[@class='rc-rate-star-second']"
    NEXT_BUTTON = (By.XPATH, "//a[text()='Next']")
    PREVIOUS_BUTTON = (By.XPATH, "//a[text()='Previous']")

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

    def select_star(self):
        star = self.random_star()
        star_selection = random.choice([self.HALF_STAR, self.FULL_STAR])
        required_xpath = f"(//li[@class='rc-rate-star rc-rate-star-zero'])[{star}]{star_selection}"
        # Use JavaScript click to avoid overlap issues
        element = self.find((By.XPATH, required_xpath))
        self.driver.execute_script("arguments[0].click();", element)
        self.temp_sleep()
        return star, "half" if "first" in star_selection else "full"

    def date_type(self):
        from_Year = self.random_year()
        to_Year = self.random_year()
        while from_Year > to_Year or from_Year == 2024:
            from_Year = self.random_year()
            to_Year = self.random_year()
        self.find(self.YEAR_DROPDOWN_FROM).click()
        self.click((By.XPATH, f"//div[contains(@class, 'flex items-center')]//div[@class='w-24 css-2b097c-container'][1]//div[contains(text(),{from_Year})]"))
        self.temp_sleep()
        self.find(self.YEAR_DROPDOWN_TO).click()
        self.click((By.XPATH, f"//div[contains(@class, 'flex items-center')]//div[@class='w-24 css-2b097c-container'][2]//div[contains(text(),{to_Year})]"))
        self.temp_sleep()
        return from_Year, to_Year

    def genre_type(self, genre_name, type_name):
        self.find(self.GENRE_DROPDOWN).click()
        xpath = GENRE_CATEGORIES.get(type_name, {}).get(genre_name)
        if not xpath:
            raise ValueError(f"Missing xpath for type '{type_name}' and genre '{genre_name}'")
        self.click((By.XPATH, xpath))
        self.temp_sleep()

    def go_next(self):
        try:
            self.click(self.NEXT_BUTTON)
            self.temp_sleep()
        except Exception:
            # If next not present, raise to let test handle negative cases
            raise

    def go_previous(self):
        try:
            self.click(self.PREVIOUS_BUTTON)
            self.temp_sleep()
        except Exception:
            raise

