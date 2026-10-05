"""Nosh Mish Mosh - sample size planning for an A/B test.

Before testing new artisanal product photography, estimate the baseline
conversion rate, the minimum detectable effect (MDE) needed to earn an
extra $1,240/week, and the sample size required to detect it.

Data: the course exposes three lists via a `noshmishmosh` module -
customer_visits, purchasing_customers and money_spent.
"""
import numpy as np
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

import noshmishmosh

REVENUE_TARGET = 1240   # extra weekly revenue needed to justify the new supplier
ALPHA = 0.10            # significance threshold (low-stakes decision)
POWER = 0.80


def main():
    all_visitors = noshmishmosh.customer_visits
    paying_visitors = noshmishmosh.purchasing_customers
    payment_history = noshmishmosh.money_spent

    total_visitor_count = len(all_visitors)
    paying_visitor_count = len(paying_visitors)

    baseline_percent = paying_visitor_count / total_visitor_count * 100
    print(f"Baseline conversion rate: {baseline_percent:.2f}%")

    average_payment = np.mean(payment_history)
    new_customers_needed = np.ceil(REVENUE_TARGET / average_payment)
    print(f"Average order value: ${average_payment:.2f}")
    print(f"Extra customers needed per week: {new_customers_needed:.0f}")

    percentage_point_increase = new_customers_needed / total_visitor_count * 100
    mde = percentage_point_increase / baseline_percent * 100
    print(f"Required lift: +{percentage_point_increase:.2f} pp  (MDE = {mde:.1f}% relative)")

    # Sample size per variant for a two-sided two-proportion z-test
    p1 = baseline_percent / 100
    p2 = p1 + percentage_point_increase / 100
    effect = proportion_effectsize(p2, p1)
    ab_sample_size = np.ceil(NormalIndPower().solve_power(effect, alpha=ALPHA, power=POWER))
    print(f"Sample size per variant (alpha={ALPHA}, power={POWER}): {ab_sample_size:.0f}")


if __name__ == "__main__":
    main()
