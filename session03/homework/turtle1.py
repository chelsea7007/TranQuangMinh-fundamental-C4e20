from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
s = 7

for i in range(s):
    if s == 7:
        color(colors[-1])
    elif s == 6:
        color(colors[-2])
    elif s == 5:
        color(colors[-3])
    elif s == 4:
        color(colors[-4])
    else:
        color(colors[-5])
    for l in range(s):
        forward(100)
        left(360/s)
    s = s - 1

mainloop()