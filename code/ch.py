import pandas as pd
import xlrd
import seaborn as sns
import matplotlib.pyplot as plt


# Read CH data from excel
ch = pd.read_excel('../data/Cadre Harmonise/cadre_harmonise.xlsx')

# Features I'm interested in:
ch = ch[['adm0_name','adm1_name','adm2_name','population','phase_class','phase35',
        'chtype','exercise_label','exercise_year','reference_label','reference_year']]

# Select adm0_name to work with
ch = ch[ch.adm0_name.isin(['Mali','Burkina Faso','Niger'])]
# Select adm1_name to work with
ch = ch[ch.adm1_name.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]


ch = ch.sort_values(by=['reference_year','adm0_name','adm1_name','adm2_name','reference_label','exercise_year','exercise_label','chtype'])
ch = ch[ch.reference_label.isin(['Jun-Aug'])]
ch = ch[ch.reference_year == ch.exercise_year]
ch = ch.reset_index(drop=True)


for i in ch.index:
    if ch.loc[i,'adm2_name']=='Tahoua_accessible':
        ch.at[i,'adm2_name']='Tahoua'
    if ch.loc[i,'adm2_name']=='Tillaberi_accessible':
        ch.at[i,'adm2_name']='Tillaberi'
    if ch.loc[i,'adm2_name']=='Tera_accessible':
        ch.at[i,'adm2_name']='Tera'
    if ch.loc[i,'adm2_name']=='Ouallam_accessible':
        ch.at[i,'adm2_name']='Ouallam'




# Filingue = Filingue + Abala + Balleyara
filingue = ch.loc[ch.adm2_name=='Filingue']
abala = ch.loc[ch.adm2_name=='Abala']
balleyara = ch.loc[ch.adm2_name=='Balleyara']
# NOTE: It MUST have the same index
abala.index += 5
balleyara.index += 3
for year in range(2014,2021):
    ch.loc[(ch.adm2_name=='Filingue')&(ch.reference_year==year),'phase_class']=pd.concat([filingue.loc[filingue.reference_year==year, 'phase_class'], abala.loc[abala.reference_year==year, 'phase_class'], balleyara.loc[balleyara.reference_year==year, 'phase_class']]).max(level=0)
    ch.loc[(ch.adm2_name=='Filingue')&(ch.reference_year==year),'population']+=abala.loc[abala.reference_year==year, 'population'] + balleyara.loc[balleyara.reference_year==year, 'population']
    ch.loc[(ch.adm2_name=='Filingue')&(ch.reference_year==year),'phase35']+=abala.loc[abala.reference_year==year, 'phase35'] + balleyara.loc[balleyara.reference_year==year, 'phase35']


# Tera = Tera + Tera_limitedaccess + Bankilare
tera = ch.loc[ch.adm2_name=='Tera']
tera_la = ch.loc[ch.adm2_name=='Tera_limitedaccess']
bankilare = ch.loc[ch.adm2_name=='Bankilare']

# NOTE: It MUST have the same index
tera_la.index -= 1
bankilare.index += 6
for year in range(2014,2021):
    if year!=2020:
        ch.loc[(ch.adm2_name=='Tera')&(ch.reference_year==year),'phase_class']=pd.concat([tera.loc[tera.reference_year==year, 'phase_class'], bankilare.loc[bankilare.reference_year==year, 'phase_class']]).max(level=0)
    else:
        bankilare.index += 1
    ch.loc[(ch.adm2_name=='Tera')&(ch.reference_year==year),'population']+=bankilare.loc[bankilare.reference_year==year, 'population']
    ch.loc[(ch.adm2_name=='Tera')&(ch.reference_year==year),'phase35']+=bankilare.loc[bankilare.reference_year==year, 'phase35']
ch.loc[(ch.adm2_name=='Tera')&(ch.reference_year==2020),'phase_class']=pd.concat([tera.loc[tera.reference_year==2020, 'phase_class'], tera_la.loc[tera_la.reference_year==2020, 'phase_class'], bankilare.loc[bankilare.reference_year==2020, 'phase_class']]).max(level=0)
ch.loc[(ch.adm2_name=='Tera')&(ch.reference_year==2020),'population']+=tera_la.loc[tera_la.reference_year==2020, 'population'].values[0]
ch.loc[(ch.adm2_name=='Tera')&(ch.reference_year==2020),'phase35']+=tera_la.loc[tera_la.reference_year==2020, 'phase35'].values[0]


