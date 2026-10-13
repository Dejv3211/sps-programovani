nakup = ["ovoce", "zelenina", "kočka"]
nakup.remove("zelenina")
srovnanejlist = sorted(nakup)
print(srovnanejlist)
for i in range(srovnanejlist):
    print i
print(len(srovnanejlist))