
# Customer Purchase Pattern & Revenue Attribution Analysis

Analyzing customer purchase behavior to identify **where revenue comes from** — broken down by gender, age group, product category, and discount-driven spending patterns.

## 📊 Project Overview

This project analyzes transactional customer data to uncover revenue drivers across different customer segments. By examining how gender, age, product choice, and discount pricing influence purchase amounts, the goal is to provide actionable insights for pricing strategy, targeted marketing, and inventory planning.

## 📁 Data Source

[Add your data source here]

## 🛠 Tools & Technologies

| Tool | Purpose |
|------|---------|
| **Jupyter (Python)** | EDA, statistical analysis, visualizations |
| **SQL** | Data extraction, aggregation, segmentation |
| **Power Query** | ETL — data cleaning, transformation |
| **Power BI** | Interactive dashboards |
| **VS Code** | Development environment |

## 🔍 Analysis Areas

### 1. Revenue by Gender
- Total and average spend per gender group
- Revenue share contribution
- Preferred product categories per gender

### 2. Revenue by Age Group
- Spending distribution across age brackets
- Average transaction value per age group
- High-value customer segments

### 3. Revenue by Product Category
- Top-performing products by revenue and quantity
- Product affinity and cross-selling opportunities
- Category-level margins with discount factored in

### 4. Discount Impact Analysis
- How discount percentage affects purchase amount
- Revenue vs. discount depth — finding the sweet spot
- Do discounted purchases attract repeat buyers?

## ❓ Key Business Questions

1. Which customer segments (gender × age) generate the highest revenue?
2. How do discounts influence average order value across different products?
3. Are there products where discounts significantly cannibalize revenue?
4. What does the ideal customer profile look like by revenue contribution?

## 📈 Power BI Dashboard



Dashboard includes:
- Revenue KPIs (total revenue, avg order value, transactions)
- Revenue breakdown by gender and age slicers
- Product performance heatmap
- Discount vs. revenue scatter plot

## 🚀 How to Run This Project

1. **Clone the repository**
   ```bash  
   git clone https://github.com/yourusername/customer-purchase-pattern-analysis.git  
   cd customer-purchase-pattern-analysis
   Set up the database

Run the SQL scripts in /sql/ to create and populate tables
Update connection strings as needed
Run Jupyter notebooks

bash
jupyter notebook notebooks/
Open Power BI

Load the cleaned data (exported from notebooks or Power Query)
Open /powerbi/dashboard.pbix
📁 Repository Structure
bash
├── data/                  # Raw and processed datasets
├── notebooks/             # Jupyter notebooks for EDA
├── sql/                   # SQL queries
├── powerbi/               # Power BI dashboard file
├── outputs/               # Exported charts, CSVs, reports
├── README.md
└── requirements.txt       # Python dependencies
📌 Results Summary
[Add your key findings once analysis is complete]

Built with Python · SQL · Power BI · Power Query

yaml

---  

Want me to help with anything else — like a `requirements.txt` starter or SQL query templates for the 4 analysis areas?
