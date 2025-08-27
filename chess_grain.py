def compound_by_period(principal, rate, periods):
    return principal * (1 + rate) ** periods

# Starting with 1 grain, doubling each square
wheat = [compound_by_period(1, 1.0, i) for i in range(64)]

# Sum the total number of grains
total_wheat = sum(wheat)

# Print each square and the total
print("Grains on each square:")
print(wheat)
print(len(wheat))
print("\nTotal grains on all 64 squares:")
print(int(total_wheat))
