countries_capitals = {
    "United States": "Washington, D.C.",
    "Canada": "Ottawa",
    "United Kingdom": "London",
    "Australia": "Canberra",
    "Germany": "Berlin",
    "France": "Paris",
    "Japan": "Tokyo",
    "India": "New Delhi",
    "Brazil": "Brasília",
    "South Africa": "Pretoria",
    "Russia": "Moscow",
    "Mexico": "Mexico City"
}
print(countries_capitals)
print("5th country capital is",countries_capitals["Germany"])
countries_capitals["India"] = "manila"
print(countries_capitals)
del countries_capitals["Russia"]
print(countries_capitals)
print("last key value is ",list(countries_capitals.items())[-1])
