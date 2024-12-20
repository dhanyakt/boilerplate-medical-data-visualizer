import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

import warnings

warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

# 1
df = pd.read_csv("medical_examination.csv")
#df.info()

# 2 Adding new column
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3 Normalize data
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4
def draw_cat_plot():
    # 5
   # df_cat = None
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active', 'alco', 'gluc', 'cholesterol', 'overweight','smoke'],ignore_index=True)

    # 6

    df_cat = df_cat.groupby(['cardio','variable','value']).value_counts().reset_index(name='total')


    # 7
    sns.catplot(data=df_cat,kind='bar',y='total',x='variable', hue='value', col='cardio')

    # 8
    fig = sns.catplot(data=df_cat,kind='bar',y='total',x='variable', hue='value', col='cardio').figure

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
        ]

    print(df_heat)
    print(df_heat.shape)
    print(df_heat.size)
    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(corr)

    # 14
    fig, ax = plt.subplots(figsize=(12,12))

    # 15
    sns.heatmap(corr, annot=True,fmt='.1f', linewidths=1,mask=mask,square=True, cbar_kws={'shrink': .5})

    # 16
    fig.savefig('heatmap.png')
    return fig
