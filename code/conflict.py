import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# DONE: conflict_numb.csv aggregated data per reference_year, adm2_name
adm2 = ['Bandiagara','Bankass','Djenne','Douentza','Koro','Mopti','Tenenkou','Youwarou',
        'Dire','Goundam','Gourma-Rharous','Niafunke','Tombouctou',
        'Ansongo','Bourem','Gao','Menaka',
        'Loroum','Yatenga',
        'Oudalan','Seno','Soum','Yagha',
        'Komonjdjari',
        'Tahoua','Tassara','Tillia',
        'Banibangou','Filingue','Kollo','Ouallam','Say','Tera','Tillaberi']
mopti = ['Bandiagara','Bankass','Djenne','Douentza','Koro','Mopti','Tenenkou','Youwarou']
tombouctou = ['Dire','Goundam','Gourma-Rharous','Niafunke','Tombouctou']
gao = ['Ansongo','Bourem','Gao','Menaka']
nord = ['Loroum','Yatenga']
sahel = ['Oudalan','Seno','Soum','Yagha']
est = ['Komonjdjari']
tahoua = ['Tahoua','Tassara','Tillia']
tillaberi = ['Banibangou','Filingue','Kollo','Ouallam','Say','Tera','Tillaberi']

confm = pd.read_csv('../data/Conflict Data/conflict_data_mli.csv')
confb = pd.read_csv('../data/Conflict Data/conflict_data_bfa.csv')
confn = pd.read_csv('../data/Conflict Data/conflict_data_ner.csv')

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
confm.drop(index=0,inplace=True)
confb.drop(index=0,inplace=True)
confn.drop(index=0,inplace=True)
confm.reference_year = confb.reference_year.astype(str).astype(int)
confb.reference_year = confb.reference_year.astype(str).astype(int)
confn.reference_year = confb.reference_year.astype(str).astype(int)
confm.fatalities = confb.fatalities.astype(str).astype(int)
confb.fatalities = confb.fatalities.astype(str).astype(int)
confn.fatalities = confb.fatalities.astype(str).astype(int)
confm = confm[confm.reference_year.isin([2014,2015,2016,2017,2018,2019,2020])]
confb = confb[confb.reference_year.isin([2014,2015,2016,2017,2018,2019,2020])]
confn = confn[confn.reference_year.isin([2014,2015,2016,2017,2018,2019,2020])]

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
        confn.at[i,'adm2_name']='Tillaberi'
    if confn.loc[i,'adm3_name']=='Torodi':
        confn.at[i,'adm2_name']='Say'
    if confn.loc[i,'adm3_name']=='Abala':
        confn.at[i,'adm2_name']='Filingue'
    if confn.loc[i,'adm2_name']=='Tchintabaraden':
        confn.at[i,'adm2_name']='Tassara'

confm = confm[confm.adm2_name.isin(['Bandiagara','Bankass','Djenne','Douentza','Koro','Mopti','Tenenkou','Youwarou',
                                    'Dire','Goundam','Gourma-Rharous','Niafunke','Tombouctou',
                                    'Ansongo','Bourem','Gao','Menaka'])]
confb = confb[confb.adm2_name.isin(['Loroum','Yatenga',
                                    'Oudalan','Seno','Soum','Yagha',
                                    'Komonjdjari'])]
confn = confn[confn.adm2_name.isin(['Tahoua','Tassara','Tillia',
                                    'Banibangou','Filingue','Kollo','Ouallam','Say','Tera','Tillaberi'])]
confm = confm.reset_index(drop=True)
confb = confb.reset_index(drop=True)
confn = confn.reset_index(drop=True)



# Total conflicts
conf = confm.append(confb.append(confn)).reset_index()




# Plot number of conflicts per year per adm2_name
ncy = pd.DataFrame(columns=['reference_year','adm0_name','adm1_name','adm2_name','conflicts','fatalities'])
for year in conf['reference_year'].unique():
    for adm2_name in conf['adm2_name'].unique():
        if adm2_name in mopti:
            adm0_name = 'Mali'
            adm1_name = 'Mopti'
        elif adm2_name in tombouctou:
            adm0_name = 'Mali'
            adm1_name = 'Tombouctou'
        elif adm2_name in gao:
            adm0_name = 'Mali'
            adm1_name = 'Gao'
        elif adm2_name in nord:
            adm0_name = 'Burkina Faso'
            adm1_name = 'Nord'
        elif adm2_name in sahel:
            adm0_name = 'Burkina Faso'
            adm1_name = 'Sahel'
        elif adm2_name in est:
            adm0_name = 'Burkina Faso'
            adm1_name = 'Est'
        elif adm2_name in tahoua:
            adm0_name = 'Niger'
            adm1_name = 'Tahoua'
        elif adm2_name in tillaberi:
            adm0_name = 'Niger'
            adm1_name = 'Tillaberi'
        ncy = ncy.append(pd.Series([year, adm0_name, adm1_name, adm2_name, 0, 0],index=ncy.columns),ignore_index=True)

ncy = ncy.sort_values(by=['reference_year','adm0_name','adm1_name','adm2_name'])
ncy = ncy.reset_index(drop=True)

# Counts the number of conflicts for each adm2_name in Mali for each year
c = pd.DataFrame({'conflicts' : conf.groupby(['reference_year','adm0_name','adm1_name','adm2_name']).size()}).reset_index()
c = c.sort_values(by=['reference_year','adm0_name','adm1_name','adm2_name'])
c = c.reset_index(drop=True)
# Counts the number of kills for each adm2_name in Mali for each year
f = pd.DataFrame({'fatalities' : conf.groupby(['reference_year','adm0_name','adm1_name','adm2_name'])['fatalities'].sum()}).reset_index()
f = f.sort_values(by=['reference_year','adm0_name','adm1_name','adm2_name'])
f = f.reset_index(drop=True)

for index, row in c.iterrows():
    ncy.loc[(ncy.reference_year == row.reference_year) & (ncy.adm2_name == row.adm2_name), 'conflicts'] = row['conflicts']

for index, row in f.iterrows():
    ncy.loc[(ncy.reference_year == row.reference_year) & (ncy.adm2_name == row.adm2_name), 'fatalities'] = row['fatalities']



ncy['projected_conflicts'] = ncy['conflicts']
project20 = ncy[ncy['reference_year'].isin([2020])]
project20.loc[:,'projected_conflicts'] *= 12/7
for a in adm2:
    ncy.loc[(ncy.reference_year==2020)&(ncy.adm2_name==a),'projected_conflicts'] = project20.loc[(project20.reference_year==2020)&(project20.adm2_name==a)]['projected_conflicts']

ncy['projected_fatalities'] = ncy['fatalities']
project20 = ncy[ncy['reference_year'].isin([2020])]
project20.loc[:,'projected_fatalities'] *= 12/7
for a in adm2:
    ncy.loc[(ncy.reference_year==2020)&(ncy.adm2_name==a),'projected_fatalities'] = project20.loc[(project20.reference_year==2020)&(project20.adm2_name==a)]['projected_fatalities']




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
