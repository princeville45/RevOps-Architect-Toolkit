def calculate_weighted_pipeline(deals_df):
    """Calculates the weighted forecast based on stage-specific win probabilities."""
    # Assuming 'stage_probability' and 'deal_value' columns exist
    deals_df['weighted_value'] = deals_df['deal_value'] * deals_df['stage_probability']
    return deals_df.groupby('forecast_month')['weighted_value'].sum().to_dict()