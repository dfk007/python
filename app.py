# Exercise


weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print(f"The weight in Lbs is {converted}")
else:
    converted = weight * 0.45
    print(f"The weight in Kgs is {converted}")
