import time

def countdown(number):
    while number >= 1:
        print(f"{number} SECOND(S)!")
        number -= 1
    print("HAPPY NEW YEAR!")
        

def countdown_with_sleep(number):
    while number >= 1:
        print(f"{number} SECOND(S)!")
        number -= 1
    print("HAPPY NEW YEAR!")
    time.sleep(1)
