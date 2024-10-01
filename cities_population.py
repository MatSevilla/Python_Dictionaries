cities_population = {
    "Tokyo": 13929286,
    "Delhi": 16787941,
    "Shanghai": 24183300,
    "São Paulo": 12176866,
    "Mexico City": 9209944,
    "Cairo": 9500000,
    "Mumbai": 12442373,
    "Beijing": 21542000,
    "Dhaka": 8906039,
    "Osaka": 2744000
}
print(cities_population)
print("the 6th city population is",cities_population["Cairo"])
cities_population["Delhi"] = "200000"
print(cities_population)
del cities_population["Dhaka"]
print(cities_population)
last_item = list(cities_population.items())[-1]
print("Last city and population:", last_item)
