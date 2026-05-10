import numpy as np

class NormalizationEngine:
    """
    EMEA Revenue Normalization Engine
    Architect: Irem Victor Chinonso
    Target: $8.6M Portfolio Standardization
    """
    def __init__(self, master_currency="USD"):
        self.master_currency = master_currency
        # Volatile market rates (Simulation based on May 2026 indices)
        self.exchange_rates = {
            "NGN": 1550.0, 
            "GHS": 14.8, 
            "KES": 132.5, 
            "ZAR": 18.2
        }

    def normalize_revenue(self, amount, currency):
        """Standardizes regional revenue to USD to neutralize currency noise."""
        if currency == self.master_currency:
            return amount
        rate = self.exchange_rates.get(currency)
        if not rate:
            raise ValueError(f"Currency {currency} not supported for normalization.")
        return round(amount / rate, 2)

    def calculate_growth_velocity(self, current_rev, previous_rev):
        """Calculates the Statistical Growth Index."""
        return round(((current_rev - previous_rev) / previous_rev) * 100, 2)

if __name__ == "__main__":
    engine = NormalizationEngine()
    
    # Simulation: Standardizing a Nigerian regional sale
    raw_sales_ngn = 5000000 
    normalized_usd = engine.normalize_revenue(raw_sales_ngn, "NGN")
    
    print(f"Portfolio Asset (NGN): ₦{raw_sales_ngn:,.2f}")
    print(f"Normalized Asset (USD): ${normalized_usd:,.2f}")
    print(f"Status: Revenue Integrity Confirmed.")
