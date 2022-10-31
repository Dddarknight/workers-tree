from workers_tree.employees.models import Employee


def build_tree():
    def get_workers(head):
        employees = []
        query = Employee.objects.filter(manager=head)
        if not query:
            return employees
        for employee in query:
            node = {'name': employee.name(),
                    'job_title': employee.job_title,
                    'employment_date': employee.employment_date,
                    'salary': employee.salary,
                    'employees': get_workers(employee)}
            employees.append(node)
        return employees

    heads = Employee.objects.filter(manager__isnull=True)
    tree = []
    for head in heads:
        node = {'name': head.name,
                'job_title': head.job_title,
                'employment_date': head.employment_date,
                'salary': head.salary,
                'employees': get_workers(head)}
        tree.append(node)
    return tree
