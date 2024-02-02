#set

untensils = {"fork", "spoon", "knife"}
dishes = {"bowl","plate","cup","knife"}

untensils.add("napkin")
untensils.remove("fork")
#untensils.update(dishes)
dinner_table = untensils.union(dishes)

print(untensils.difference(dishes))
print(untensils.intersection(dishes))

for x in untensils:
    print(x)

for x in dinner_table:
    print(x)
