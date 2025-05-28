"""6) მომხმარებელმა უნდა შეიყვანოს რიცხვები,
სანამ -1-ს არ შეიყვანს. საბოლოოდ გამოიანგარიშოს შეყვანილი რიცხვების საშულო
"""

user_num = int(input("Enter the number: "))

sum = 0 
count = 0 
average = 0

while user_num != -1:
    sum = sum + user_num
    count = count + 1

    user_num = int(input("Enter the number: "))

average = sum / count
print(average)