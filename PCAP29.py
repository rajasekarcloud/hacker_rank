try:
    f=open("non_existing_file","w")
    print(1, end=" ")
    s=f.readline()
    print(2, end=" ")
except IOError as error:
    print(3, end=" ")
else:
    f.close()
    print(4, end=" ")