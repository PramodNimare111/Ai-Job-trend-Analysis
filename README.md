# AI Job Trend Analysis

An end-to-end data analytics project that explores **15,000 AI-related job postings** with **Python** (pandas, seaborn, matplotlib) and presents the findings in an interactive **Power BI** dashboard.

![Power BI Dashboard](PowerBi%20dashboard%20screenshot.png)

## Objectives

- Understand how many AI jobs are posted and which companies hire the most and pay the most
- Find which job roles and countries stand out
- Measure how experience, company size, education and remote work relate to salary
- Track hiring volume over time
- Present results as a clear, interactive dashboard

## Repository Structure

```
Ai-Job-trend-Analysis/
├── ai_job_dataset.csv                    # Raw dataset (15,000 rows x 19 columns)
├── ai_job_market_analysis.py             # Python cleaning, analysis and chart script
├── AI job trend powerbi dashboard.pbix   # Power BI report
├── PowerBi dashboard screenshot.png      # Dashboard preview
├── Charts/                               # Exported chart images
└── README.md
```

## Dataset

| Column | Description |
|---|---|
| `job_id` | Unique posting ID |
| `job_title` | Role (20 titles, e.g. Machine Learning Engineer, AI Architect, Data Analyst) |
| `salary_usd` | Salary in USD |
| `salary_currency` | Original currency (USD, EUR, GBP) |
| `experience_level` | EN = Entry, MI = Mid, SE = Senior, EX = Executive |
| `employment_type` | FT = Full-time, PT = Part-time, CT = Contract, FL = Freelance |
| `company_location` | Country of the company |
| `company_size` | S, M or L |
| `employee_residence` | Country of the employee |
| `remote_ratio` | 0 = on-site, 50 = hybrid, 100 = fully remote |
| `required_skills` | Comma-separated skills |
| `education_required` | Associate, Bachelor, Master or PhD |
| `years_experience` | Years of experience required (0 to 19) |
| `industry` | 15 industries |
| `posting_date` / `application_deadline` | Posting window dates (Jan 2024 to Apr 2025) |
| `job_description_length` | Length of the job description |
| `benefits_score` | Benefits rating (5.0 to 10.0) |
| `company_name` | Hiring company (16 companies) |

> The categories are almost perfectly evenly distributed, so the dataset appears to be synthetic. Treat the results as a demonstration of method, not as real market statistics.

## Tools and Technologies

- **Python:** pandas, numpy, matplotlib, seaborn
- **Power BI Desktop:** dashboard, slicers, maps and charts
- **Concepts:** data cleaning, EDA, KPIs, correlation, outlier detection, aggregation, visual storytelling

## Python Analysis (`ai_job_market_analysis.py`)

1. Load the CSV and convert date columns to datetime
2. Check shape, data types, missing values and duplicates
3. Clean: drop duplicates, trim text and create an ordered `posting_month`
4. Calculate KPIs: total hiring, average benefit rate, top hiring company, highest-paying company
5. Generate 10 charts:

| # | Chart |
|---|---|
| 1 | Salary distribution (histogram) |
| 2 | Jobs by experience level |
| 3 | Top 5 highest-paying roles (average salary) |
| 4 | Hiring and salary by month |
| 5 | Top 5 hiring countries |
| 6 | Job share by experience level |
| 7 | Years of experience vs average salary |
| 8 | Job share by employment type |
| 9 | Correlation heatmap |
| 10 | Salary outlier boxplot |

## Power BI Dashboard

**KPI cards:** Total Hiring, Average Benefit Rate, Top Hiring Company, High Salary Company

**Visuals:** Top 5 High Salary Job Roles, Hiring and Salary by Month, Top 5 Hiring Countries, Job by Experience, Job by Work Type, Experience vs Salary, Hiring by Country (map)

**Interactivity:** an **industry slicer** filters every visual on the page.

## Key Insights

- **15,000** job postings analysed, with no missing values and no duplicate rows
- Average salary is **$115,349** and median is **$99,705**, a right-skewed distribution (range $32,519 to $399,095)
- Salary rises with level: Entry **$63K**, Mid **$88K**, Senior **$122K**, Executive **$188K**
- Years of experience and salary have a strong positive correlation of **0.74**
- Larger companies pay more: Small **$102K**, Medium **$114K**, Large **$130K**
- Education level and remote ratio have little effect on average salary in this data
- **TechCorp Inc** is both the top hiring company (980 postings) and has the highest average salary ($121K)
- Highest average-salary role: **AI Specialist** (about $121K); country with most postings: **Germany** (814)
- Most requested skills: **Python**, **SQL**, **TensorFlow**, **Kubernetes**

## Known Limitations

- The data covers Jan 2024 to Apr 2025, so grouping by month name alone combines Jan to Apr of two years. Group by year-month for a true trend.
- "High salary" visuals can mean average or maximum salary. The Python script uses the average; label the aggregation clearly in dashboards.
- The dataset looks synthetic, so conclusions should not be generalised to the real job market.

## How to Run

```bash
# 1. Clone the repo
git clone https://github.com/PramodNimare111/Ai-Job-trend-Analysis.git
cd Ai-Job-trend-Analysis

# 2. Install dependencies
pip install pandas numpy matplotlib seaborn

# 3. Run the analysis (saves chart1 ... chart10 PNG files and prints KPIs)
python ai_job_market_analysis.py
```

To explore the dashboard, open `AI job trend powerbi dashboard.pbix` in **Power BI Desktop** (Windows).

## Future Improvements

- Replace implicit aggregations with named DAX measures
- Add a Date table for month-over-month and year-over-year analysis
- Split `required_skills` in Power Query and add a "Top Skills" chart
- Add salary prediction with a simple regression model
- Publish the report to Power BI Service

## Author

**Pramod Nimare**: [GitHub](https://github.com/PramodNimare111)