# Say = Say + Torodi
say = ch.loc[ch.adm2_name=='Say']
torodi = ch.loc[ch.adm2_name=='Torodi']
# NOTE: It MUST have the same index
torodi.index -= 3
for year in range(2014,2021):
    if year==2018:
        torodi.index-=1
    if year==2020:
        torodi.index-=2
    ch.loc[(ch.adm2_name=='Say')&(ch.reference_year==year),'phase_class']=pd.concat([say.loc[say.reference_year==year, 'phase_class'], torodi.loc[torodi.reference_year==year, 'phase_class']]).max(level=0)
    ch.loc[(ch.adm2_name=='Say')&(ch.reference_year==year),'population']+=torodi.loc[torodi.reference_year==year, 'population']
    ch.loc[(ch.adm2_name=='Say')&(ch.reference_year==year),'phase35']+=torodi.loc[torodi.reference_year==year, 'phase35']
    if year==2018:
        torodi.index+=1


# Ouallam = Ouallam + Ouallam_limitedaccess
ouallam = ch.loc[ch.adm2_name=='Ouallam']
ouallam_la = ch.loc[ch.adm2_name=='Ouallam_limitedaccess']
# NOTE: It MUST have the same index
ouallam_la.index -= 1
ch.loc[(ch.adm2_name=='Ouallam')&(ch.reference_year==2020),'phase_class']=pd.concat([ouallam.loc[ouallam.reference_year==2020, 'phase_class'], ouallam_la.loc[ouallam_la.reference_year==2020, 'phase_class']]).max(level=0)
ch.loc[(ch.adm2_name=='Ouallam')&(ch.reference_year==2020),'population']+=ouallam_la.loc[ouallam_la.reference_year==2020, 'population'].values[0]
ch.loc[(ch.adm2_name=='Ouallam')&(ch.reference_year==2020),'phase35']+=ouallam_la.loc[ouallam_la.reference_year==2020, 'phase35'].values[0]


# Tillaberi = Tillaberi + Tillaberi_limitedaccess + Tillaberi Commune + Ayerou + Gotheye
tillaberi = ch.loc[ch.adm2_name=='Tillaberi']
tillaberi_la = ch.loc[ch.adm2_name=='Tillaberi_limitedaccess']
tillaberi_commune = ch.loc[ch.adm2_name=='Tillaberi Commune']
ayerou = ch.loc[ch.adm2_name=='Ayerou']
gotheye = ch.loc[ch.adm2_name=='Gotheye']
# NOTE: It MUST have the same index
tillaberi_la.index -= 1
tillaberi_commune.index -= 1
ayerou.index += 10
gotheye.index += 5
for year in range(2014,2021):
    if year!=(2018&2020):
        ch.loc[(ch.adm2_name=='Tillaberi')&(ch.reference_year==year),'phase_class']=pd.concat([tillaberi.loc[tillaberi.reference_year==year, 'phase_class'], ayerou.loc[ayerou.reference_year==year, 'phase_class'], gotheye.loc[gotheye.reference_year==year, 'phase_class']]).max(level=0)
    if year==2020:
        ayerou.index += 2
        gotheye.index += 2
    ch.loc[(ch.adm2_name=='Tillaberi')&(ch.reference_year==year),'population']+=ayerou.loc[ayerou.reference_year==year, 'population'] + gotheye.loc[gotheye.reference_year==year, 'population']
    ch.loc[(ch.adm2_name=='Tillaberi')&(ch.reference_year==year),'phase35']+=ayerou.loc[ayerou.reference_year==year, 'phase35'] + gotheye.loc[gotheye.reference_year==year, 'phase35']
