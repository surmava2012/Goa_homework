def age_category(age):
    if age < 0:
        return "მოწოდებული ასაკი არასწორია"
    if age <= 12:
        return "თქვენ ხართ ბავშვი"
    if age <= 18:
        return "თქვენ ხართ მოზარდი"
    if age <= 60:
        return "თქვენ ხართ ზრდასრული"
    else:
        return "თქვენ ხართ ხანდაზმული ადამიანი"

age = int(input("გთხოვთ, შეიყვანოთ თქვენი ასაკი: "))


print(age_category(age))
