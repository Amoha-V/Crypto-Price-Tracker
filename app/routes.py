from flask import Blueprint, render_template, jsonify, request
from app.services import price_service

# Create the main blueprint
main_bp = Blueprint('main', __name__)

# Define the home route
@main_bp.route('/')
def index():
    """
    Render the home page.
    """
    return render_template('index.html')

# Route to fetch current cryptocurrency prices
@main_bp.route('/prices')
def get_prices():
    """
    Fetch and display current cryptocurrency prices.
    """
    prices = price_service.get_current_prices()
    return render_template('prices.html', prices=prices)

# Route to fetch historical prices for a specific cryptocurrency
# @main_bp.route('/historical/<coin_id>')
# def historical_prices(coin_id):
#     """
#     Fetch historical prices for a specific cryptocurrency.
#     """
#     chart_data = price_service.get_historical_prices(coin_id)
#     return render_template('prices.html', chart_data=chart_data)

# Route to add a new price alert
@main_bp.route('/add_alert', methods=['POST'])
def add_alert():
    """
    Add a new price alert.
    """
    data = request.json
    alert_id = price_service.add_alert(
        data['cryptocurrency'], 
        float(data['target_price']), 
        data['condition']
    )
    return jsonify({'alert_id': alert_id})

# Route to check triggered alerts
@main_bp.route('/check_alerts')
def check_alerts():
    """
    Check and return triggered alerts.
    """
    current_prices = price_service.get_current_prices()
    triggered = price_service.check_alerts(current_prices)
    return jsonify(triggered)

# Route to list all active alerts
@main_bp.route('/alerts')
def list_alerts():
    """
    List all active alerts.
    """
    alerts = [alert.to_dict() for alert in price_service.alerts]
    return render_template('alerts.html', alerts=alerts)
@main_bp.route('/set_email', methods=['POST'])
def set_email():
    """
    Set the recipient email for alerts
    """
    data = request.json
    email = data.get('email')
    
    if not email:
        return jsonify({'error': 'Email is required'}), 400
    
    # Validate email (you might want to add more robust email validation)
    if '@' not in email:
        return jsonify({'error': 'Invalid email format'}), 400
    
    price_service.set_recipient_email(email)
    return jsonify({'message': 'Email set successfully'})
# In routes.py, modify the historical_prices route
@main_bp.route('/historical/<coin_id>')
def historical_prices(coin_id):
    """
    Fetch historical prices for a specific cryptocurrency.
    
    Args:
        coin_id (str): Identifier of the cryptocurrency
    """
    # Use 30 days as default, could be made configurable
    chart_data = price_service.get_historical_prices(coin_id, days=30)
    
    if chart_data:
        return render_template('historical.html', chart_data=chart_data, coin_id=coin_id)
    else:
        # Handle case where no data is available
        return render_template('historical.html', chart_data=None, coin_id=coin_id)