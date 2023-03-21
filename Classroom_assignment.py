from collections import defaultdict

students, room_max = map(int,input().split())

male = defaultdict(int)
female = defaultdict(int)

for student in range(students):
    gender, grade = map(int,input().split())
    if gender :
        male[grade] += 1
    else :
        female[grade] += 1
        
room = 0
for grade in range(1, 7):
    
    w, m = female[grade], male[grade]
    
    
    room += w//room_max + m//room_max
    if w%room_max :
        room += 1
    if m%room_max :
        room += 1
    
print(room)


