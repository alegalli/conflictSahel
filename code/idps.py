import pandas as pd
import xlrd
import numpy as np

adm2 = ['Bandiagara','Bankass','Djenne','Douentza','Koro','Mopti','Tenenkou','Youwarou',
        'Dire','Goundam','Gourma-Rharous','Niafunke','Tombouctou',
        'Ansongo','Bourem','Gao','Menaka']

# The following data are useful to us
dec14 = pd.read_excel('../data/IDPs Data/Baseline_Assessment_Round_12.xlsx')
nov15 = pd.read_excel('../data/IDPs Data/Baseline_Assessment_Round_18.xlsx')
gen16 = pd.read_excel('../data/IDPs Data/Baseline_Assessment_Round_19.xlsx')
dec16 = pd.read_excel('../data/IDPs Data/Baseline_Assessment_Round_28.xlsx')

dec17 = pd.read_excel('../data/IDPs Data/Baseline_December_2017.xlsx')
dec18 = pd.read_excel('../data/IDPs Data/Mali_Baseline_Assessment_December_2018.xlsx')
dec19 = pd.read_excel('../data/IDPs Data/IOM_DTM_Mali_Baseline_Assessment_Dec_2019_Round_60.xlsx')
apr20 = pd.read_excel('../data/IDPs Data/DTM_Mali_Baseline_Assessment_Round_64_April_2020.xlsx')


# I'm just interested in IDPs Ind# Variation from the prior year
dec17.rename(columns={'Total No. of IDPs Ind.' : 'Total No# of IDPs Ind#'}, inplace=True)
dec18.rename(columns={'Total No. of IDPs Ind.' : 'Total No# of IDPs Ind#'}, inplace=True)
dec19.rename(columns={'Total No. of IDPs Ind.' : 'Total No# of IDPs Ind#'}, inplace=True)

dec14 = dec14[['Snapshot Date','Admin 0','Admin 1','Admin 2','Total No# of IDPs Ind#']]
dec14 = dec14[dec14['Admin 1'].isin(['Gao','Mopti','Tombouctou'])]
dec14 = dec14.reset_index(drop=True)
dec14.rename(columns={'Snapshot Date' : 'date',
                      'Admin 0' : 'adm0_name',
                      'Admin 1' : 'adm1_name',
                      'Admin 2' : 'adm2_name'}, inplace=True)
dec14['date'] = dec14['date'].astype(str)
#Create column reference_year
dec14['reference_year'] = dec14.date.str.split('-',expand=True)[0]
dec14['reference_year'] = dec14['reference_year'].astype(int)
dec14 = dec14.sort_values(by=['adm1_name','adm2_name']).reset_index(drop=True)

nov15 = nov15[['Snapshot Date','Admin 0','Admin 1','Admin 2','Total No# of IDPs Ind#']]
nov15 = nov15[nov15['Admin 1'].isin(['Gao','Mopti','Tombouctou'])]
nov15 = nov15.reset_index(drop=True)
nov15.rename(columns={'Snapshot Date' : 'date',
                      'Admin 0' : 'adm0_name',
                      'Admin 1' : 'adm1_name',
                      'Admin 2' : 'adm2_name'}, inplace=True)
nov15['date'] = nov15['date'].astype(str)
#Create column reference_year
nov15['reference_year'] = nov15.date.str.split('-',expand=True)[0]
nov15['reference_year'] = nov15['reference_year'].astype(int)
nov15 = nov15.sort_values(by=['adm1_name','adm2_name']).reset_index(drop=True)

gen16 = gen16[['Snapshot Date','Admin 0','Admin 1','Admin 2','Total No# of IDPs Ind#']]
gen16 = gen16[gen16['Admin 1'].isin(['Gao','Mopti','Tombouctou'])]
gen16 = gen16.reset_index(drop=True)
gen16.rename(columns={'Snapshot Date' : 'date',
                      'Admin 0' : 'adm0_name',
                      'Admin 1' : 'adm1_name',
                      'Admin 2' : 'adm2_name'}, inplace=True)
gen16['date'] = gen16['date'].astype(str)
#Create column reference_year
gen16['reference_year'] = gen16.date.str.split('-',expand=True)[0]
gen16['reference_year'] = gen16['reference_year'].astype(int)
gen16 = gen16.sort_values(by=['adm1_name','adm2_name']).reset_index(drop=True)

dec16 = dec16[['Snapshot Date','Admin 0','Admin 1','Admin 2','Admin 3','Total No# of IDPs Ind#']]
adm3_menaka = ['Anderamboukane','Inekar','Tidermene']
dec16 = dec16[dec16['Admin 1'].isin(['Gao','Mopti','Tombouctou'])]
dec16 = dec16.reset_index(drop=True)
dec16.rename(columns={'Snapshot Date' : 'date',
                      'Admin 0' : 'adm0_name',
                      'Admin 1' : 'adm1_name',
                      'Admin 2' : 'adm2_name'}, inplace=True)
for adm3 in adm3_menaka:
    dec16.loc[dec16['Admin 3']==adm3,'adm1_name'] = 'Not Gao'
    # Not summed, no problem (they are not too much)
    #adm3_displaced = dec16[(dec16['Admin 3']==adm3),'Total No# of IDPs Ind#']
    #dec16.loc[(dec16['Admin 3']=='Menaka'),'Total No# of IDPs Ind#'] += adm3_displaced
