"""
AI JOB MARKET - COMPLETE DATA ANALYSIS PROJECT
================================================
Goal: Reproduce and extend the insights shown in the Power BI "AI Job Trend"
dashboard using Python, following a standard analytics workflow:

1. Import libraries & load data
2. Data understanding (shape, types, nulls, duplicates)
3. Data cleaning / preparation
4. Univariate analysis (distributions of key columns)
5. KPI cards (single-number metrics, same as dashboard top cards)
6. Bivariate / grouped analysis (the charts in the dashboard)
7. Correlation analysis
8. Outlier check
9. Final insights summary
"""

# ---------------------------------------------------------------
# STEP 1: IMPORT LIBRARIES & LOAD DATA
# ---------------------------------------------------------------
import pandas as pd                 # data handling
import numpy as np                  # numeric operations
import matplotlib.pyplot as plt     # plotting
import seaborn as sns               # nicer statistical plots

sns.set_style("darkgrid")           # global plot style
plt.rcParams["figure.figsize"] = (8, 4)   # default figure size

# Load the CSV file into a DataFrame (a table-like structure)
df = pd.read_csv("ai_job_dataset.csv")

# Convert date columns from text to actual datetime objects
# so we can extract month/year for trend charts
df["posting_date"] = pd.to_datetime(df["posting_date"])
df["application_deadline"] = pd.to_datetime(df["application_deadline"])

# ---------------------------------------------------------------
# STEP 2: DATA UNDERSTANDING
# ---------------------------------------------------------------
print("Shape of data (rows, columns):", df.shape)
print("\nColumn data types:\n", df.dtypes)
print("\nMissing values per column:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nQuick statistical summary of numeric columns:\n", df.describe())

# ---------------------------------------------------------------
# STEP 3: DATA CLEANING / PREPARATION
# ---------------------------------------------------------------
# The dataset is already clean (no nulls, no duplicates), but in real
# projects we always add safety steps like these:

df.drop_duplicates(inplace=True)               # remove exact duplicate rows
df["job_title"] = df["job_title"].str.strip()   # remove stray spaces in text
df["company_name"] = df["company_name"].str.strip()

# Create a "posting_month" column (e.g. "January") for the monthly trend chart
df["posting_month"] = df["posting_date"].dt.month_name()

# Keep months in calendar order (not alphabetical) for correct chart sorting
month_order = ["January","February","March","April","May","June","July",
               "August","September","October","November","December"]
df["posting_month"] = pd.Categorical(df["posting_month"],
                                      categories=month_order, ordered=True)

# ---------------------------------------------------------------
# STEP 4: UNIVARIATE ANALYSIS (distribution of single columns)
# ---------------------------------------------------------------
# Salary distribution
plt.figure()
sns.histplot(df["salary_usd"], bins=40, kde=True, color="dodgerblue")
plt.title("Distribution of Salaries (USD)")
plt.xlabel("Salary (USD)")
plt.tight_layout()
plt.savefig("chart1_salary_distribution.png")
plt.close()

# Experience level counts (Intern/Mid/Senior/Expert split -> matches donut chart)
plt.figure()
df["experience_level"].value_counts().plot(kind="bar", color="mediumpurple")
plt.title("Job Count by Experience Level")
plt.ylabel("Number of Jobs")
plt.tight_layout()
plt.savefig("chart2_experience_level.png")
plt.close()

# ---------------------------------------------------------------
# STEP 5: KPI CARDS (single headline numbers, same as dashboard top row)
# ---------------------------------------------------------------
total_hiring = df["job_id"].count()                                  # Total Hiring (15.0K card)
avg_benefit_rate = round(df["benefits_score"].mean(), 1)             # Average Benefit Rate card
top_hiring_company = df["company_name"].value_counts().idxmax()      # Top Hiring company card
high_salary_company = (df.groupby("company_name")["salary_usd"]
                          .mean().idxmax())                          # High Salary Company card

print("\n--- KPI CARDS ---")
print("Total Hiring:", total_hiring)
print("Average Benefit Rate:", avg_benefit_rate)
print("Top Hiring Company (most job posts):", top_hiring_company)
print("Highest Average Salary Company:", high_salary_company)

# ---------------------------------------------------------------
# STEP 6: GROUPED / BIVARIATE ANALYSIS (recreating each dashboard chart)
# ---------------------------------------------------------------

# 6.1 Top 5 High Salary Job Roles (bar chart)
top5_salary_roles = (df.groupby("job_title")["salary_usd"]
                        .mean().sort_values(ascending=False).head(5))
plt.figure()
top5_salary_roles.plot(kind="bar", color="dodgerblue")
plt.title("Top 5 High Salary Job Roles")
plt.ylabel("Average Salary (USD)")
plt.tight_layout()
plt.savefig("chart3_top5_salary_roles.png")
plt.close()

