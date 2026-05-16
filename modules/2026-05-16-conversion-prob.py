def calculate_stage_probability(stage_history):
    """Estimates the probability of winning a deal based on its current stage."""
    conversions = stage_history.groupby('stage')['is_won'].mean()
    return conversions.to_dict()