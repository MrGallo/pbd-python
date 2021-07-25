import json
import re
import os

ROOT_DIR = 'source/exercises'

# files = []
# for item in os.listdir(ROOT_DIR):
#     if item.endswith(".md"):
#         files.append(item)

# with open("index.rst", "w") as f:
#     for file in files:
#         i = file.index("-") + 1
#         os.rename(f"{ROOT_DIR}/{file}", f"{ROOT_DIR}/{file[i:]}")
#         # f.write(file[i:-3] + "\n")

# with open(f"{ROOT_DIR}/exercise_index.json", "r") as f:
#     exercises = json.load(f)

# sections = []
# last_section = None
# for ex in exercises:
#     number = ex["number"]
#     section = ex["section"]
#     if last_section is None or section != last_section:
#         last_section = section
#     # if section not in sections:
#         while section in sections:
#             section += "I"
#         sections.append(section)

# print(*sections, sep="\n")


# sections = """Basics and Printing
# Variables
# Keyboard Input
# If Statements
# GUIs
# If Statements II
# Random Numbers
# While Loops
# Post-test Loops
# While Loops II
# For Loops
# Random Numbers II
# Projects
# Graphics
# Functions
# Post-test Loops II
# Projects II
# For Loops II
# Nested Loops
# File RW
# Lists
# Sorting
# Records
# Sorting II
# Objects
# ArrayLists
# Projects III
# Project Euler
# Graphics II
# Projects IIII""".split("\n")

# from slugify import slugify

# for sec in sections:
#     print(slugify(sec))
#     with open(f'source/{slugify(sec)}.rst', 'w') as f:
#         f.write(sec + "\n")
#         f.write("=" * len(sec) + "\n")
#         f.write(".. toctree::\n    :maxdepth: 1\n\n")


# regex = r"`[0-9]{3}_(.+.py)`"
# subst = "`\\1`"
# regex = r"\((examples/.+)\)"
# subst = "(../_static/\\1)"

# regex = r"\[[0-9]{3}_(.+)\]\((.+)[0-9]{3}_(.+)\)"
# subst = "[\\1](\\2\\3)"

# regex = r"\* \[(.+)\]\(../_static/(.+)\)"
# subst = "```eval_rst\\n* :download:`\\1 <\\2>`\\n```"

## Iterate through exercise files and regex sub it's source
# for file in os.listdir(ROOT_DIR):
#     if not file.endswith(".md"):
#         continue

#     with open(ROOT_DIR + "/" + file, 'r') as f:
#         source = f.read()

#     result = re.sub(regex, subst, source, 0, re.MULTILINE)

#     if result != source:
#         with open(ROOT_DIR + "/" + file, 'w') as f:
#             f.write(result)
#         print(f"Changed: {file}")


# for file in os.listdir(ROOT_DIR):
#     if not file.endswith(".md"):
#         continue

#     with open(ROOT_DIR + "/" + file, 'r') as f:
#         source = f.read()

#     if "../_static/" in source:
#         print(file)


# for file in os.listdir(ROOT_DIR + "/examples"):
#     try:
#         int(file[:3])
#     except ValueError:
#         pass
#     else:
#         new_name = file[4:]
#         print(f"{file} => {new_name}")
#         os.rename(ROOT_DIR + "/examples/" + file, ROOT_DIR + "/examples/" + new_name)
