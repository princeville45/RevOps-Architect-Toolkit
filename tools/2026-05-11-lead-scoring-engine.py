def score_leads(leads_list):
    """
    Weighted lead scoring engine.
    Criteria:
    - Company Size (Weight 20%)
    - Engagement Score (Weight 30%)
    - Industry Match (Weight 20%)
    - Days Since Contact (Weight 10%)
    - Deal Stage (Weight 20%)
    """
    scored_leads = []
    for lead in leads_list:
        # Size Score (0-100)
        size_score = 100 if lead['size'] > 500 else 50 if lead['size'] > 50 else 20
        
        # Engagement Score (Direct 0-100)
        engagement = lead['engagement']
        
        # Industry Match
        industry_score = 100 if lead['industry'] in ['Tech', 'Finance', 'Manufacturing'] else 40
        
        # Recency (Max 10 points)
        recency_score = max(0, (30 - lead['days_since_contact']) / 3)
        
        # Stage Score
        stage_map = {"Discovery": 20, "Demo": 60, "Negotiation": 90}
        stage_score = stage_map.get(lead['stage'], 10)
        
        final_score = (size_score * 0.2) + (engagement * 0.3) + (industry_score * 0.2) + (recency_score) + (stage_score * 0.2)
        
        action = "High Priority - Call Now" if final_score > 75 else "Nurture" if final_score > 40 else "Cold"
        
        scored_leads.append({
            "name": lead['name'],
            "score": round(final_score, 2),
            "action": action
        })
    return sorted(scored_leads, key=lambda x: x['score'], reverse=True)

if __name__ == "__main__":
    leads = [
        {"name": "TechCorp", "size": 1000, "engagement": 85, "industry": "Tech", "days_since_contact": 2, "stage": "Demo"},
        {"name": "SmallBiz", "size": 10, "engagement": 20, "industry": "Retail", "days_since_contact": 15, "stage": "Discovery"},
    ]
    
    ranked_leads = score_leads(leads)
    print("--- Ranked Lead List ---")
    for l in ranked_leads:
        print(f"Lead: {l['name']} | Score: {l['score']} | Action: {l['action']}")
