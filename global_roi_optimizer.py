"""
Global ROI Intelligence Optimizer
Pillar: Holistic Asset Management (Financial + Knowledge + Equity)
Architect: Irem Victor Chinonso
"""

class ROIOptimizer:
    def __init__(self):
        # Weighting factors for different types of "Capital"
        self.weights = {
            "cash_flow": 0.3,      # Immediate liquidity (C-Way Depot)
            "equity_growth": 0.4,  # Long-term asset building (Street Code Studios)
            "knowledge_equity": 0.3 # Foundational skill-up (OAU Statistics)
        }

    def calculate_daily_performance(self, hours_cway, units_sold, scripts_produced, study_hours):
        """
        Calculates a 'Success Index' based on daily allocation.
        """
        # 1. Cash Flow Score (Normalized against a high-performance day)
        cash_score = (units_sold / 250) * 100 
        
        # 2. Equity Score (Scripts produced vs Goal of 8)
        equity_score = (scripts_produced / 8) * 100
        
        # 3. Knowledge Score (Study hours vs Target of 4)
        knowledge_score = (study_hours / 4) * 100
        
        # Weighted Global Index
        global_index = (
            (cash_score * self.weights["cash_flow"]) +
            (equity_score * self.weights["equity_growth"]) +
            (knowledge_score * self.weights["knowledge_equity"])
        )
        
        return {
            "Global Intelligence Index": round(global_index, 2),
            "Cash Flow Velocity": f"{round(cash_score, 1)}%",
            "Asset Building Speed": f"{round(equity_score, 1)}%",
            "Knowledge Compounding": f"{round(knowledge_score, 1)}%"
        }

if __name__ == "__main__":
    optimizer = ROIOptimizer()
    
    # Simulation: A day of high-level architectural execution
    perf = optimizer.calculate_daily_performance(
        hours_cway=8, 
        units_sold=210, 
        scripts_produced=6, 
        study_hours=3
    )
    
    for key, value in perf.items():
        print(f"{key}: {value}")
    
    print("\nStatus: Global ROI Intelligence Synchronized.")
