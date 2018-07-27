fs = [5, 7, 300, 90, 24, 50, 75]
print ("Hello my name is Mam and here are my sheep's sizes")
print (fs) #2.1

#2.2
print ("Now my biggest sheep has size", max(fs), "let's shear it")

#2.3
print("After shearing, here is my flock")
fs [fs.index(max(fs))] = 8
print(fs)

#2.4 & 2.5
print("MONTH 1:")
print("One month has passed, now here is my flock")
newfs = [x+50 for x in fs]
print(newfs)
print ("Now my biggest sheep has size", max(newfs), "let's shear it")
print("After shearing, here is my flock")
newfs [newfs.index(max(newfs))] = 8
print(newfs)

print("MONTH 2:")
print("One month has passed, now here is my flock")
newfs1 = [x+50 for x in newfs]
print(newfs1)
print ("Now my biggest sheep has size", max(newfs1), "let's shear it")
print("After shearing, here is my flock")
newfs1 [newfs1.index(max(newfs1))] = 8
print(newfs1)

print("MONTH 3:")
print("One month has passed, now here is my flock")
newfs2 = [x+50 for x in newfs1]
print(newfs2)

#2.6
print("My flock's size in total:", sum(newfs2))
print("I would get", sum(newfs2), "* 2$ =", sum(newfs2) * 2,"$")