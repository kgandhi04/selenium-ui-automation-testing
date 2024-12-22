import pytest
from selenium import webdriver
from src.pages.homepage import HomePage
import yaml

class TestLanguageSwitch:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.home_page = HomePage(self.driver)
        with open("config/config.yaml", "r") as file:
            self.config = yaml.safe_load(file)

    def teardown_method(self):
        self.driver.quit()

    def test_language_switch(self):
        self.home_page.load(self.config['default']['base_url'])
        self.home_page.switch_language(self.config['default']['language'])
        assert self.config['default']['language'] in self.driver.current_url
