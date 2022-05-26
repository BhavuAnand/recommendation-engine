import pandas as pd
import pickle
import streamlit as st


def recommend(products):
    products_index = prod[prod['productDisplayName'] == products].index[0]
    distances = similarity[products_index]
    products_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_products = []
    for i in products_list:
        recommended_products.append(prod.iloc[i[0]].productDisplayName)
        recommended_products.append(prod.iloc[i[0]].homepage)
    return recommended_products


products_dict = pickle.load(open('product_dict.pkl', 'rb'))

prod = pd.DataFrame(products_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('PHARMACY RECOMMENDS')
selected_product_name = st.selectbox(
    'Enter the products you need...',
    prod['productDisplayName'].values)

if st.button('Recommend Me'):
    recommendations = recommend(selected_product_name)
    for i in recommendations:
        st.write(i)
