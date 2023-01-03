import time

s = time.localtime()[5]
m = time.localtime()[4]
h = time.localtime()[3]
d = time.localtime()[2]
y = time.localtime()[0]
s1 = 60 - s
m1 = 59 - m
h1 = 23 - h
y1 = y % 4
y2 = y + 1
d0 = 365 - d
d1 = 364 - d

if y1 == 0:
    print("还有",d0,"天",h1,"h",m1,"m",s1,"s","就是",y2,"年了",)
else:
    print("还有",d1,"天",h1,"h",m1,"m",s1,"s","就是",y2,"年了",)
