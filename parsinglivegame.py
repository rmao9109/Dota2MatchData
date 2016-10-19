import json
import pprint as pprint
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


data_path = r'C:\Users\Ruiqi\Documents\Python Scripts\Dota 2 data\livegamedata.txt'
save_path = r'C:\Users\Ruiqi\Documents\Python Scripts\Dota 2 data\leaguedata.csv'


with open(data_path,'r') as fn:
    data_raw = json.load(fn)



data_all = data_raw['result']

leagues = data_all['leagues']
header = []

for key in leagues[0]:
    header.append(key)

output_data = []

for row in leagues:
    tmp_list = []
    for key in row:
        tmp_list.append(row[key])
    output_data.append(tmp_list)

print(type(output_data))


with open(save_path,'w') as fn:
    writer = csv.writer(fn)
    writer.writerow(header)
    writer.writerows(output_data)


