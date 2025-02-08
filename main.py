from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import streamlit as st
import os

os.environ['GOOGLE_API_KEY'] = st.secrets['GOOGLE_API_KEY']

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash-thinking-exp-01-21")

# Create prompt template for suggesting food

food_template = " For city {city}, suggest me top {number} food names along with name and address of  best place or resturant where i can get the food "

food_prompt = PromptTemplate(template = food_template, input_variables = ['city', 'number'])




# Create LLM chain using the prompt template and model
food_chain = food_prompt | gemini_model


import streamlit as st

st.header("Food Suggestion App - Abhishek")

st.subheader("Suggest food which is famous in city along with places to eat")

city = st.text_input("Enter city Name")

number = st.number_input("Number of food suggestion", min_value = 1, max_value = 10, value = 1, step = 1)

if st.button("Find me Food"):
    food = food_chain.invoke({"city" : city, "number" : number})
    st.write(food.content)
    
