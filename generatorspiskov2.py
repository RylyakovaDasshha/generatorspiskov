students = [ 
    {'id': 1, 'full_name': 'Алекберов Рамиль Русланович'}, 
    {'id': 2, 'full_name': 'Бобровская Анастасия Дмитриевна'}, 
    {'id': 3, 'full_name': 'Винговатов Александр Олегович'}
]

students_with_long_names = [student['full_name'] for student in students if len(student['full_name']) > ]

print(students_with_long_names)
