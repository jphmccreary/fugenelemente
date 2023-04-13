import pandas as pd
import plotly.express as px
from constants import FUGENELEMENTE_FREQUENCY_ORDER

pd.options.plotting.backend = 'plotly'
df = pd.read_csv('lemma_strat_ratios.csv')

fig = px.scatter(df,
                 x="year",
                 y=FUGENELEMENTE_FREQUENCY_ORDER,
                 trendline="ols",
                 title="Overview — All Fugenelemente"
                )

fig.update_layout(
    # font_family="Roboto",
    font_size=18,
    yaxis_title="Proportion of all Compounds",
    legend_title="Fugenelement",
    # font_color="blue",
    # title_font_family="Times New Roman",
    # title_font_color="red",
    # legend_title_font_color="green"
)

fig.layout.yaxis.tickformat = ',.0%'

fig.show()

fig2 = fig = px.scatter(df,
                 x="year",
                 y=without_big_ones,
                 trendline="ols",
                 title="Less Common Fugenelemente"
                )

fig2.update_layout(
    # font_family="Roboto",
    font_size=18,
    yaxis_title="Proportion of all Compounds",
    legend_title="Fugenelement",
    # font_color="blue",
    # title_font_family="Times New Roman",
    # title_font_color="red",
    # legend_title_font_color="green"
)

fig2.layout.yaxis.tickformat = ',.0%'

# fig2.show()
