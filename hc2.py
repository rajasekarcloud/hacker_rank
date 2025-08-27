'''Sample inpute
AABCAAADA   s = 'AABCAAADA'
3           k = 3
There are three substrings of length  to consider: 'AAA', 'BCA' and 'DDE'.
If there are duplicate characters remove and sort them alphabetically
'''
def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        #print(string[i:i + k])
        print(''.join(set(string[i:i + k])))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

