"""
ab-test-calculator-skill: Client SDK
Computes statistical significance, Z-score, and p-value for conversion A/B tests.
"""
from __future__ import annotations
import math
from typing import Optional


class ABTestCalculatorClient:
    """
    SDK for A/B testing statistical calculations.
    """

    def calculate_results(
        self,
        visitors_a: int,
        conversions_a: int,
        visitors_b: int,
        conversions_b: int,
    ) -> dict:
        rate_a = conversions_a / max(1, visitors_a)
        rate_b = conversions_b / max(1, visitors_b)

        # Standard Error calculation
        se_a = math.sqrt(rate_a * (1 - rate_a) / max(1, visitors_a))
        se_b = math.sqrt(rate_b * (1 - rate_b) / max(1, visitors_b))

        # Z-score and p-value approximation
        se_diff = math.sqrt(se_a**2 + se_b**2)
        if se_diff == 0:
            z_score = 0.0
            p_value = 1.0
        else:
            z_score = (rate_b - rate_a) / se_diff
            # Cumulative normal distribution approximation for p-value (two-tailed)
            p_value = 2 * (1 - self._normal_cdf(abs(z_score)))

        is_significant = p_value < 0.05
        uplift = ((rate_b - rate_a) / max(0.0001, rate_a)) * 100

        return {
            "conversion_rate_a_pct": round(rate_a * 100, 2),
            "conversion_rate_b_pct": round(rate_b * 100, 2),
            "relative_uplift_pct": round(uplift, 2),
            "z_score": round(z_score, 3),
            "p_value": round(p_value, 5),
            "is_significant": is_significant,
            "confidence_level": "95%+" if is_significant else "Not Significant",
        }

    @staticmethod
    def _normal_cdf(x: float) -> float:
        # Standard approximation of normal CDF
        return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))
