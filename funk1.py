import os
os.system('cls')

def eng_kop_3_soz(matn):
    sozlar = matn.split()
    sanash = {}
    for soz in sozlar:
        if soz in sanash:
            sanash[soz] += 1
        else:
            sanash[soz] = 1

    saralangan = sorted(sanash.items(), key=lambda juftlik: juftlik[1], reverse=True)

    for i in range(3):
        print(saralangan[i][0])
matn = "olma nok olma gilos olma nok shaftoli"
eng_kop_3_soz(matn)