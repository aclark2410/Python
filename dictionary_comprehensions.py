# Dictionary Comprehensions = create dictionaries using an expression
#                             can replace for loops and certain lambda functions

# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}

# Example 1) dictionary = {key: expression for (key,value) in iterable}

cities_in_farenheit = {"New York": 32,
                       "Boston": 75,
                       "Los Angles": 100,
                       "Chicargo": 50
                       }

# We will create another dictionary which contains the same cities but with temperatures in celcius 

cities_in_celcius = {key: round((value-32)*(5/9)) for (key,value) in cities_in_farenheit.items()}

print(cities_in_celcius)


# Example 2) dictionary = {key: expression for (key,value) in iterable if conditional}

weather = {"New York": "snowing",
           "Boston": "sunny",
           "Los Angles": "Sunny",
           "Chicargo": "cloudy"}

sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}

print(sunny_weather)


# Example 3) dictionary = {key: (if/else) for (key,value) in iterable}

# We will replace the value of the temperature with a description of the temperature depending if it is warm or cold

weather_description = {key: "Warm" if value >= 20 else "Cold" for (key,value) in cities_in_celcius.items()}

print(weather_description)


# Alternatively if the dictionary comprehension becomes to complex, we can define a function for the if/else conditional and simply call it inside of the dictionary comprehension

weather_function = lambda value: "Warm" if value >= 20 else "Cold"

weather_description_alternative = {key: weather_function(value) for (key,value) in cities_in_celcius.items()}

print(weather_description_alternative)