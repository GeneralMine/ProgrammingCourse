current = []

def perm(list1):
	if len(list1) == 1:
		current.append(list1[0])
		print(current)
		current.pop()
	else:
		for i in range(len(list1)):
			rest = list1[:i] + list1[i+1:]
			current.append(list1[i])
			perm(rest)
			current.pop()

perm([1,2,3,4])
