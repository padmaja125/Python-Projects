import pandas as pd
import matplotlib.pyplot as plt

# saving the credentials inside the csv file for future use
logindetails = {'username': ['admin', 'Padmaja'],'password':['admin','Padmaja']}
df = pd.DataFrame(logindetails)
df.to_csv('loginDetails.csv', index=False)

print('__Login__')

username1 = input('Enter your username :')
password1 = input('Enter your password :')

usernamelst = list(df['username'])
passwordlst = list(df['password'])

""" 
print(username1, usernamelst, username1 not in usernamelst)
print(password1 not in passwordlst)
print(password1 not in passwordlst and username1 not in usernamelst)
"""
if not (username1 in usernamelst and password1 in passwordlst):
    print('Wrong credential !!!')
else:
    print('Logged in successfully')

    studentlist = []
    # Issue1 : If at the beginning of the file is empty then it doesnot work even after applying if condition.
    #Appending part
    try:
        reading = pd.read_csv('studentsDatails.csv')
        if reading.empty:
            pass
        else:
            for i in range(len(reading)):
                data = dict(reading.iloc[i])
                studentlist.append(data)
    except:
        pass


    choice = int(input('Enter \n 1.adding name and classes in text file \n 2. Bar Graph \n 3. Histogram'))
    if choice == 1:
        noOfStudents = int(input('Enter no of students you have to add: '))
        studentdict = {}
        for i in range(noOfStudents):
            studentdict['Name'] = input('Enter name:')
            studentdict['class'] = input('Enter class: ')
            studentdict['English'] = int(input('Enter English Marks: '))
            studentdict['Maths'] = int(input('Enter Maths Marks: '))
            studentdict['Science'] = int(input('Enter Science Marks : '))
            studentdict['Hindi'] = int(input('Enter Hindi Mark: '))
            studentdict['History'] = int(input('Enter History Mark: '))
            studentdict['Total'] = studentdict['English'] + studentdict['Maths'] + studentdict['Science'] + studentdict['Hindi'] + studentdict['History']
            studentdict['percentage'] = (studentdict['Total'] // 5) *100
            if studentdict['percentage'] > 75:
                grade = 'A'
            elif studentdict['percentage'] >= 60:
                grade = 'B'
            elif studentdict['percentage'] >= 40:
                grade = 'C'
            else:
                grade = 'Fail'

            studentdict['Grades'] = grade

            studentlist.append(studentdict)

        students = pd.DataFrame(studentlist)
        students.to_csv('studentsDetails.csv', index=False)

        print(students)

    if choice ==2:
        students = pd.read_csv('studentsDetails.csv')
        x = list(students['Total'])
        bins = len(set(x))
        plt.hist(x, bins = bins)
        plt.show()

    if choice == 3:
        students = pd.read_csv('studentsDatails.csv')
        gradecount = students['grades'].value_counts()
        plt.bar(gradecount.index, gradecount)
        plt.show()

    if choice == 4:
        exit()
