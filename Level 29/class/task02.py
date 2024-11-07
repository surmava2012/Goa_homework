def check_number():
    number = float(input("შეიყვანეთ რიცხვი: "))
    print("რიცხვი დადებითია." if number > 0 else "რიცხვი უარყოფითია." if number < 0 else "რიცხვი ნულია.")

check_number()
