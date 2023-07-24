# We wrote a print statement to let us know that the program has entered the loop. However, the program is looping
# endlessly, fix it before it crashes our computer! Tasks (1): In the while loop, change the value of the loop
# variable such that "Entered the loop!" is printed only once.

loop = True
while loop:
    print("Entered the loop!")
    loop = False
