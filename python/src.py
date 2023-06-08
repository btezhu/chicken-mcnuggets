from math import gcd
 
def is_expressible(a: int, b: int, c: int, n: int) -> bool:
	if (n % a) * (n % b) * (n % c) == 0:
		return True

	for i in range(0, int(n/a)+1):
		for j in range(0, int(n/b)+1):
			for k in range(0, int(n/c)+1):
				if i * a + j * b + k * c == n:
					return True

	return False

def max_nuggets(a: int, b: int, c: int) -> int:
	if gcd(a, b, c) != 1: # if gcd is not 1, then there is no max
		return print(f"Given package sizes {a}, {b}, and {c}, there is no largest number of McNuggets that cannot be bought in exact quantity")

	nums = (a, b, c)
	for (x, y, z) in [(0, 1, 2), (0, 2, 1), (1, 2, 0)]: # test for gcd pairwise

		k = gcd(nums[x], nums[y])

		if k != 1:
			m = nums[x] // k
			n = nums[y] // k
			p = nums[z]
			
			N = k*(m-1)*(n-1)+k*p-k-p # formula found in https://services.artofproblemsolving.com/download.php?id=YXR0YWNobWVudHMvZi84LzcyMWI0NTc1NWQ2ZWZlOTVlZTM3ZTM2ZjFiYzcwNDQ3Yjk3OTBj&rn=U01QRiBDaGlja2VuIG51Z2dldHMgNS5wZGY=, page 4.
			
			return N

	smallest = min(a, b, c)
	
	in_a_row = 0
	num = 1

	while True:
		if is_expressible(a, b, c, num):
			in_a_row += 1
			if in_a_row == smallest:
				return num - in_a_row
		else:
			in_a_row = 0
		num += 1