# Dodawanie int + float => Wynik float
x = int(10)
y = float(3.00)
z = x + y
print(type(z))

print('---')

# Napisz program, który przyjmie a i b i zwróci sumę, różnicę, a / b, a * b, a do potegi b,
# dzielenie bez reszty
a = 2
b = 4

mySum = a + b
myDifference = a - b
myDivide = a / b
myMultiplication = a * b
myPower = a ** b
myDivideNext = a // b

print(mySum, myDifference, myDivide, myMultiplication, myPower)
print('---')

# Printowanie w jednej lini
print("test,", end="")
print("test2")

print('---')

# Odwoływanie sie do konkretnej litery
name = 'Ala ma kota'
print(name[0])
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

#  Lista - apend - dodawanie - mutable
myList = []
myList.append('truskawka')

print(myList)
# Lista - count - zliczanie elementów
countStrawbery = myList.count('truskawka')
print(countStrawbery)

# Lista - extend - dodawanie
myList.extend(['jabłko', 'banan'])
print(myList)

# Lista - clear - czyszczenie
myList.clear()
print(myList)

# Lista - remove - co chcemy usunąc
marks = [6, 2, 1]
marks.remove(1)
print(marks)
marks.remove(marks[0])
print(marks)

# Lista - insert - dodawanie do listy na konkretne miejsce
watch = ['garmin']

watch.insert(0, 'polar')

print(watch)

# Lista - Sortowanie
drink = ['kawa', 'piwo', 'coca-cola']
drink.sort(reverse=False)
print(drink)

# Wrzucenie do Listy - split
name = 'Tomek jest na zajęciach'

print(name.split(" "))

print('---')

# Część wspolna :
a = [1, 2]
b = [2, 3]
c = [i for i in a if i in b]
print(c)

# sortowanie można tylko ten sam TYP danych !

# PĘTLA WHILE I FOR
a = 10

while a >= 0:
    print('Powtarza')
    break

# Pętla for
name = 'Ala ma kota'

for x in name:
    print(x, end=" ")

print("")
marks = [1, 4, 6]

for mark in marks:
    print(mark)

print('---')

# Pętla for 2 - wykonywanie ilość razy
name = 'coca cola'
for x in range(2):
    print(name)

for i in range(10, 15):
    print(i)

x = 4
while x > 0:
    print(x)
    x -= 1

print('---')

num = 1

# Wydrukuj takie cos:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# I sposób
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print('---')

# II sposób
for i in range(1, 6):
    numbers = [str(num) for num in range(1, i + 1)]
    print(" ".join(numbers))


print('---')
# Krotka - non- mutable - nie są mutowalne
# Ale jak chce dodać to mogę obejść:
myTuple = (1, 2, 3)
newTuple = myTuple + (4,)

print(newTuple)

# Słowniki - mutable
marks = {"1": "niedostateczny", "2": "dopuszczający"}
print(marks)
print(marks['2'])

# słownik - dodawanie
marks.update({"3": "dostateczzny"})

print(marks)

# usuwanie - pop
marks.pop("2")
print(marks)

# słownik - klucze
print(marks.keys())

# słownik wartości
print(marks.values())
print('---')

# Funkcje - zbieranie instrukcji
def fun1(*args):
    return f"{args}"

print(fun1('gruszka', 'jabłko'))


def fun2 (a, b):
    return a + b

print(fun2('2', '4'))
print(fun2((1, 2), (3, 4)))

# funkcja defaultowa 
def swim(a ='Pływamy rano'):
    return a

print(swim())

a = 4
b = 10

def addNum (a, b):
    c = a + b
    return c

print(addNum(a, b))

# Dodanie słowników
def dictionary(**kwargs):
    return kwargs

print(dictionary(d1={"1" : "one"}, d2={"pies": "dog"}))


