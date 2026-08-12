frontend_students={"asha","rahul","neha"}
backend_students={"rahul","vivek","meera"}

backend_students.add("kiran")
frontend_students.remove("neha")
both_course=frontend_students.intersection(backend_students)
print("who are enrolled both course:",both_course)

backend_only=backend_students.difference(frontend_students)
print("backend course only:",backend_only)
unique_students=frontend_students.union(backend_students)
print("number of unique students:",unique_students)

courses={
    "frontend":len(frontend_students),
    "backend":len(backend_students)
}
for course, count in courses.items():
    print(f"Course: {course}, Students: {count}")
    fullstack_count = sum(courses.values())

fullstack_count = sum(courses.values())

updated_courses = courses.copy()
updated_courses["Fullstack"] = fullstack_count

print(updated_courses)