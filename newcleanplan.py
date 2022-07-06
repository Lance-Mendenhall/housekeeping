import datetime


class Clean:
    def __init__(self, area, freq, offset):
        self.area = area
        self.freq = int(freq)
        self.offset = int(offset)


thislist = []
f = open("areastoclean.txt", "r")
for x in f:
    if(x.strip(' \n') != ""):
        # print(x,"   zzz")
        q = x.split("\t")
        mm = Clean(q[0], q[1], q[2])
        thislist.append(mm)

print("\n\t\t starting...\n")

x = datetime.datetime(2021, 5, 21)
y = datetime.datetime.now()
diff = (y - x).days

dc = 0  # day counter

while dc < 7:
    z = diff + dc
    x = y + datetime.timedelta(days=(dc))
    print("\t\t", x.strftime("%a"), x.strftime("%b"), x.strftime("%d"))
    for b in thislist:
        if (z + b.offset) % b.freq == 0:
            print("\t\t", b.area)
    print("")
    dc += 1

print("\n\t\t ...ending\n")
