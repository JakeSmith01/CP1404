TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print('Electricity bill estimator')
user_tariff = input('Which tariff? 11 or 31:')
daily_use = float(input('Enter daily use in kWh:'))
billing_days = int(input('Enter number of billing days:'))

if user_tariff == '11':
    billing_cost = (TARIFF_11 * daily_use) * billing_days
    print('Estimated bill: $', billing_cost)

elif user_tariff == '31':
    billing_cost = (TARIFF_31 * daily_use) * billing_days
    print('Estimated bill: $', billing_cost)

else:
    print('Invalid Tariff')
