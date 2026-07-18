employees = [
    {
        "name": "Alice Johnson",
        "department": "Engineering",
        "salary": 85000,
        "active": True,
    },
    {"name": "Bob Smith", "department": "Sales", "salary": 62000, "active": True},
    {
        "name": "Carol White",
        "department": "engineering",
        "salary": 91000,
        "active": True,
    },  # lowercase 'engineering' - tests case sensitivity
    {
        "name": "David Brown",
        "department": "Engineering",
        "salary": 78000,
        "active": False,
    },
    {
        "name": "Eve Davis",
        "salary": 55000,
        "active": True,
    },  # missing 'department' key entirely
    {"name": "Frank Miller", "department": "HR", "salary": 60000, "active": True},
    {
        "name": "Grace Lee",
        "department": "Engineering",
        "salary": 102000,
        "active": True,
    },
    {
        "name": "Henry Wilson",
        "department": "Marketing",
        "salary": 67000,
        "active": False,
    },
]


def get_employees_by_department(employees, department):
    return [emp for emp in employees if emp.get("department") == department]


print(get_employees_by_department(employees, "Engineering"))
