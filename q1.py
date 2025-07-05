div = []
for x in range(1000):
    if x % 3 == 0 or x % 5 == 0 :
      div.append(x)
#print(div) 
k=0   
for i in div:
   k = k + i
print(k)