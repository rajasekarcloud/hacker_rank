'''
Given the names and grades for each student in a class of  students, store them in a nested list
print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade,
order their names alphabetically and print each name on a new line.
python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
The lowest grade of 37.2 belongs to Tina
The second lowest grade of 37.21 belongs to both Harry and Berry,
so we order their names alphabetically and print each name on a new line.
'''
if __name__ == '__main__':
    record = []
    record_temp = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record_temp.append(name)
        record_temp.append(score)
        record.append(record_temp)
        record_temp = []
#print(sorted(record))# This sorts by first element
second_lowest = sorted(record, key=lambda x: x[1],reverse=False) # Sort by second element in the list
#print(second_lowest[1])
second_lowest_score = second_lowest[1][1]
#print(second_lowest_score)
same_score = []
for x in second_lowest:
    if x[1] == second_lowest_score:
        same_score.append(x[0])
for x in sorted(same_score):
    print(x)