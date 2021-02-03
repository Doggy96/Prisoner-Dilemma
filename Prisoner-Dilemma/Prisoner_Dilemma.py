print("Δώσε τιμή YES η NO")

A = "";
B = "";

while A != "YES" and A != "NO":
    A = input("Ομολόγησε o A; (YES/NO): ")

while B != "YES" and B != "NO":
    B = input("Ομολόγησε o B; (YES/NO): ")



if A == "YES" and B == "YES":
    poiniA = "5"
    poiniB = "5"
elif A == "NO" and B == "NO":
    poiniA = "1"
    poiniB = "1"
elif A == "YES" and B == "NO":
    poiniA = "0"
    poiniB = "20"
else:
    poiniA = "20"
    poiniB = "0"

print("O κρατούμενος A: " + poiniA + " χρόνια φυλακής," + " o κρατούμενος Β: " + poiniB + " χρόνια φυλακής")



   