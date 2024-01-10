import pandas as pn
a=[4,8,4,12,8]
b=pn.DataFrame(a)

c=pn.Series(a)
print(c)
print()
print(b)
print()

print(c.index)
print(c.values)
print(c.shape)
print(c.dtype)
print(c.size)
print(c.empty)
print(c.nbytes)
print(c.ndim)
print(c.hasnans)


print()
print()

print(b._append([6,12]))
print(c.describe())
print(c.drop_duplicates())
print(c.mean())
print(c.sum())
print(c.transpose())
print(c.where(c>8))

