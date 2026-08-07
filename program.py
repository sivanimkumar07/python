program="""python 
is a
simple 
program."""

print(len(program))
print("First character:", program[0])
print("Last character:", program[-1])

print("Preview:", program[:50])

updated_program = program.replace("Python", "PYTHON")
print("\nParagraph after replacement:")
print(updated_program)

lowercase_program = program.lower()
print("\nParagraph in lowercase:")
print(lowercase_program)

words = program.split()
print("\nList of words:")
print(words)

if "course" in program.lower():
    print("\nThe word 'course' was found in the paragraph.")

    print("\nThe course description is {} characters long and has {} words.".format(
        len(program), len(words)))
