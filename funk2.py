import os
os.system('cls')

def orta_ball(students):
    
    natija = {}

    for ism, fanlar in students.items():
        summa = 0
        soni = 0
        for baho in fanlar.values():
            summa += baho
            soni += 1
        natija[ism] = summa / soni

    return natija

students = {
    "Ali": {"math": 90, "en": 80},
    "Vali": {"math": 70, "en": 85}
}
print(orta_ball(students))