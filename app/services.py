import requests
from pycoingecko import CoinGeckoAPI
import plotly
import plotly.graph_objs as go
import json
from datetime import datetime, timedelta
from app.models import PriceAlert
from config import Config

class CryptoPriceService:
    def __init__(self):
        self.cg = CoinGeckoAPI()
        self.alerts = []

    def get_current_prices(self, cryptocurrencies=None):
        """
        Fetch current prices for specified cryptocurrencies
        """
        if cryptocurrencies is None:
            cryptocurrencies = Config.CRYPTOCURRENCIES

        prices = {}
        for coin in cryptocurrencies:
            try:
                data = self.cg.get_price(ids=coin, vs_currencies='usd')
                prices[coin] = data[coin]['usd']
            except Exception as e:
                prices[coin] = None
        return prices

    def get_historical_prices(self, coin_id, days=30):
        """
        Retrieve historical price data for a cryptocurrency
        """
        try:
            historical_data = self.cg.get_coin_market_chart_by_id(
                id=coin_id, 
                vs_currency='usd', 
                days=days
            )
            
            prices = [price[1] for price in historical_data['prices']]
            dates = [datetime.fromtimestamp(price[0]/1000).strftime('%Y-%m-%d') 
                     for price in historical_data['prices']]
            
            trace = go.Scatter(x=dates, y=prices, mode='lines+markers')
            layout = go.Layout(
                title=f'{coin_id.capitalize()} Price History',
                xaxis={'title': 'Date'},
                yaxis={'title': 'Price (USD)'}
            )
            fig = go.Figure(data=[trace], layout=layout)
            
            return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        except Exception as e:
            print(f"Error fetching historical prices: {e}")
            return None

    def add_alert(self, cryptocurrency, target_price, condition):
        """
        Add a new price alert
        """
        alert = PriceAlert(cryptocurrency, target_price, condition)
        self.alerts.append(alert)
        return alert.id

    def check_alerts(self, current_prices):
        """
        Check all active alerts against current prices
        """
        triggered_alerts = []
        for alert in self.alerts:
            current_price = current_prices.get(alert.cryptocurrency)
            if current_price and alert.check_alert(current_price):
                triggered_alerts.append({
                    'id': alert.id,
                    'cryptocurrency': alert.cryptocurrency,
                    'current_price': current_price,
                    'target_price': alert.target_price,
                    'condition': alert.condition
                })
        return triggered_alerts

# Global service instance
price_service = CryptoPriceService()