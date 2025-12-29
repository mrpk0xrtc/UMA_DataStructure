def TowerOfHonoi(n, from_rod, to_rod, helper_rod):
	if n == 0: return
	TowerOfHonoi(n-1, from_rod, helper_rod, to_rod)
	print(f"Disk {n} from {from_rod} to {to_rod}")
	TowerOfHonoi(n-1, helper_rod, to_rod, from_rod)

if __name__ == "__main__":
	n = int(input())
	TowerOfHonoi(n, 'A', 'B', 'C')

