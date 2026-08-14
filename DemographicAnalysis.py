import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

df = pd.read_csv('data/processed/FARSmaster.csv')
print(df.columns.tolist())
print(df.head(2))

# Correlation with Crash Rate per 10k population

# Aggregate data by Census Tract
tract_stats = df.groupby(['GEOID', 'NAMELSAD']).agg(
    crash_count=('ST_CASE', 'nunique'), # Using nunique for ST_CASE in case of multiple persons per crash
    MEDIAN_INCOME=('MEDIAN_INCOME', 'first'),
    TOTAL_POPULATION=('TOTAL_POPULATION', 'first'),
    PCT_WHITE=('PCT_WHITE', 'first'),
    PCT_BLACK=('PCT_BLACK', 'first'),
    PCT_HISPANIC=('PCT_HISPANIC', 'first'),
    PCT_TRANSIT_WALK_COMMUTE=('PCT_TRANSIT_WALK_COMMUTE', 'first')
).reset_index()

# Filter out tracts with 0 population
tract_stats = tract_stats[tract_stats['TOTAL_POPULATION'] > 0]

# Calculate crashes per 10,000 population
tract_stats['crash_rate_per_10k'] = (tract_stats['crash_count'] / tract_stats['TOTAL_POPULATION']) * 10000

# Compute correlations
target = 'crash_rate_per_10k'
predictors = ['MEDIAN_INCOME', 'PCT_WHITE', 'PCT_BLACK', 'PCT_HISPANIC', 'PCT_TRANSIT_WALK_COMMUTE']

cols = [target] + predictors
corr_data = tract_stats[cols].dropna()
print(len(corr_data))  # should print 489

results = []
for col in predictors:
    res = pearsonr(corr_data[target], corr_data[col])
    ci_low, ci_high = res.confidence_interval(confidence_level=0.95)
    results.append({
        'variable': col,
        'r': round(res.statistic, 3),
        'p_value': round(res.pvalue, 4),
        'ci_95_low': round(ci_low, 3),
        'ci_95_high': round(ci_high, 3),
        'n': len(corr_data)
    })

corr_results_df = pd.DataFrame(results)
print(corr_results_df)


# Income / Black Tiers crash rate per 10k population 

tract_stats = df.groupby(['GEOID', 'NAMELSAD']).agg(
    crash_count=('ST_CASE', 'nunique'), 
    MEDIAN_INCOME=('MEDIAN_INCOME', 'first'),
    TOTAL_POPULATION=('TOTAL_POPULATION', 'first'),
    PCT_WHITE=('PCT_WHITE', 'first'),
    PCT_BLACK=('PCT_BLACK', 'first'),
    PCT_HISPANIC=('PCT_HISPANIC', 'first'),
    PCT_TRANSIT_WALK_COMMUTE=('PCT_TRANSIT_WALK_COMMUTE', 'first')
).reset_index()

tract_stats = tract_stats[tract_stats['TOTAL_POPULATION'] > 0]
tract_stats['crash_rate_per_10k'] = (tract_stats['crash_count'] / tract_stats['TOTAL_POPULATION']) * 10000

# Create Income Quartiles
tract_stats['Income_Quartile'] = pd.qcut(tract_stats['MEDIAN_INCOME'], q=4, labels=['Q1 (Lowest)', 'Q2', 'Q3', 'Q4 (Highest)'])

# Calculate mean crash rate by income quartile
income_summary = tract_stats.groupby('Income_Quartile')['crash_rate_per_10k'].mean().reset_index()

# Plot Income Quartile vs Crash Rate
plt.figure(figsize=(8, 5))
sns.barplot(x='Income_Quartile', y='crash_rate_per_10k', data=income_summary, palette='viridis')
plt.title('Average Fatal Pedestrian/Cyclist Crash Rate by Income Quartile', fontsize=16)
plt.ylabel('Crash Rate (per 10k residents)', fontsize=16)
plt.xlabel('Median Income Quartile', fontsize=16)
plt.tight_layout()
plt.savefig('income_chart.png')
plt.close()

# Discretize PCT_BLACK and PCT_TRANSIT_WALK_COMMUTE for simple visualization
tract_stats['Black_Pop_Tier'] = pd.qcut(tract_stats['PCT_BLACK'], q=3, labels=['Low', 'Medium', 'High'], duplicates='drop')
black_summary = tract_stats.groupby('Black_Pop_Tier')['crash_rate_per_10k'].mean().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(x='Black_Pop_Tier', y='crash_rate_per_10k', data=black_summary, palette='viridis')
plt.title('Average Fatal Crash Rate by % Black Population (Tiers)', fontsize=16)
plt.ylabel('Crash Rate (per 10k residents)', fontsize=16)
plt.xlabel('% Black Population Tier', fontsize=16)
plt.tight_layout()
plt.savefig('black_pop_chart.png')
plt.close()

print(income_summary)
print(black_summary)


# Transit / Hispanic Tiers crash rate per 10k population

tract_stats_transit = df.groupby(['GEOID', 'NAMELSAD']).agg(
    crash_count=('ST_CASE', 'nunique'),
    TOTAL_POPULATION=('TOTAL_POPULATION', 'first'),
    PCT_HISPANIC=('PCT_HISPANIC', 'first'),
    PCT_TRANSIT_WALK_COMMUTE=('PCT_TRANSIT_WALK_COMMUTE', 'first')
).reset_index()

tract_stats_transit = tract_stats_transit[tract_stats_transit['TOTAL_POPULATION'] > 0]
tract_stats_transit['crash_rate_per_10k'] = (tract_stats_transit['crash_count'] / tract_stats_transit['TOTAL_POPULATION']) * 10000

# Discretize PCT_HISPANIC and PCT_TRANSIT_WALK_COMMUTE
tract_stats_transit['Hispanic_Pop_Tier'] = pd.qcut(tract_stats_transit['PCT_HISPANIC'], q=3, labels=['Low', 'Medium', 'High'], duplicates='drop')
hisp_summary = tract_stats_transit.groupby('Hispanic_Pop_Tier')['crash_rate_per_10k'].mean().reset_index()

tract_stats_transit['Transit_Walk_Tier'] = pd.qcut(tract_stats_transit['PCT_TRANSIT_WALK_COMMUTE'], q=3, labels=['Low', 'Medium', 'High'], duplicates='drop')
transit_summary = tract_stats_transit.groupby('Transit_Walk_Tier')['crash_rate_per_10k'].mean().reset_index()

print("Hispanic Summary:\n", hisp_summary)
print("Transit/Walk Summary:\n", transit_summary)