ch.loc[(ch.adm2_name=='Tillaberi')&(ch.reference_year==2018),'phase_class']=pd.concat([tillaberi.loc[tillaberi.reference_year==2018, 'phase_class'], tillaberi_commune.loc[tillaberi_commune.reference_year==2018, 'phase_class'], ayerou.loc[ayerou.reference_year==year, 'phase_class'], gotheye.loc[gotheye.reference_year==year, 'phase_class']]).max(level=0)
ch.loc[(ch.adm2_name=='Tillaberi')&(ch.reference_year==2018),'population']+=tillaberi_commune.loc[tillaberi_commune.reference_year==2018, 'population'].values[0]
ch.loc[(ch.adm2_name=='Tillaberi')&(ch.reference_year==2018),'phase35']+=tillaberi_commune.loc[tillaberi_commune.reference_year==2018, 'phase35'].values[0]
ch.loc[(ch.adm2_name=='Tillaberi')&(ch.reference_year==2020),'phase_class']=pd.concat([tillaberi.loc[tillaberi.reference_year==2020, 'phase_class'], tillaberi_la.loc[tillaberi_la.reference_year==2020, 'phase_class'], ayerou.loc[ayerou.reference_year==year, 'phase_class'], gotheye.loc[gotheye.reference_year==year, 'phase_class']]).max(level=0)
ch.loc[(ch.adm2_name=='Tillaberi')&(ch.reference_year==2020),'population']+=tillaberi_la.loc[tillaberi_la.reference_year==2020, 'population'].values[0]
ch.loc[(ch.adm2_name=='Tillaberi')&(ch.reference_year==2020),'phase35']+=tillaberi_la.loc[tillaberi_la.reference_year==2020, 'phase35'].values[0]


# Tahoua = Tahoua + Tahoua_limitedaccess + Ville De Tahoua
tahoua = ch.loc[ch.adm2_name=='Tahoua']
ville_tahoua = ch.loc[ch.adm2_name=='Ville De Tahoua']
tahoua_la = ch.loc[ch.adm2_name=='Tahoua_limitedaccess']
# NOTE: It MUST have the same index
tahoua_la.index -= 1
ville_tahoua.index -= 4
ch.loc[(ch.adm2_name=='Tahoua')&(ch.reference_year==2018),'phase_class']=pd.concat([tahoua.loc[tahoua.reference_year==2018, 'phase_class'], ville_tahoua.loc[ville_tahoua.reference_year==2018, 'phase_class']]).max(level=0)
ch.loc[(ch.adm2_name=='Tahoua')&(ch.reference_year==2018),'population']+=ville_tahoua.loc[ville_tahoua.reference_year==2018, 'population'].values[0]
ch.loc[(ch.adm2_name=='Tahoua')&(ch.reference_year==2018),'phase35']+=ville_tahoua.loc[ville_tahoua.reference_year==2018, 'phase35'].values[0]
ch.loc[(ch.adm2_name=='Tahoua')&(ch.reference_year==2020),'phase_class']=pd.concat([tahoua.loc[tahoua.reference_year==2020, 'phase_class'], tahoua_la.loc[tahoua_la.reference_year==2020, 'phase_class']]).max(level=0)
ch.loc[(ch.adm2_name=='Tahoua')&(ch.reference_year==2020),'population']+=tahoua_la.loc[tahoua_la.reference_year==2020, 'population'].values[0]
ch.loc[(ch.adm2_name=='Tahoua')&(ch.reference_year==2020),'phase35']+=tahoua_la.loc[tahoua_la.reference_year==2020, 'phase35'].values[0]


# Tassara = Tassara + Tchintabaraden
tassara = ch.loc[ch.adm2_name=='Tassara']
tchintabaraden = ch.loc[ch.adm2_name=='Tchintabaraden']
# NOTE: It MUST have the same index
tchintabaraden.index -= 1
for year in range(2014,2021):
    ch.loc[(ch.adm2_name=='Tassara')&(ch.reference_year==year),'phase_class']=pd.concat([tassara.loc[tassara.reference_year==year, 'phase_class'], tchintabaraden.loc[tchintabaraden.reference_year==year, 'phase_class']]).max(level=0)
    ch.loc[(ch.adm2_name=='Tassara')&(ch.reference_year==year),'population']+=tchintabaraden.loc[tchintabaraden.reference_year==year, 'population']
    ch.loc[(ch.adm2_name=='Tassara')&(ch.reference_year==year),'phase35']+=tchintabaraden.loc[tchintabaraden.reference_year==year, 'phase35']




