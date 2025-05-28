"""7) მომხმარებელს შემოაყვანინეთ წინადადება,
შემდეგ for ციკლისა და პირობითი განცხადებების საშვალებით დაბეჭდეთ ჯერ ხმოვნების,
შემდეგ კი თანხმოვნების რაოდენობა (ხმოვნებად ჩათვალეთ სიმბოლოები: a, e, i, o, u
ხოლო სხვა ყველა თანხმოვნად)
"""
sentence = input("Enter the sentence: ")
vowels = "aeiou"
vowels_count = 0
consonant_count = 0

for i in sentence:
    if i in vowels:
        vowels_count = vowels_count + 1
    else:
        consonant_count = consonant_count + 1

print("The Consonants count is", consonant_count)
print("The Vowels count is",vowels_count)