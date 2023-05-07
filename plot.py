import pandas as pd
import plotly.express as px
from constants import FUGENELEMENTE_FREQUENCY_ORDER

pd.options.plotting.backend = 'plotly'
df = pd.read_csv('results/test.csv')

all_fn = list(FUGENELEMENTE_FREQUENCY_ORDER)

fig = px.scatter(df,
                 x="Year",
                 y=all_fn,
                 trendline="ols",
                 title="Overview — All Fugenelemente",
                 color_discrete_sequence=px.colors.qualitative.Dark24,
                 labels={
                    'NULL': 'Ø',             # 48.7%
                    'ADD_S': '⊕s',            # 20.6%
                    'ADD_N': '⊕n',            # 11.4%
                    'ADD_EN': '⊕en',           # 9.2%
                    'ADD_NEN': '⊕nen',          # 5.6%
                    'DEL_US_ADD_EN': '⊖us ⊕en',    # 1.3%
                    'DEL_UM_ADD_EN': '⊖um ⊕en',    # 0.7%
                    'DEL_UM_ADD_A': '⊖um ⊕a',
                    'DEL_E': '⊖e',
                    'DEL_A_ADD_EN': '⊖a ⊕en',
                    'ADD_E': '⊕e',
                    'UMLAUT_ADD_E': '“ ⊕e',
                    'DEL_ON_ADD_EN': '⊖on ⊕a',
                    'ADD_ES': '⊕es',
                    'UMLAUT_ADD_ER': '“ ⊕er',
                    'DEL_EN': '⊖en',
                    'DEL_ON_ADD_A': '⊖on ⊕a',
                    'ADD_ER': '⊕er',
                    'ADD_IEN': '⊕ien',
                    'DEL_E_ADD_I': '⊖e ⊕i',
                 }
                #  nbins=27
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

without_big_ones = list(FUGENELEMENTE_FREQUENCY_ORDER[3:])

fig2 = fig = px.scatter(df,
                 x="Year",
                 y=without_big_ones,
                 trendline="ols",
                 title="Less Common Fugenelemente",
                 color_discrete_sequence=px.colors.qualitative.Dark24,
                #  nbins=27
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

fig2.layout.yaxis.tickformat = ',.00%'

fig2.show()
