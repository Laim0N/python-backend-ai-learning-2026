from age_check import is_adult
print("Hello, World!")

print("What is your name?")
name = input().strip().capitalize()
if name == "" or name.isdigit():
    print("Error: Invalid name")
    exit()
print("Hello", name)

print("How old are you?")
age = int(input())
if is_adult(age):
    print("You are an adult")
else:
    print("You are not an adult")
