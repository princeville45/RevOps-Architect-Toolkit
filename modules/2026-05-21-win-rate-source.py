def win_rate_by_source(opportunities_df):
    """Calculates win rate percentages segmented by lead source."""
    won = opportunities_df[opportunities_df['stage'] == 'Closed Won'].groupby('lead_source').size()
    total = opportunities_df.groupby('lead_source').size()
    win_rate = (won / total * 100).fillna(0).round(2)
    return win_rate.to_dict()