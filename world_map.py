import folium
import pandas as pd

# Make a data frame with dots to show on the map
df = pd.read_csv('globalterrorismdb_0718dist.csv', sep=',', index_col=0, engine='python',parse_dates=True, encoding=None, tupleize_cols=None, infer_datetime_format=False)
df = df[~df['city'].isin(['Unknown'])]            #Unknown
#df = df[~df['city'].isin(['nan'])]               The nan changed into Unknown in dataset
df = df[~df['longitude'].isin(['nan'])]
df = df[~df['latitude'].isin(['nan'])]

# Make an empty map
m = folium.Map(location=[20, 0], tiles="Mapbox Bright", zoom_start=2)
#size = df.size
#times = (size//691)+1
print(len(df))

for i in range(168000,169174):
    print(df.iloc[i]['latitude'], df.iloc[i]['longitude'], df.iloc[i]['city'], i)
    folium.Marker([df.iloc[i]['latitude'], df.iloc[i]['longitude']], popup=df.iloc[i]['city']).add_to(m)
# Save it as html
m.save('terrorist '.html')

'''
# I can add marker one by one on the map
for j in range(0,times):
    for i in range(691*j, 691*j+691):
        print(df.iloc[i]['latitude'], df.iloc[i]['longitude'],df.iloc[i]['city'],i)
        folium.Marker([df.iloc[i]['latitude'], df.iloc[i]['longitude']], popup=df.iloc[i]['city']).add_to(m)
    # Save it as html
    m.save('terrorist_'+str(j)+'.html')


lon = df['longitude'].__array__()
lat = df['latitude'].__array__()
name = df['city'].__array__()
data = pd.DataFrame({'lat':lat,'lon':lon,'name':name})
'''

