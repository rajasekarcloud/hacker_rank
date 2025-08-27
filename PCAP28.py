try:
    f = open("PCAP24.py","rt")
    spam = f.readlines()
    print(len(spam))
    f.close()
except IOError:
    print(-1)
