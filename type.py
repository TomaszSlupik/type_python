# Dodawanie int + float => Wynik float 
x= int (10)
y = float(3.00)
z = x + y
print(type(z))

print('---')

# Napisz program, który przyjmie a i b i zwróci sumę, różnicę, a / b, a * b, a do potegi b, 
# dzielenie bez reszty 
a =  2
b = 4

mySum  = a + b
myDifference = a - b
myDivide  = a / b
myMultiplication = a * b
myPower = a ** b 
myDivideNext = a // b

print (mySum, myDifference, myDivide, myMultiplication, myPower)
print('---')

# Printowanie w jednej lini
print("test,", end="")
print("test2")

print('---')

# Odwoływanie sie do konkretnej litery 
name = 'Ala ma kota'
print(name [0])
print(name[2])
print(name[-2])

# Slice 
print(name[:3])
print(id(name))

print('---')

# Listy
myList = [2, 3]
secondList = list("Ala")
marks = [1, 2, 3, 4, 5]

print(myList)
print(secondList)
print(marks[-1])

print('---')

# Te same id - Napisy (non- mutable)
apple = 'jabłko'
appleTwo = apple[:]

print(id(apple))
print(id(appleTwo))
print(apple == appleTwo)

# Różna id: - listy (mutable)

# Sprawdzenie zawartości obiektów:
#  == porównujemy zawartośc , a is sprawdza ID również + zawartość
food = ['pomarańcza', 'jablko']
foodTwo = food[:]

print(id(food))
print(id(foodTwo))
print(f"Sprawdzenie id True or False: {food is foodTwo}")

print('---')

#  