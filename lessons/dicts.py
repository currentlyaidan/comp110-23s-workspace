"""Practice with dictionaries."""

# Create a new dictionary.
ice_cream: dict[str,int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
ice_cream["mint"] = 3
print(ice_cream)
ice_cream.pop("mint")
ice_cream["vanilla"] = 10
print(f"There are {ice_cream['chocolate']} orders of chocolate")
print(ice_cream)
print(len(ice_cream))
if "mint" in ice_cream:
    print(f"There are {ice_cream['mint']} orders of mint.")
else:
    print("There are no orders of mint.")
for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders.")