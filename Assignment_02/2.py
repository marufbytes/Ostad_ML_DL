def set_operations(set1=set(), set2=set()):
    union_set = set1.union(set2)
    intersection_set = set1.intersection(set2)
    difference_set = set1.difference(set2)

    return union_set, intersection_set, difference_set


s1 = set(map(int, input("Enter elements of Set 1: ").split()))
s2_input = input("Enter elements of Set 2 (or press Enter to skip): ")

if s2_input:
    s2 = set(map(int, s2_input.split()))
    union_set, intersection_set, difference_set = set_operations(set1=s1, set2=s2)
else:
    union_set, intersection_set, difference_set = set_operations(set1=s1)

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (Set1 - Set2):", difference_set)