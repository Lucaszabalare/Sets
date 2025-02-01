# Creating a set

cat_set = {"susie","SUSIE","susie2!"}
print(cat_set)

# Union of sets

A = {"susie1","susie2","susie3","susie4","susie5"}
B = {"susie4","susie5","susie6","susie7","susie8","susie100"}

print(A.union(B))
print(A|B)

# Intersection of sets

print(A.intersection(B))
print(A&B)

# Difference of sets

print(A.difference(B))
print(A-B)

# Symmetric difference of sets

print(A.symmetric_difference(B))
print(A^B)

# Converting a list into set

cat_list = ["susiee","susieee","susieeee"]
print(set(cat_list))

flower_set = set([])
flower_set.add("Rose")
flower_set.add("Sunflower")
flower_set.add("Tulip")
flower_set.add("Daisy")
print(flower_set)

# Removing an element using remove function

A.remove("susie1")
print(A)

# Removing an elment using discard function

B.discard("susie100")
print(B)