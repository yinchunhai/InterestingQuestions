for i in range (111, 1000):
	threednum = str(i)
	if threednum[0] == threednum[1] or threednum[1] == threednum[2] or threednum[0] == threednum[2]:
		pass
	elif threednum[1] == str(0) or threednum[2] == str(0):
		pass
	else:
		for j in range (1, 10):
			if threednum[0] == str(j) or threednum[1] == str(j) or threednum[2] == str(j):
				pass
			else:
				k = i * j
				fourdnum = str(k)
				if len(fourdnum) < 4 or fourdnum[1] == str(0) or fourdnum[2] == str(0) or fourdnum[3] == str(0):
					pass
				elif fourdnum[0] == fourdnum[1] or fourdnum[0] == fourdnum[2] or fourdnum[0] == fourdnum[3] or fourdnum[1] == fourdnum[2] or fourdnum[1] == fourdnum[3] or fourdnum[2] == fourdnum[3]:
					pass
				elif fourdnum[0] == threednum[0] or fourdnum[0] == threednum[1] or fourdnum[0] == threednum[2]:
					pass
				elif fourdnum[1] == threednum[0] or fourdnum[1] == threednum[1] or fourdnum[1] == threednum[2]:
					pass
				elif fourdnum[2] == threednum[0] or fourdnum[2] == threednum[1] or fourdnum[2] == threednum[2]:
					pass
				elif fourdnum[3] == threednum[0] or fourdnum[3] == threednum[1] or fourdnum[3] == threednum[2]:
					pass
				elif fourdnum[0] == str(j) or fourdnum[1] == str(j) or fourdnum[2] == str(j) or fourdnum[3] == str(j):
					pass
				else:
					print i, j, k