# 6.2 Hiring and Salary by Month (line chart, dual metric)
monthly_trend = df.groupby("posting_month", observed=True).agg(
    job_count=("job_id", "count"),
    total_salary=("salary_usd", "sum")
)
fig, ax1 = plt.subplots()
ax1.plot(monthly_trend.index, monthly_trend["job_count"], color="salmon", label="Job Count")
ax1.set_ylabel("Job Count", color="salmon")
ax2 = ax1.twinx()   # second y-axis sharing the same x-axis
ax2.plot(monthly_trend.index, monthly_trend["total_salary"], color="blue", label="Total Salary")
ax2.set_ylabel("Total Salary (USD)", color="blue")
plt.title("Hiring and Salary by Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("chart4_hiring_salary_by_month.png")
plt.close()

# 6.3 Top 5 Hiring Countries (bar chart)
top5_countries = df["company_location"].value_counts().head(5)
plt.figure()
top5_countries.plot(kind="bar", color="dodgerblue")
plt.title("Top 5 Hiring Countries")
plt.ylabel("Number of Job Postings")
plt.tight_layout()
plt.savefig("chart5_top5_countries.png")
plt.close()

# 6.4 Job by Experience (pie/donut chart)
exp_share = df["experience_level"].value_counts(normalize=True) * 100
plt.figure()
plt.pie(exp_share, labels=exp_share.index, autopct="%1.1f%%",
        colors=sns.color_palette("cool", len(exp_share)))
plt.title("Job Share by Experience Level")
plt.tight_layout()
plt.savefig("chart6_job_by_experience.png")
plt.close()

# 6.5 Experience (years) vs Salary (line/scatter with trend)
exp_vs_salary = df.groupby("years_experience")["salary_usd"].mean()
plt.figure()
exp_vs_salary.plot(kind="line", marker="o", color="orangered")
plt.title("Years of Experience vs Average Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Average Salary (USD)")
plt.tight_layout()
plt.savefig("chart7_experience_vs_salary.png")
plt.close()

# 6.6 Job by Work Type (donut chart: FT/PT/CT/FL)
work_type_share = df["employment_type"].value_counts(normalize=True) * 100
plt.figure()
plt.pie(work_type_share, labels=work_type_share.index, autopct="%1.1f%%",
        colors=sns.color_palette("Set2", len(work_type_share)))
plt.title("Job Share by Employment Type")
plt.tight_layout()
plt.savefig("chart8_job_by_worktype.png")
plt.close()

# 6.7 Job count by Industry (side list panel in dashboard)
industry_counts = df["industry"].value_counts()
print("\n--- Job Count by Industry ---\n", industry_counts)

# ---------------------------------------------------------------
# STEP 7: CORRELATION ANALYSIS (extra insight beyond the dashboard)
# ---------------------------------------------------------------
# Check how numeric fields relate to salary (e.g. does experience or
# benefits score move together with salary?)
numeric_cols = ["salary_usd", "years_experience", "remote_ratio",
                 "job_description_length", "benefits_score"]
corr_matrix = df[numeric_cols].corr()
plt.figure()
sns.heatmap(corr_matrix, annot=True, cmap="Blues", fmt=".2f")
plt.title("Correlation Between Numeric Features")
plt.tight_layout()
plt.savefig("chart9_correlation_heatmap.png")
plt.close()

# ---------------------------------------------------------------
# STEP 8: OUTLIER CHECK (boxplot on salary)
# ---------------------------------------------------------------
plt.figure()
sns.boxplot(x=df["salary_usd"], color="lightgreen")
plt.title("Salary Outlier Check")
plt.tight_layout()
plt.savefig("chart10_salary_outliers.png")
plt.close()

# ---------------------------------------------------------------
# STEP 9: FINAL INSIGHTS SUMMARY (printed as a text report)
# ---------------------------------------------------------------
print("\n===================== FINAL INSIGHTS =====================")
print(f"1. Total job postings analyzed: {total_hiring}")
print(f"2. Average benefits score across all jobs: {avg_benefit_rate}")
print(f"3. Company with most job postings: {top_hiring_company}")
print(f"4. Company with highest average salary: {high_salary_company}")
print(f"5. Highest paying role on average: {top5_salary_roles.index[0]} "
      f"(${top5_salary_roles.iloc[0]:,.0f})")
print(f"6. Country with most job postings: {top5_countries.index[0]}")
print(f"7. Correlation of years_experience with salary: "
      f"{corr_matrix.loc['salary_usd','years_experience']:.2f} "
      f"(closer to 1 = stronger positive relationship)")
print("============================================================")
