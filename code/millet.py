import pandas as pd
# TODO: control on the import https://realpython.com/pandas-project-gradebook/ (loading)

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


# Create column reference_year
food['reference_year'] = food.date.str.split('-',expand=True)[0]
food['reference_year'] = food['reference_year'].astype(int)

food = food[['date','reference_year','adm0_name','adm1_name','category','cmname',
        'price','currency','unit']]

food['price'] = food['price'].astype(float)

# Select index I'm interested in
food = food[food.reference_year.isin([2011,2012,2013,2014,2015,2016,2017,2018,2019])]
food = food[food.adm1_name.isin(['Gao','Mopti','Tombouctou','Nord','Sahel','Est','Tahoua','Tillaberi'])]
food = food.reset_index(drop=True)

# Drop nan Values: drop the index if any value is Null
food = food.dropna(axis='index', how='any')




# Interested only on millet price variations
# NOTE: to do it for all food types just delete the following row
food = food[food['cmname'] == 'Millet - Retail']

food = food[['reference_year','adm0_name','adm1_name','price']]

# Create millet DataFrame with actual_price of that year and decade_price mean of all decade
millet = pd.DataFrame({'actual_price' : food.groupby(['reference_year','adm0_name','adm1_name'])['price'].mean()}).reset_index()
decade = pd.DataFrame({'decade_price' : food.groupby(['adm0_name','adm1_name'])['price'].mean()}).reset_index()
lg_decade = food['price'].mean()

millet = pd.merge(millet,decade)
millet['lg_decade_price'] = lg_decade

# Sort # Not necessary
#millet = millet.sort_values(['reference_year','adm0_name','adm1_name']).reset_index()

millet['var_price'] = millet['actual_price']-millet['decade_price']
millet['lg_var_price'] = millet['actual_price']-millet['lg_decade_price']




# Export millet at adm1 level, with a simple merge each adm2 level which shares
# the same adm1 will have the same food price
millet.to_csv('../data/Food Prices/millet_price.csv',index=False)
