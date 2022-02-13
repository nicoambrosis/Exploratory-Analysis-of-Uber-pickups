#!/usr/bin/env python
# coding: utf-8

# In[116]:


get_ipython().run_line_magic('pylab', 'inline')
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


# In[117]:


file_name = 'uber-raw-data-apr14.csv'
data = pd.read_csv(file_name)
print(data.shape)
data.head()


# In[118]:


data.dtypes


# In[119]:


# data['Date/Time'] = data['Date/Time'].map(pd.to_datetime)


# In[120]:


dt = '4/1/2014 0:11:00'


# In[121]:


d, t = dt.split(' ') # esta es una forma de asignar valores a las variables que todavia no conocia!


# In[122]:


d


# In[123]:


t


# In[124]:


dt.split(' ')[0] == d


# In[125]:


d, m, y = d.split('/')
print(d)
print(m)
print(y)


# In[126]:


type(y)


# In[127]:


int(y)


# In[128]:


print(type(y))


# In[129]:


dt


# In[130]:


print(type(dt))
dt = pd.to_datetime(dt)
print(type(dt))
print(dt)


# In[131]:


dt


# In[132]:


data['Date/Time'] = data['Date/Time'].map(pd.to_datetime) 


# In[133]:


data.dtypes


# In[134]:


def  get_dom(dt):
    return dt.day

data['dom'] = data['Date/Time'].map(get_dom)
data


# In[135]:


def get_weekday(dt):
    return dt.weekday()

data['weekday'] = data['Date/Time'].map(get_weekday)


# In[136]:


def get_hour(dt):
    return dt.hour

data['hour'] = data['Date/Time'].map(get_hour)


# In[137]:


data


# # Data Visualization

# In[138]:


fig, ax = plt.subplots(figsize=(10, 5))


histogram = hist(data.dom,
                bins=30,
                color='#065c40',
                align='mid',
                rwidth=0.8,
                range=(0.5, 30.5))

plt.xlabel('Date of the month')
plt.ylabel('Frequency')
plt.title('xxx')

plt.show()


# In[139]:


def count_rows(rows):
    return len(rows)


by_date = data.groupby('dom').apply(count_rows)
by_date


# In[140]:


fig, ax = plt.subplots(figsize=(10, 5))

line_plot = plot(by_date)



plt.show()


# In[141]:


by_date_sorted = by_date.sort_values()
by_date_sorted


# In[142]:


fig, ax = plt.subplots(figsize=(10,5))


bar_plot = bar(range(1,31),by_date_sorted,label='xxx')
plt.xticks(range(1,31), by_date_sorted.index)


plt.legend()


plt.show()


# In[143]:


fig, ax = plt.subplots(figsize=(10, 5))


histogram = hist(data['hour'],
                bins=24,
                color='#065c40',
                align='mid',
                rwidth=0.8,
                range=(0.5, 24))

plt.xlabel('Date of the month')
plt.ylabel('Frequency')
plt.title('xxx')

plt.show()


# In[144]:


fig, ax = plt.subplots(figsize=(10, 5))


histogram = hist(data['weekday'],
                bins=7,
                color='#065c40',
                align='mid',
                rwidth=0.8,
                range=(-0.5, 6.5),
                alpha=.55)

plt.xticks = (range(7), 'Mon Tue Wed Thu Fri Sat Sun'.split())


plt.xlabel('Date of the month')
plt.ylabel('Frequency')
plt.title('xxx')

plt.show()


# In[145]:


# genial!!! un pasito adelante comprendiendo las posibilidades que da pandas!!!!

by_cross = (data
          .groupby(['weekday', 'hour'])
          .apply(count_rows)
          .unstack()
         )
by_cross


# In[146]:


fig, ax = subplots(figsize=(15,5))

sns.heatmap(by_cross,
           cbar=True,
           square=False,
           cmap='Blues',
            )

# Setting title and labels
plt.title('Heatmap practice', fontsize=25)
plt.xlabel('Hours', fontsize=18)
plt.ylabel('Days', fontsize=18)


# save figure
plt.savefig('UBER.png', dpi=200, format='png', bbox_inches='tight')
print('Figure has been saved!!')


