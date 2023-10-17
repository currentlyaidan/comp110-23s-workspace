"""Using for/in loops."""

pets: list[str] = ["Louie", "Bo", "Bear"]

for name in pets:
    print(f"Good boy, {name}!")

names: list[str] = ["Alyssa", "Janet","Vrinda"]
for idx in range(0,3):
    name: str = names[idx]
    print(f"{idx}: {name}")