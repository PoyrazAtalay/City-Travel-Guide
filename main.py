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


# Performs an iterative binary search on a list of city IDs.
def binary_search_iterative(city_ids, target_id):
    city_ids = sorted(city_ids)
    left = 0
    right = len(city_ids) - 1
    while left <= right:
        mid = (left + right) // 2
        if city_ids[mid] == target_id:
            return mid
        elif city_ids[mid] < target_id:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Performs a recursive binary search on a list of city IDs.
def binary_search_recursive(city_ids, target_id, left=0, right=len(city_ids)-1):
    city_ids = sorted(city_ids)
    if right >= left:
        mid = (left + right) // 2
        if city_ids[mid] == target_id:
            return mid
        elif city_ids[mid] < target_id:
            return binary_search_recursive(city_ids, target_id, mid+1, right)
        else:
            return binary_search_recursive(city_ids, target_id, left, mid-1)
    else:
        return -1


# Main function
def main():
    cities = load_cities_from_file(FILE)
    print_cities(cities)
    print("\nAdding a new city named Istanbul\n")
    add_city(cities,1011,"Istanbul","Turkey",15.6)
    print_cities(cities)
    print("\nRemoving the city with id 1008\n")
    remove_city(cities,1008)
    print_cities(cities)
    print("\nAdding tags to city with id 1011\n")
    add_tag(cities,1011,'crowded')
    add_tag(cities,1011,'seaside')
    print_cities(cities)
    print("\nRemoving tags from city with id 1001\n")
    remove_tag(cities,1001,"historical")
    print_cities(cities)
    print(f"\nindex of id 1001 is {linear_search_iterative(city_ids,1001)}")
    print(f"index of id 1002 is {linear_search_recursive(city_ids,1002)}")
    print(f"index of id 1003 is {binary_search_iterative(city_ids,1003)}")
    print(f"index of id 1004 is {binary_search_recursive(city_ids,1004)}")

main()






