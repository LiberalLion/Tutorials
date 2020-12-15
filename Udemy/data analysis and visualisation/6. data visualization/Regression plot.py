import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = sns.load_dataset('diamonds').sample(franc=1).head(100)
print df

sns.lmplot('price','carat',df).savefig('regression1.png')

#modify
sns.lmplot('price','carat',df,scatter_kws={'maker':'o','color':'green'},line_kws={'color':'red','linewidth':1}).savefig('regression2.png')

#higher order trend line
sns.lmplot('price','carat',df,order=4,scatter_kws={'maker':'o','color':'green'},line_kws={'color':'red','linewidth':1}).savefig('regression3.png')

#scatter plot without trend line
sns.lmplot('price','carat',df,fit_reg=False).savefig('regression4.png')

#hue arguments
sns.lmplot('price','carat',df,hue='cut',makers=['^','v','*','.','s']).savefig('regression5.png')
sns.lmplot('price','carat',df,hue='cut').savefig('regression6.png')

#local regression
sns.lmplot('price','carat',df,lowess=True).savefig('regression7.png')

#regplot
sns.lmplot('price','carat',df).get_figure().savefig('regression8.png')

#sub plots
image , (plt1, plt2) = plt.subplot(1,2,Sharey = True)

sns.regplot('price','carat',df,ax=plt1).get_figure().savefig('regression9.png')
sns.boxplot(df['carat'],df['depth'],color='green',ax=plt2).get_figure().savefig('regression10.png')