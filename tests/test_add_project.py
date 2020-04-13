__author__ = 'Ekaterina'

from model.project import Project
import pytest


def test_add_project(app, json_projects):
    project = json_projects
    app.project.redirect_to_manage_projects_page()
    app.project.create_project(project)
