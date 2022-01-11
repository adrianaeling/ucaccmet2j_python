# import json

# with open('precipitation.json')as file:
#     data = json.load(file)

# i = {

# "key1":"value1",

# "key2":"value2",

# "key3":"value3"

#   }
# print(i["key1"])

# i = {
# "datatype": "PRCP",
# "date": "2010-01-02",
# "station": "GHCND:USW00093814",
# "value": 3
# }

# print(i["station"])

# for i in data:
#     print (i)
#     for "station"in data[i]:
#         print "station", data[i]["station"]

Stations = list()

with open('stations.csv') as file:
    headers = file.readline()
    for line in file:
        print(line)
        columns = line.strip().split(',')
        print(columns)
        Stations.append(columns)
print(Stations)

SeattleID = Stations[1][2]

print(SeattleID)
import json
with open('precipitation.json')as file:
    data = json.load(file)


sampledata = data[0]
print(sampledata)

print(sampledata['station'])

if (sampledata['station']) == SeattleID:
    print("yes")
else:
    print("no")

for item in data:
    if (item['station']) == SeattleID:
        print("yes")
    else:
        print("no")


values_all_year = [[],[],[],[],[],[],[],[],[],[],[],[]]
valuesJanuary = []

valuesFebruary = []

valuesMarch = []

valuesSeattle = []
for item in data:
    if (item['station']) == SeattleID:
        valuesSeattle.append(item['value'])
        month = item['date'].split('-')[1]
        index = int(month) - 1
        print(month,index)
        
        values_all_year[index].append(item['value'])

printable = sum(values_all_year[0])

sumsallyear = [0] * 12
avsallyear = [0] * 12

for i in range(len(values_all_year)):
    summonth = sum(values_all_year[i])
    sumsallyear[i] = summonth
print(sumsallyear)

for i in range(len(values_all_year)):
    avmonth = values_all_year[i] / len(values_all_year[i])
    avsallyear[i] = avmonth
print(avsallyear)

print(printable)
#         if month == '02':
#             values_all_year[1].append(item['value'])
#         if month == '03':
#             values_all_year[2].append(item['value'])
# print(valuesJanuary)
# print(valuesFebruary)
# print(valuesMarch)

#sumjan = sum(valuesJanuary)
#avjan = sumjan / len(valuesJanuary)
#print(avjan)





