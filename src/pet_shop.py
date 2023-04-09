# WRITE YOUR FUNCTIONS HERE
#1
def get_pet_shop_name(cc_pet_shop):
    return cc_pet_shop["name"]

#2
def get_total_cash(cc_pet_shop):
    get_total_cash = cc_pet_shop["admin"]["total_cash"]
    return (get_total_cash)
#3
def add_or_remove_cash(cc_pet_shop, money):
    cc_pet_shop ["admin"]["total_cash"] = cc_pet_shop ["admin"]["total_cash"] + money 
    print(cc_pet_shop["admin"]["total_cash"])
    return cc_pet_shop["admin"]["total_cash"]
#4
def add_or_remove_cash(cc_pet_shop, money):
    cc_pet_shop ["admin"]["total_cash"] = cc_pet_shop ["admin"]["total_cash"] + money 
    print(cc_pet_shop["admin"]["total_cash"])
    return cc_pet_shop["admin"][ "total_cash"]

#5- not working

# def get_pets_sold (cc_pet_shop,sales):
#     sales = (0)
#     cc_pet_shop["admin"]["pets_sold"] += sales
#     print(cc_pet_shop["admin"]["pets_sold"])
#     return cc_pet_shop["admin"]["pets_sold"]

#6 - not working 
# def get_pets_sold (cc_pet_shop,sales):
#     sales = (0)
#     cc_pet_shop["admin"]["pets_sold"] += sales
#     print(cc_pet_shop["admin"]["pets_sold"])
#     return cc_pet_shop["admin"]["pets_sold"]

#7

def get_stock_count(cc_pet_shop):
    return len(cc_pet_shop["pets"])
    print (len(cc_pet_shop["pets"]))

#8


def get_pets_by_breed(cc_pet_shop, breed):
    pets_breed = []
    for pet in cc_pet_shop["pets"]:
        if pet["breed"] == breed:
            pets_breed.append(pet)
    print (pets_breed)
    return pets_breed

#9

#want this to return  list of none if breed isnt there

# def get_pets_by_breed(cc_pet_shop, breed):
#     pets_breed = []
#     for pet in cc_pet_shop["pets"]:
#         if pet["breed"] == breed:
#             pets_breed.append(pet)
#     print (pets_breed)
#     return pets_breed

#10

# def find_pet_by_name(cc_pet_shop, name):
#     pets_in_shop = [0]
#     for name in cc_pet_shop:
#         return pets_in_shop


#12