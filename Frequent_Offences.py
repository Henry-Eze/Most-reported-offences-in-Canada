
Crime = {
    'Year':	              [2025,	  2024,	  2023,  	2022,	  2021,	 2020,	 2019],		
    'Mischief':	          [307909,	319888,	 328235,	314486,	305557,	299020,	283986],
    'Theft>5,000':        [222516,	237014,	 236831,	215275,	185666,	180504,	226428],
    'Assault level_1':	  [219951,	216989,	 209899,	196990,	185199,	178952, 198215],
    'Shoplifting>$5,000': [208941,	185799,	 175794,	160032,	150366,	165575,	188186],
    'Fraud':              [177472, 182696,	 155792,	151365,	138296,	138049,	160476],
    'Fail_comply_order':	[142540,	141378,	 139311,	133453,	136003,	137208,	142013],
    'Breaking_Entering':	[112762,	120924,	 136195,	132548,	125215,	129595,	140415],
    'Theft>$5,000_MV':	  [109437,	113751,	 130706,	127940,	107542,	108982,	135164],
    'Disturb_peace':	    [109248,	108392,	 111078,	105590,	95242,	91347,	108804],
    'Uttering_threats':	   [97324,	 97317, 	94630,	87771,	87799,	84818,	80828]

}
#Suppress the warning
import warnings

warnings.filterwarnings(
    "ignore",
    category=FutureWarning,
    module="bar_chart_race"
)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(18, 12))
ax.set_xlim(0, 350000)

plt.close(fig)

bcr.bar_chart_race(
    df=df,
    filename='Crime_Categories_sample.gif',
    orientation='h',
    sort='desc',
    n_bars=len(df.columns),
    fixed_order=False,
    fixed_max=True,
    steps_per_period=10,
    period_length=250,
    title='Crime Categories in Canada',
    bar_size=0.8,
    bar_label_font={'size': 22},
    tick_label_font={'size': 16},
    bar_texttemplate='{x:,.0f}',
    period_label={
        'x': 0.95,
        'y': 0.15,
        'ha': 'right',
        'size': 35,
        'weight': 'bold'
    },
    fig=fig,
    writer='pillow'
)


#Display your faster animation
from IPython.display import Image, display

display(Image(filename='Crime_Categories_sample.gif'))
