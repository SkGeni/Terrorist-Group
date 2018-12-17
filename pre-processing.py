import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('globalterrorismdb_0718dist.csv', sep=',', index_col=0, engine='python',parse_dates=True, encoding=None, tupleize_cols=None, infer_datetime_format=False)

#year = df['iyear']
region = df['region_txt']
region_agg = dict(region.value_counts())
regions = region_agg.keys()
numbers = region_agg.values()
eject = np.zeros(len(regions))
eject[0:3] =[0.1,0.1,0.1]
plt.figure(1)
plt.title("The regions with the percentage of attacks.")
plt.pie(numbers,explode=eject,labels=regions,autopct='%1.1f%%')#rotatelabels=20)
plt.show()


country = df['country_txt']
country_agg = dict(country.value_counts())
sorted(country_agg)
country_df = pd.DataFrame.from_dict(country_agg,orient='index')
top10_country = country_df.iloc[:10]
eject = np.zeros(len(top10_country))
lab = top10_country.index.values.tolist()

eject[0]=0.1
plt.figure(2)
plt.pie(top10_country,explode=eject,labels=lab,autopct='%1.1f%%')#rotatelabels=20)
plt.title("Top 10 Countries with the percentage of attacks.")
plt.show()

attack_type = df['attacktype1_txt']
attack_agg = dict(attack_type.value_counts())
sorted(attack_agg)
attack_type_df = pd.DataFrame.from_dict(attack_agg,orient='index')
#top10_country = country_df.iloc[:10]
eject = np.zeros(len(attack_type_df))
lab = attack_type_df.index.values.tolist()
#lab = top10_country.index.values()

eject[0]=0.1
plt.figure(3)
plt.pie(attack_type_df,explode=eject,labels=lab,autopct='%1.1f%%')#rotatelabels=20)
plt.title("Study of several attack types.")
plt.show()

success = df['success']
success = success.replace([1,0],["Succeeded","Failed"])
success_agg = dict(success.value_counts())
success_df = pd.DataFrame.from_dict(success_agg,orient='index')
eject = np.zeros(len(success_df))
lab = success_df.index.values.tolist()
eject[0]=0.1
plt.figure(4)
plt.pie(success_df,explode=eject,labels=lab ,autopct='%1.1f%%')#rotatelabels=20)
plt.title("Terrorist Attack : Success Ratio")
plt.show()


target_type = df['targtype1_txt']
target_type_agg = dict(target_type.value_counts())
sorted(target_type_agg)
target_type_df = pd.DataFrame.from_dict(target_type_agg,orient='index')
top10_target_type = target_type_df.iloc[:10]
eject = np.zeros(len(top10_target_type))
lab = top10_target_type.index.values.tolist()
#lab = top10_country.index.values()
eject[0]=0.1
plt.figure(5)
plt.pie(top10_target_type,explode=eject,labels=lab,autopct='%1.1f%%')#rotatelabels=20)
plt.title("Analysis of the Targets of Terrorist Attacks")
plt.show()

#######print(df['targetype1_txt']=="Private Citizens & Property")

#countries = country_agg.keys()
#num = country_agg.values()
#plt.subplot(2,1,2)

#relevant_data = df['iyear','imonth', 'iday',  ]

claimed = df['claimed']
claimed = claimed.replace([1,0,None],["Claimed","Non-Claimed","Unknown"])
claimed_agg = dict(claimed.value_counts())
claimed_df = pd.DataFrame.from_dict(claimed_agg,orient='index')
eject = np.zeros(len(claimed_df))
lab = claimed_df.index.values.tolist()
eject[0]=0.1
plt.figure(6)
plt.pie(claimed_df,explode=eject,labels=lab ,autopct='%1.1f%%')#rotatelabels=20)
plt.title("Do they claim for the attack.")
plt.show()

claimmode_txt = df['claimmode_txt']
claimmode_txt_agg = dict(claimmode_txt.value_counts())
claimmode_txt_df = pd.DataFrame.from_dict(claimmode_txt_agg,orient='index')
eject = np.zeros(len(claimmode_txt_df))
lab = claimmode_txt_df.index.values.tolist()
eject[0]=0.1
plt.figure(7)
plt.pie(claimmode_txt_df,explode=eject,labels=lab ,autopct='%1.1f%%')#rotatelabels=20)
plt.title("Claiming Methods for terrorists")
plt.show()

weaptype1_txt = df['weaptype1_txt']
weaptype1_txt_agg = dict(weaptype1_txt.value_counts())
weaptype1_txt_df = pd.DataFrame.from_dict(weaptype1_txt_agg,orient='index')
lab = weaptype1_txt_df.index.values.tolist()
plt.figure(8)
plt.pie(weaptype1_txt_df,labels=lab,autopct='%1.1f%%')#rotatelabels=20)
plt.title("Weapon study of terrorist attacks")
plt.show()

property = df['property']
property = property.replace([1,0],['Property Damaging Attacks', 'No Property Damage'])
property_agg = dict(property.value_counts())
property_df = pd.DataFrame.from_dict(property_agg,orient='index')
lab = property_df.index.values.tolist()
plt.figure(8)
plt.pie(property_df,labels=lab,autopct='%1.1f%%')#rotatelabels=20)
plt.title("Property Damage Analysis of Terrorist Attacks")
plt.show()

