import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# Load the dataset
df = pd.read_csv(r"C:\Users\prane\Downloads\hw_200.csv")
df.columns = ['Index', 'Height(Inches)', 'Weight(Pounds)']

# Basic statistics
height_mean = df['Height(Inches)'].mean()
weight_mean = df['Weight(Pounds)'].mean()
height_min = df['Height(Inches)'].min()
height_max = df['Height(Inches)'].max()
weight_min = df['Weight(Pounds)'].min()
weight_max = df['Weight(Pounds)'].max()

# Create a scatter plot
plt.figure(figsize=(6, 4))
plt.scatter(df['Height(Inches)'], df['Weight(Pounds)'], alpha=0.7)
plt.title("Height vs Weight")
plt.xlabel("Height (inches)")
plt.ylabel("Weight (pounds)")
plt.grid(True)
plt.tight_layout()

# Save the chart
chart_path = "height_weight_chart.png"
plt.savefig(chart_path)
plt.close()

# Create PDF report
pdf = FPDF()
pdf.add_page()

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Automated Report: Height and Weight Analysis", ln=True, align="C")

# Add stats
pdf.set_font("Arial", '', 12)
pdf.ln(10)
pdf.cell(0, 10, f"Number of Records: {len(df)}", ln=True)
pdf.cell(0, 10, f"Average Height: {height_mean:.2f} inches", ln=True)
pdf.cell(0, 10, f"Min Height: {height_min:.2f} inches, Max Height: {height_max:.2f} inches", ln=True)
pdf.cell(0, 10, f"Average Weight: {weight_mean:.2f} pounds", ln=True)
pdf.cell(0, 10, f"Min Weight: {weight_min:.2f} pounds, Max Weight: {weight_max:.2f} pounds", ln=True)

# Add chart
pdf.ln(10)
pdf.cell(0, 10, "Scatter Plot: Height vs Weight", ln=True)
pdf.image(chart_path, x=30, w=150)

# Save the PDF
report_path = "height_weight_report.pdf"
pdf.output(report_path)
print(f"Report saved as {report_path}")
