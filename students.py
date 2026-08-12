python={"asha","rahul","vivek"}
data_science={"asha","meera","rohan"}

python .add("kiran")
data_science.remove("rohan")
print(python & data_science)
print(python ^ data_science)

all_students=python.intersection(data_science)
print("common students:",all_students)

python_course=python.difference(data_science)
print("python course only:",python_course)

both_students=python.union(data_science)
print("both students:",both_students)

courses={
    "python":len(python),
    "data_science":len(data_science)
}
for course, count in courses.items():
    print(f"Course: {course}, Students: {count}")
expected_growth = {course: count * 2 for course, count in courses.items()}

print("Expected Growth:", expected_growth)