from typing import Dict, List
import json


def main():
    with open("exercises-2.json", "r") as f:
        exercises = json.load(f)
    
    print("These are the most difficult dictionary exercises:")
    difficult_and_published = []  # call filter_difficult_and_published here
    for ex in difficult_and_published:
        print("\t- " + ex["name"])


def filter_difficult_and_published(exercises: List[Dict]) -> List[Dict]:
    """COMPLETE THIS DOCSTRING"""
    filtered = []
    for ex in exercises:
        filtered.append(ex)
    
    return filtered


def is_difficult(exercise: Dict) -> bool:
    """Determines if an exercise is difficult.

    A difficult exercise is one of 50 or more points.

    Args:
        exercise (Dict): An exercise dictionary.
    
    Returns:
        True if difficult, false otherwise.
    """
    return True


def is_published(exercise: Dict) -> bool:
    """COMPLETE THE DOCSTRING"""
    return True


if __name__ == "__main__":
    main()