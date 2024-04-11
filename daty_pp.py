from datetime import date, timedelta, datetime

today = date.today()
print(today)

tomorrow = today + timedelta(days=1)

products = [
    {'sku':1, 'exp_date':today, 'price':100},
    {'sku':2, 'exp_date':tomorrow, 'price':200},
    {'sku':3, 'exp_date':today, 'price':90.3},
    {'sku':4, 'exp_date':today, 'price':132.3345},
    ]
# for product in products:
#     print(product)