plt.show()


# In[147]:


hist(data['Lat'],
     bins=100,
    range=(40.5, 41))
plt.show()


# In[148]:


data.dtypes


# In[149]:


plot(data['Lat'], '.', ms=5, alpha=0.8)
xlim(1,100)


# In[170]:


fig, ax = subplots(figsize=(10,10))
# definimos un dot plot como grfico principal
dot_plot = plot(data['Lon'],
                data['Lat'],
                '.',
                ms=.5,
                alpha=.5
               )
# modificamos el fondo del grafico principal
ax.set_facecolor("white")

# definimos los limites x e y del grafico
plt.xlim(-74.1, -73.7)
plt.ylim(40.6, 40.9)

# definimos nombers y propiedades de los ejes
plt.xlabel('Longitud', fontsize=12)
plt.ylabel('Latitude', fontsize=12)
plt.title('Uber: Manhatam', fontsize=18)

plt.arrow(-74.00, 40.70, 0.05, -0.01,
         color='#004f01',
         linewidth=2,
         alpha=1
         )

#################################################################################
# second axes
ax_2 = fig.add_axes([0.60,0.60,0.25,0.25])

# definimos un dot plot como grfico principal
dot_plot = plot(data['Lon'],
                data['Lat'],
                'o',
                ms=.5,
                color='#a30a0a'
               )

# definimos los limites x e y del grafico
plt.xlim(-73.99, -73.97)
plt.ylim(40.76, 40.78)

xticks([])
yticks([])

plt.title('Central Park', fontweight='bold')
##################################################################################

# third axes
ax_3 = fig.add_axes([0.45,0.15,0.25,0.25])

# definimos un dot plot como grfico principal
dot_plot = plot(data['Lon'],
                data['Lat'],
                '.',
                ms=.5,
                alpha=.5,
                color='#004f01'
               )

# definimos los limites x e y del grafico
plt.xlim(-74.03, -73.95)
plt.ylim(40.70, 40.75)

xticks([])
yticks([])

plt.title('Lower Manhattam', fontweight='bold')

##################################################################################

# save figure
plt.savefig('UBER_Manhatam.png', dpi=200, format='png', bbox_inches='tight')
print('Figure has been saved!!')

plt.show()


# In[151]:


fig, ax = subplots(figsize=(10,10))



# definimos un dot plot como grfico principal
dot_plot = plot(data['Lon'],
                data['Lat'],
                'o',
                ms=1,
                )


# modificamos el fondo del grafico principal
ax.set_facecolor("#cccccc")


# definimos los limites x e y del grafico
plt.xlim(-73.99, -73.97)
plt.ylim(40.76, 40.78)


# definimos nombers y propiedades de los ejes
plt.xlabel('Longitud', fontsize=12)
plt.ylabel('Latitude', fontsize=12)
plt.title('Uber: Manhatam', fontsize=18)


# second axes
# sub_axes = plt.axes([-73.8, 40.8, -73.71, 40.89])



# save figure
plt.savefig('UBER_Manhatam_zoom.png', dpi=200, format='png', bbox_inches='tight')
print('Figure has been saved!!')

plt.show()


# In[152]:


fig, ax = subplots(figsize=(10,10))



# definimos un dot plot como grfico principal
dot_plot = plot(data['Lon'],
                data['Lat'],
                '.',
                ms=.5,
                alpha=.5
               )


# modificamos el fondo del grafico principal
ax.set_facecolor("#cccccc")


# definimos los limites x e y del grafico
plt.xlim(-74.03, -73.95)
plt.ylim(40.70, 40.75)


# definimos nombers y propiedades de los ejes
plt.xlabel('Longitud', fontsize=12)
plt.ylabel('Latitude', fontsize=12)
plt.title('Uber: Manhatam', fontsize=18)


# second axes
# sub_axes = plt.axes([-73.8, 40.8, -73.71, 40.89])



# save figure
plt.savefig('UBER_Manhatam_zoom_2.png', dpi=200, format='png', bbox_inches='tight')
print('Figure has been saved!!')

plt.show()


# In[ ]:




