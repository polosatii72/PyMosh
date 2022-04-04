from dataclasses import field


course_name = "Programming python"

naming = """
some text
and more
"""

print(len(course_name))
# access to element via []
print(course_name[0])
print(course_name[-1])
print(course_name[0:3])
print(course_name[0:])
print(course_name[:3])
print(course_name[:])

print("*******************************")
# escape sequences
# \'    \""     \\      \n
course_name = "Programming \"python"
print(course_name)

print("*******************************")
# formatted strings
first = "Mosh"
last = "Hamedini"
full = f"{first} {last}"
full = f"{len(first)} {2 + 1}"
print(full)

print("*******************************")
# str methods
course_name = "Programming python"
print(course_name.upper())
print(course_name.lower())
print(course_name.title())
# trim whitespaces
course_name_space = "   Programming python"
print(course_name.strip())  # rstrip lstrip
# find
print(course_name.find("python"))  # -1 if not found
# replace
print(course_name.replace("p", "j"))
# if exist character
print("Pro" in course_name)
print("Swift" not in course_name)
