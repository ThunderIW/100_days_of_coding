sum_of_student_heights=0
number_of_students=0
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


for height in student_heights:
    sum_of_student_heights+=height
    number_of_students += 1


avg_height=round(sum_of_student_heights/number_of_students)
print(f"total height = {sum_of_student_heights}\n"
      f"number of students = {number_of_students}\n"
      f"average height = {avg_height}")



