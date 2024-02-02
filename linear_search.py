def linear_search(value_to_find, array_to_search_through):
    # your code here
    my_list=array_to_search_through

    for i, x in enumerate(my_list):
        if x == value_to_find:
           return i
    return None
    

def linear_search_global(value_to_find, array_to_search_through):
    # your code here
    my_list = array_to_search_through
    result_list = []
    for i, x in enumerate(my_list):
        if x == value_to_find:
            result_list.append(i)
    return result_list  
   

# print(linear_search(3,[1,2,3])) 
print(linear_search_global("a", ["b", "a", "n", "a", "n", "a", "s"]))
