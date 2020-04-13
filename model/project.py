__author__ = 'Ekaterina'


class Project:
    def __init__(self, Name=None, Description=None):
        self.Name = Name
        self.Description = Description
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.Name, self.Description)
