#!/usr/bin/env python
# coding: utf-8

# In[77]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

from bokeh.plotting import figure, output_file, show, output_notebook
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral
from bokeh.palettes import Spectral6, Magma, Inferno
from bokeh.themes import built_in_themes
from bokeh.io import curdoc

from datetime import date, timedelta
from IPython import get_ipython
from PIL import Image
from streamlit import caching


# ### Setting Title of the App

# In[88]:


st.title('Sample Deploy')


# In[100]:


st.header('This is a header')
st.subheader('This is a subheader')


# In[102]:


st.text('This is some text.')
st.write('This is some text.')


# ### Dataframes

# In[98]:


df = pd.DataFrame(np.random.randn(50, 20), columns=('col %d' % i for i in range(20)))
st.dataframe(df)


# In[ ]:


df = pd.DataFrame(np.random.randn(5, 5), columns=('col %d' % i for i in range(5)))
st.table(df)


# ### Images

# In[51]:


image = Image.open('logo/eskwelabs.png')
st.sidebar.image(image, caption='', use_column_width=True)


# ### Reports

# In[55]:


plt.figure(figsize=(20,10))

tips = sns.load_dataset("tips")
ax = sns.barplot(x="day", y="total_bill", data=tips)
st.pyplot()


# In[53]:


st.set_option('deprecation.showPyplotGlobalUse', False)


# In[103]:


fig, ax = plt.subplots()
ax.scatter([1, 2, 3], [1, 2, 3])
st.pyplot(fig)


# ### Using Bokeh

# ### Barplot

# In[104]:


caching.clear_cache()
source1 = ColumnDataSource(data=dict(column_values=['InvoiceNo', 'StockCode', 'Description', 'Quantity', 
                                                'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country'], 
                                 column_null_count=[0, 0, 0, 100, 0, 0, 10000, 0], 
                                 color=['#35193e', '#35193e', '#701f57','#701f57', '#ad1759', '#e13342', 
                                        '#f37651', '#f6b48f']))

null_plot= figure(x_range=['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 
                           'CustomerID', 'Country'], plot_height=600, title='Column Null Counts')

null_plot.vbar(x='column_values', top='column_null_count', width=0.5, color='color', 
           legend_field='column_values', source=source1)

null_plot.xaxis.axis_label = 'Columns'
null_plot.yaxis.axis_label = 'Null Counts'
null_plot.xaxis.major_label_orientation = 1.2
st.bokeh_chart(null_plot)


# ### Line Chart

# In[82]:


p = figure(plot_width=600, plot_height=300)
p.line([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 
           [6881.968530629305,5313.478199667941,4443.874408180387,3768.1695746453115,3373.7522363125245,
            3059.781169027937,2813.043183722383,2640.4207898996333,2480.861787245848,2315.6257820620967,
            2165.7180506392915,2037.9850112053998,1961.0375346160306,1892.507829213857,1823.9033825466,
            1755.628369326791,1699.6836724215682, 1637.0241109836584], line_width=2)

st.bokeh_chart(p)


# In[64]:


# st.sidebar.markdown("<h1 style='text-align: center;margin-bottom:50px'>DS Cohort V</h1>", unsafe_allow_html=True)


add_selectbox = st.sidebar.radio(
    "",
    ("Sample 1", "Sample 2", "Sample 3")
)


# In[83]:


if add_selectbox == 'Sample 1':
    st.write('Sample')
elif add_selectbox == 'Sample 2':
    st.write('Sample 2')


# ###  Using HTML

# In[84]:


st.markdown("<ul>"    "<li>Danilo Jr. Gubaton</li>"    "<li>Fili Emerson Chua</li>"
    "<li>John Barrion</li>"\
    "<li>Justine Brian Santoalla </li>"\
    "<li>Rhey Ann Magcalas</li>"\
    "</ul>", unsafe_allow_html=True)


# ### User Input

# In[86]:


st.subheader('Recommender Engine')
st.write('-----------------------------')
user_input = st.text_input("Song Title")
st.write(user_input)


# In[28]:


# jupyter nbconvert --to script sample.ipynb


# ### Running Streamlit Application
# ##### streamlit run sample.py

# ### Git Notes
# 
# 1. Git Add <File Names to Add> 
# 2. Git commit -m "your message"
# 3. Git push origin master

# ### Four Important Files
# 
# 1. python script
# 2. Procfile
# 3. requirements.txt
# 4. setup.sh

# ### Deployment Notes
# 
# 1. cd <repository_name>
# 2. heroku login -i
# 3. heroku create
# 4. git push heroku master
# 5. heroku ps:scale web=1
# 
# ### For checking of errors
# 1. Heroku logs --tail
# 
# ### Renaming URL
# 1. heroku apps:rename <new_url_name>
