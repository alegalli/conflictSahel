import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read data
foodm = pd.read_csv('../data/Food Prices/wfp_food_prices_mali.csv',low_memory=False)
foodb = pd.read_csv('../data/Food Prices/wfp_food_prices_burkina-faso.csv',low_memory=False)
foodn = pd.read_csv('../data/Food Prices/wfp_food_prices_niger.csv',low_memory=False)

foodm = foodm.drop(0)
foodb = foodb.drop(0)
foodn = foodn.drop(0)


# Work on a single dataset
food = foodm.append(foodb.append(foodn)).reset_index()
# Select columns I'm interested in
food.rename(columns={'country':'adm0_name',
                     'admname':'adm1_name'}, inplace=True)
food = food[['date','adm0_name','adm1_name','mktname','category','cmname',
        'price','currency','unit']]
# Create column reference_year
food['reference_year'] = food.date.str.split('-',expand=True)[0]
food['reference_year'] = food['reference_year'].astype(int)

food['price'] = food['price'].astype(float)

# Select index I'm interested in
food = food[food.reference_year.isin([2013,2014,2015,2016,2017,2018,2019])]
food = food[food.adm1_name.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
food = food.reset_index(drop=True)



# Interested only on millet price variations
millet = food[food['cmname'] == 'Millet - Retail']
millet = millet[['reference_year','adm0_name','adm1_name','price']]

# Price mean
mmil = pd.DataFrame({'mean' : millet.groupby(['reference_year','adm1_name'])['price'].mean()}).reset_index()
# Price std
stmil = pd.DataFrame({'std' : millet.groupby(['reference_year','adm1_name'])['price'].std()}).reset_index()

# Difference of price mean
diffmil = pd.DataFrame(columns=['reference_year','adm1_name','price_var'])

for year in range(2013,2020):
    for elem in millet['adm1_name'].unique():
        diffmil = diffmil.append(pd.Series([year, elem, 0],index=diffmil.columns),ignore_index=True)

mmil = mmil.sort_values(['reference_year','adm1_name']).reset_index()
diffmil = diffmil.sort_values(['reference_year','adm1_name']).reset_index()
# Finally him:
for adm1 in diffmil.adm1_name.unique():
    diffmil.loc[diffmil.adm1_name == adm1,'price_var'] = mmil[mmil.adm1_name == adm1]['mean'].diff()

diffmil = diffmil[diffmil.reference_year.isin(range(2014,2020))]
diffmil.reset_index(inplace=True)
diffmil = diffmil[['reference_year','adm1_name','price_var']]


plt.style.use('fivethirtyeight')

# Plot millet price std
gra = stmil[stmil.adm1_name.isin(['Gao'])].plot(x='reference_year',y=['std'],figsize=(10,7))
gra.xaxis.label.set_visible(False)

# Plot millet price mean
gra = m_p[m_p.adm1_name.isin(['Nord'])].plot(x='reference_year',y=['mean'],figsize=(10,7))
gra.xaxis.label.set_visible(False)

# Plot millet price variations
gra = diffmil[diffmil.adm1_name.isin(['Gao'])].plot(x='reference_year',y=['price_var'],figsize=(10,7))
gra.xaxis.label.set_visible(False)

plt.show()




# Data to be exported
millet_price = mmil
millet_price = millet_price[millet_price.reference_year.isin([2014,2015,2016,2017,2018,2019])]
millet_price.reset_index(inplace=True)
millet_price['price_var'] = diffmil['price_var']
millet_price = millet_price[['reference_year','adm1_name','mean','price_var']]


# From adm1_name to adm2_name
adm2 = ['Bankass','Koro','Douentza','Djenne','Bandiagara','Tenenkou','Mopti','Youwarou',
        'Gourma-Rharous','Dire','Niafunke',
        'Gao','Ansongo','Menaka','Bourem',
        'Yatenga','Loroum',
        'Yagha','Seno','Soum','Oudalan',
        'Komonjdjari',
        'Tillia', # I take out Tillaberi and Tahoua because of some values are in Tillaberi Department and Tahoua Department
        'Banibangou','Filingue','Ouallam','Say','Tera','Torodi','Abala','Ayerou']
m_p = pd.DataFrame(columns=['reference_year','adm2_name','mean','price_var'])
for year in range(2014,2020):
    for adm2_name in adm2:
        m_p = m_p.append(pd.Series([year, adm2_name, 0, 0],index=m_p.columns),ignore_index=True)

# Can be prettier
for index, row in millet_price.iterrows():
    if row.adm1_name == 'Gao':
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Ansongo'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Ansongo'), 'price_var'] = row['price_var']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Bourem'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Bourem'), 'price_var'] = row['price_var']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Gao'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Gao'), 'price_var'] = row['price_var']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Menaka'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Menaka'), 'price_var'] = row['price_var']
    if row.adm1_name == 'Mopti':
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Bandiagara'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Bandiagara'), 'price_var'] = row['price_var']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Bankass'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Bankass'), 'price_var'] = row['price_var']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Djenne'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Djenne'), 'price_var'] = row['price_var']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Douentza'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Douentza'), 'price_var'] = row['price_var']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Koro'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Koro'), 'price_var'] = row['price_var']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Mopti'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Mopti'), 'price_var'] = row['price_var']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Tenenkou'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Tenenkou'), 'price_var'] = row['price_var']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Youwarou'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Youwarou'), 'price_var'] = row['price_var']
    if row.adm1_name == 'Tombouctou':
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Dire'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Dire'), 'price_var'] = row['price_var']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Gourma-Rharous'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Gourma-Rharous'), 'price_var'] = row['price_var']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Niafunke'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Niafunke'), 'price_var'] = row['price_var']
    if row.adm1_name == 'Est':
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Komonjdjari'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Komonjdjari'), 'price_var'] = row['price_var']
    if row.adm1_name == 'Nord':
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Loroum'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Loroum'), 'price_var'] = row['price_var']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Yatenga'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Yatenga'), 'price_var'] = row['price_var']
    if row.adm1_name == 'Sahel':
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Oudalan'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Oudalan'), 'price_var'] = row['price_var']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Seno'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Seno'), 'price_var'] = row['price_var']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Soum'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Soum'), 'price_var'] = row['price_var']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Yagha'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Yagha'), 'price_var'] = row['price_var']
    if row.adm1_name == 'Tahoua':
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Tillia'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Tillia'), 'price_var'] = row['price_var']
    if row.adm1_name == 'Tillaberi':
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Abala'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Abala'), 'price_var'] = row['price_var']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Ayerou'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Ayerou'), 'price_var'] = row['price_var']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Banibangou'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Banibangou'), 'price_var'] = row['price_var']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Filingue'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Filingue'), 'price_var'] = row['price_var']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Ouallam'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Ouallam'), 'price_var'] = row['price_var']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Say'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Say'), 'price_var'] = row['price_var']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Tera'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Tera'), 'price_var'] = row['price_var']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Torodi'), 'mean'] = row['mean']
        m_p.loc[(m_p.reference_year == row.reference_year) & (m_p.adm2_name == 'Torodi'), 'price_var'] = row['price_var']





# export data
m_p.to_csv('../data/Food Prices/millet_price.csv',index=False)
