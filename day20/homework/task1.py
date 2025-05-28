"""2) შექმენით პროგრამა რომელიც მომხმარებლისგან მიიღებს რიცხვს,
შემდეგ დაადგენს დადებითია, უარყოფითი თუ ნული if-elif-else ის საშვალებით,
თუ რიცხვი დადებითია შეამოწმეთ არის თუ არა ლუწი თუ არის დაბეჭდეთ
"The number is positive and even." ხოლო სხვა შემთხვევაში დაბეჭდეთ "The number is positive and odd."
"""
num1=int(input("enter your number"))
if num1 >0 and num1%2==0 :
    print("The number is positive and even")
else :
    print("The number is positive and odd.")
