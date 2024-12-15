import streamlit as st
import streamlit.components.v1 as components
import analysis.analysis_one as analysis_one
import analysis.analysis_multiple as analysis_multiple
import forecasting.forecasting as forecasting
import forecasting.advance_forecasting as advance_forecasting
import pandas as pd
import guide

st.set_page_config(layout="wide")

ticker_list = pd.read_csv("scrapping_ticker/Ticker_list.csv")


section = st.sidebar.radio(
    "**Select Section:**", 
    options=["📊 Stock Analysis","🔮 Stock Forecasting","📈 Expert Details"])
#st.sidebar.divider()

ticker= ticker_list['Ticker'].values
ticker_map = {ticker: ticker + '.JK' for ticker in ticker}
display_names = list(ticker_map.keys())

selected_display_name = st.sidebar.selectbox('Select Stock Symbol', options=display_names , index=1)
stock_symbol = ticker_map[selected_display_name]




if section == "📊 Stock Analysis" : 

    tab1, tab2 = st.tabs(["Single Stock Analysis", "Multiple Stock Analysis"])

    with tab1 :

        analysis_one.Analysis_stock_data(stock_symbol=stock_symbol)
    
    with tab2 : 
         
      selected_display_names = st.sidebar.multiselect('Select Stock Symbols', options=display_names , max_selections=4 , default=display_names[:2])

      selected_symbols = [ticker_map[name] for name in selected_display_names]

      analysis_multiple.multiply_alalysis(selected_symbols)

elif section == "🔮 Stock Forecasting":

    tab1 , tab2 = st.tabs(["Forecast" , "Documentation"])

    with tab1 : 
        forecasting.Forecasting(stock_symbol = stock_symbol)
    with tab2 : 
        guide.Forecast()


elif section == '⚙️ Customize LSTM Parameters':
    advance_forecasting.Forecasting(stock=stock_symbol)
elif section == '📈 Expert Details' :

    st.title(":green[Expert Details]")
    st.image("experts/1.jpg", caption="Shubham Kadam")
    st.text("Teaching Stock Trading/Future & Options trading")
    st.text("I teach my students from zero level to advance level each and every concept and also provide")
    st.text("practical demonstration of my teachings in live market sessions,which boost their confidence as they know the market concepts")
    st.markdown('[Instagram Profile](https://www.instagram.com/shubh_kadam__/?hl=en) | [Telegram Channel](https://t.me/subh_kadam)')
    st.image("experts/2.jpg", caption="Rachana Phadke Ranade")
    st.text("A teacher and a finfluencer")
    st.markdown('[Instagram Profile](https://www.instagram.com/ca_rachanaranade/) | [Email](mailto:brands@rachanaranade.com)')
    st.image("experts/3.jpg", caption="Buddhi prakash karol")
    st.text("Finance & Stock Market influencer")
    st.markdown('[Instagram Profile](https://www.instagram.com/financebyanmoll/) | [Telegram channel](https://t.me/tradingwithkarol)')
else : 
    st.title(":red[select section]")

# Embedding the chatbot iframe
components.html(
    """
    <iframe
src="https://www.chatbase.co/chatbot-iframe/d9vNazMKD7XRuYyAu42lL"
width="100%"
style="height: 100%; min-height: 700px"
frameborder="0"
></iframe>
    """,
    height=700 # Set the iframe height based on your layout needs
)








