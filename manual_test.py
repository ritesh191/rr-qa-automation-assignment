from utilities.driver_factory import get_driver
from utilities.config import BASE_URL

# Quick manual test to verify driver works
if __name__ == "__main__":
    print("Testing driver factory...")
    driver = get_driver('chrome')
    print("Driver initialized successfully!")
    
    driver.get(BASE_URL)
    print(f"Navigated to: {BASE_URL}")
    print(f"Page title: {driver.title}")
    
    driver.quit()
    print("Driver closed. Test successful!")

