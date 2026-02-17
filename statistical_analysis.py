import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

import os
import matplotlib.pyplot as plt

# This creates the folder if it doesn't exist
if not os.path.exists('visualizations'):
    os.makedirs('visualizations')

# When saving any plot, use this format:
plt.savefig('visualizations/my_plot_name.png')

# 1. Load Data
df = pd.read_csv('data/sales_data(4).csv')

# 2. Descriptive Statistics
stats_summary = df['Total_Sales'].describe()
print("--- Descriptive Statistics ---\n", stats_summary)

# 3. Hypothesis Testing
# Test 1: ANOVA - Do regions have significantly different average sales?
region_groups = [df[df['Region'] == r]['Total_Sales'] for r in df['Region'].unique()]
f_stat, p_val_f = stats.f_oneway(*region_groups)
print(f"\nANOVA Region Test: p-value = {p_val_f:.4f}")

# Test 2: t-test - North vs South Sales comparison
north = df[df['Region'] == 'North']['Total_Sales']
south = df[df['Region'] == 'South']['Total_Sales']
t_stat, p_val_t = stats.ttest_ind(north, south)
print(f"t-test (North vs South): p-value = {p_val_t:.4f}")

# 4. Confidence Intervals (95% for Mean Sales)
mean = df['Total_Sales'].mean()
sem = stats.sem(df['Total_Sales'])
ci = stats.t.interval(0.95, len(df)-1, loc=mean, scale=sem)
print(f"\n95% Confidence Interval for Sales: {ci}")

# 5. Linear Regression (Impact of Price/Quantity on Sales)
X = sm.add_constant(df[['Price', 'Quantity']])
y = df['Total_Sales']
model = sm.OLS(y, X).fit()
print("\n--- Regression Summary ---")
print(f"R-squared: {model.rsquared:.4f}")