# Pandas Basics: Building a DataFrame, Grouping Data, and Comparing Series vs DataFrame Output

import pandas as pd

print("--- Starting Terminal Data Script ---")

# 1. Create a raw dictionary of employee data
raw_data = {
    "Employee": ["Alice", "Bob", "Charlie", "David"],
    "Department": ["HR", "IT", "IT", "HR"],
    "Salary":[50000, 75000, 100000, 75000]
}

# 2. Call the library to convert the dictionary into a DataFrame (a table)
df = pd.DataFrame(raw_data)

# 3. Call the library to calculate the average salary per department
# This is a specific data task that pandas handles for us
average_salaries = df.groupby("Department")["Salary"].mean()

# 4. Print the final results directly to the terminal
print("\nFull Employee Table")
# DataFrame with default index -> already clean, no metadata shown
print(df)

print("\nCalculated Average Salary by Department")
# Series with 'Department' as index -> shows Name/dtype metadata
print(average_salaries)
# converts Series back to a clean 2-column DataFrame
print(average_salaries.reset_index())

print("\n--- Script Finished ---")