# Select adm2_name to work with
ch = ch[ch.adm2_name.isin(['Bandiagara','Bankass','Djenne','Douentza','Koro','Mopti','Tenenkou','Youwarou',
                           'Dire','Gourma-Rharous','Niafunke', # At adm2 level not considered Goundam and Tombouctou in the study
                           'Ansongo','Bourem','Gao','Menaka',
                           'Komonjdjari',
                           'Loroum','Yatenga',
                           'Oudalan','Seno','Soum','Yagha',
                           'Tahoua','Tassara','Tillia', # I put in Tillaberi and Tahoua considering that some values are in Tillaberi Department and Tahoua Department, Ville De Tahoua, Tillaberi Commune
                           'Banibangou','Filingue','Kollo','Ouallam','Say','Tera','Tillaberi'])]#removed: Torodi, Ayerou, Abala, Gotheye, Bankilare, Balleyara Because considered in the other adm2


ch = ch.reset_index(drop=True)


# Check that no row has a nan value:
ch[ch.isna().any(axis=1)]




# We want to work just with the Lean Season data
# We need just the spring estimation: Select exercise_label=='Jan-May'
lean = ch[ch.exercise_label == 'Jan-May']
# Select reference_label='Jun-Aug'
lean = lean[lean.reference_label == 'Jun-Aug']
# Select chtype=='projected'
lean = lean[lean.chtype == 'projected']
lean = lean.reset_index(drop=True)
# Select featueres
lean = lean[['adm0_name','adm1_name','adm2_name','population','phase_class','phase35','reference_year']]

# Let's plot things out
# phase35 density between the population in Lean Season: (phase35%, reference_year)
lean['p35_density'] = lean['phase35'].div(lean['population'])
#lean_graph = lean[lean.adm2_name=='Gao'].plot(x='reference_year',y='p35_density',figsize=(12,8))

lean['population'] = lean['population'].astype('int32')
lean['phase35'] = lean['phase35'].astype('int32')
lean['phase_class'] = lean['phase_class'].astype('int32')



