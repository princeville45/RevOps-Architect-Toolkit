def cac_payback_period(cac, arpu, gross_margin):
    """Calculates the number of months required to recover Customer Acquisition Cost."""
    monthly_gross_profit = arpu * gross_margin
    if monthly_gross_profit == 0: return float('inf')
    return round(cac / monthly_gross_profit, 2)