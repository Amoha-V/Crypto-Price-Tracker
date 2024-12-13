document.addEventListener('DOMContentLoaded', () => {
    const alertForm = document.getElementById('alert-form');
    
    if (alertForm) {
        alertForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const cryptocurrency = document.getElementById('cryptocurrency').value;
            const targetPrice = document.getElementById('target-price').value;
            const condition = document.getElementById('condition').value;

            try {
                const response = await fetch('/add_alert', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        cryptocurrency,
                        target_price: targetPrice,
                        condition
                    })
                });
                const data = await response.json();
                alert(`Alert set successfully. Alert ID: ${data.alert_id}`);
            } catch (error) {
                console.error('Error setting alert:', error);
                alert('Failed to set alert');
            }
        });
    }

    // Periodic alert checking
    function checkAlerts() {
        fetch('/check_alerts')
            .then(response => response.json())
            .then(triggeredAlerts => {
                if (triggeredAlerts.length > 0) {
                    triggeredAlerts.forEach(alert => {
                        alert(`ALERT: ${alert.cryptocurrency} is ${alert.condition} ${alert.target_price}. Current price: ${alert.current_price}`);
                    });
                }
            })
            .catch(error => console.error('Error checking alerts:', error));
    }

    // Check alerts every 5 minutes
    setInterval(checkAlerts, 5 * 60 * 1000);
});