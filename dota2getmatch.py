import requests as r
import os
import json as j

savepath = r'C:\Users\Ruiqi\Desktop\livegamedata.txt'

key = os.environ.get('D2_API_KEY')
params = {'key':key}

## get last 25 matches

liveleaguegames_url = 'https://api.steampowered.com/IDOTA2Match_570/GetLeagueListing/v0001'

#url = 'https://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/V001/?format=XML&key='+key

matches = r.get(liveleaguegames_url,params=params)
data = matches.json()

if matches.status_code ==200:
    with open(savepath,'w') as f:
        j.dump(data,f)
            

