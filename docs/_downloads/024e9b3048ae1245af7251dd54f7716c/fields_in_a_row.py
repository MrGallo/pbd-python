def print_row() -> None:
    """Print out a dictionary's fields in a single row.

    Args:
        dictionary (dict): The dictionary to print out.
        fields (List[str]): A list of field names to print out
            in order.
    """
    pass


car = {
    "model": "Prius",
    "make": "Toyota",
    "color": "grey"
}

fields = ["make", "model"]

# print table header
print("\t".join(fields))
print("\t".join(["-" * len(title) for title in fields]))

# print single row
print_row(car, fields)
