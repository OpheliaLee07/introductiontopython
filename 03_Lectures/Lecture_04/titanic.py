#%%
import pandas as pd

data = pd.read_csv(r"/Users/Oofy/introductiontopython/03_Lectures/Lecture_04/titanic/train.csv")
# %%
print(data.columns)


# %%
data.Survived.value_counts()
survived = data["Survived (String)"].value_counts()
data["Survived (String)"]= data.Survived.apply(lambda x:"Survived" if x==1 else "Dead")

# %%
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(
    go.Bar(
        x = survived.index,
        y = survived.values
    )
)

fig.update_layout(
    title= "Titanic: Survivors",
    template="simple_white",
    yaxis =dict(
        title="Amount",
        range=[0,600]
    )
    xaxis=dict(
        title="Status"
    )
)
fig.write_image("survivors.jpeg")
# %%
data.corr()

# %%
