import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast favorites')
streamlit.text('🥣omega3 & blueberry oatmeal')
streamlit.text('🥗kale,spinach & rocket smoothie')
streamlit.text('🐔Hard-Boiled free Range Egg');
streamlit.text(' 🥑🍞 Avocado Toast');
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
