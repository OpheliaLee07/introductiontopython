#%%
import pandas as pd
data = pd.read_csv(r"/Users/Oofy/introductiontopython/04_Assignments/Assignment_4/cereal.csv")
# %%
import sqlalchemy as db

#%%
engine = db.create_engine

metadata = db.MetaData()

Cereal = db.Table("Cereal", )