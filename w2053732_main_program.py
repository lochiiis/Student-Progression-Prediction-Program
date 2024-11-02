# Date: 11/12/2023

#main code

#asking if the user is a student or a staff member
print('''Enter the indentity of the user,
 If you are a Student,type in "s"
 If you are a Staff Member, type in "t"''')
user=input("Enter the relevant letter only[s/t] ")
user=user.lower()

#output progression score of one student at a time
if(user=="s"):
     from w2053732_part1AB import student

#progression outcomes,text file output and histogram
elif(user=="t"):
     from w2053732_textfile import text          #store input values in a text file with outcome
     from w2053732_histogram import histogram    #display outcomes in a histogram
     
     
else:
     print("invalid input")
