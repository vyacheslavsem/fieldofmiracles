import random

val_list = [0,5,10,15,20,25,'банкрот']

p_s = 0

a = input("Начать?(1 - да, 0 - выход): ")

while a != "1" and a != "0":
    print("Введен неверный ответ!")
    a = input("Начать?(1 - да, 0 - выход): ")
    
while a != "0":
    
    b = random.choice(val_list)
    print("Счет:", p_s)
    print("Ставка: ", b)
    
    if type(b) != int:
        print("Банкрот!")
        p_s -= p_s
        print("Счет:", p_s)
        print()

    if type(b) == int:
        q = input("Ответ был верным?(1 - да, 2 - нет, 0 - выход): ")
        if q == "1":
            p_s += b
            print("Счет:", p_s)
            print()
            
        if q == "2":
            print()
            print("Ответ неверный!")
            print("Счет:", p_s)
            print()
            
        if q == "0":
            print()
            print("Пока!")
            print("Счет был:", p_s)
            print()
            break

if a == "0":
    print("Пока!")