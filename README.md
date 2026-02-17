# Week7_Statistical_Analysis

Project Overview
This project focuses on applying Inferential Statistics and Predictive Modeling to real-world e-commerce data. The goal is to move beyond simple data cleaning and use mathematical evidence to validate business hypotheses, identify significant correlations, and build a linear regression model to forecast sales.

🛠️ Key Tasks Completed
Descriptive Statistics: Calculated Mean, Median, Mode, and Standard Deviation to establish data baselines.

Hypothesis Testing: * ANOVA: Evaluated if sales performance varies significantly across different geographic regions.

T-Tests: Compared specific regional performance (North vs. South).

Correlation Analysis: Measured the Pearson correlation coefficient between Price, Quantity, and Revenue.

Regression Modeling: Developed an Ordinary Least Squares (OLS) regression model to quantify the impact of pricing on total sales.

Confidence Intervals: Determined the 95% CI for average transaction values to account for margin of error.

📂 Project Structure
Plaintext
├── data/
│   └── sales_data.csv             # Raw transaction dataset
├── visualizations/                # Statistical plots generated via Matplotlib/Seaborn
│   ├── sales_distribution.png     # Frequency and Density Analysis
│   ├── correlation_heatmap.png    # Variable Relationship Mapping
│   └── regression_plot.png        # Linear Trend Visualization
├── statistical_analysis.ipynb     # Interactive Jupyter Notebook analysis
├── statistical_report.pdf         # Formal Executive Summary
├── hypothesis_tests_results.txt   # Detailed p-value and t-stat logs
├── requirements.txt               # Project dependencies
└── README.md                      # Project documentation
🚀 Setup & Installation
Clone the repository:

Bash
git clone https://github.com/your-username/week-7-statistical-analysis.git
Install dependencies:

Bash
pip install -r requirements.txt
Run the analysis:
Open statistical_analysis.ipynb in Jupyter Lab/VS Code or run:

Bash
python statistical_analysis.py
📈 Key Insights
Hypothesis Result: Our ANOVA test returned a p-value > 0.05, indicating that there is no statistically significant difference in sales performance between regions.

Correlation: A strong positive correlation (r ≈ 0.82) exists between Unit Price and Total Sales, suggesting price-inelastic demand for core products.

Model Accuracy: The Linear Regression model achieved an R-squared of 0.84, meaning 84% of sales variance is explained by our input variables.

🧰 Tech Stack
Language: Python 3.12

Libraries: Pandas, NumPy, Scipy.stats, Statsmodels, Matplotlib, Seaborn
