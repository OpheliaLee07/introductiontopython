#%%
#Problem 1
import pandas as pd
data = pd.read_csv(r"/Users/Oofy/introductiontopython/04_Assignments/Assignment_4/cereal.csv")
#Problem 2
print(data.head(5))
#%%
print(data.head)
data.head()
#%%
#Problem 3
import plotly.graph_objects as go
data.describe(include='all')
#%%
#mfrs = data.mfr.unique()
#factorize = {}
#num = 0
#for i in mfrs:
#    factorize[i] = num
#    num += 1
#data["mfrs_num"] = data["mfr"].apply(lambda x:factorize[x])
#%%
#Problem 4
data.corr(numeric_only=True)
#%%
#codes, uniques = pd.factorize(data["mfr"])
#data["mfr_num"]= codes
#data[["mfr","mfr_num"]]

#%%
#Problem 4 as graph
import matplotlib.pyplot as plt
import numpy as np 
corrs = data.corr(numeric_only=True)
np.fill_diagonal(corrs.values, np.nan)
def heatmap(x,y,size):
    fig, ax= plt.subplots()
    x_labels = [v for v in sorted(x.unique())]
    y_labels = [v for v in sorted(y.unique())]
    x_to_num = {p[1]:p[0] for p in enumerate(x_labels)} 
    y_to_num = {p[1]:p[0] for p in enumerate(y_labels)} 
    
    size_scale = 300
    ax.scatter(
        x=x.map(x_to_num), 
        y=y.map(y_to_num),
        s=size * size_scale,
        marker='s' 
    )

    ax.set_xticks([x_to_num[v] for v in x_labels])
    ax.set_xticklabels(x_labels, rotation=45, horizontalalignment='right')
    ax.set_yticks([y_to_num[v] for v in y_labels])
    ax.set_yticklabels(y_labels)
corr = data.corr(numeric_only=True)
corr = pd.melt(corr.reset_index(), id_vars='index')
corr.columns = ['x', 'y', 'value']

heatmap(
    x=corr['x'],
    y=corr['y'],
    size=corr['value'].abs()
)
#weight and calories have high corr as well as ratings and sugars
#lowest corr fiber and far as well as vitamins and protein
#%%
#Colored graph without data
#plt.matshow(data.corr(numeric_only=True))
#plt.show()

#%%
#Individual Scatterplot
import pandas as pd
import numpy as np
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
import plotly.graph_objects as go

data["name_num"]= pd.factorize(data["name"])[0]
data["Color"]= data["name_num"].apply(lambda x:"red" if x==1
                else ("blue" if x ==0 else"green"))
color = {
    0:"blue",
    1:"red",
    2:"green"
}
fig = px.scatter_matrix(data)
fig = go.Figure()
fig.add_trace (
 go.Scatter(
        x = data["sugars"],
        y = data["potass"],
        mode="markers",
        marker=dict(
            color=data["Color"]
        )
    )
)
fig.update_layout(
    title='Cereal Data',
    dragmode='select',
    width=500,
    height=500,
    xaxis_title = "Sugars",
    yaxis_title = "Potassium"
)
fig.show()
# %%
#Problem 5
import plotly.express as px
fig = px.scatter_matrix(data)
Color = {
    0:"blue",
    1:"red",
    2:"green"
}
fig.add_trace(
    go.Scatter(
        y =y,
        mode="markers",
        marker=dict(
            color=data["Color"]
    )
    )
)
fig.update_layout(
    title='Cereal Data',
    dragmode='select',
    width=4000,
    height=4000,
    hovermode='closest'
)
fig.show()
# %%
#import plotly.graph_objects as go
#import pandas as pd
#fig = go.Figure()
#fig.add_trace(
#    go.Bar(
#        x= data["mfr"],
#        y= data["mfr"].value_counts().values
#    )
#)
#fig.update_layout(
#    title = "Manufacturers and Cereals",
#    template = "simple_white",
#    yaxis=dict(
#        title= "Number of Cereals"
#    ),
#    xaxis=dict(
#        title = "Manufacturers",
#    )
#)
#fig.show()
#%%
#Problem 6
snip= data[["name","mfr", "rating"]]
mfr = data["mfr"].value_counts()
x = mfr.index
y = mfr.values
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=x,
        y=y
    )
)
fig.update_layout(
    xaxis_title="Manufactuer",
    yaxis_title="Count"
)
# %%
#Problem 7
import pandas as pd
import numpy as np
import plotly.graph_objects as go

color = {
    0:"blue",
    1:"red",
    2:"green"
}
fig = px.scatter_matrix(data)

fig = go.Figure()
fig.add_trace (
 go.Scatter(
        x = data["calories"],
        y = data["rating"],
        mode="markers",
        marker=dict(
            color=data["Color"]
        )
    )
)
fig.update_layout(
    title='Cereal Data',
    dragmode='select',
    width=500,
    height=500,
    xaxis_title = "Calories",
    yaxis_title = "Rating"
)
fig.show()

# %%
#Problem 8

#%%
#Problem 9
import matplotlib.pyplot as plt
x = data["rating"]
plt.xlabel("Ratings")
plt.ylabel("Number of Cereals")
plt.title('Ratings Histogram')
plt.hist(x)
plt.show()

#Problem 10
#Conclusions about dataset: There are correlations between...

