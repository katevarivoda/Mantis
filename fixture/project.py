__author__ = 'Ekaterina'


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def redirect_to_manage_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create_project(self, project):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.change_field_value("name", project.Name)
        self.change_field_value("description", project.Description)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()



