"""
Pipeline Health Monitor
Logic for HubSpot RevOps Architecture

This script defines a sales pipeline, calculates conversion rates between stages,
flags bottlenecks, and outputs a health report.
"""

def calculate_pipeline_health(pipeline_data, threshold=0.2):
    """
    Analyzes the health of a sales pipeline.
    
    Args:
        pipeline_data (dict): Dictionary with stage names as keys and deal counts as values.
        threshold (float): Conversion rate threshold to flag bottlenecks.
        
    Returns:
        dict: Report containing conversion rates, bottlenecks, and total volume.
    """
    stages = [
        "Lead",
        "Qualified",
        "Proposal",
        "Negotiation",
        "Closed Won",
        "Closed Lost"
    ]
    
    report = {
        "conversion_rates": {},
        "bottlenecks": [],
        "total_deals": sum(pipeline_data.values()),
        "status": "Healthy"
    }
    
    # Iterate through stages to calculate step-by-step conversion
    for i in range(len(stages) - 2):  # Stop before Closed Won/Lost
        current_stage = stages[i]
        next_stage = stages[i+1]
        
        current_count = pipeline_data.get(current_stage, 0)
        next_count = pipeline_data.get(next_stage, 0)
        
        if current_count > 0:
            rate = next_count / current_count
        else:
            rate = 0.0
            
        report["conversion_rates"][f"{current_stage} -> {next_stage}"] = rate
        
        if rate < threshold and current_count > 0:
            report["bottlenecks"].append({
                "from": current_stage,
                "to": next_stage,
                "rate": rate,
                "reason": f"Conversion rate {rate:.1%} is below threshold {threshold:.1%}"
            })
            report["status"] = "At Risk"
            
    return report

def print_health_report(report):
    """Prints a formatted pipeline health report."""
    print("="*40)
    print("SALES PIPELINE HEALTH REPORT")
    print("="*40)
    print(f"Total Deals in Pipeline: {report['total_deals']}")
    print(f"Overall Status: {report['status']}")
    print("-" * 40)
    print("Conversion Rates:")
    for transition, rate in report["conversion_rates"].items():
        print(f"  {transition:25}: {rate:.1%}")
    
    if report["bottlenecks"]:
        print("-" * 40)
        print("BOTTLENECKS DETECTED:")
        for b in report["bottlenecks"]:
            print(f"  [!] {b['from']} -> {b['to']}: {b['rate']:.1%} (Threshold: {b['reason'].split(' ')[-1]})")
    else:
        print("-" * 40)
        print("No significant bottlenecks detected.")
    print("="*40)

if __name__ == "__main__":
    # Sample HubSpot-style Deal Data
    sample_data = {
        "Lead": 100,
        "Qualified": 80,
        "Proposal": 30,  # Large drop here
        "Negotiation": 25,
        "Closed Won": 15,
        "Closed Lost": 10
    }
    
    report = calculate_pipeline_health(sample_data)
    print_health_report(report)
