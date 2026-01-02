#330201054
#330201062


FILE = "cities.txt"

# Reads the file and returns the cities dictionary.
def load_cities_from_file(filename):
    cities = {}
    lines = []

    with open(filename, "r") as f:
        file = f.readlines()
        
        for i in range(len(file)):
            line = file[i].strip()
            line = line.replace(";", ",").split(",")
            lines.append(line)

    for a in range(len(lines)):
        tags = set()
        for b in range(len(lines[a])-4):
            tags.add(lines[a][b+4])
        cities[int(lines[a][0])] = {
            "name" : lines[a][1],
            "country" : lines[a][2],
            "population": float(lines[a][3]),
            "tags" : tags
        }

    return cities


# Adds a new city to the dictionary.
def add_city(cities:dict, city_id:int, name:str, country:str, population:float):
    if city_id in cities.keys():
        print("This city already exists.")
    else:
        cities[city_id] = {
            "name" : name,
            "country" : country,
            "population" : population,
            "tags" : set()
        }


# Removes the city with the given id from the dictionary.
def remove_city(cities:dict, city_id:int):
    try:
        del cities[city_id]
    except:
        print("This city does not exist.")


# Adds a tag to the given city's tag set.
def add_tag(cities:dict, city_id:int, tag:str):
    try:
        cities[city_id]["tags"].add(tag)
    except:
        print("This city does not exist.")


# Removes the given tag from the city’s tag set.
def remove_tag(cities:dict, city_id:int, tag:str):
    # Checking the city.
    try:
        test = cities[city_id]
    except:
        print("This city does not exist.")

    # Real purpose
    try:
        cities[city_id]["tags"].remove(tag)
    except:
        print("This tag does not exist.")


# Prints the current cities data.
def print_cities(cities:dict):
    print(f"{'CityID':^8} | {'Name':^10} | {'Country':^20} | {'Population':^15} | {'Tags'}")
    print("-" * 100)

    for city_id, info in cities.items():
        print(f"{city_id:^8} | {info['name']:^10} | {info['country']:^20} | {info['population']:^15} | {info["tags"]}")


# Creating a list of city IDs.
city_ids = list(load_cities_from_file(FILE).keys())


# Performs an iterative linear search on a list of city IDs.
def linear_search_iterative(city_ids, target_id):
    for i in range(len(city_ids)):
        if target_id == city_ids[i]:
            return i
    return -1

# Performs a recursive linear search on a list of city IDs.
def linear_search_recursive(city_ids, target_id, index=0):
    if index == len(city_ids):
        return -1
    elif city_ids[index] == target_id:
        return index
    return linear_search_recursive(city_ids, target_id, index+1)






