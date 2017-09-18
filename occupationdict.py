from decimal import Decimal
import random

f = open('occupations.csv','r')
s = f.read()
f.close()

data = s.split("\n")[1:len(s.split("\n"))-2]


occupationdict = {}
for i in range(len(data)):
	if data[i][0] == '"':
		jobName = data[i].split('"')[1]
		jobPercentage = Decimal(data[i].split('"')[2][1:len(data[i].split('"')[2])])
	else:
		jobName = data[i].split(",")[0]
		jobPercentage = Decimal(data[i].split(",")[1])
	#print jobName
	#print jobPercentage
	occupationdict[jobName] = jobPercentage

# for k, v in occupationdict.items() :
#     print k, v

def weightedrandom():
	det = Decimal(random.randrange(0, 998))/10
	#print det
	currentjob = ""
	total = 0
	for jobs in occupationdict:
		currentjob = jobs
		percentage = occupationdict[jobs]
		total += percentage
		if det < total:
			break
	print currentjob

weightedrandom()