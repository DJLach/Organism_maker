import random
random.seed()

def get_organism(organism_list):
    organism = input("What organism type are you selecting?").lower()
    while organism not in organism_list:
        organism = input("What organism type are you selecting?").lower()
    return(organism)

def get_size(organism, size_list):

    if organism == "mammal" or organism == "bird" or organism == "fish":
        size_list.remove("tiny")
    if organism == "amphibian" or organism == "insect" or organism == "arachnid":
        size_list.remove("large")
    if organism == "amphibian" or organism == "insect" or organism == "arachnid" or organism == "reptile" or organism == "huge":
        size_list.remove("huge")
    
    print(size_list)
    size = random.choice(size_list)
    return size

def main():
    
    carnivorous = False
    organism_list = ["mammal", "bird", "reptile", "amphibian", "insect", "arachnid", "fish"]
    size_list = ["tiny", "small", "medium", "large", "huge"]
    food_list = []
    movement_list = ["two legs", "four legs", "wings", "webbed gliders", "fins", "flippers"]
    defense_list = ["armor", "spines", "bite", "claws", "camouflage", "intimidation", "bad taste", "poison", "sting", "hide"]
    cold_list = ["fur or hair", "body fat", "hibernation", "migration"]
    status_list = ["fine", "protected", "endangered", "extinct"]
    
    organism = get_organism(organism_list)

    size = get_size(organism, size_list)

    print(size)

main()