import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

@st.cache_data
@st.cache_resource
def load_data():
    data = pd.read_csv('air+quality/2.csv', sep=";", index_col=0, parse_dates=True)
    # Фильтр по июлю 2004
    data = data['01.07.2004':'30.07.2004']
    data = data[['T','RH','AH','COGT','C6H6GT','Category']]
    return data

st.header('Вывод данных и графиков')

data_load_state = st.text('Загрузка данных...')
data = load_data()
data_load_state.text('Данные загружены!')

if st.checkbox('Описание Датасета'):
    '''
	Набор данных по исследованию качества воздуха - https://archive.ics.uci.edu/dataset/360/air+quality

	Набор содержит почасовые данные, полученные от комбинированного газоанализатора, установленного в итальянском городе вблизи автомобильной магистрали. 
	Данные записывались с Марта 2004 по февраль 2005 (один год).

	Каждый файл содержит следующие колонки:

	Date: дата в формате ДЕНЬ-МЕСЯЦ-ГОД Набор данных содержит данные с интервалом измерения в один час. 
	
	Time: время в формате ЧАСЫ:МИНУТЫ:СЕКУНДЫ. 
	
	CO(GT): концентрация СО mg/m^3 
	
	PT08.S1(CO): концентрация СО mg/m^3 усредненная за час 
	
	NMHC(GT): максимальная концентрация паров гидрокарбонатов усредненная за час microg/m^3 
	
	C6H6(GT): максимальная концентрация паров бензина усредненная за час microg/m^3 
	
	PT08.S2(NMHC): концентрация паров гидрокарбонатов усредненная за час microg/m^3 
	
	NOx(GT): максимальная концентрация оксидов азота усредненная за час microg/m^3 
	
	PT08.S3(NOx): концентрация оксидов азота усредненная за час microg/m^3 
	
	NO2(GT): максимальная концентрация двуокиси азота усредненная за час microg/m^3 
	
	PT08.S4(NO2): концентрация двуокиси азота усредненная за час microg/m^3 
	
	PT08.S5(O3): концентрация озона усредненная за час microg/m^3 
	
	T: температура в градусах Цельсия 
	
	RH: относительная влажность в %. 
	
	AH: абсолютная влажность в %. 
	
	Category: категория качества воздуха - Good/Bad
	
    '''
    
    
st.subheader('Первые 5 значений')
st.write(data.head())

if st.checkbox('Показать все данные'):
    st.subheader('Данные')
    st.write(data)

st.subheader('Временные ряды для числовых колонок')
fig1, ax = plt.subplots(1, 1, sharex='col', sharey='row', figsize=(10,5))
ax = data.plot(ax=ax,legend=True)
st.pyplot(fig1)

