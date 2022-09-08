# dictionary comprehension: create dictionaries using an expression
# can replace fr loops and certain lambda functions

# dictionary = {key: expression for (key, value) in iterable}
# dictionary = {key: (if/else) for (key, value) in iterable}
# dictionary = {key: function(value) for (key, value) in iterable}
cities_in_F = {
    'new york': 32,
    'boston': 75,
    'los angeles': 100,
    'lchicago': 50,
}

cities_in_C = {k: ((value - 32)*(5/9)) for (k, value) in cities_in_F.items()}
print(cities_in_C)
# -------------------------------------------------------------------------------------------

weather = {
    'New York': "snowing",
    "Boston": "sunny",
    'Los Angeles': 'sunny',
    'Chicago': 'cloudy'
}

sunny_weather = {key: value for (key, value) in weather.items() if value == 'sunny'}
print(sunny_weather)
# -------------------------------------------------------------------------------------------
cities = {
    'new york': 32,
    'boston': 75,
    'los angeles': 100,
    'chicago': 50,
}
desc_cities = {k: ('warm' if v > 40 else 'cold') for (k, v) in cities.items()}
print(desc_cities)
# -------------------------------------------------------------------------------------------
cities2= {
    'new york': 32,
    'boston': 75,
    'los angeles': 100,
    'chicago': 50,
}
def check_temp(value):
    if value >= 70:
        return 'hot'
    elif value >= 40:
        return 'warm'
    else:
        return 'cold'
desc_cities2 = {k: check_temp(v) for (k, v) in cities.items()}
print(desc_cities2)














