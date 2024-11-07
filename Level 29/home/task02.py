def average(numbers):
    if len(numbers) == 0:  
        return 0
    return sum(numbers) / len(numbers)


numbers = [1, 2, 3, 4, 5]
print("საშუალო რიცხვი:", average(numbers))