"""
# I should create a DataFrame where a column is year, the other columns are the different areas (same as biomass)
# Create a DataFrame to plot population growth
pop1 = pd.DataFrame()
pop1['adm0_name'] = lean.adm0_name[lean.reference_year.isin([2014])]
pop1['adm1_name'] = lean.adm1_name[lean.reference_year.isin([2014])]
pop1['adm2_name'] = lean.adm2_name[lean.reference_year.isin([2014])]
pop1[2014] = lean.population[lean.reference_year.isin([2014])]
pop1 = pop1.sort_values(by=['adm0_name','adm1_name','adm2_name'])
pop1 = pop1.reset_index(drop=True)

for anno in range(2015,2020):
    pop2 = pd.DataFrame()
    pop2['adm0_name'] = lean.adm0_name[lean.reference_year.isin([anno])]
    pop2['adm1_name'] = lean.adm1_name[lean.reference_year.isin([anno])]
    pop2['adm2_name2'] = lean.adm2_name[lean.reference_year.isin([anno])]
    pop2[anno] = lean.population[lean.reference_year.isin([anno])]
    # NOTE: with nan all the sort will create wrong values
    # For the above reason I have to drop all NaN before sorting
    #pop1.dropna()
    # but it's easyer not to put Tillaberi and Tahoua from the beginning
    pop2 = pop2.sort_values(by=['adm0_name','adm1_name','adm2_name2'])
    pop2 = pop2.reset_index(drop=True)
    pop1[anno] = pop2[anno]

# Preapare DataFrame to plot population
p = pop1[[2014,2015,2016,2017,2018,2019]]
p.index = pop1['adm2_name']
p = p.T

# Select adm2_name to observe
pop = p[['Bankass','Torodi','Gao','Yatenga']]

# Plot population
plt.style.use('fivethirtyeight')
graph = pop.plot(figsize=(10,7))
plt.show()




# WHAT I WANT TO PREDICT
# Create a DataFrame to plot p35_density
p351 = pd.DataFrame()
p351['adm0_name'] = lean.adm0_name[lean.reference_year.isin([2014])]
p351['adm1_name'] = lean.adm1_name[lean.reference_year.isin([2014])]
p351['adm2_name'] = lean.adm2_name[lean.reference_year.isin([2014])]
p351[2014] = lean.p35_density[lean.reference_year.isin([2014])]
p351 = p351.sort_values(by=['adm0_name','adm1_name','adm2_name'])
p351 = p351.reset_index(drop=True)

for anno in range(2015,2020):
    p352 = pd.DataFrame()
    p352['adm0_name'] = lean.adm0_name[lean.reference_year.isin([anno])]
    p352['adm1_name'] = lean.adm1_name[lean.reference_year.isin([anno])]
    p352['adm2_name2'] = lean.adm2_name[lean.reference_year.isin([anno])]
    p352[anno] = lean.p35_density[lean.reference_year.isin([anno])]
    p352 = p352.sort_values(by=['adm0_name','adm1_name','adm2_name2'])
    p352 = p352.reset_index(drop=True)
    p351[anno] = p352[anno]

# Preapare DataFrame to plot p35
phase35 = p351[[2014,2015,2016,2017,2018,2019]]
phase35.index = p351['adm2_name']
phase35 = phase35.T

# Select adm2_name to observe
p35 = phase35[['Djenne']]

# Plot p35
plt.style.use('fivethirtyeight')
graph = p35.plot(figsize=(10,7))
plt.show()




# NOT SO INTERESTING:
# Create a DataFrame to plot phase_class
phase_class1 = pd.DataFrame()
phase_class1['adm0_name'] = lean.adm0_name[lean.reference_year.isin([2014])]
phase_class1['adm1_name'] = lean.adm1_name[lean.reference_year.isin([2014])]
phase_class1['adm2_name'] = lean.adm2_name[lean.reference_year.isin([2014])]
phase_class1[2014] = lean.phase_class[lean.reference_year.isin([2014])]
phase_class1 = phase_class1.sort_values(by=['adm0_name','adm1_name','adm2_name'])
phase_class1 = phase_class1.reset_index(drop=True)

for anno in range(2015,2020):
    phase_class2 = pd.DataFrame()
    phase_class2['adm0_name'] = lean.adm0_name[lean.reference_year.isin([anno])]
    phase_class2['adm1_name'] = lean.adm1_name[lean.reference_year.isin([anno])]
    phase_class2['adm2_name2'] = lean.adm2_name[lean.reference_year.isin([anno])]
    phase_class2[anno] = lean.phase_class[lean.reference_year.isin([anno])]
    phase_class2 = phase_class2.sort_values(by=['adm0_name','adm1_name','adm2_name2'])
    phase_class2 = phase_class2.reset_index(drop=True)
    phase_class1[anno] = phase_class2[anno]

# Preapare DataFrame to plot phase_class
phase = phase_class1[[2014,2015,2016,2017,2018,2019]]
phase.index = phase_class1['adm2_name']
phase = phase.T

# Select adm2_name to see
phase_class = phase[['Bankass','Torodi','Gao','Yatenga']]

# NOTE: Should plot this with "dotplot"
# Plot phase_class
plt.style.use('fivethirtyeight')
graph = phase_class.plot(figsize=(10,7))
plt.show()

# ENDOF NOT SO INTERESTING




# TO DEVELOP
# I would like to visualize adm2_name with the same color and put a legend
sns.swarmplot(x='reference_year',y='phase_class',data=phase_class)




# BANAL
# Visualize all the data available (year, phase_class)
sns.swarmplot(x='reference_year',y='phase_class',data=lean)




# CURIOSITY:
# Visualize all the data available (year, p35_density)
sns.swarmplot(x='reference_year',y='p35_density',data=lean)
#sns.swarmplot(x='reference_year',y='p35_density',data=lean[lean.adm2_name.isin(['Gao','Torodi','Yagha'])])




# NOT SO INTERESTING
# Small linear regression model
#sns.lmplot(x='population',y='p35_density',data=lean,figsize=(10,8))

plt.show()
"""

# Export data
lean.to_csv('../data/Cadre Harmonise/lean.csv',index=False)