dec16 = dec16[dec16['adm1_name'].isin(['Gao','Mopti','Tombouctou'])]
dec16 = dec16[['date','adm0_name','adm1_name','adm2_name','Total No# of IDPs Ind#']]
dec16['date'] = dec16['date'].astype(str)
#Create column reference_year
dec16['reference_year'] = dec16.date.str.split('-',expand=True)[0]
dec16['reference_year'] = dec16['reference_year'].astype(int)
dec16 = dec16.sort_values(by=['adm1_name','adm2_name']).reset_index(drop=True)

dec17 = dec17[['Snapshot Date','Admin 0','Admin 1','Admin 2','Total No# of IDPs Ind#']]
dec17.loc[:,'Admin 0'] = 'Mali'
dec17 = dec17[dec17['Admin 1'].isin(['Gao','Mopti','Tombouctou'])]
dec17 = dec17.reset_index(drop=True)
dec17.rename(columns={'Snapshot Date' : 'date',
                      'Admin 0' : 'adm0_name',
                      'Admin 1' : 'adm1_name',
                      'Admin 2' : 'adm2_name'}, inplace=True)
#dec17['date'] = dec17['date'].astype(str)
dec17['date'] = '2017-12-31'
#Create column reference_year
dec17['reference_year'] = dec17.date.str.split('-',expand=True)[0]
dec17['reference_year'] = dec17['reference_year'].astype(int)
dec17 = dec17.sort_values(by=['adm1_name','adm2_name']).reset_index(drop=True)

dec18 = dec18[['Snapshot Date','Admin 0','Admin 1','Admin 2','Total No# of IDPs Ind#']]
dec18.loc[:,'Admin 0'] = 'Mali'
dec18 = dec18[dec18['Admin 1'].isin(['Gao','Mopti','Tombouctou'])]
dec18 = dec18.reset_index(drop=True)
dec18.rename(columns={'Snapshot Date' : 'date',
                      'Admin 0' : 'adm0_name',
                      'Admin 1' : 'adm1_name',
                      'Admin 2' : 'adm2_name'}, inplace=True)
dec18['date'] = dec18['date'].astype(str)
#Create column reference_year
dec18['reference_year'] = dec18.date.str.split('-',expand=True)[0]
dec18['reference_year'] = dec18['reference_year'].astype(int)
dec18 = dec18.sort_values(by=['adm1_name','adm2_name']).reset_index(drop=True)

dec19 = dec19[['Snapshot Date','Admin 0','Admin 1','Admin 2','Total No# of IDPs Ind#']]
dec19 = dec19[dec19['Admin 1'].isin(['Gao','Mopti','Tombouctou'])]
dec19 = dec19.reset_index(drop=True)
dec19.rename(columns={'Snapshot Date' : 'date',
                      'Admin 0' : 'adm0_name',
                      'Admin 1' : 'adm1_name',
                      'Admin 2' : 'adm2_name'}, inplace=True)
dec19['date'] = dec19['date'].astype(str)
#Create column reference_year
dec19['reference_year'] = dec19.date.str.split('-',expand=True)[0]
dec19['reference_year'] = dec19['reference_year'].astype(int)
dec19 = dec19.sort_values(by=['adm1_name','adm2_name']).reset_index(drop=True)

apr20 = apr20[['Snapshot Date','Admin 0','Admin 1','Admin 2','Total No# of IDPs Ind#']]
apr20 = apr20[apr20['Admin 1'].isin(['Gao','Mopti','Tombouctou'])]
apr20 = apr20.reset_index(drop=True)
apr20.rename(columns={'Snapshot Date' : 'date',
                      'Admin 0' : 'adm0_name',
                      'Admin 1' : 'adm1_name',
                      'Admin 2' : 'adm2_name'}, inplace=True)
apr20['date'] = apr20['date'].astype(str)
#Create column reference_year
apr20['reference_year'] = apr20.date.str.split('-',expand=True)[0]
apr20['reference_year'] = apr20['reference_year'].astype(int)
apr20 = apr20.sort_values(by=['adm1_name','adm2_name']).reset_index(drop=True)




# Create DataFrame dec15 with the mean values of nov15 and gen16
dec15 = pd.DataFrame(columns=['date','adm0_name','adm1_name','adm2_name','Total No# of IDPs Ind#','reference_year'])
dec15['adm0_name'] = nov15['adm0_name']
dec15['adm1_name'] = nov15['adm1_name']
dec15['adm2_name'] = nov15['adm2_name']
dec15['reference_year'] = nov15['reference_year']
dec15['Total No# of IDPs Ind#'] = round((nov15['Total No# of IDPs Ind#'] + gen16['Total No# of IDPs Ind#'])/2).astype(int)
dec15 = dec15.assign(date='2015-12-31')




# Merge all different years in a unique dataframe, create column difference_last_year, difference_per_month and export in csv

# Append it all from dec14
idps_mali = dec14.append(dec15.append(dec16.append(dec17.append(dec18.append(dec19.append(apr20)))))).reset_index(drop=True)

idps_mali['diff_last_year'] = idps_mali.groupby('adm2_name')['Total No# of IDPs Ind#'].diff().fillna(0)
idps_mali['diff_per_month'] = idps_mali['diff_last_year']/12

permonth20 = idps_mali[idps_mali['reference_year'].isin([2020])]
permonth20.loc[:,'diff_per_month'] *= 3
for a in adm2:
    idps_mali.loc[(idps_mali.reference_year==2020)&(idps_mali.adm2_name==a),'diff_per_month'] = permonth20.loc[(permonth20.reference_year==2020)&(permonth20.adm2_name==a)]['diff_per_month']



# Export in csv
idps_mali.to_csv('../data/IDPs Data/idps_mali.csv',index=False)
