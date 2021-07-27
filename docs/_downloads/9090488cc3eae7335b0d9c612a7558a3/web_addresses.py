import requests


class Address:
    street: str
    city: str
    state: str
    zip: int


def main():
    r = requests.get("https://raw.githubusercontent.com/MrGallo/pbd-python/master/web-files/fake-addresses.txt")
    file_lines = r.text.split("\n")

    one = Address()
    one.street = file_lines[0]
    one.city   = file_lines[1]
    one.state = file_lines[2][:2]
    one.zip    = int(file_lines[2][3:])

    two = Address()
    two.street = file_lines[3]
    two.city   = file_lines[4]
    two.state = file_lines[5][:2]
    two.zip    = int(file_lines[5][3:])

    three = Address()
    three.street = file_lines[6]
    three.city   = file_lines[7]
    three.state = file_lines[8][:2]
    three.zip    = int(file_lines[8][3:])

    print(f"{one.street}, {one.city}, {one.state} {one.zip}")
    print(f"{two.street}, {two.city}, {two.state} {two.zip}")
    print(f"{three.street}, {three.city}, {three.state} {three.zip}")


if __name__ == "__main__":
    main()