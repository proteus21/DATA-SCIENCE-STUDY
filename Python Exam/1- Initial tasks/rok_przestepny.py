"""
    Napisz program, który prosi użytkownika o podanie roku,
    a następnie sprawdza, czy dany rok jest przestępny.

    Rok jest przestępny, kiedy dzieli się przez 400 lub kiedy dzieli się
    przez 4, ale jednocześnie nie dzieli się przez 100.
"""
year=input("Give only year:")
if int(year)%400==0  or int(year)%4==0 and  int(year)%100!=0:
    print("Year is ")
else:
    print("Year is not")