from datetime import datetime

def analyze_lead_decay(leads_df):
    """Calculates the age of leads and identifies 'stale' leads based on decay thresholds."""
    current_date = datetime.now()
    leads_df['lead_age_days'] = (current_date - leads_df['created_at']).dt.days
    # Thresholds: Hot (< 2 days), Warm (2-7 days), Cold (> 7 days)
    leads_df['decay_status'] = leads_df['lead_age_days'].apply(
        lambda x: 'Hot' if x < 2 else ('Warm' if x <= 7 else 'Cold')
    )
    return leads_df