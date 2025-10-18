from utilities.driver_factory import get_driver
from utilities.config import BASE_URL
from pages.home_page import HomePage
import time

# Quick manual test to verify page objects work
if __name__ == "__main__":
    print("Testing page objects...")
    driver = get_driver('chrome')
    print("Driver initialized successfully!")
    
    driver.get(BASE_URL)
    print(f"Navigated to: {BASE_URL}")
    print(f"Page title: {driver.title}")
    
    # Test search functionality
    home = HomePage(driver)
    print("\nTesting search functionality...")
    home.search("batman")
    print("Searched for 'batman'")
    time.sleep(3)  # Wait to see results
    
    driver.quit()
    print("\nDriver closed. Test successful!")

