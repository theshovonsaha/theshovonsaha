import os
import json
import re

# Read the current README
with open('README.md', 'r') as file:
    content = file.read()

# Get Medium stats from environment
medium_stats = json.loads(os.environ['MEDIUM_STATS'])

# Create stats section
stats_section = f"""
## Medium Stats 📊
- Total Articles: {medium_stats['total_posts']}
- Total Views: {medium_stats['total_views']}
- Total Claps: {medium_stats['total_claps']}
"""

# Update the README
with open('README.md', 'w') as file:
    file.write(content.replace('<!-- MEDIUM-STATS -->', stats_section))
