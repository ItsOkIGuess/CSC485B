import pandas as pd


	
def to_sorted_list(dict,metric):
		ls = [[0],[0]]
		i = 0
		for x in dict:
			#print(ls)
			while(dict[x][metric] < ls[i][0]):
				i = i + 1
			if(i <len(ls) - 1):
				ls.insert(i,[dict[x][0],dict[x][1],x])
			elif(len(ls) == 1):
				ls[0] = ([dict[x][0],dict[x][1],x])
			else:
				ls.append([dict[x][0],[dict][x][1],x])
			i = 0
		return ls
	
def to_tuples(ls):
	blacklist = []
	tuplelist = []
	floor = 1
	for j in range(0,len(ls) - 1):
		for i in range(floor,len(ls) - 1):
			if(ls[j] != ls[i]):
				x = (ls[j],ls[i])
				#print(x)
				tuplelist.append(x)
		floor = floor + 1
	
	return ls

df = pd.read_csv (r'all_eggs_data.csv')
df =  df.to_dict()
ls1 = list(df["name"].values())
ls2 = list((df["owners"].values()))
ls3 = list(df["downloads"].values())
ls4 = list(df["release_year"].values())
ls = []
for i in range(0,len(ls1) -1):
	ls.append((ls1[i],ls2[i],ls3[i],ls4[i]))
	#print(ls[i])
lw = {}
n = {}
hmm = []
devcons = []
for x in ls:
	#print("STILL GOING")
	
	e = x[1].split(',')
	if(len(e) == 1):
		d = e[0]
		try:
			lw[d][0] = lw[d][0] + x[2]
			lw[d][1].append(x[0])
		except KeyError:
			lw[d] = [x[2],[str(x[0])]]

	if(len(e) > 1):
		devcons.append(e)
		for element in e:
			hmm.append(element)
			try:
				n[element][0] = n[element][0] + x[2]
				n[element][1].append(x[0])
				
			except KeyError:
				n[element] = [x[2],[str(x[0])]]
			

for x in hmm:
	try:
		del(lw[x])
	except:
		pass
	
#print(devcons)	
'''
unique_connections = []
for x in devcons:
	temp = to_tuples(x)
	if temp not in unique_connections:
		unique_connections.append(temp)
print(len(unique_connections))
'''

temp = []
total_cons = 0
for x in devcons:
	total_cons = total_cons + len(x)
#print(total_cons)

#print(len(unique_connections) / len(lw))

solos = 0

odf = {}
for x in lw:
	if len(lw[x][1]) == 1:
		solos = solos + 1
		odf[x] = lw[x]
for key in odf:
	del(lw[key])
for x in n:
	if len(n[x][1]) == 1:
		solos = solos + 1
print(len(odf))
'''
oo = to_sorted_list(odf,0)
ll = to_sorted_list(lw,0)
nn = to_sorted_list(n,0)
top = 0
pop = 0
slop = 0
top5p = []
j,k,l = 0,0,0
for i in range(0,16090):
	if(oo[j][0] > ll[k][0] and oo[j][0] > nn[l][0]):
		top5p.append(oo[j])
		j = j + 1
	elif(ll[k][0] > oo[j][0] and ll[k][0] > nn[l][0]):
		top5p.append(ll[k])
		k = k + 1
	else:
		top5p.append(nn[l])
		l = l + 1
for i in range(0,len(top5p)):
	top = top + top5p[i][0]
		
for i in range(j + 1, len(oo) - 1):
	pop = pop + oo[i][0]
	
for i in range(k + 1, len(ll) - 1):
	pop = pop + oo[j][0]
	
for i in range(l + 1, len(nn) - 1):
	pop = pop + oo[j][0]
	
print(top)
print(pop)
print(len(oo))
for i in range(0,5):
	print(ll[i])

print

print(len(oo))
'''

