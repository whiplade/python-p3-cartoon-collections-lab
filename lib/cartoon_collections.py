def roll_call_dwarves(names):
    for i, name in enumerate(names, 1):
        print(f"{i}. {name}")

def summon_captain_planet(planeteer_calls):
    capitalized_words = [word.capitalize() + '!' for word in planeteer_calls]
    return capitalized_words

def long_planeteer_calls(words):
    return any(len(word) > 4 for word in words)

def find_the_cheese(soups):
    cheese_options = {"cheddar", "gouda", "camembert"}
    common_cheeses = cheese_options & set(soups)
    if common_cheeses:
        return common_cheeses.pop()
    else:
        return None