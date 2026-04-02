import matplotlib.pyplot as plt
import os

os.popen("cat sample.pcap | tshark -r - -Y udp -T fields -e udp.payload | sed 's/://g' | xxd -r -p > output.txt")

stream=""
with open("output.txt","r")as file:
    stream="".join(file.readlines())

stream=stream.replace("com","")
stream=stream.replace("microsoft","")
stream=stream.replace("google","")
stream=stream.replace("reddit","")
stream=stream.replace("python","")
stream=stream.replace("wikipedia","")
stream=stream.replace("github","")
stream=stream.replace("org","")
stream=stream.replace("example","")
stream=stream.replace("openai","")
stream=stream.replace("	","")

stream=stream[len("timestamp,x,y,left_button_holding,right_button_holding"):]
header="timestamp,x,y,left_button_holding,right_button_holding"
stream=stream.replace("17471","\n17471")
print(stream)

events=[]
for line in stream.split("\n"):
    parts=line.strip().split(",")
    if len(parts)!=5:
        continue
    try:
        ts=float(parts[0])
        x=int(parts[1])
        y=int(parts[2])
        left_button_holding = parts[3] == "True"
        right_button_holding = parts[4] == "True"
        events.append([ts,x,y,left_button_holding,right_button_holding])
    except Exception as err:
        pass
    except ValueError as err:
        pass

pts=[(x,y)for _,x,y,left,_ in events if left]

xs=[p[0]for p in pts]
ys=[p[1]for p in pts]
minx,miny=min(xs),min(ys)

xs=[x-minx for x in xs]
ys=[y-miny for y in ys]
maxx,maxy=max(xs),max(ys)

ys=[maxy-y for y in ys]

plt.figure(figsize=(10,10))
plt.scatter(xs,ys,s=2)
plt.gca().set_aspect('equal',adjustable='box')
plt.axis('off')
plt.tight_layout()
plt.savefig("mouse.png")
plt.show()

# ans: SECRET PLACE WUKONG'S DEN