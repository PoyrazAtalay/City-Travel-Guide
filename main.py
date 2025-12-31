#330201054
#330201062


# Reads the file and returns the cities dictionary
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
        cities[lines[a][0]] = {
            "name" : lines[a][1],
            "country" : lines[a][2],
            "population": lines[a][3],
            "tags" : tags
        }

    return cities
