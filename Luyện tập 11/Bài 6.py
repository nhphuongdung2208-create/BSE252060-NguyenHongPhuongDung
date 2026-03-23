n = int(input("Nhập số lượng người:"))
people = {}
for _ in range(n):
    name = input("Tên: ")
    age = int(input("tuổi: "))
    people[name] = age

avg_age = sum(people.values()) / len(people)
print("tuổi trung bình:", avg_age)

items = list(people.items())
for i in range(len(items)):
    max_idx = i
    for j in range(i+1, len(items)):
        max_idx = i
        for j in range(i+1, len(items)):
            if items[j][1] > items[max_idx][1]:
                max_idx = j
        items[i], items[max_idx] = items[max_idx], items[i]
print("Tuổi giảm dần:", dict(items))



