enemy_set = {"angrycat","fakecat","susie?"}
print(enemy_set)

A = {"1","2","3","4","5","1000000"}
B = {"4","5","6","7","8","9","1000000"}

print(A|B)

print(A&B)

print(B-A)

print(B^A)


enemy_list = ["notacat","notsusie","enemy"]
print(set(enemy_list))

B.remove("9")
print(B)

B.discard("1000000")
print(B)