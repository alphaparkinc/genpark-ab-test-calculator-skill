"""
example_usage.py -- Demonstrates ABTestCalculatorClient
"""
from client import ABTestCalculatorClient

def main():
    client = ABTestCalculatorClient()
    result = client.calculate_results(
        visitors_a=10000,
        conversions_a=150,
        visitors_b=10050,
        conversions_b=210
    )
    print("[A/B Test Significance Calculator]")
    print(f"CR A: {result['conversion_rate_a_pct']}% | CR B: {result['conversion_rate_b_pct']}%")
    print(f"Uplift: {result['relative_uplift_pct']}%")
    print(f"P-Value: {result['p_value']} | Significant: {result['is_significant']}")

if __name__ == "__main__":
    main()
