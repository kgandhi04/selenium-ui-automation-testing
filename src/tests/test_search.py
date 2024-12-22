import pytest
from selenium import webdriver
from src.pages.homepage import HomePage

class TestSearch:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.home_page = HomePage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_search_functionality(self):
        self.home_page.load("https://www.wikipedia.org")
        self.home_page.search("Python (programming language)")
        assert "Python" in self.driver.title
