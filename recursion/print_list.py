cities = ["New York", "London", "Tokyo", "Swat", "Paris"]

def print_list(list , idx=0):
    if(idx == len(list)):
        return
    print(list[idx] ,end=" ")
    print_list(list , idx+1)

print_list(cities)