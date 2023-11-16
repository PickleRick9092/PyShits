# به اين روش ميگن استفاده از متغير موقت يا متغير سوم براي جابجايي
def swap1(a,b):
    temp = a
    a = b
    b = temp
    print(a,b)
#روش بعدي جابجايي با عملگر کاما يا همون ", هست"    
def swap2(a,b):
    a,b = b,a
    print(a,b)
#روش سوم استفاده از عملگرهاي اصلي رياضي يني + * / - هست   
def swap3(a,b):
    a = a+b
    b = a-b
    a = a-b
    print(a,b)

def swap4(a,b):
    a = a*b
    b = a/b
    a = a/b
    print(a,b)

a = int(input("يه عدد بده سگ "))
b = int(input("عدد بعدي، بجنب آشغال"))

swap1(a,b)
swap2(a,b)
swap3(a,b)
swap4(a,b)

# زيبا بود 










