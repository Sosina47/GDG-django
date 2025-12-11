def get_expense_products(prices):
    return [price for price in prices if price > 100]

prices = [120, 45, 300, 85, 150]
print(get_expense_products(prices))