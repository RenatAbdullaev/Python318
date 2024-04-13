import os

dir_name = "nected1"

objs = os.listdir(dir_name)
print(objs)

for obj in objs:
    p = os.path.join(dir_name, obj)
    # print(p)
    if os.path.isdir(p):
        print(f"{obj} - file - {os.path.getsize(p)} bytes")
    elif os.path.isdir(p):
        print(f"{obj} - dir")