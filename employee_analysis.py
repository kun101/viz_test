# Employee Performance Analysis
# Verification email: blakpot32@gmail.com

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import StringIO
import base64

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

df = pd.read_csv(StringIO(data))

# -----------------------------
# Step 2: Frequency count of R&D
# -----------------------------
rd_count = (df['department'] == "R&D").sum()
print(f"Frequency count for R&D department: {rd_count}")

# -----------------------------
# Step 3: Histogram with Seaborn
# -----------------------------
plt.figure(figsize=(8,6))
sns.countplot(data=df, x="department", color="skyblue", edgecolor="black")
plt.title("Department Distribution of Employees")
plt.xlabel("Department")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart as PNG
png_file = "department_distribution.png"
plt.savefig(png_file)

# Encode PNG as Base64
with open(png_file, "rb") as img_f:
    encoded = base64.b64encode(img_f.read()).decode("utf-8")

# -----------------------------
# Step 4: Save HTML (embed PNG + email + Python code)
# -----------------------------
html_file = "employee_performance_analysis.html"

# Write HTML with embedded image + email
with open(html_file, "w", encoding="utf-8") as f:
    f.write("<html><head><title>Employee Performance Analysis</title></head><body>")
    f.write("<h2>Department Distribution of Employees</h2>")
    f.write(f"<img src='data:image/png;base64,{encoded}'/>")
    f.write(f"<p style='text-align:center;font-size:14px;color:gray;'>Verification Email: blakpot32@gmail.com</p>")

    # Embed Python code itself
    with open(__file__, "r", encoding="utf-8") as code_f:
        python_code = code_f.read()
    f.write("<h3>Embedded Python Code:</h3><pre><code>")
    f.write(python_code)
    f.write("</code></pre></body></html>")

print(f"HTML file saved as: {html_file}")
