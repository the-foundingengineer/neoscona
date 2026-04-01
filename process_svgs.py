import os
import glob
import re

svg_dir = r"c:\Users\ZBOOK STUDIO G5\Documents\dev\neoscona\images"
files = glob.glob(os.path.join(svg_dir, "wir-*.svg"))

# We use the previous surface-container background color #2E2C27 for a subtle line effect against the #1F1E1B background
LINE_COLOR = "#2E2C27"

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove background layer exported from Illustrator
    content = re.sub(r'<g\s+id="background".*?</g>', '', content, flags=re.DOTALL|re.IGNORECASE)
    
    # Remove gradients to save space
    content = re.sub(r'<linearGradient.*?</linearGradient>', '', content, flags=re.DOTALL|re.IGNORECASE)
    content = re.sub(r'<radialGradient.*?</radialGradient>', '', content, flags=re.DOTALL|re.IGNORECASE)

    # Replace inline gradient fills/strokes
    content = re.sub(r'style="fill:url\([^)]+\);?"', f'fill="{LINE_COLOR}"', content)
    content = re.sub(r'fill="url\([^)]+\)"', f'fill="{LINE_COLOR}"', content)
    
    content = re.sub(r'style="stroke:url\([^)]+\);?"', f'stroke="{LINE_COLOR}"', content)
    content = re.sub(r'stroke="url\([^)]+\)"', f'stroke="{LINE_COLOR}"', content)
    
    # Replace solid colors (except 'none')
    content = re.sub(r'style="fill:#[0-9a-fA-F]{3,6};?"', f'fill="{LINE_COLOR}"', content)
    content = re.sub(r'fill="#[0-9a-fA-F]{3,6}"', f'fill="{LINE_COLOR}"', content)
    
    content = re.sub(r'style="stroke:#[0-9a-fA-F]{3,6};?"', f'stroke="{LINE_COLOR}"', content)
    content = re.sub(r'stroke="#[0-9a-fA-F]{3,6}"', f'stroke="{LINE_COLOR}"', content)
    
    # In case there are CSS classes defined in a <style> block
    content = re.sub(r'fill:\s*url\([^)]+\);?', f'fill:{LINE_COLOR};', content)
    content = re.sub(r'stroke:\s*url\([^)]+\);?', f'stroke:{LINE_COLOR};', content)
    content = re.sub(r'fill:\s*#[0-9a-fA-F]{3,6};?', f'fill:{LINE_COLOR};', content)
    content = re.sub(r'stroke:\s*#[0-9a-fA-F]{3,6};?', f'stroke:{LINE_COLOR};', content)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Processed {len(files)} SVG files.")
