basket = ["ვაშლი", "ბანანი", "კივი", "ატამი", "ალუბალი"]


favorite_fruit = input("შეიყვანეთ თქვენი საყვარელი ხილი: ")


fruit_basket = False


for fruit in basket:
    if fruit == favorite_fruit:
        fruit_basket = True
        break 


if fruit_basket:
    print("კარგი არჩევანია")
else:
    print("ხილი არ გვაქვს")