"""
Project 1: Sales Data Analysis Dashboard
Navyan Internship | Python + Matplotlib
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────
# STEP 1: LOAD THE DATASET
# ─────────────────────────────────────────
# If you have the Superstore CSV, replace the path below:
# df = pd.read_csv("superstore.csv", encoding='latin-1')

# ── Sample data (use this if you don't have Kaggle dataset yet) ──
np.random.seed(42)
n = 500

categories   = ['Furniture', 'Office Supplies', 'Technology']
regions      = ['East', 'West', 'Central', 'South']
products     = ['Chairs', 'Binders', 'Phones', 'Tables', 'Storage',
                'Accessories', 'Bookcases', 'Appliances', 'Paper', 'Labels']

df = pd.DataFrame({
    'Order ID'  : [f'ORD-{i:04d}' for i in range(n)],
    'Product'   : np.random.choice(products, n),
    'Category'  : np.random.choice(categories, n),
    'Region'    : np.random.choice(regions, n),
    'Sales'     : np.random.randint(50, 3000, n).astype(float),
    'Profit'    : np.random.randint(-200, 800, n).astype(float),
    'Order Date': pd.date_range(start='2022-01-01', periods=n, freq='17h')
})

# ─────────────────────────────────────────
# STEP 2: CLEAN THE DATA
# ─────────────────────────────────────────
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month']      = df['Order Date'].dt.to_period('M')
df['Year']       = df['Order Date'].dt.year

print("✅ Dataset loaded and cleaned.")
print(f"   Rows: {len(df)} | Columns: {list(df.columns)}\n")

# ─────────────────────────────────────────
# STEP 3: ANALYZE KEY METRICS
# ─────────────────────────────────────────
total_sales  = df['Sales'].sum()
total_profit = df['Profit'].sum()
profit_margin = (total_profit / total_sales) * 100

top_products = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(5)
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
category_sales = df.groupby('Category')['Sales'].sum()
monthly_sales = df.groupby('Month')['Sales'].sum()

print(f"💰 Total Sales   : ₹{total_sales:,.0f}")
print(f"📈 Total Profit  : ₹{total_profit:,.0f}")
print(f"📊 Profit Margin : {profit_margin:.1f}%\n")
print("🏆 Top Products by Sales:")
print(top_products.to_string())

# ─────────────────────────────────────────
# STEP 4: VISUALIZATIONS — 2x3 DASHBOARD
# ─────────────────────────────────────────
fig = plt.figure(figsize=(18, 12), facecolor='#0f0f1a')
fig.suptitle('Sales Data Analysis Dashboard',
             fontsize=22, fontweight='bold', color='white', y=0.98)

gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.45, wspace=0.35)

ACCENT  = ['#6C63FF', '#FF6584', '#43D9AD', '#FFD166', '#EF476F']
BG      = '#1a1a2e'
TEXT    = '#e0e0e0'
GRID    = '#2a2a3e'

def style_ax(ax, title):
    ax.set_facecolor(BG)
    ax.set_title(title, color=TEXT, fontsize=11, fontweight='bold', pad=10)
    ax.tick_params(colors=TEXT, labelsize=8)
    ax.spines['bottom'].set_color(GRID)
    ax.spines['left'].set_color(GRID)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.label.set_color(TEXT)
    ax.xaxis.label.set_color(TEXT)
    ax.grid(axis='y', color=GRID, linewidth=0.5, alpha=0.7)

# ── Chart 1: Top 5 Products by Sales (Horizontal Bar) ──
ax1 = fig.add_subplot(gs[0, 0])
bars = ax1.barh(top_products.index, top_products.values, color=ACCENT, edgecolor='none', height=0.6)
for bar, val in zip(bars, top_products.values):
    ax1.text(val + 50, bar.get_y() + bar.get_height()/2,
             f'₹{val:,.0f}', va='center', color=TEXT, fontsize=7)
style_ax(ax1, '🏆 Top 5 Products by Sales')
ax1.set_xlabel('Total Sales (₹)')
ax1.grid(axis='x', color=GRID, linewidth=0.5, alpha=0.7)
ax1.grid(axis='y', visible=False)

# ── Chart 2: Sales by Region (Bar Chart) ──
ax2 = fig.add_subplot(gs[0, 1])
ax2.bar(region_sales.index, region_sales.values,
        color=ACCENT[:len(region_sales)], edgecolor='none', width=0.5)
for i, (reg, val) in enumerate(region_sales.items()):
    ax2.text(i, val + 200, f'₹{val:,.0f}', ha='center', color=TEXT, fontsize=7)
style_ax(ax2, '🌍 Sales by Region')
ax2.set_ylabel('Total Sales (₹)')

# ── Chart 3: Category Distribution (Pie Chart) ──
ax3 = fig.add_subplot(gs[0, 2])
wedges, texts, autotexts = ax3.pie(
    category_sales.values,
    labels=category_sales.index,
    autopct='%1.1f%%',
    colors=ACCENT[:3],
    startangle=90,
    wedgeprops={'edgecolor': '#0f0f1a', 'linewidth': 2}
)
for t in texts:
    t.set_color(TEXT); t.set_fontsize(9)
for at in autotexts:
    at.set_color('white'); at.set_fontsize(8); at.set_fontweight('bold')
ax3.set_facecolor(BG)
ax3.set_title('📦 Category Distribution', color=TEXT, fontsize=11,
              fontweight='bold', pad=10)

# ── Chart 4: Monthly Sales Trend (Line Chart) ──
ax4 = fig.add_subplot(gs[1, :2])
months = [str(m) for m in monthly_sales.index]
values = monthly_sales.values
ax4.plot(months, values, color='#6C63FF', linewidth=2.5, marker='o',
         markersize=4, markerfacecolor='#FFD166')
ax4.fill_between(months, values, alpha=0.15, color='#6C63FF')
ax4.set_xticks(range(0, len(months), max(1, len(months)//12)))
ax4.set_xticklabels([months[i] for i in range(0, len(months), max(1, len(months)//12))],
                    rotation=30, ha='right')
style_ax(ax4, '📅 Monthly Sales Trend')
ax4.set_ylabel('Sales (₹)')

# ── Chart 5: Profit by Category (Bar Chart) ──
ax5 = fig.add_subplot(gs[1, 2])
cat_profit = df.groupby('Category')['Profit'].sum()
colors_profit = ['#43D9AD' if v >= 0 else '#EF476F' for v in cat_profit.values]
ax5.bar(cat_profit.index, cat_profit.values, color=colors_profit,
        edgecolor='none', width=0.5)
for i, (cat, val) in enumerate(cat_profit.items()):
    ax5.text(i, val + 50, f'₹{val:,.0f}', ha='center', color=TEXT, fontsize=7)
style_ax(ax5, '💹 Profit by Category')
ax5.set_ylabel('Total Profit (₹)')
ax5.axhline(0, color=TEXT, linewidth=0.8, linestyle='--', alpha=0.4)

plt.savefig('sales_dashboard.png', dpi=150, bbox_inches='tight',
            facecolor='#0f0f1a')
print("\n✅ Dashboard saved as 'sales_dashboard.png'")
plt.show()
