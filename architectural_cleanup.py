import re

with open("neoscona.html", "r", encoding="utf-8") as f:
    html = f.read()

# STRIP CHEAP EFFECTS: Drop shadows, blurs, translations, bouncy scales, gradients
removals = [
    r'shadow-\[[^\]]+\]',
    r'hover:shadow-\[[^\]]+\]',
    r'shadow-\w+',
    r'hover:shadow-\w+',
    r'backdrop-blur-\w+',
    r'blur-\w+',
    r'hover:-translate-y-\d+',
    r'hover:scale-\w+',
    r'group-hover:scale-\w+',
    r'bg-gradient-to-\w+',
    r'from-\w+',
    r'via-\w+',
    r'to-\w+',
    r'text-transparent',
    r'bg-clip-text',
    r'rounded-2xl', # Oasis uses tighter borders, usually rounded-xl or rounded-lg
    r'rounded-full', # except buttons/icons
]

for pattern in removals:
    html = re.sub(pattern, '', html)

# Fix background transparencies to solid colors
html = re.sub(r'bg-surface-container-highest/\d+', 'bg-[#1F1E1B]', html)
html = re.sub(r'bg-surface-container-high/\d+', 'bg-[#1F1E1B]', html)
html = re.sub(r'bg-surface-container-low/\d+', 'bg-[#1F1E1B]', html)
html = re.sub(r'bg-surface-dim/\d+', 'bg-[#1F1E1B]', html)
html = re.sub(r'bg-[#111318]/\d+', 'bg-[#1F1E1B]', html)
html = re.sub(r'bg-surface-container-low', 'bg-[#1F1E1B]', html)
html = re.sub(r'bg-surface-container-high', 'bg-[#1F1E1B]', html)
html = re.sub(r'bg-surface-container-highest', 'bg-[#1f1e1B]', html)

# Change bouncy/long transitions to short, sharp ones
html = re.sub(r'duration-500', 'duration-200', html)
html = re.sub(r'duration-700', 'duration-200', html)
html = re.sub(r'duration-1000', 'duration-200', html)

# Make corners sharper (Oasis style)
# We removed rounded-2xl. Let's add rounded-xl to cards where padding is applied.
# Find class attributes containing 'p-8', 'p-10', 'p-11' without rounded
def add_rounded(match):
    classes = match.group(1)
    if 'p-8' in classes or 'p-10' in classes or 'p-11' in classes or 'min-w-' in classes:
        return f'class="{classes} rounded-xl"'
    return match.group(0)

html = re.sub(r'class="([^"]*)"', add_rounded, html)

# Add structural borders to everything that has p-8, p-10 (cards) to match Oasis' framed look
def add_structural_borders(match):
    classes = match.group(1)
    # Don't add to buttons or primary colored cards
    if ('p-8' in classes or 'p-10' in classes or 'p-11' in classes) and 'bg-[#7C3AED]' not in classes and 'bg-[#F1EFE8]' not in classes:
        if 'border' not in classes:
            return f'class="{classes} border border-[#2E2C27] hover:bg-[#2E2C27]"'
        else:
            # Replace existing border with correct one
            c = re.sub(r'border-\w+/\d+', 'border-[#2E2C27]', classes)
            c = c.replace('border-[#d8b4fe]', 'border-[#2E2C27]')
            if 'hover:bg-[#2E2C27]' not in c:
                c += ' hover:bg-[#2E2C27]'
            return f'class="{c}"'
    return match.group(0)

html = re.sub(r'class="([^"]*)"', add_structural_borders, html)

# Fix hover over borders
html = re.sub(r'hover:border-primary/\d+', 'hover:border-[#3e3c37]', html)

# Remove stray transparent/blurred graphic nodes
# A lot of them were <div class="absolute ... bg-primary/5 rounded-full ..."></div>
# Just delete elements that look like pure decorative blur blobs
html = re.sub(r'<div class="[^"]*bg-primary/\d+[^"]*blur-[^"]*"></div>', '', html)
html = re.sub(r'<div class="[^"]*opacity-20 blur-[^"]*"></div>', '', html)

# Fix button roundness (Oasis buttons are pills)
# We removed rounded-full globally, need it back for buttons containing "px-" and "py-"
def fix_buttons(match):
    classes = match.group(1)
    if 'px-' in classes and 'py-' in classes:
        if 'rounded-full' not in classes:
            classes += ' rounded-full'
    return f'class="{classes}"'
html = re.sub(r'class="([^"]*)"', fix_buttons, html)

# Refine Typography for Oasis feel
html = html.replace('font-extrabold', 'font-medium tracking-tight')
html = html.replace('font-bold', 'font-medium tracking-tight')

# Clean up multiple whitespaces in class strings
def clean_whitespaces(match):
    c = match.group(1)
    c = re.sub(r'\s+', ' ', c).strip()
    return f'class="{c}"'
html = re.sub(r'class="([^"]*)"', clean_whitespaces, html)

with open("neoscona.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Applied architectural structural cleanup.")
