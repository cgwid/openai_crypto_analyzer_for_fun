# openai_crypto_analyzer_for_fun

This is a project to experiment with OpenAI. This analysis is NOT intended for actual use. DO NOT use for investment advice. 

Basic application that uses streamlit for the UI. Makes a call to coinranking API to get the past 7 day history of bitcoin prices.
Makes a call to openai api, passes over the data gathered from coinranking API with a prompt to analyze the data and provide analysis. 

# To run app

1) Need to get an API key for coinranking which is on RapidAPI.
2) Need an API key from OpenAI
3) Command to run from terminal -> streamlit run app.py
