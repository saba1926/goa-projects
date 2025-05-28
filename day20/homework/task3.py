"""4) შექმენით პროგრამა რომელშიც მომხმარებელმა უნდა შეიყვანოს რიცხვები,
სანამ უარყოფითს არ შეიყვანს.
დაბეჭდეთ შეყვანილი ლუწი და კენტი რიცხვების
რაოდენობა გამოიყენეთ პირობითი განცხადებები
"""
num1=int(input("enter something"))
evencount=0
oddcount=0
while num1%2==0:
    print(num1, "is even number")
    evencount+=1
else:
    print(num1, "is odd number")
    oddcount+=1
print(evencount)
print(oddcount)