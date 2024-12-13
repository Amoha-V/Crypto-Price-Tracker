from datetime import datetime

class PriceAlert:
    def __init__(self, cryptocurrency, target_price, condition):
        self.id = id(self)  # Unique identifier
        self.cryptocurrency = cryptocurrency
        self.target_price = float(target_price)
        self.condition = condition  # 'above' or 'below'
        self.created_at = datetime.now()
        self.is_active = True

    def check_alert(self, current_price):
        """
        Check if the alert condition is met
        
        Args:
            current_price (float): Current price of the cryptocurrency
        
        Returns:
            bool: True if alert condition is met, False otherwise
        """
        try:
            current_price = float(current_price)
            if self.condition == 'above' and current_price > self.target_price:
                return True
            elif self.condition == 'below' and current_price < self.target_price:
                return True
            return False
        except (TypeError, ValueError):
            return False

    def to_dict(self):
        """
        Convert alert to dictionary representation
        
        Returns:
            dict: Dictionary with alert details
        """
        return {
            'id': self.id,
            'cryptocurrency': self.cryptocurrency,
            'target_price': self.target_price,
            'condition': self.condition,
            'created_at': self.created_at.isoformat(),
            'is_active': self.is_active
        }