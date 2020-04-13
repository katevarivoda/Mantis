__author__ = 'Ekaterina'

import getopt
import json
import os.path
import random
import string
import sys

import jsonpickle

from model.project import Project

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of projects", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/projects.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Project(Name = "", Description = "")] + [
    Project(Name = random_string("name", 10), Description = random_string("description", 10))
    for i in range(n)
]

# .. в этом случаей - переход на корневую директорию:
file = 'C:/Users/user/PycharmProjects/Mantis/data/projects.json'
# открываем файл на запись:
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent = 2)
    out.write(jsonpickle.encode(testdata))
