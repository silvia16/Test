


#simplified and faster method to
#calculate the fibonacci sequence

a = 0
b = 1
count = 0
max_count = 10

while count < max_count:
    count = count +1
    print (a, b, end=" ") #notice the magic end=" "
    a = a+b
    b = a+b
print () #gets a new (empty) line 
