# string slicing
# indexing[] or slice()
# [start:stop:step]

name = "Petr Kroutil"
first_name = name[:4]
last_name = name[5:]
first_name_funky = name[::2]
reversed_name = name[::-1]

print(first_name, last_name, first_name_funky)
print(reversed_name)

website1 = "https://google.com"
website2 = "https://seznam.com"
sliced_website = slice(8,-4)
print(website1[sliced_website])
print(website2[sliced_website])
