import numpy as np
import pandas as pd

# Area [sqkm]


lean = pd.read_csv('../data/Cadre Harmonise/lean.csv')

c = pd.DataFrame(columns=['adm0_name','adm1_name','adm2_name','area'])

# Burkina Faso
c = c.append({'adm0_name':'Burkina Faso','adm1_name':'Est','adm2_name':'Komonjdjari','area':5088.588437}, ignore_index=True)
c = c.append({'adm0_name':'Burkina Faso','adm1_name':'Nord','adm2_name':'Loroum','area':3699.84375}, ignore_index=True)
c = c.append({'adm0_name':'Burkina Faso','adm1_name':'Nord','adm2_name':'Yatenga','area':6807.1125}, ignore_index=True)
c = c.append({'adm0_name':'Burkina Faso','adm1_name':'Sahel','adm2_name':'Oudalan','area':10062.26688}, ignore_index=True)
c = c.append({'adm0_name':'Burkina Faso','adm1_name':'Sahel','adm2_name':'Seno','area':7008.368125}, ignore_index=True)
c = c.append({'adm0_name':'Burkina Faso','adm1_name':'Sahel','adm2_name':'Soum','area':12630.2125}, ignore_index=True)
c = c.append({'adm0_name':'Burkina Faso','adm1_name':'Sahel','adm2_name':'Yagha','area':6489.309375}, ignore_index=True)

# Mali
# Goudam e Tombouctou si estendono troppo a nord e non li consideriamo nello studio di Liptako-Gourma
c = c.append({'adm0_name':'Mali','adm1_name':'Gao','adm2_name':'Ansongo','area':23037.4025}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Gao','adm2_name':'Bourem','area':42654.755}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Gao','adm2_name':'Gao','area':34429.1475}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Gao','adm2_name':'Menaka','area':76744.76}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Mopti','adm2_name':'Bandiagara','area':7967.27625}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Mopti','adm2_name':'Bankass','area':6217.776875}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Mopti','adm2_name':'Djenne','area':4495.46875}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Mopti','adm2_name':'Douentza','area':23223.365}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Mopti','adm2_name':'Koro','area':10633.3725}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Mopti','adm2_name':'Mopti','area':7242.456875}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Mopti','adm2_name':'Tenenkou','area':11468.63125}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Mopti','adm2_name':'Youwarou','area':8009.15}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Tombouctou','adm2_name':'Dire','area':2405.831875}, ignore_index=True)
#c = c.append({'adm0_name':'Mali','adm1_name':'Tombouctou','adm2_name':'Goundam','area':}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Tombouctou','adm2_name':'Gourma-Rharous','area':42475.46}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Tombouctou','adm2_name':'Niafunke','area':8785.14}, ignore_index=True)
#c = c.append({'adm0_name':'Mali','adm1_name':'Tombouctou','adm2_name':'Tombouctou','area':}, ignore_index=True)

# Niger
c = c.append({'adm0_name':'Niger','adm1_name':'Tahoua','adm2_name':'Tahoua','area':12269.856016}, ignore_index=True)
# ch: Tahoua 11462.7225+ Ville De Tahoua 807.133516
c = c.append({'adm0_name':'Niger','adm1_name':'Tahoua','adm2_name':'Tassara','area':40722.49375}, ignore_index=True)
# ch: Tassara 29647.7125+ Tchintabaraden 11074.78125
c = c.append({'adm0_name':'Niger','adm1_name':'Tahoua','adm2_name':'Tillia','area':17873.395}, ignore_index=True)
c = c.append({'adm0_name':'Niger','adm1_name':'Tillaberi','adm2_name':'Banibangou','area':6549.830625}, ignore_index=True)
c = c.append({'adm0_name':'Niger','adm1_name':'Tillaberi','adm2_name':'Filingue','area':23998.076016}, ignore_index=True)
# ch: Filingue 10499.86875+ Abala 12213.74+ Balleyara 1284.467266
c = c.append({'adm0_name':'Niger','adm1_name':'Tillaberi','adm2_name':'Kollo','area':8915.9375}, ignore_index=True)
c = c.append({'adm0_name':'Niger','adm1_name':'Tillaberi','adm2_name':'Ouallam','area':14603.85}, ignore_index=True)
c = c.append({'adm0_name':'Niger','adm1_name':'Tillaberi','adm2_name':'Say','area':13760.84625}, ignore_index=True)
# ch: Say 6612.579375+ Torodi 7148.266875
c = c.append({'adm0_name':'Niger','adm1_name':'Tillaberi','adm2_name':'Tera','area':10933.95391}, ignore_index=True)
# ch: Tera 9619.6575+ Bankilare 1314.296406
c = c.append({'adm0_name':'Niger','adm1_name':'Tillaberi','adm2_name':'Tillaberi','area':12344.234063}, ignore_index=True)
# ch: Tillaberi 5345.1725+ Tillaberi Commune (NOT THERE)+ Gotheye 3949.414688+ Ayerou 3049.646875


c['population'] = lean['population']


c.to_csv('../data/areas.csv',index=False)
