from selenium.webdriver.common.by import By

class ArticlePage:
    def __init__(self, driver):
        self.section = (By.ID, "toc")

    def navigate_to_section(self, section_name):
        self.driver.find_element(By.LINK_TEXT, section_name).click()
