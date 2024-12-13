import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'CG-JHehLbL77G2iauc2JSFEJe4c')
    COINGECKO_API_BASE_URL = 'https://www.coingecko.com/en/api'
    CRYPTOCURRENCIES = [
        'bitcoin', 
        'ethereum', 
        'dogecoin', 
        'ripple', 
        'cardano'
    ]
    TRACKING_INTERVAL = 5  # minutes

    