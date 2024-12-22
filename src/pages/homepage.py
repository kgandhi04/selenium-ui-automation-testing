from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.ID, "searchInput")
        self.search_button = (By.XPATH, "//button[@type='submit']")
        self.language_dropdown = (By.ID, "js-lang-list-button")

    def load(self, base_url):
        self.driver.get(base_url)

    def search(self, keyword):
        self.driver.find_element(*self.search_box).send_keys(keyword)
        self.driver.find_element(*self.search_button).click()

    def switch_language(self, language_code):
        self.driver.find_element(*self.language_dropdown).click()
        self.driver.find_element(By.CSS_SELECTOR, f"a[lang='{language_code}']").click()
