import requests
from typing import List


def main():
    adjectives = list_from_url("https://raw.githubusercontent.com/MrGallo/pbd-python/master/web-files/adjectives.txt")
    nouns = list_from_url("https://raw.githubusercontent.com/MrGallo/pbd-python/master/web-files/nouns.txt")

    print("Random Movie Title Generator\n")

    print(f"Choosing randomly from {len(adjectives)} adjectives ", end="")
    print(f"and {len(nouns)} nouns ({len(adjectives) * len(nouns)} combinations).")

    adjective = "Flappy"
    noun = "Hummingbird"

    print(f"Your movie title is: {adjective} {noun}")


def list_from_url(url) -> List[str]:
    """Gets a string list from a file served on the web.
    
    Args:
        url: the URL that points to the hosted file.
    
    Returns:
        A string list of all the lines in the file.
    """
    r = requests.get(url)
    contents = r.text.strip()
    word_list = []
    for line in contents.split("\n"):
        word_list.append(line)

    return word_list



if __name__ == "__main__":
    main()