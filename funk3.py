import os
os.system('cls')

ombor = [
    {"mahsulot": "olma", "miqdor": 5},
    {"mahsulot": "nok", "miqdor": 9},
    {"mahsulot": "shaftoli", "miqdor": 7},
    {"mahsulot": "anor", "miqdor": 4},
    {"mahsulot": "banan", "miqdor": 6},
    {"mahsulot": "uzum", "miqdor": 8},
    {"mahsulot": "gilos", "miqdor": 2},
    {"mahsulot": "tarvuz", "miqdor": 1},
    {"mahsulot": "qovun", "miqdor": 3},
    {"mahsulot": "limon", "miqdor": 5}
]


total = sum(item["miqdor"] for item in ombor)

three = sorted(ombor, key=lambda x: x["miqdor"])[:3]
names = [item["mahsulot"] for item in three]

print(f"Umumiy mahsulotlar miqdori: {total}")
print("Eng kam qolgan 3 ta mahsulot:", ", ".join(names))