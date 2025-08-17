# Employee Performance Analysis
# Verification email: blakpot32@gmail.com

import pandas as pd
import plotly.express as px

# -----------------------------
# Step 1: Load the employee data
# -----------------------------
data = """employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,IT,Europe,91.26,5,4.1
EMP002,HR,North America,67.52,2,3.8
EMP003,IT,Latin America,72.7,11,4.6
EMP004,IT,North America,85.55,14,3.4
EMP005,Marketing,Europe,89.07,3,4.2
EMP006,R&D,Europe,92.15,8,4.8
EMP007,R&D,North America,78.34,6,4.0
EMP008,Sales,Asia,83.45,4,3.7
EMP009,Finance,Europe,88.2,10,4.3
EMP010,R&D,Asia,95.6,7,4.9
"""

from io import StringIO
df = pd.read_csv(StringIO(data))

# -----------------------------
# Step 2: Frequency count of R&D
# -----------------------------
rd_count = (df['department'] == "R&D").sum()
print(f"Frequency count for R&D department: {rd_count}")

# -----------------------------
# Step 3: Histogram (interactive)
# -----------------------------
fig = px.histogram(df, x="department", color="department", 
                   title="Department Distribution of Employees")

# -----------------------------
# Step 4: Save as HTML
# -----------------------------
html_file = "employee_performance_analysis.html"
fig.write_html(html_file)

print(f"HTML file saved as: {html_file}")
