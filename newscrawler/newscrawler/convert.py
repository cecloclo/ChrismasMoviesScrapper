import pandas as pd
import json

with open('lbc1.json') as json_data:
    data_dict = json.load(json_data)

data_str = json.dumps(data_dict)

data2 = json.loads(data_str)

data1 = pd.read_json('lbc1.json')
df = pd.DataFrame(data1)
df = df.drop('images', axis = 1)
#print(df)

#df = pd.DataFrame(data1)
#df = df.drop('images', axis = 1)

#description_list = []
#titre_list = []
#image_list = []



# """
# df['description'] = [item.replace(",                       ", " ") for item in df['description']]
# df['description'] = [item.replace("\n        \n            ", "") for item in df['description']]
# df['description'] = [item.replace("\n\n    ", "\n") for item in df['description']]
# df['description'] = [item.replace("\n    \n    \n                   \n                \n    ", "") for item in df['description']]
# df['description'] = [item.replace("\n                      ", "") for item in df['description']]
# df['description'] = [item.replace("'',", "") for item in df['description']]
# df['description'] = [item.replace("\n", "") for item in df['description']]
#df['description']
#df['description'][0]# = [item.replace("\n    \n    \n                   \n                \n    ", "") for item in df['description']]

df['description'][0] = [item.replace(",                       ", " ") for item in df['description'][0]]
df['description'][0] = [item.replace("\n        \n            ", "") for item in df['description'][0]]
df['description'][0] = [item.replace("\n\n    ", "\n") for item in df['description'][0]]
df['description'][0] = [item.replace("\n    \n    \n                   \n                \n    ", "") for item in df['description'][0]]
df['description'][0] = [item.replace("\n                      ", "") for item in df['description'][0]]
df['description'][0] = [item.replace("'',", "") for item in df['description'][0]]
df['description'][0] = [item.replace("\n", "") for item in df['description'][0]]
df['description'][0].remove(df['description'][0][0])


#df['description']= df['description'][0][0].drop()
#print(df['description'][0])

df['Evaluation spectateur'] = [item.replace("--", "None") for item in df['Evaluation spectateur'][i]]

# df['titre'] = [item.replace(" \n        , ", "") for item in df['titre']]
# df['titre'] = [item.replace("\n            ", "") for item in df['titre']]
# df['titre'] = [item.replace(" \n        ", "") for item in df['titre']]
# df['titre'] = [item.replace(" \n         ", "") for item in df['titre']]
# df['titre'] = [item.replace(" \n         ", "") for item in df['titre']]
# df['titre'] = [item.replace(" \n         ", "") for item in df['titre']]
# df['titre'] = [item.replace(" \n        , ", "") for item in df['titre']]
# df['titre'] = [item.replace("        ", "") for item in df['titre']]
# df['titre'] = [item.replace(", \n, ,", ", \n,") for item in df['titre']]
# df['titre'] = [item.replace("\n", "") for item in df['titre']]"""

# """for d in (df['description'][i]):
#     if (d != ''):
#         description_list.append(d)

# for t in (df['titre'][i]):
#     if (t != ''):
#         titre_list.append(t)

# for i in (df['image_urls'][i]):
#     if (i != ''):
#         image_list.append(i)

# #print(len(description_list))"""

# """columns = df.columns
# for col in columns:
#     print(col)"""

# #print(len(image_list))
# #print(len(df['Evaluation spectateur']))
# #print(df)

#print(df['description'])