s1 = "Keep learning"
s2 = "Keep coding"
print("Motto: " + s1 + ", " + s2)

name = "Alex"
age = 18
major = "software engineering"
hobby = "Python and Java"

print("Hi, I'm " + name + ". I'm " + str(age) + ", I study " + major
      + ", and I love " + hobby + ".")
print("Hi, I'm %s. I'm %s, I study %s, and I love %s." % (name, age, major, hobby))
print(f"Hi, I'm {name}. I'm {age}, I study {major}, and I love {hobby}.")
print(f"Next year I'll be {age + 1}.")

# Output:
# Motto: Keep learning, Keep coding
# Hi, I'm Alex. I'm 18, I study software engineering, and I love Python and Java.
# Hi, I'm Alex. I'm 18, I study software engineering, and I love Python and Java.
# Hi, I'm Alex. I'm 18, I study software engineering, and I love Python and Java.
# Next year I'll be 19.
