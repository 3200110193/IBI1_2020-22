a=060702
b=190784
c=100321
d=abs(a-c)
e=abs(a-b)
if d<e:
    print("d<e")
elif d>e:
    print("d>e")
else:
    print("d=e")
x=True
y=False
z=(x and not y)or(y and not x)
print(z)
w=(x!=y)
print(w)
print(z==w)
