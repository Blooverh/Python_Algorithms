from copy import deepcopy

a= [1,2,3,4] #[1,2,3,4]
b= deepcopy(a) # [1,2,3,4]

c=[10,20,30]

print(a)
print(b)
print(c)

b=deepcopy(a) + c # [1,2,3,4,10,20,30]

print(b)