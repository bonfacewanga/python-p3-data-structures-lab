spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # We have a list of dictionaries, we're looking for specific key values, we can loop through each dictionary, and access each key and its value
    # We can also use .items(), to access the keys and value independently, without needing the otherwise a[b],
    
    # names = [key for key, value in spicy_foods.items()]
    # return names

    names = [spicy_food['name'] for spicy_food in spicy_foods]
    return names


def get_spiciest_foods(spicy_foods):
    spicy = [spicy_food for spicy_food in spicy_foods if spicy_food['heat_level'] > 5]
    return spicy

def print_spicy_foods(spicy_foods):
     for food in spicy_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")

# def get_spicy_food_by_cuisine(spicy_foods, cuisine):
#     food_cuisine = [spicy_food for spicy_food in spicy_foods if spicy_food['cuisine'] == cuisine]
#     return food_cuisine


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
     for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
     for food in spicy_foods:
        if food["heat_level"] > 5:
            heat_level_emojis = "🌶" * food["heat_level"]
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")


def get_average_heat_level(spicy_foods):
    total_heat = sum(spicy_food['heat_level'] for spicy_food in spicy_foods)
    average_heat_level = total_heat / len(spicy_foods)
    return average_heat_level
# Notice, it's not total_heat = [sum.....] because that would mean in the average_heat_level, we'll be dividing the length of spicy_foods against a list, coz remember, list comprehensions return lists, so it basically looks like -- [] / len(spicy_foods)
# And that's not math, so we do away with the [] to not make it a list comprehension, so that now we're dividing numbers with numbers,
   #   --- like (10 + 12 + 15) / 6


def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_foods = spicy_foods.copy()
    new_spicy_foods.append(spicy_food)
    return new_spicy_foods
