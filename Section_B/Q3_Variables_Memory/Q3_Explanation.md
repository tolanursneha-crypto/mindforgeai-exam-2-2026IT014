# Explanation
* a = 25 creates an integer object with value 25.
* b = a makes b refer to the same object as a.
* c = 25 also refers to the same integer object (Python usually reuses small integers).
* names is a list object.
* same_names = names makes both variables refer to the same list.
* same_names.append("Neha") modifies the original list, so both variables show the updated list.

# Final Output
a = 25
b = 25
c = 25

names = ["Asha", "Riya", "Neha"]
same_names = ["Asha", "Riya", "Neha"]