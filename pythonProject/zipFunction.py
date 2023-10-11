name=("navin","kiran","harsh","navin")
comps=("dell","apple","ms")

zipped=zip(name,comps)
#zipped=list(zip(name,comps))

print(zipped)

for(a,b) in zipped:
    print(a,b)