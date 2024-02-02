#dictionary

capitals = {"USA":"Washington DC", "Czech Republic":"Prague", "Germany":"Berlin","India":"New Dehli"}

print(capitals["Germany"]) #Berlin simple
print(capitals.get("Germany")) #this is safer than above
print(capitals.keys())
print(capitals.values())
print(capitals.items())

capitals.update({"Russia":"Moscow"})
capitals.update({"USA":"nothing"})

for key, value in capitals.items():
    print(key, value)
