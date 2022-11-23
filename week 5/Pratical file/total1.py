import sys

count = len(sys.argv)
total = 0
argu=[]
a=sys.argv[1:]
if (a==argu):
    print("No argument is passed ")
else:
    while count > 1:
        count -= 1
        total += float(sys.argv[count])
    average=total/len(sys.argv[1:])
    print("Total is", total)
    print("The average of nuber is",average)
