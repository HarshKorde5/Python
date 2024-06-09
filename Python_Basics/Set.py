# Set datatype

# Heterogeneous
# UnOrdered
# UnIndexed
# Mutable
# Duplicate not allowed

Arr = {11,18.90,True,"JaiGanesh",11}        
#any one 11 will be shown in display means duplicate is discarded no error given

print(Arr)
print(len(Arr))
#print(Arr[0])

Arr.add("Python")

print(Arr)

Arr.remove("Python")            #Arr.discard("Python")

print(Arr)