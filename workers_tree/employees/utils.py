from workers_tree.employees.models import Employee


def build_tree(heads):
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

    tree = []
    for head in heads:
        node = {'name': head.name(),
                'job_title': head.job_title,
                'employment_date': head.employment_date,
                'salary': head.salary,
                'employees': get_workers(head)}
        tree.append(node)
    return tree


def build_js_tree():
    def get_workers(head, tree):
        query = Employee.objects.filter(manager=head)
        if not query:
            return
        for employee in query:
            node = {'id': employee.user.get_full_name(),
                    'parent': head.user.get_full_name(),
                    'text': employee.user.get_full_name()}
            get_workers(employee, tree)
            tree.append(node)

    heads = Employee.objects.filter(manager__isnull=True)
    tree = []
    for head in heads:
        node = {'id': head.user.get_full_name(),
                'parent': '#',
                'text': head.user.get_full_name()}
        tree.append(node)
        get_workers(head, tree)
    return tree
