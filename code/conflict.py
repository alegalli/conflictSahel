import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# DONE: conflict_numb.csv aggregated data per reference_year, adm2_name


confm = pd.read_csv('../data/Conflict Data/Conflict Data for Mali.csv')
confb = pd.read_csv('../data/Conflict Data/Conflict Data for Burkina Faso.csv')
confn = pd.read_csv('../data/Conflict Data/Conflict Data for Niger.csv')

# Select columns I'm interested in
confm.rename(columns={'country':'adm0_name',
                    'admin1':'adm1_name',
                    'admin2':'adm2_name',
                    'admin3':'adm3_name',
                    'actor1' : 'actor1',
                    'inter1' : 'inter1',
                    'actor2' : 'actor2',
                    'inter2' : 'inter2',
                    'interaction' : 'interaction',
                    'event_date':'date',
                    'year':'reference_year'}, inplace=True)
confb.rename(columns={'country':'adm0_name',
                    'admin1':'adm1_name',
                    'admin2':'adm2_name',
                    'admin3':'adm3_name',
                    'actor1' : 'actor1',
                    'inter1' : 'inter1',
                    'actor2' : 'actor2',
                    'inter2' : 'inter2',
                    'interaction' : 'interaction',
                    'event_date':'date',
                    'year':'reference_year'}, inplace=True)
confn.rename(columns={'country':'adm0_name',
                    'admin1':'adm1_name',
                    'admin2':'adm2_name',
                    'admin3':'adm3_name',
                    'actor1' : 'actor1',
                    'inter1' : 'inter1',
                    'actor2' : 'actor2',
                    'inter2' : 'inter2',
                    'interaction' : 'interaction',
                    'event_date':'date',
                    'year':'reference_year'}, inplace=True)
confm = confm[['reference_year','date','adm0_name','adm1_name','adm2_name','adm3_name',
        'event_type','sub_event_type','actor1','inter1','actor2','inter2','interaction','fatalities']]
confb = confb[['reference_year','date','adm0_name','adm1_name','adm2_name','adm3_name',
        'event_type','sub_event_type','actor1','inter1','actor2','inter2','interaction','fatalities']]
confn = confn[['reference_year','date','adm0_name','adm1_name','adm2_name','adm3_name',
        'event_type','sub_event_type','actor1','inter1','actor2','inter2','interaction','fatalities']]

# Extract reference_year
confm = confm[confm.reference_year.isin([2014,2015,2016,2017,2018,2019])]
confb = confb[confb.reference_year.isin([2014,2015,2016,2017,2018,2019])]
confn = confn[confn.reference_year.isin([2014,2015,2016,2017,2018,2019])]

# Select adm1_name to work with
confm = confm[confm.adm1_name.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
confm = confm.reset_index(drop=True)
confb = confb[confb.adm1_name.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
confb = confb.reset_index(drop=True)
confn = confn[confn.adm1_name.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
confn = confn.reset_index(drop=True)

# Manipulate data to create consistency with the other data
# adm3=='Ayorou' => adm2:'Ayerou'
# adm3=='Torodi' => adm2:'Torodi'
# adm3=='Abala' => adm2:'Abala'
for i in confn.index:
    if confn.loc[i,'adm3_name']=='Ayorou':
        confn.at[i,'adm2_name']='Ayerou'
    if confn.loc[i,'adm3_name']=='Torodi':
        confn.at[i,'adm2_name']='Torodi'
    if confn.loc[i,'adm3_name']=='Abala':
        confn.at[i,'adm2_name']='Abala'

confm = confm[confm.adm2_name.isin(['Bankass','Koro','Douentza','Djenne','Bandiagara','Tenenkou','Mopti','Youwarou', 'Gourma-Rharous','Dire','Niafunke', 'Gao','Ansongo','Menaka','Bourem'])]
confb = confb[confb.adm2_name.isin(['Yatenga','Loroum', 'Yagha','Seno','Soum','Oudalan', 'Komonjdjari'])]
confn = confn[confn.adm2_name.isin(['Tillia', 'Banibangou','Filingue','Ouallam','Say','Tera','Torodi','Abala','Ayerou'])]#removed: Tassara, Gotheye, Bankilare, Balleyara Because are not in the database, Tillaberi,Tahoua because in lean these data are mess
confm = confm.reset_index(drop=True)
confb = confb.reset_index(drop=True)
confn = confn.reset_index(drop=True)



# Total conflicts
conf = confm.append(confb.append(confn)).reset_index()

conf['fatalities'] = conf['fatalities'].astype(str).astype(int)



# Plot number of conflicts per year per adm2_name
ncy = pd.DataFrame(columns=['reference_year','adm2_name','conflicts','fatalities'])
for year in conf['reference_year'].unique():
    for adm2_name in conf['adm2_name'].unique():
        ncy = ncy.append(pd.Series([year, adm2_name, 0, 0],index=ncy.columns),ignore_index=True)

ncy = ncy.sort_values(by=['reference_year','adm2_name'])
ncy = ncy.reset_index(drop=True)

# Counts the number of conflicts for each adm2_name in Mali for each year
c = pd.DataFrame({'conflicts' : conf.groupby(['reference_year','adm2_name']).size()}).reset_index()
c = c.sort_values(by=['reference_year','adm2_name'])
c = c.reset_index(drop=True)
# Counts the number of kills for each adm2_name in Mali for each year
f = pd.DataFrame({'fatalities' : conf.groupby(['reference_year','adm2_name'])['fatalities'].sum()}).reset_index()
f = f.sort_values(by=['reference_year','adm2_name'])
f = f.reset_index(drop=True)

for index, row in c.iterrows():
    ncy.loc[(ncy.reference_year == row.reference_year) & (ncy.adm2_name == row.adm2_name), 'conflicts'] = row['conflicts']

for index, row in f.iterrows():
    ncy.loc[(ncy.reference_year == row.reference_year) & (ncy.adm2_name == row.adm2_name), 'fatalities'] = row['fatalities']

# Data explored in Jupyter Notebook
"""
# Plot number of conflicts and fatalities in Gao per reference_year
plt.style.use('fivethirtyeight')
g = ncy[ncy.adm2_name.isin(['Mopti'])].plot(x='reference_year',y=['conflicts','fatalities'],figsize=(10,7))
g.xaxis.label.set_visible(False)
plt.show()
"""




# Export data
# Data exported will miss all the adm2 where no conflict has appened in that reference_year
# Consequently all this missing adm2 will have 0 fatalities
ncy.to_csv('../data/Conflict Data/conflict_numb.csv',index=False)


# conflict_tot.csv
conf.to_csv('../data/Conflict Data/conflict_tot.csv',index=False)
