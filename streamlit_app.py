import streamlit
import pandas
import requests
import snowflake.connector
streamlit.title('my parents new healthy dinner')
#streamlit.text('Kale, Spinach & Rocket Smoothie@@@')
streamlit.header('breakfast menu')
#streamlit.text('Omega 3 & Blueberry Oatmeal')
#streamlit.text('Kale, Spinach & Rocket Smoothie')
#streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('Build ur own fruit smothiee')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())
fruitvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruitvice_normalized)
streamlit.header('fruitvice fruit advice')
fruit_choice=streamlit.text_input('whta fruit u like to informed about','Kiwi')
streamlit.write('user enterded',fruit_choice)
#fruit_choice1=streamlit.text_input('whta fruit u like to informed about','Apple')
#streamlit.write('user enterded',fruit_choice)

#fruityvice_response=request.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#fruityvice_response=request.get("https://fruityvice.com/api/fruit/watermelon")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

fruitvice_normalized=pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruitvice_normalized)

fruit_choice1=streamlit.text_input('whta fruit u like to informed about','Apple')
streamlit.write('user enterded',fruit_choice)

#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
#my_data_row = my_cur.fetchall()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)

#fruit_choice2=streamlit.text_input('whta fruit u like to informed about','Kiwi')

#streamlit.write('user enterded',fruit_choice2)
