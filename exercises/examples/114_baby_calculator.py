def main():
    while True:
        a, op, b = input("> ").split(" ")
        a = float(a)
        b = float(b)

        if op == "+":
            c = a + b
        else:
            print(f"Undefined operator: '{op}'.")
            c = 0

        print(c)


if __name__ == "__main__":
    main()