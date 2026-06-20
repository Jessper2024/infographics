#!/usr/bin/env python3
"""Fix quoting issues in the generator script"""
with open('_gen_dongpo_ch9_12.py', 'r') as f:
    content = f.read()

# Fix: replace ASCII apostrophes in HTML content with HTML entities
# These break Python single-quoted strings
fixes = [
    ("Zhou's", "Zhou&rsquo;s"),
    ("Qin's", "Qin&rsquo;s"),
    ("Lu's", "Lu&rsquo;s"),
    ("Duke's", "Duke&rsquo;s"),
    ("king's", "king&rsquo;s"),
    ("ruler's", "ruler&rsquo;s"),
    ("someone's", "someone&rsquo;s"),
    ("daughter's", "daughter&rsquo;s"),
    ("Confucius's", "Confucius&rsquo;s"),
    ("One Defeat", "One Defeat"),
]

count = 0
for old, new in fixes:
    count_here = content.count(old)
    if count_here > 0:
        content = content.replace(old, new)
        count += count_here

print(f"Fixed {count} apostrophe occurrences")

with open('_gen_dongpo_ch9_12.py', 'w') as f:
    f.write(content)
print("Done")