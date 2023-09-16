import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merge_data = employee.merge(employee, left_on='managerId', right_on='id', how='left', indicator=True)
    return (pd.DataFrame({'Employee': merge_data['name_x'][merge_data['salary_x'] > merge_data['salary_y']]}))