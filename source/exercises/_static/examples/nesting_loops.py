def main():

    # this is #1 - I'll call it "CN"
    for c in ('A', 'B', 'C', 'D', 'E'):
        for n in range(1, 4):
            print(f"{c} {n}")


    print("\n")

    # this is #2 - I'll call it "AB"
    for a in range(1, 4):
        for b in range(1, 4):
            print(f"{a}-{b} ", end="")
        # You will add a line of code here.

    print("\n")


if __name__ == "__main__":
    main()