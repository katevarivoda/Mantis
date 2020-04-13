__author__ = 'Ekaterina'


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        # self.app.open_home_page()
        wd.find_element_by_name("username").send_keys("administrator")

        wd.find_element_by_name("password").send_keys("root")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()