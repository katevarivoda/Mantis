__author__ = 'Ekaterina'

# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)


    def test_add_project(self):
        wd = self.wd
        wd.get("http://localhost/mantisbt-1.2.20/login_page.php")


        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys("Key")
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

        print('Ok')



    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
