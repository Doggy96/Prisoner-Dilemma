valA = input("Ομολόγησε o A; (YES/NO): ")
valB = input("Ομολόγησε o B; (YES/NO): ")

if valA == "YES" and valB == "YES":
    poiniA = "5"
    poiniB = "5"
elif valA == "NO" and valB == "NO":
    poiniA = "1"
    poiniB = "1"
elif valA == "YES" and valB == "NO":
    poiniA = "0"
    poiniB = "20"
else:
    poiniA = "20"
    poiniB = "0"

print("O κρατούμενος A: " + poiniA + " χρόνια φυλακής," + " o κρατούμενος Β: " + poiniB + " χρόνια φυλακής")



   