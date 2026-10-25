my_dict={}
my_dict={
    "name": "Shreeja",
    "age":11 ,
    "city": "Mumbai",
    "role": "Student",
    "school": "PCS",
} 
print("Available keys to search:", list(my_dict.keys())) 
search_key = input("Enter the key you want to look up: ")    
value = my_dict.get(search_key, "Key not found in the dictionary.")   
print(value) 
result = my_dict()
print("Result:", result)
