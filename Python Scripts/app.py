import os
import streamlit as st
# EDA Pkgs
import pandas as pd
# Viz Pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import numpy as np 


def main():

    st.title("Streamlit introduction")
    st.subheader("Introduction to Streamlit and EDA")
    
    # html_temp = """
    # <div style="background-color:tomato;">
    # <p style="color:white;font-size:50px;padding:10px">Streamlit is Awesome</p>
    # </div>
    # """
    # st.markdown(html_temp,unsafe_allow_html=True)

    def file_selector(folder_path='./datasets'):
        filenames = os.listdir(folder_path)
        selected_filename = st.selectbox("Select file", filenames)
        return os.path.join(folder_path, selected_filename)

    filename = file_selector()
    st.info("You Selected {}".format(filename))

    
    # Afficher le dataset chargé suivant un nombre de ligne entrées par l’utilisateur
        
    data = pd.read_csv(filename)
    
    # Show dataset
    if st.checkbox("Show Dataset"):
        number =  st.number_input("Number of Rows ", value=1)
        st.dataframe(data.head(number))

    # Afficher le nom des colonnes du dataset 

    if st.button("Column Names"):
        st.write(data.columns)
    # Afficher le type des colonnes du dataset ainsi que les colonnes sélectionnées 
    if st.button("Data Types"):
        st.write(data.dtypes)

    # La shape du dataset, par lignes et par colonnes
    if st.checkbox("Shape of Dataset"):
        data_dim = st.radio("Show Dimension By ",("Rows","Columns"))
        if data_dim == 'Rows':
            st.text("Number of Rows")
            st.write(data.shape[0])
        elif data_dim == 'Columns':
            st.text('Number of Rows')
            st.write(data.shape[1])
        else:
            st.write(data.shape)
    # Afficher les statistiques descriptives du dataset
    if st.checkbox("Description"):
        st.write(data.describe().T)
    
    # Afficher plusieurs type de graphique dans une partie visualisation avec notamment : 
    st.subheader("Data Visualization")
    
        # Une heatmap des corrélations avec Matplotlib et Seaborn (avec les valeurs annotés)
    
    if st.checkbox("Correlation Plot[Seaborn]"):
        
        st.write(sns.heatmap(data.iloc[:,1:15].corr(), annot = True))
        st.pyplot()


        # Un graphique en barres afin de visualiser la taille du dataset par caractéristiques (on pourra notamment grouper les données afin d’avoir des graphiques plus précis)
        st.subheader("Customizable Plot")
        all_columns_names = data.columns.tolist()
        type_of_plot = st.selectbox("Select Type of Plot",["area","bar","line","hist","box","kde"])
        selected_columns_names = st.multiselect("Select Columns To Plot",all_columns_names)

        if st.button("Genera Plot"):
            st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))

            # Plot By Streamlit
        if type_of_plot == 'area':
            cust_data = data[selected_columns_names]
            st.area_chart(cust_data)

        elif type_of_plot == 'bar':
            cust_data = data[selected_columns_names]
            st.bar_chart(cust_data)

        elif type_of_plot == 'line':
            cust_data = data[selected_columns_names]
            st.line_chart(cust_data)
        
        # Custom Plot 
        elif type_of_plot:
            cust_plot= data[selected_columns_names].plot(kind=type_of_plot)
            st.write(cust_plot)
            st.pyplot()

st.set_option('deprecation.showPyplotGlobalUse', False)

def sidebar():
    st.sidebar.header("Example de Side Bar")
    st.sidebar.text("Hello")


if __name__ == '__main__':
    main()
    sidebar()





################################################################################################################################################################################
################################# USEFULL ##############################################

# €rror : TabError: inconsistent use of tabs and spaces in indentation
# $olver: 
# Ctrl+Shift+P or View->Command Palette. and 
# Convert Indentation to spaces