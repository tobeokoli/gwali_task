import json
final_result = []
list_of_courses = []
with open('raw_strings.txt') as f:
    lines = f.readlines()
for line in lines:
    course = line.split()
    list_of_courses.append(course)
print(course)
for course in list_of_courses:
    course.pop()
    dept_prefix = course[0]
    course_number = course[1]
    course_title = " ".join(course[2:]).upper()
    course_data = {'dept_prefix': dept_prefix, 'course_number': course_number, 'course_title': course_title}
    final_result.append(course_data)
print(json.dumps(final_result))