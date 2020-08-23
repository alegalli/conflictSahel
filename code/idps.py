import pandas as pd
import numpy as np

# Read IDPs data
gen14 = pd.read_excel('../data/IDPs Data/Baseline_Assessment_Round_1.xlsx')
feb14 = pd.read_excel('../data/IDPs Data/Baseline_Assessment_Round_2.xlsx')
dec14 = pd.read_excel('../data/IDPs Data/Baseline_Assessment_Round_12.xlsx')
nov15 = pd.read_excel('../data/IDPs Data/Baseline_Assessment_Round_18.xlsx')
gen16 = pd.read_excel('../data/IDPs Data/Baseline_Assessment_Round_19.xlsx')

dec16 = pd.read_excel('../data/IDPs Data/Baseline_Assessment_Round_28.xlsx')
dec17 = pd.read_excel('../data/IDPs Data/Baseline_December_2017.xlsx')
dec18 = pd.read_excel('../data/IDPs Data/Mali_Baseline_Assessment_December_2018.xlsx')
dec19 = pd.read_excel('../data/IDPs Data/IOM_DTM_Mali_Baseline_Assessment_Dec_2019_Round_60.xlsx')
apr20 = pd.read_excel('../data/IDPs Data/DTM_Mali_Baseline_Assessment_Round_64_April_2020.xlsx')


# Rename columns with different name
dec17.rename(columns={'Total No. of IDPs HH' : 'Total No# of IDPs HH',
                      'Total No. of IDPs Ind.' : 'Total No# of IDPs Ind#',
                      'Total No. of Returnees HH.' : 'Total No# of Returnees HH#',
                      'Total No. of Returnees Ind.' : 'Total No# of Returnees Ind#'}, inplace=True)
dec18.rename(columns={'Total No. of IDPs HH' : 'Total No# of IDPs HH',
                      'Total No. of IDPs Ind.' : 'Total No# of IDPs Ind#',
                      'Total No. of Returnees HH.' : 'Total No# of Returnees HH#',
                      'Total No. of Returnees Ind.' : 'Total No# of Returnees Ind#'}, inplace=True)
dec19.rename(columns={'Total No. of IDPs HH' : 'Total No# of IDPs HH',
                      'Total No. of IDPs Ind.' : 'Total No# of IDPs Ind#',
                      'Total No. of Returnees HH.' : 'Total No# of Returnees HH#',
                      'Total No. of Returnees Ind.' : 'Total No# of Returnees Ind#'}, inplace=True)

# for cycle didn't work to clean data
"""
idps = [gen14,feb14,dec14,nov15,gen16,dec16,dec17,dec18,dec19,apr20]
for survey in idps:
    survey = survey[['Snapshot Date','Admin 0','Admin 1','Admin 2','Total No# of IDPs HH',
                   'Total No# of IDPs Ind#','Total No# of Returnees HH#','Total No# of Returnees Ind#']]
    survey = survey[survey['Admin 1'].isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
    survey = survey.reset_index(drop=True)
    survey.rename(columns={'Snapshot Date' : 'date',
                          'Admin 0' : 'adm0_name',
                          'Admin 1' : 'adm1_name',
                          'Admin 2' : 'adm2_name'}, inplace=True)
    survey['date'] = survey['date'].astype(str)
    #Create column reference_year
    survey['reference_year'] = survey.date.str.split('-',expand=True)[0]
    survey['reference_year'] = survey['reference_year'].astype(int)
"""

# Horrible way to clean data

# Here we have data just for adm1 in gen14
gen14 = gen14[['Snapshot Date','Admin 0','Admin 1','Admin 2','Total No# of IDPs HH',
                 'Total No# of IDPs Ind#','Total No# of Returnees HH#','Total No# of Returnees Ind#']]
