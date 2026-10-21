overrall_score = int(300)
number_of_subject = int(3)
student_name = input("Enter name: ")
age = input("Enter age: ")
math_score = int (input("Enter math_score: "))
english_score = int(input("Enter english_score: "))
com_score = int(input("Enter com_score: "))
total_score = math_score + english_score + com_score
print(total_score)
average_score = total_score/number_of_subject
print(average_score)
percentage = total_score/overrall_score * 100
print(percentage)
pass_mark = 50
if pass_mark >= math_score:
    print("math: Failed")
else:
    print("math: Passed")
if pass_mark >= english_score:
    print("english: Failed")
else:
    print("english: Passed") 
if pass_mark >= com_score:
    print("computer: Passed")
else:
    print("computer: Failed")

