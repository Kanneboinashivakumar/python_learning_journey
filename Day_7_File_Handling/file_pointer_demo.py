with open("sample.txt","w") as f:
    f.write("This is Shiva")
with open("sample.txt","r") as f:
    txt = f.read(5)
    print("READ:",txt)
    print("current position:",f.tell())
    f.seek(0)
    print(f"after seek :{f.read()}")