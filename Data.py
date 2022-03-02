#Precurser to FOSSE.py
import pandas as pd

def counter(x):
	sasafrass = {}
	for element in x:
		try:
			sasafrass[element] = sasafrass[element] + 1
		except:
			sasafrass[element] = 1
			
	return(sasafrass)


df = pd.read_csv (r'all_eggs_data.csv')
df =  df.to_dict()
ls = df["owners"]
max = 0
#print(ls)
owners = []
multiman = []
users = []
for element in ls:
	owners.append(ls[element])
	
ownersnodups = set(owners)
gravy = counter(owners)
notsolousers = 0
for x in gravy:
	users.append((gravy[x],x))
	if gravy[x] > 1:
		notsolousers = notsolousers + 1
		temp = x.split(',')
		if len(temp) > 1:
			multiman.append(temp)
users.sort()
for z in users:	
	for x in multiman:
		for y in x:
			if y == z[1]:
				temp = z[0] + 1
				z = (y,temp)
print("Number of unique users: " + str(len(ownersnodups)))
print("Number of users who only work on one project: " + str(len(ownersnodups) - notsolousers))
print("Number of users who work more than one project: " + str(notsolousers))
print("Number of projects with more than one contributor: " + str(len(multiman)))
print(users[len(users) - 1])