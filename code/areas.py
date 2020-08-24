import numpy as np
import pandas as pd

c = pd.DataFrame(columns=['adm0_name','adm1_name','adm2_name'])

# Burkina Faso
c = c.append({'adm0_name':'Burkina Faso','adm1_name':'Est','adm2_name':'Komonjdjari'}, ignore_index=True)
c = c.append({'adm0_name':'Burkina Faso','adm1_name':'Nord','adm2_name':'Loroum'}, ignore_index=True)
c = c.append({'adm0_name':'Burkina Faso','adm1_name':'Nord','adm2_name':'Yatenga'}, ignore_index=True)
c = c.append({'adm0_name':'Burkina Faso','adm1_name':'Sahel','adm2_name':'Oudalan'}, ignore_index=True)
c = c.append({'adm0_name':'Burkina Faso','adm1_name':'Sahel','adm2_name':'Seno'}, ignore_index=True)
c = c.append({'adm0_name':'Burkina Faso','adm1_name':'Sahel','adm2_name':'Soum'}, ignore_index=True)
c = c.append({'adm0_name':'Burkina Faso','adm1_name':'Sahel','adm2_name':'Yagha'}, ignore_index=True)

# Mali
c = c.append({'adm0_name':'Mali','adm1_name':'Gao','adm2_name':'Ansongo'}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Gao','adm2_name':'Bourem'}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Gao','adm2_name':'Gao'}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Gao','adm2_name':'Menaka'}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Mopti','adm2_name':'Bandiagara'}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Mopti','adm2_name':'Bankass'}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Mopti','adm2_name':'Djenne'}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Mopti','adm2_name':'Douentza'}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Mopti','adm2_name':'Koro'}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Mopti','adm2_name':'Mopti'}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Mopti','adm2_name':'Tenenkou'}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Mopti','adm2_name':'Youwarou'}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Tombouctou','adm2_name':'Dire'}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Tombouctou','adm2_name':'Goundam'}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Tombouctou','adm2_name':'Gourma-Rharous'}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Tombouctou','adm2_name':'Niafunke'}, ignore_index=True)
c = c.append({'adm0_name':'Mali','adm1_name':'Tombouctou','adm2_name':'Tombouctou'}, ignore_index=True)

# Niger
c = c.append({'adm0_name':'Niger','adm1_name':'Tahoua','adm2_name':'Tahoua'}, ignore_index=True)
# ch: Tahoua + Ville De Tahoua + Tahoua Department
c = c.append({'adm0_name':'Niger','adm1_name':'Tahoua','adm2_name':'Tassara'}, ignore_index=True)
# ch: Tassara + Tchintabaraden
c = c.append({'adm0_name':'Niger','adm1_name':'Tahoua','adm2_name':'Tillia'}, ignore_index=True)
c = c.append({'adm0_name':'Niger','adm1_name':'Tillaberi','adm2_name':'Banibangou'}, ignore_index=True)
c = c.append({'adm0_name':'Niger','adm1_name':'Tillaberi','adm2_name':'Filingue'}, ignore_index=True)
# ch: Filingue + Abala + Balleyara
c = c.append({'adm0_name':'Niger','adm1_name':'Tillaberi','adm2_name':'Kollo'}, ignore_index=True)
c = c.append({'adm0_name':'Niger','adm1_name':'Tillaberi','adm2_name':'Ouallam'}, ignore_index=True)
c = c.append({'adm0_name':'Niger','adm1_name':'Tillaberi','adm2_name':'Say'}, ignore_index=True)
# ch: Say + Torodi
c = c.append({'adm0_name':'Niger','adm1_name':'Tillaberi','adm2_name':'Tera'}, ignore_index=True)
# ch: Tera + Bankilare
c = c.append({'adm0_name':'Niger','adm1_name':'Tillaberi','adm2_name':'Tillaberi'}, ignore_index=True)
# ch: Tillaberi + Tillaberi Commune + Tillaberi Department + Gotheye + Ayerou

c.to_csv('../data/areas.csv',index=False)
