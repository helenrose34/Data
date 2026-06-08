import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
import seaborn as sns

# Sample language composition data
# Replace with your actual data from GitHub API
languages = {
    'Python': 35,
    'JavaScript': 25,
    'TypeScript': 20,
    'Java': 12,
    'CSS': 8
}

# Prepare data
lang_names = list(languages.keys())
lang_values = list(languages.values())
colors = sns.color_palette("husl", len(languages))

# Create figure with 4 subplots
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('GitHub Repository Language Composition - 4 Visualizations', 
             fontsize=16, fontweight='bold', y=0.995)

# 1. PIE CHART (Top Left)
ax1 = axes[0, 0]
wedges, texts, autotexts = ax1.pie(lang_values, labels=lang_names, autopct='%1.1f%%',
                                     colors=colors, startangle=90, textprops={'fontsize': 10})
ax1.set_title('1. Pie Chart - Language Distribution', fontweight='bold', fontsize=12, pad=10)
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

# 2. BAR CHART (Top Right)
ax2 = axes[0, 1]
bars = ax2.bar(lang_names, lang_values, color=colors, edgecolor='black', linewidth=1.5)
ax2.set_title('2. Bar Chart - Language Usage by Count', fontweight='bold', fontsize=12, pad=10)
ax2.set_ylabel('Lines of Code / Files', fontsize=10)
ax2.set_xlabel('Programming Language', fontsize=10)
ax2.tick_params(axis='x', rotation=45)
# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height)}',
            ha='center', va='bottom', fontsize=9)
ax2.grid(axis='y', alpha=0.3, linestyle='--')

# 3. HORIZONTAL BAR CHART (Bottom Left)
ax3 = axes[1, 0]
y_pos = np.arange(len(lang_names))
bars_h = ax3.barh(y_pos, lang_values, color=colors, edgecolor='black', linewidth=1.5)
ax3.set_yticks(y_pos)
ax3.set_yticklabels(lang_names)
ax3.set_title('3. Horizontal Bar Chart - Comparative View', fontweight='bold', fontsize=12, pad=10)
ax3.set_xlabel('Lines of Code / Files', fontsize=10)
ax3.invert_yaxis()
# Add value labels on bars
for i, bar in enumerate(bars_h):
    width = bar.get_width()
    ax3.text(width, bar.get_y() + bar.get_height()/2.,
            f' {int(width)}',
            ha='left', va='center', fontsize=9)
ax3.grid(axis='x', alpha=0.3, linestyle='--')

# 4. DONUT CHART (Bottom Right)
ax4 = axes[1, 1]
wedges, texts, autotexts = ax4.pie(lang_values, labels=lang_names, autopct='%1.1f%%',
                                     colors=colors, startangle=90, textprops={'fontsize': 10})
# Create donut hole
centre_circle = Circle((0, 0), 0.70, fc='white')
ax4.add_artist(centre_circle)
ax4.set_title('4. Donut Chart - Language Composition', fontweight='bold', fontsize=12, pad=10)
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(9)

# Adjust layout
plt.tight_layout()

# Save figure
plt.savefig('language_visualization.png', dpi=300, bbox_inches='tight')
print("Visualization saved as 'language_visualization.png'")

# Display figure
plt.show()

# Print statistics
print("\n" + "="*50)
print("Language Composition Statistics")
print("="*50)
total = sum(lang_values)
for lang, value in sorted(languages.items(), key=lambda x: x[1], reverse=True):
    percentage = (value / total) * 100
    print(f"{lang:15} {value:6} ({percentage:5.1f}%)")
print("="*50)
print(f"{'TOTAL':15} {total:6} (100.0%)")
print("="*50)
