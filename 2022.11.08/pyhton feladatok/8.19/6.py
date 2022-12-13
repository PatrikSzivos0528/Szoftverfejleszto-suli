# This program prints a multiplication table for the numbers 1-10

# Print the header row
print("  |", end="")
for i in range(1, 13):
    print(f"{i:>3}", end="")
print()

# Print a separator row
print("-" * 25)

# Print the multiplication table rows
for i in range(1, 11):
    print(f"{i:>2}|", end="")
    for j in range(1, 13):
        print(f"{i * j:>3}", end="")
    print()
