animal_sounds = {
    "Dog": "Bark",
    "Cat": "Meow",
    "Cow": "Moo",
    "Sheep": "Baa",
    "Duck": "Quack",
    "Pig": "Oink",
    "Lion": "Roar",
    "Frog": "Ribbit"
}
print(animal_sounds)
print("4th animals sound", animal_sounds["Cow"])
animal_sounds["lion"] = "meow"
print(animal_sounds)
del animal_sounds["Pig"]
print(animal_sounds)
print("last animal_sounds:", list(animal_sounds.items())[-1])