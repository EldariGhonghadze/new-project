1.

car = 'subaru'
print("Is car == 'subaru'?  True.")
print(car == 'subaru')
print("Is car == 'audi'?  False.")
print(car == 'audi')

car = 'bmw'
print("Is car == 'bmw'?  True.")
print(car == 'bmw')
print("Is car == 'vw'?  False.")
print(car == 'vw')


car = 'mercedes'
print("Is car == 'mercedes'?  True.")
print(car == 'mercedes')
print("Is car == 'jaguar'?  False.")
print(car == 'jaguar')

person = 'humanity'
print("Is person == 'humanity'?  True.")
print(person == 'humanity')
print("Is person == 'terrible'?  False.")
print(person == 'humanity')

person = 'hard working'
print("Is person == 'hard working'?  True.")
print(person == 'hard working')
print("Is person == 'lazy'?  False.")
print(person == 'lazy')

person == 'hard working'
if person == 'hard working':  # kargad ver mivxvdi am stilshi unda gameketebina tu zemot rogorc maqvs ise amitom es erti magaliti davtove aq.
    print('true')
elif person == 'lazy':
    print('false')


2.

car_brand = "Toyota"
bike_brand = "Honda"
print("Equality Test:")
print(car_brand == "Toyota")
print(car_brand == "Tesla")

print("\nInequality Test:")
print(car_brand != "BMW")
print(car_brand != "Toyota")


print("\nLowercase Test:")
username = "michael"
print(username.lower() == "michael")
print(username.lower() == "michael")


age = 25
print("\nNumerical Tests:")
print(age == 25)
print(age != 30)
print(age > 20)
print(age < 30)
print(age >= 25)
print(age <= 25)


x = 5
y = 10
print("\n'and' and 'or' Tests:")
print(x > 3 and y > 5)
print(x > 7 and y < 15)
print(x > 7 or y < 15)
print(x < 3 or y < 15)


fruits = ["apple", "banana", "orange"]
print("\nList Membership Test:")
print("banana" in fruits)
print("grape" in fruits)


print("\nList Non-Membership Test:")
print("kiwi" not in fruits)
print("orange" not in fruits)


3.

alien_color = 'green'
if alien_color =='green':
    print('player earned 5 point')


alien_color = 'green'
if alien_color =='red':
    print('fail')

4.

alien_color = 'green'
if alien_color =='green':
    print('player earned 5 point')
else:
    print('player earned 10 point')


alien_color = 'red'

if alien_color == 'green':
    print(" You just earned 5  point")
else:
    print(" You just earned 10 points.")

5.

alien_color = 'green'

if alien_color == 'green':
    print(" earned 5 points.")
elif alien_color == 'yellow':
    print(" earned 10 points n.")
else:
    print(" earned 15 pointsn.")


alien_color = 'yellow'

if alien_color == 'green':
    print(" earned 5 points.")
elif alien_color == 'yellow':
    print(" earned 10 points n.")
else:
    print(" earned 15 pointsn.")


alien_color = 'red'

if alien_color == 'green':
    print(" earned 5 points.")
elif alien_color == 'yellow':
    print(" earned 10 pointsn.")
else:
    print(" earned 15 pointsn.")

6.

age = 22

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")


7.

favorite_fruits = ["Apple", "Banana", "Mango"]

if "Apple" in favorite_fruits:
    print("You really like apples!")

if "Banana" in favorite_fruits:
    print("You really like bananas!")

if "Orange" in favorite_fruits:
    print("You really like oranges!")

if "Mango" in favorite_fruits:
    print("You really like mangoes!")

if "Grape" in favorite_fruits:
    print("You really like grapes!")


8.

username = ["admin" , "david" , "john" , "serena" , "angelina" ]

for username in username:
    if username == "admin":
        print("Hello admin would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")


9.


'?'


10.

current_users = ["michael" , "kobe" , "lebron" , "kevin" , "shaq" ]
new_users = ["michael" , "scottie" , "lebron" , "hakim" , "oscar" ]


for new_user  in new_users:
    print(f"Sorry, the username '{new_user}' is already taken. Please enter a new username.")
else:
    print(f"The username '{new_user}' is available")


11.

numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
