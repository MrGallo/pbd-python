my_list = [45, 87, 39, 32, 93, 86, 12, 44, 75, 50]

# Display the original (unsorted values)
print("before: ", end="")
for n in my_list:
    print(f"{n} ", end="")
print()

# Exchange sort inner loop here...
"""
marker = 0
for ...  # start from marker + 1
    if marker value is greater...
        # swap the values in the two slots
"""

# Display the values again, now after ONE PASS of the exchange sort algorithm.
print("after : ", end="")
for n in my_list:
    print(f"{n} ", end="")
print()