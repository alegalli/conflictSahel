import numpy as np
import pandas as pd
from numpy import corrcoef
import seaborn as sns
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

food = pd.read_csv('../data/Food Prices/millet_price.csv')
conf = pd.read_csv('../data/Conflict Data/conflict_numb.csv')
idps = pd.read_csv('../data/IDPs Data/idps_mali.csv')
lean = pd.read_csv('../data/Cadre Harmonise/lean.csv')


mopti = ['Bandiagara','Bankass','Djenne','Douentza','Koro','Mopti','Tenenkou','Youwarou']
tombouctou = ['Dire','Gourma-Rharous','Niafunke'] # Goundam and Tombouctou were not considered in the Liptako-Gourma study as adm2
gao = ['Ansongo','Bourem','Gao','Menaka']
nord = ['Loroum','Yatenga']
sahel = ['Oudalan','Seno','Soum','Yagha']
est = ['Komonjdjari']
tahoua = ['Tahoua','Tassara','Tillia']
tillaberi = ['Banibangou','Filingue','Kollo','Ouallam','Say','Tera','Tillaberi']




# Add adm2_name in millet
#millet = food
millet = pd.DataFrame(columns=['reference_year','adm0_name','adm1_name','adm2_name','actual_price','decade_price','lg_decade_price','diff_price','lg_diff_price'])

for index, row in food.iterrows():
    if row.reference_year > 2013:
        if row.adm1_name =='Est':
            for adm2 in est:
                millet = millet.append(pd.Series([row['reference_year'],row['adm0_name'],row['adm1_name'],adm2,row['actual_price'],row['decade_price'],row['lg_decade_price'],row['diff_price'],row['lg_diff_price']],index=millet.columns),ignore_index=True)
        elif row.adm1_name == 'Nord':
            for adm2 in nord:
                millet = millet.append(pd.Series([row['reference_year'],row['adm0_name'],row['adm1_name'],adm2,row['actual_price'],row['decade_price'],row['lg_decade_price'],row['diff_price'],row['lg_diff_price']],index=millet.columns),ignore_index=True)
        elif row.adm1_name == 'Sahel':
            for adm2 in sahel:
                millet = millet.append(pd.Series([row['reference_year'],row['adm0_name'],row['adm1_name'],adm2,row['actual_price'],row['decade_price'],row['lg_decade_price'],row['diff_price'],row['lg_diff_price']],index=millet.columns),ignore_index=True)
        elif row.adm1_name == 'Gao':
            for adm2 in gao:
                millet = millet.append(pd.Series([row['reference_year'],row['adm0_name'],row['adm1_name'],adm2,row['actual_price'],row['decade_price'],row['lg_decade_price'],row['diff_price'],row['lg_diff_price']],index=millet.columns),ignore_index=True)
        elif row.adm1_name == 'Mopti':
            for adm2 in mopti:
                millet = millet.append(pd.Series([row['reference_year'],row['adm0_name'],row['adm1_name'],adm2,row['actual_price'],row['decade_price'],row['lg_decade_price'],row['diff_price'],row['lg_diff_price']],index=millet.columns),ignore_index=True)
        elif row.adm1_name =='Tombouctou':
            for adm2 in tombouctou:
                millet = millet.append(pd.Series([row['reference_year'],row['adm0_name'],row['adm1_name'],adm2,row['actual_price'],row['decade_price'],row['lg_decade_price'],row['diff_price'],row['lg_diff_price']],index=millet.columns),ignore_index=True)
        elif row.adm1_name == 'Tahoua':
            for adm2 in tahoua:
                millet = millet.append(pd.Series([row['reference_year'],row['adm0_name'],row['adm1_name'],adm2,row['actual_price'],row['decade_price'],row['lg_decade_price'],row['diff_price'],row['lg_diff_price']],index=millet.columns),ignore_index=True)
        elif row.adm1_name == 'Tillaberi':
            for adm2 in tillaberi:
                millet = millet.append(pd.Series([row['reference_year'],row['adm0_name'],row['adm1_name'],adm2,row['actual_price'],row['decade_price'],row['lg_decade_price'],row['diff_price'],row['lg_diff_price']],index=millet.columns),ignore_index=True)


# THE DIMENSIONS of FOOD CONFLICTS SECURITY
# Merge variables we are interested in
tot = pd.DataFrame(columns=['reference_year','adm0_name','adm1_name','adm2_name','population','phase_class','phase35','p35_density','actual_price','decade_price','lg_decade_price','diff_price','lg_diff_price','conflicts','fatalities'])
tot['reference_year'] = lean['reference_year']
tot['adm0_name'] = lean['adm0_name']               # Key
tot['adm1_name'] = lean['adm1_name']               # Key
tot['adm2_name'] = lean['adm2_name']               # Key
tot['population'] = lean['population']             # Key
tot['phase_class'] = lean['phase_class'] #no
tot['phase35'] = lean['phase35']         #no
tot['p35_density'] = lean['p35_density']           # Evaluator
tot['actual_price'] = millet['actual_price']       # Access Dimension
tot['decade_price'] = millet['decade_price']       # Balanced prize for the region
tot['lg_decade_price'] = millet['lg_decade_price']     #no
tot['diff_price'] = millet['diff_price']           # Stability Dimension (valabs on this value? YES, see millet.py for explanation)
tot['lg_diff_price'] = millet['lg_diff_price'] #no
tot['conflicts'] = conf['projected_conflicts']     # fatalities/conflicts : Conflict Severity
tot['fatalities'] = conf['projected_fatalities']   # Conflict Size


# Merge IDPs variables in Mali
mali = tot[tot.adm0_name=='Mali'].reset_index(drop=True)
mali['projected_idps'] = idps['projected_idps']
mali['diff_last_year'] = idps['diff_last_year']
mali



tot.to_csv('../data/Data/data.csv',index=False)
mali.to_csv('../data/Data/malidataidps.csv',index=False)
