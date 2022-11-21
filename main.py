

print(amount, from_currency, "<-----|------>", to_currency)

result = c.convert(from_currency, to_currency, amount)

print(f"{result:.2f}")

