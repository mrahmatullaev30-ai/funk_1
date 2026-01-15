mylist = ["olma", "", "olma", "gilos", ""]


result = []
for word in mylist:
    if word and word not in result:
        result.append(word)

print("mylist =", result)