import psutil

# get info
def infohippo():
    stuff = [] # store here
    for hippo in psutil.process_iter(attrs=['name', 'pid', 'status', 'cpu_percent', 'memory_percent']):
        stuff.append(hippo.info)
    return stuff

# Put it in hippofile.txt   
file = open('hippofile.txt', 'w')
things = infohippo()
for thing in things:
    file.write(f"Name: {thing['name']} - PID: {thing['pid']} - Status: {thing['status']} - CPU%: {thing['cpu_percent']} - Memory%: {thing['memory_percent']}\n")

file.close() # close the file
print("info dumped to hippofile.txt") # print message


