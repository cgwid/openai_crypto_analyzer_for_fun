import openai
import getBitCoinPrices
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# update to use env_variables at some point
openai.api_key = os.environ.get('openai-api-key')

def BasicGeneration(userPrompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": userPrompt}]
    )

    return completion.choices[0].message.content

# There was a bug with Python 3.9.7 and streamlit so updated venv to 3.11.3
st.title('Bitcoin analyzer with ChatGPT')
st.subheader('Example: Analyzing Live Crypto Prices')

if st.button('Analyze'):
    with st.spinner('Getting Bitcoin prices'):
        bitcoinPrices = getBitCoinPrices.GetBitcoinPrices();
        st.success('Done')
    with st.spinner('Anaylzing Bitcoin prices'):
        chatGPTPrompt = f"""You are an expert crypto trader with more than 10 years of experience,
            I will provide you with a list of bitcoin prices for the last 7 days
            can you provide me with technical analysis of Bitcoin based on these prices. Here is 
            what I want: 
            Price Overview,
            Moving Averages,
            Relative Strength Index (RSI),
            Moving Average Convergence Divergence (MACD),
            Advice and Suggestion,
            Do I buy or sell?
            Please be as detailed as you can, and explain in a way any beginner can understand.
            And here is the price list {bitcoinPrices}
            """
        
        analysis = BasicGeneration(chatGPTPrompt)

        st.text_area("Analysis", analysis, height=500)
        st.success("Done")










