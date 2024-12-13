# CryptoPrice Tracker 

## Overview

CryptoPrice Tracker is a web application that allows users to track cryptocurrency prices, set price alerts, and view historical price charts. The application leverages the CoinGecko API to fetch real-time and historical cryptocurrency price data.

## Features

-  Real-time cryptocurrency price tracking
-  Live price display for multiple cryptocurrencies
-  Price alert system
-  Historical price charts
-  Support for multiple cryptocurrencies (Bitcoin, Ethereum, Dogecoin)

## Prerequisites

- Python 3.8+
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cryptoprice_tracker.git
   cd cryptoprice_tracker
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root and add any necessary configuration variables.

## Project Structure

- `app/`
  - `models.py`: Defines data models (e.g., PriceAlert)
  - `routes.py`: Flask route handlers
  - `services.py`: Business logic for price fetching and alert management
  - `static/`: Contains static assets (CSS and JavaScript)
- `templates/`
  - `base.html`: Base template for consistent styling
  - `index.html`: Main dashboard template
  - `prices.html`: Cryptocurrency prices page
  - `alerts.html`: Alerts management page
- `config.py`: Application configuration
- `run.py`: Application entry point

## Configuration

Modify `config.py` to customize:
- Cryptocurrency list
- API settings
- Other application configurations

## Running the Application

1. Start the application locally:
   ```bash
   python run.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## Deployment

This project is deployed on Render. 
Access the live application here:
[CryptoPrice Tracker](https://crypto-price-tracker-fwuw.onrender.com/)

### Start Command :
```bash
web: gunicorn run:app
```

## Key Dependencies

- Flask
- CoinGecko API
- Plotly
- Requests
- Gunicorn

## Alert System

Users can:
- Set price alerts for specific cryptocurrencies
- Choose 'above' or 'below' conditions
- Receive notifications when price targets are met

## Customization

Easily extend the application by:
- Adding more cryptocurrencies
- Implementing additional alert conditions
- Creating more advanced visualization features

## License

Distributed under the MIT License. See [LICENSE](https://opensource.org/licenses/MIT) for more information.

