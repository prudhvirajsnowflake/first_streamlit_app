import streamlit
import pandas
import requests

streamlit.title("My Mom's New Healthy Diner")

streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Test')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruits_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruits_list = my_fruits_list.set_index('Fruit')

fruits_selected = streamlit.multiselect("Pick Some Fruits:", list(my_fruits_list.index),['Avocado','Strawberries'])
my_fruits_to_show = my_fruits_list.loc[fruits_selected]
streamlit.dataframe(my_fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# Normalize Json Response
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Create as a Pandas Dataframe which is Table
streamlit.dataframe(fruityvice_normalized)
