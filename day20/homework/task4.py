"""5) მომხმარებელს 3 მცდელობა აქვს სწორი PIN კოდის შეყვანისთვის.
თუ შეიყვანს სწორად, დაიბეჭდება "Access Granted"
სხვა შემთხვევაში "Access Denied" გამოიყენეთ პირობითი განცხადებები
"""
try_counts = 2
user_pin = int(input("Enter the PIN code: "))
pin = 1234


while try_counts > 0:
    if user_pin == pin:
        print("Access Granted")
        break
    else:
        user_pin = int(input("Enter the PIN code: "))
        try_counts = try_counts - 1


if try_counts == 0 :
    print("Access denied")