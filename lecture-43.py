#map function
#map(function, iterable)

store = [
    ('shirt', 20.00),
    ('pants', 30.00),
    ('shoe', 40.00),
    ('sock', 50.00)
]
#function to convert dollars to euros
to_euros = lambda data: (data[0], data[1] * 0.82)
#function to convert euros to dollars
to_dolars = lambda data: (data[0], data[1] / 0.82)

store_euros = list(map(to_euros, store))
store_dolars = list(map(to_dolars, store_euros))

for i in store_euros:
    print(i)
for i in store_dolars:
    print(i)