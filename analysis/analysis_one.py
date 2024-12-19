import streamlit as st
import pandas as pd
import datetime
import preprocessing
import helper
import time
from helper import line_plot, Overview_all


def Analysis_stock_data(stock_symbol):
    st.title(f":green[{stock_symbol.replace('.JK','')} Stock Data Analysis]")
    st.markdown(
        """
        **Welcome to the Stock Analysis Dashboard!**
        Explore various tools and features designed to help you analyze stock performance with ease. Select the stock you wish to analyze and dive deeper into the data through interactive visualizations.
        Leverage key metrics such as daily returns, cumulative returns, moving averages, and other essential ratios to support your investment decisions.
        **Start analyzing your stocks now!**
        """
    )
    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        start = st.date_input("Start-Date : ", value=pd.to_datetime("2023-01-01"))
    with col2:
        end = st.date_input(
            "End-Date : ", value=pd.to_datetime(datetime.date.today())
        )

    if st.button("Retrieve Data and Perform Analysis"):
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.020)
            progress_bar.progress(i + 1)

        data = preprocessing.Get_Analysis_Data(
            start=start, end=end, ticker=stock_symbol
        )
        data_compare = preprocessing.Get_compare_data(start=start, end=end)

        with st.expander("Display Stock Data"):
            with st.container():
                st.table(data)
            col1, col2 = st.columns([2, 1])
            with col1:
                st.subheader(f"Total Rows : {data.shape[0]}")
            with col2:
                st.subheader(f"Total Columns : {data.shape[1]}")

        with st.expander("Comprehensive Data Overview"):
            st.title("Graphical Data Representation : ")
            st.plotly_chart(
                helper.Overview_all(data=data, drop=True, title="Volume", width=1000, height=500),
                use_container_width=True,
            )

            st.divider()

            col1, col2, col3 = st.columns(3)

            with col1:
                st.subheader("Highest Price : ")
                st.subheader(f":green[{data.High.max():.2f}]")
                st.subheader("Most Recent Closing Price")
                st.subheader(f":green[{data.Close.iloc[-1]}]")

            with col2:
                st.subheader("Lowest Price : ")
                st.subheader(f":red[{data.Low.min():.2f}]")
                st.subheader("Most Recent Opening Price")
                st.subheader(f":red[{data.Open.iloc[-1]:.2f}]")

            with col3:
                st.subheader("Average Price : ")
                st.subheader(f":blue[{data.Close.mean():.2f}]")
                st.subheader("Average Daily Volume")
                st.subheader(f":blue[{(data.Volume.sum()/30):.2f}]")

            st.divider()

            st.title("Volume Data Visualization: ")
            st.plotly_chart(
                helper.line_plot(data=data, column="Volume", color="blue", width=1000, height=500),
                use_container_width=True,
            )

            st.title("Candlestick Chart")
            st.plotly_chart(helper.candle_plot(df=data.reset_index(), multi=False, width=1000, height=500))

        # Adding the TradingView Widget
        st.markdown("""
        ### Live Market Tracker
        The following is a live market tracker for selected stocks:
        """)

        tradingview_widget = """
        <!-- TradingView Widget BEGIN -->
        <div class="tradingview-widget-container" style="height:100%;width:100%">
            <div class="tradingview-widget-container__widget" style="height:100%;width:100%"></div>
            <div class="tradingview-widget-copyright">
                    <span class="blue-text">Track all Stock markets on Here</span>
                </a>
            </div>
            <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
            {

                "width": 1000,
                "height": 650,
                "symbol": "NASDAQ:AAPL",
                "timezone": "Etc/UTC",
                "theme": "dark",
                "style": "1",
                "locale": "en",
                "backgroundColor": "rgba(0, 0, 0, 1)",
                "gridColor": "rgba(101, 101, 101, 0.06)",
                "withdateranges": true,
                "range": "YTD",
                "hide_side_toolbar": false,
                "allow_symbol_change": true,
                "watchlist": [
                    "NSE:BPCL",
                    "AMEX:EV",
                    "NASDAQ:AAPL",
                    "BSE:IDEA",
                    "NSE:SBIN",
                    "NSE:GOLDBEES",
                    "NASDAQ:MSFT",
                    "NSE:NIFTY",
                    "NSE:MRF"
                    "NASDAQ:TSLA",
                    "NASDAQ:AMZN",
                    "NSE:BANKNIFTY",
                    "NASDAQ:MSTR",
                    "NASDAQ:META",
                    "NASDAQ:GOOGL",
                    "NASDAQ:COIN",
                    "NSE:RELIANCE",
                    "NSE:HDFCBANK",
                    "NSE:ICICIBANK",
                    "NSE:SBIN",
                    "NSE:AXISBANK"
                ],
                "details": true,
                "hotlist": true,
                "calendar": false,
                "support_host": "https://www.tradingview.com"
            }
            </script>
        </div>
        <!-- TradingView Widget END -->
        """

        st.components.v1.html(tradingview_widget, height=650)

# Example usage
if __name__ == "__main__":
    stock_symbol = "NASDAQ:AAPL"
    Analysis_stock_data(stock_symbol)
