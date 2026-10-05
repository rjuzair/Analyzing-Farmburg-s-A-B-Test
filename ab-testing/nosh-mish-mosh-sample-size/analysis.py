import noshmishmosh
import numpy as np

all_visitors = noshmishmosh.customer_visits
#print(all_visitors)

paying_customers = noshmishmosh.purchasing_customers
#print(paying_customers)

total_visitors_count = len(all_visitors)
paying_visitor_count = len(paying_customers)

baseline_percent = (paying_visitor_count / total_visitors_count) * 100
print('Baseline Conversion rate: ' +str(baseline_percent) + '%')

#9
payment_history = noshmishmosh.money_spent
average_payment = np.mean(payment_history)
print(average_payment)
new_customer_needed = np.ceil(1240/average_payment)
print(new_customer_needed)

percentage_point_increase = new_customer_needed / total_visitors_count * 100
print(percentage_point_increase)

mde = percentage_point_increase / baseline_percent * 100
print(mde)
