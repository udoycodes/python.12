#Ask user for their name
name= input("What's your name?").strip().title()

#Split user's name into first and last name
first_name, last_name = name.split(" ")

#Say hello to the user
print(f"Hello, {first_name}")