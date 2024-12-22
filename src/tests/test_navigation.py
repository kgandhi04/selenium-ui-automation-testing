import pytest
from selenium import webdriver
from src.pages.homepage import HomePage
from src.pages.article_page import ArticlePage

class TestNavigation:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.home_page = HomePage(self.driver)
        self.article_page = ArticlePage(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_section_navigation(self):
        self.home_page.load("https://www.wikipedia.org")
        self.home_page.search("Python (programming language)")
        self.article_page.navigate_to_section("History")
        assert "History" in self.driver.current_url
