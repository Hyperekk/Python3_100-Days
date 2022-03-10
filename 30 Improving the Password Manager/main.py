try:
    f = open("something.txt")
except FileNotFoundError:
    f = open("something.txt","w")
    f.write("Something")