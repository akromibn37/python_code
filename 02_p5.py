price = float(input())
coupon = input().strip()
card = input().strip()
discount = 0
if coupon == "Y":
	discount += 5
if card == "Y":
	if discount > 0:
		discount += 15
	else:
		discount += 10
print( price*(1-discount/100))