gen14 = gen14[gen14['Admin 1'].isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
gen14 = gen14.reset_index(drop=True)
gen14.rename(columns={'Snapshot Date' : 'date',
                      'Admin 0' : 'adm0_name',
                      'Admin 1' : 'adm1_name',
                      'Admin 2' : 'adm2_name'}, inplace=True)
gen14['date'] = gen14['date'].astype(str)
#Create column reference_year
gen14['reference_year'] = gen14.date.str.split('-',expand=True)[0]
gen14['reference_year'] = gen14['reference_year'].astype(int)
gen14.sort_values(['adm0_name','adm1_name','adm2_name']).reset_index()

feb14 = feb14[['Snapshot Date','Admin 0','Admin 1','Admin 2','Total No# of IDPs HH',
                 'Total No# of IDPs Ind#','Total No# of Returnees HH#','Total No# of Returnees Ind#']]
feb14 = feb14[feb14['Admin 1'].isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
feb14 = feb14.reset_index(drop=True)
feb14.rename(columns={'Snapshot Date' : 'date',
                      'Admin 0' : 'adm0_name',
                      'Admin 1' : 'adm1_name',
                      'Admin 2' : 'adm2_name'}, inplace=True)
feb14['date'] = feb14['date'].astype(str)
#Create column reference_year
feb14['reference_year'] = feb14.date.str.split('-',expand=True)[0]
feb14['reference_year'] = feb14['reference_year'].astype(int)
feb14.sort_values(['adm0_name','adm1_name','adm2_name']).reset_index()

dec14 = dec14[['Snapshot Date','Admin 0','Admin 1','Admin 2','Total No# of IDPs HH',
                 'Total No# of IDPs Ind#','Total No# of Returnees HH#','Total No# of Returnees Ind#']]
dec14 = dec14[dec14['Admin 1'].isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
dec14 = dec14.reset_index(drop=True)
dec14.rename(columns={'Snapshot Date' : 'date',
                      'Admin 0' : 'adm0_name',
                      'Admin 1' : 'adm1_name',
                      'Admin 2' : 'adm2_name'}, inplace=True)
dec14['date'] = dec14['date'].astype(str)
#Create column reference_year
dec14['reference_year'] = dec14.date.str.split('-',expand=True)[0]
dec14['reference_year'] = dec14['reference_year'].astype(int)
dec14.sort_values(['adm0_name','adm1_name','adm2_name']).reset_index()

nov15 = nov15[['Snapshot Date','Admin 0','Admin 1','Admin 2','Total No# of IDPs HH',
                 'Total No# of IDPs Ind#','Total No# of Returnees HH#','Total No# of Returnees Ind#']]
nov15 = nov15[nov15['Admin 1'].isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
nov15 = nov15.reset_index(drop=True)
nov15.rename(columns={'Snapshot Date' : 'date',
                      'Admin 0' : 'adm0_name',
                      'Admin 1' : 'adm1_name',
                      'Admin 2' : 'adm2_name'}, inplace=True)
nov15['date'] = nov15['date'].astype(str)
#Create column reference_year
nov15['reference_year'] = nov15.date.str.split('-',expand=True)[0]
nov15['reference_year'] = nov15['reference_year'].astype(int)
nov15.sort_values(['adm0_name','adm1_name','adm2_name']).reset_index()

gen16 = gen16[['Snapshot Date','Admin 0','Admin 1','Admin 2','Total No# of IDPs HH',
                 'Total No# of IDPs Ind#','Total No# of Returnees HH#','Total No# of Returnees Ind#']]
gen16 = gen16[gen16['Admin 1'].isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
gen16 = gen16.reset_index(drop=True)
gen16.rename(columns={'Snapshot Date' : 'date',
                      'Admin 0' : 'adm0_name',
                      'Admin 1' : 'adm1_name',
                      'Admin 2' : 'adm2_name'}, inplace=True)
gen16['date'] = gen16['date'].astype(str)
#Create column reference_year
gen16['reference_year'] = gen16.date.str.split('-',expand=True)[0]
gen16['reference_year'] = gen16['reference_year'].astype(int)
gen16.sort_values(['adm0_name','adm1_name','adm2_name']).reset_index()


dec16 = dec16[['Snapshot Date','Admin 0','Admin 1','Admin 2','Total No# of IDPs HH',
                 'Total No# of IDPs Ind#','Total No# of Returnees HH#','Total No# of Returnees Ind#']]
dec16 = dec16[dec16['Admin 1'].isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
dec16 = dec16.reset_index(drop=True)
dec16.rename(columns={'Snapshot Date' : 'date',
                      'Admin 0' : 'adm0_name',
                      'Admin 1' : 'adm1_name',
                      'Admin 2' : 'adm2_name'}, inplace=True)
dec16['date'] = dec16['date'].astype(str)
#Create column reference_year
dec16['reference_year'] = dec16.date.str.split('-',expand=True)[0]
dec16['reference_year'] = dec16['reference_year'].astype(int)
dec16.sort_values(['adm0_name','adm1_name','adm2_name']).reset_index()

dec17 = dec17[['Snapshot Date','Admin 0','Admin 1','Admin 2','Total No# of IDPs HH',
                 'Total No# of IDPs Ind#','Total No# of Returnees HH#','Total No# of Returnees Ind#']]
dec17 = dec17[dec17['Admin 1'].isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
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
dec17.sort_values(['adm0_name','adm1_name','adm2_name']).reset_index()

dec18 = dec18[['Snapshot Date','Admin 0','Admin 1','Admin 2','Total No# of IDPs HH',
                 'Total No# of IDPs Ind#','Total No# of Returnees HH#','Total No# of Returnees Ind#']]
dec18 = dec18[dec18['Admin 1'].isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
dec18 = dec18.reset_index(drop=True)
dec18.rename(columns={'Snapshot Date' : 'date',
                      'Admin 0' : 'adm0_name',
                      'Admin 1' : 'adm1_name',
                      'Admin 2' : 'adm2_name'}, inplace=True)
dec18['date'] = dec18['date'].astype(str)
#Create column reference_year
dec18['reference_year'] = dec18.date.str.split('-',expand=True)[0]
dec18['reference_year'] = dec18['reference_year'].astype(int)
dec18.sort_values(['adm0_name','adm1_name','adm2_name']).reset_index()


dec19 = dec19[['Snapshot Date','Admin 0','Admin 1','Admin 2','Total No# of IDPs HH',
                 'Total No# of IDPs Ind#','Total No# of Returnees HH#','Total No# of Returnees Ind#']]
dec19 = dec19[dec19['Admin 1'].isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
dec19 = dec19.reset_index(drop=True)
dec19.rename(columns={'Snapshot Date' : 'date',
                      'Admin 0' : 'adm0_name',
                      'Admin 1' : 'adm1_name',
                      'Admin 2' : 'adm2_name'}, inplace=True)
dec19['date'] = dec19['date'].astype(str)
#Create column reference_year
dec19['reference_year'] = dec19.date.str.split('-',expand=True)[0]
dec19['reference_year'] = dec18['reference_year'].astype(int)
dec19.sort_values(['adm0_name','adm1_name','adm2_name']).reset_index()

apr20 = apr20[['Snapshot Date','Admin 0','Admin 1','Admin 2','Total No# of IDPs HH',
                 'Total No# of IDPs Ind#','Total No# of Returnees HH#','Total No# of Returnees Ind#']]
apr20 = apr20[apr20['Admin 1'].isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
apr20 = apr20.reset_index(drop=True)
apr20.rename(columns={'Snapshot Date' : 'date',
                      'Admin 0' : 'adm0_name',
                      'Admin 1' : 'adm1_name',
                      'Admin 2' : 'adm2_name'}, inplace=True)
apr20['date'] = apr20['date'].astype(str)
#Create column reference_year
apr20['reference_year'] = apr20.date.str.split('-',expand=True)[0]
apr20['reference_year'] = apr20['reference_year'].astype(int)
apr20.sort_values(['adm0_name','adm1_name','adm2_name']).reset_index()

# Create DataFrame dec15 with the mean values of nov15 and gen16
dec15 = pd.DataFrame(columns=['date','adm0_name','adm1_name','adm2_name','Total No# of IDPs HH','Total No# of IDPs Ind#',
                              'Total No# of Returnees HH#','Total No# of Returnees Ind#','reference_year'])
dec15['date'] = '2015-12-31'
dec15['adm0_name'] = nov15['adm0_name']
dec15['adm1_name'] = nov15['adm1_name']
dec15['adm1_name'] = nov15['adm2_name']
dec15['reference_year'] = nov15['reference_year']
dec15['Total No# of IDPs HH'] = (nov15['Total No# of IDPs HH'] + gen16['Total No# of IDPs HH'])/2
dec15['Total No# of IDPs Ind#'] = (nov15['Total No# of IDPs Ind#'] + gen16['Total No# of IDPs Ind#'])/2
dec15['Total No# of Returnees HH#'] = (nov15['Total No# of Returnees HH#'] + gen16['Total No# of Returnees HH#'])/2
dec15['Total No# of Returnees Ind#'] = (nov15['Total No# of Returnees Ind#'] + gen16['Total No# of Returnees Ind#'])/2
