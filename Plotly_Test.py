import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from plotly.subplots import make_subplots


df = pd.read_csv('IBM_Customer.csv')

fig_h = px.density_heatmap(df, x="State", y="Education")
fig_h.write_html('heatmap_test.html', auto_open=False)

fig_s = px.scatter(df, x="State", y="Education",color = 'Income')
fig_s.write_html('scatter_test.html', auto_open=False)

df_sub = df[['Number of Policies','Income']]
mean_list = []
for i in range(1,10):
    mean_list.append(df_sub[df_sub['Number of Policies'] == i]['Income'].mean(axis = 1)
    )
groups = sorted(df['Number of Policies'].unique())
fig_b = go.Figure([go.Bar(x=groups, y=mean_list)])
fig_b.update_layout(
    xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text='Number of Policies')),
    yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="AVG Income"))
    )
fig_b.write_html('bar_test.html', auto_open=False)

"""
fig = make_subplots(rows=2, cols=2)

fig.add_trace(
    px.density_heatmap(df, x="State", y="Education"),
    row=1, col=1
)
fig.add_trace(
    px.scatter(df, x="State", y="Education",color = 'Income '),
    row=1, col=2
)
"""

