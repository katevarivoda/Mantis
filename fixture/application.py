__author__ = 'Ekaterina'

from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
import pytest


class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        # self.contact = ContactHelper(self)
        self.base_url = base_url

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/my_view_page.php") and len(
                wd.find_elements_by_xpath("//tr[3]/td/table/tbody/tr/td") > 0)):
            wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
