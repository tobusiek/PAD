import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import time


st.title('Praca domowa 10')
with st.sidebar:
    selected = option_menu(
        menu_title='Praca domowa 10',
        options=['Ankieta', 'Staty'],
        default_index=0
    )

if selected == 'Ankieta':
    st.header('Ankieta')
    fname = st.text_input('Wprowadz swoje imie:')
    lname = st.text_input('Wprowadz swoje nazwisko:')
    if st.button('Ok'):
        if fname.title() and lname.title():
            st.success('Formularz zostal zapisany poprawnie')
        else:
            st.error('Nie wprowadzono wszystkich danych')
else:
    st.header('Staty')
    data = st.file_uploader('Wgraj dane csv', type=['csv'])
    if data is not None:
        with st.spinner('Wczytywanie...'):
            time.sleep(2)
        df = pd.read_csv(data, sep=';')
        st.success('Pomyslne wczytywanie ramki')
        st.dataframe(df.head(10))

        columns = df.columns.tolist()
        selected_columns = st.multiselect('Wybierz kolumny do wykresu', columns)
        plot_data = df[selected_columns]
        selected_chart = st.selectbox('Wybierz rodzaj wykresu:', ['slupkowy', 'liniowy'])
        if selected_chart == 'slupkowy':
            st.bar_chart(plot_data)
        elif selected_chart == 'liniowy':
            st.line_chart(plot_data)
