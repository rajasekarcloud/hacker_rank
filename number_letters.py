# Enter a strings with digit and alpha
# Output should be missing digit and alpha in sorted strings
# input = car12345bike
# ouput = 67890<missing characters from a t z except car and bike>

import string;
num = range(0,10);
num = list(map(str, num));
alpha = list(string.ascii_lowercase);
input='8hypotheticall024y6wxz';
alpha_num = num + alpha;
# Difference between two list should give the missing numbers
c = list(set(alpha_num) - set(sorted(input)));
result='';
for i in sorted(c):
    result = result + i;
print(result);