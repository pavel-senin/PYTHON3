'''4. Программа загадывает число от 0 до 1000. 
Необходимо угадать число за 10 попыток. 
Программа должна подсказывать «больше» или «меньше» после каждой попытки. 
Для генерации случайного числа используйте код:
from random import
randint num = randint(LOWER_LIMIT, UPPER_LIMIT)'''

from random import randint 
num = randint(0, 1000)
usernum = 0
for i in range(1, 11):
    print (f"Угадайте загаданное число, попытка {i}/10")
    usernum = input(">>>")
    if int(usernum)==int(num):
        print (f"Угадали на попытке {i}/10")
        break
    else:
        if int(usernum)>int(num):
            print ("Ваше число больше загаданного")
        else:
            print ("Ваше число меньше загаданного")
print (f"Загаданное число: {num}")