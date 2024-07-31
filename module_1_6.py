my_dict = {"Denis": 1983 , "Vova": 1995, "Anton": 2010 }
print(my_dict)
print("Existing value:", my_dict ["Denis"])
print("Not existing value:", my_dict .get("Max"))
my_dict .update({"Danil": 2015, "Roma": 1975})
print("Deleted value:", my_dict .pop("Vova"))
print("Modified dictionary: ", my_dict)
print()

my_self = {1, 2, 2, 3, 4, 5, 5.25, 5, 1, 2, 3, 3, 4, "string"}
print(my_self)
my_self .add((10, 100))
my_self .discard(5)
print(my_self)












