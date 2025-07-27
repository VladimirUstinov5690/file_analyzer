from tabulate import tabulate


def pretty_print(data, headers=None):
    """Function for beautiful output of tables"""
    return tabulate(data, headers=headers,
                    tablefmt='grid')
