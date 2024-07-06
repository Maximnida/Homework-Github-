def find_top_department(employee_data):
    department_performance = {}

    for line in employee_data:
        parts = line.split()
        bonus = int(parts[3])
        department = parts[4]

        if bonus > 0:
            if department in department_performance:
                department_performance[department] += 1
            else:
                department_performance[department] = 1

    max_performance = max(department_performance.values())
    top_departments = [dept for dept, perf in department_performance.items() if perf == max_performance]
    print("Top departments:")
    print(", ".join(top_departments))

employee_data = [
    "Anvar Junior 500 100 1-bolim",
    "Asror Middle 1500 500 2-bolim",
    "Kamola Senior 2500 -100 3-bo'lim",
    "Vali Junior 500 -100 1-bo'lim",
    "Davron Middle 1500 100 2-bo'lim",
    "Bahodir Senior 2500 -100 3-bolim",
    "Farrux Junior 500 100 1-bo'lim",
    "Jamila Middle 1500 200 2-bolim",
    "Jasur Senior 2500 500 3-bolim",
    "Komila Junior 500 -100 1-bo'lim"
]

find_top_department(employee_data)