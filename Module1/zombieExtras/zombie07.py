areaToPaint = int(input("How many m2 have your area: "))
if areaToPaint % 54 != 0:
    buckets = int(areaToPaint / 54) + 1
else:
    buckets = areaToPaint / 54
print("You need buy %i and this will cost to you R$%i" %(buckets, (buckets * 80)))
