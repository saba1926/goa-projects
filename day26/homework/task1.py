start = int(input("შეიყვანეთ დაწყების რიცხვი: "))
end = int(input("შეიყვანეთ დასრულების რიცხვი: "))


if end < start:
    print("არასწორი შუალედი.")
else:
    sum= 0 
    print("რიცხვები შუალედში:")
    for i in range(start, end + 1): 
        print(i)
        sum += i
    print("რიცხვების ჯამი არის:", sum)
