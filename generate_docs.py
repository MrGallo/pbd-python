import json
import pathlib
import shutil
import os
from typing import List

from slugify import slugify

DOCS_DIR = pathlib.Path("docs/")
ROOT_DIR = pathlib.Path("source/")
EXERCISES_DIR = ROOT_DIR / "exercises"
INDEX_PATH = pathlib.Path("exercise_index.json")

ROOT_DIR.mkdir(parents=True, exist_ok=True)
EXERCISES_DIR.mkdir(parents=True, exist_ok=True)


def generate_docs():
    print("GENERATING DOCS")
    remove_docs()
    remove_section_index_files()

    with open(INDEX_PATH, "r") as f:
        exercises = json.load(f)

    # GENERATE DOCUMENTATION
    not_found = []

    current_section = exercises[0]["section"]
    sections = [slugify(current_section)]
    current_total = [0, 0]
    current_section_links = ""
    for ex in exercises:
        md_file_path = pathlib.Path(EXERCISES_DIR / f"{slugify(ex['name'])}.md")
        if not md_file_path.exists():
            not_found.append(md_file_path)

        if current_section != ex["section"]:
            write_section(current_section, current_total, current_section_links)
            
            current_section = ex["section"]
            sections.append(slugify(current_section))
            current_section_links = ""
            current_total = [0, 0]

        if ex["published"] is False:
            continue
            
        try:
            points = int(ex['points'])
            current_total[0] += points
            current_total[1] += points
        except ValueError:
            low, high = tuple(map(int, ex['points'].split("-")))
            points = ex['points']
            current_total[0] += low
            current_total[1] += high
        
        current_section_links += f"    {ex['name']} ({points} points) <exercises/{slugify(ex['name'])}>\n"
    
    # write last section
    write_section(current_section, current_total, current_section_links)
    create_root_index(sections)
    create_nojekyll()


def remove_docs():
    shutil.rmtree(DOCS_DIR)

def remove_section_index_files():
    for file in os.listdir(ROOT_DIR):
        if not file.endswith(".rst"):
            continue
        print(f"Removing: {ROOT_DIR / file}")
        os.remove(ROOT_DIR / file)


def create_nojekyll():
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    with open(DOCS_DIR / ".nojekyll", 'w') as f:
        f.write("\n")


def write_section(current_section, current_total, current_section_links):
    low, high = current_total
    if low == high:
        section_points = str(low)
    else:
        section_points = f"{low}-{high}"
    
    title = current_section + f" ({section_points} points)"
    current_section_index = f"{title}\n{'=' * len(title)}\n\n.. toctree::\n    :maxdepth: 1\n\n"
    current_section_index += current_section_links

    file_name = slugify(current_section) + ".rst"

    with open(ROOT_DIR / file_name, "w") as f:
        f.write(current_section_index)


def create_root_index(sections: List[str]):
    contents = """Python Fundamental Exercises
============================

.. toctree::
    :maxdepth: 2
    :numbered: 1

"""
    for sec in sections:
        contents += f"    {sec}\n"
    
    with open(ROOT_DIR / "index.rst", "w") as f:
        f.write(contents)


if __name__ == "__main__":
    generate_docs()


# print(*no_markdown, sep="\n")
# print("-" * 50)
# print(*not_found, sep="\n")
