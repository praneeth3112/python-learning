student_name = str(input('enter the name of the student : '))
usn_no = str(input('enter the usn of the student : '))
branch = str(input('enter the branch of the student : '))
semester = int(input('enter ur current semester(1 - 8) : '))
if 1<=semester<=8 :
    print(f'current semester : {semester}')
else :
    print('invalid')
subject1 = float(input('enter ur marks in subject1(0-100)'))
subject2 = float(input('enter ur marks in subject2(0-100)'))
subject3 = float(input('enter ur marks in subject3(0-100)'))
total_marks = subject1 + subject2 + subject3
average = total_marks/3
print(f'name of the student is {student_name}')
print(f'usn of the student is {usn_no}')
print(f'branch of the student is {branch}')
print(f'current semester of the student is {semester}')
print(f'average marks of the student in 3 subjects is {average}')
print('testing github push')

 
