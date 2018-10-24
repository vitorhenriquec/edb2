'''
	Implementado por Vitor Henrique
	Ideia: pegar a maior substring de uma string
'''

def max_substring(x):
	start, stop = 0,0
	u_start , u_stop = 0,0 
	maior_string = ""
	seen = set()
	for i in range(len(x)):
		if x[i] not in seen:
			stop = i
			seen.add(x[i])
		else:
			seen.clear()
			start = stop
			stop = i
			seen.add(x[start])
			seen.add(x[stop])

		if stop - start + 1 > u_stop - u_start + 1:
			u_start = start
			u_stop = stop

	return x[u_start:u_stop+1]


print(max_substring("adacbbbbbebxcaay"))

