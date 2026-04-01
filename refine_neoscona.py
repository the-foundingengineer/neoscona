import re

with open("neoscona.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Replace the color config so that all surface variants use #1F1E1B
# We can just do string replacements for the specific JSON lines
color_replacements = {
    '"surface-container-low": "#2E2C27"': '"surface-container-low": "#1F1E1B"',
    '"surface-container": "#2E2C27"': '"surface-container": "#1F1E1B"',
    '"surface-container-high": "#3A3832"': '"surface-container-high": "#1F1E1B"',
    '"surface-container-highest": "#403D37"': '"surface-container-highest": "#1F1E1B"',
    '"outline-variant": "#3A3832"': '"outline-variant": "#2E2C27"', # Darken outlines slightly so they don't pop too much if they were relying on the background
}

for old, new in color_replacements.items():
    text = text.replace(old, new)

# 2. Replace all <img ... src="images/wireframe_X.png" ... /> with SVG
svgs = [
    '''<svg viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="0.5" class="{img_class} text-primary opacity-60">
  <polygon points="50,10 90,30 90,70 50,90 10,70 10,30" />
  <polyline points="10,30 50,50 90,30" />
  <line x1="50" y1="50" x2="50" y2="90" />
  <line x1="10" y1="70" x2="50" y2="50" />
</svg>''',
    '''<svg viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="0.5" class="{img_class} text-primary opacity-60">
  <ellipse cx="50" cy="50" rx="40" ry="15" transform="rotate(0 50 50)" />
  <ellipse cx="50" cy="50" rx="40" ry="15" transform="rotate(60 50 50)" />
  <ellipse cx="50" cy="50" rx="40" ry="15" transform="rotate(120 50 50)" />
  <circle cx="50" cy="50" r="40" />
</svg>''',
    '''<svg viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="0.5" class="{img_class} text-primary opacity-60">
  <circle cx="20" cy="30" r="2" fill="currentColor"/>
  <circle cx="80" cy="20" r="2" fill="currentColor"/>
  <circle cx="70" cy="80" r="2" fill="currentColor"/>
  <circle cx="30" cy="70" r="2" fill="currentColor"/>
  <circle cx="50" cy="50" r="3" fill="currentColor"/>
  <line x1="20" y1="30" x2="50" y2="50" />
  <line x1="80" y1="20" x2="50" y2="50" />
  <line x1="70" y1="80" x2="50" y2="50" />
  <line x1="30" y1="70" x2="50" y2="50" />
  <line x1="20" y1="30" x2="30" y2="70" />
  <line x1="80" y1="20" x2="70" y2="80" />
</svg>''',
    '''<svg viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="0.5" class="{img_class} text-primary opacity-60">
  <polygon points="50,10 90,80 10,80" />
  <line x1="50" y1="10" x2="50" y2="80" />
  <line x1="50" y1="80" x2="90" y2="60" />
  <line x1="50" y1="80" x2="10" y2="60" />
  <line x1="10" y1="80" x2="90" y2="80" />
</svg>'''
]

svg_index = 0

def replace_img(match):
    global svg_index
    # Extract the class attribute from the matched img tag
    full_tag = match.group(0)
    class_match = re.search(r'class="([^"]*)"', full_tag)
    img_class = class_match.group(1) if class_match else "w-full h-full"
    
    # Remove opacity and mix-blend overrides from the original image classes to keep the SVG clean,
    # because the SVG already has opacity-60 and text-primary.
    img_class = re.sub(r'opacity-\d+', '', img_class)
    img_class = re.sub(r'group-hover:opacity-\d+', '', img_class)
    img_class = re.sub(r'mix-blend-\w+', '', img_class)
    img_class = img_class.replace('  ', ' ').strip()
    
    replacement = svgs[svg_index % len(svgs)].format(img_class=img_class)
    svg_index += 1
    return replacement

# Find all <img src="images/wireframe_... />
text = re.sub(r'<img[^>]*src="images/wireframe_[0-9]+\.png"[^>]*/>', replace_img, text)

# Also there might be a big abstract image for the Hero if it wasn't replaced with wireframes,
# But my previous script replaced ALL googleusercontent links to wireframes. So they all start with images/wireframe.

with open("neoscona.html", "w", encoding="utf-8") as f:
    f.write(text)

print(f"Replaced {svg_index} images with inline SVGs and unified background colors.")
