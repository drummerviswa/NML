data = []
for i in range(5):
    f, to, timestamp, d1, d2 = list(map(str,input().split()))
    timestamp=int(timestamp)
    d1=float(d1)
    d2=float(d2)
    data.append([f,to,timestamp,d1,d2])

print(data)