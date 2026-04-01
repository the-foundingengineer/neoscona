import re
import os
import shutil
import random

project_dir = r'c:\Users\ZBOOK STUDIO G5\Documents\dev\neoscona'
html_file = os.path.join(project_dir, 'neoscona.html')
images_dir = os.path.join(project_dir, 'images')

if not os.path.exists(images_dir):
    os.makedirs(images_dir)

# List of generated images
source_images = [
    r'C:\Users\ZBOOK STUDIO G5\.gemini\antigravity\brain\e03e45d1-95c9-4392-b966-025d17649f75\oasis_wireframe_1_1775002664594.png',
    r'C:\Users\ZBOOK STUDIO G5\.gemini\antigravity\brain\e03e45d1-95c9-4392-b966-025d17649f75\oasis_wireframe_cube_1775002699190.png',
    r'C:\Users\ZBOOK STUDIO G5\.gemini\antigravity\brain\e03e45d1-95c9-4392-b966-025d17649f75\oasis_wireframe_loop_1775002711248.png',
    r'C:\Users\ZBOOK STUDIO G5\.gemini\antigravity\brain\e03e45d1-95c9-4392-b966-025d17649f75\oasis_wireframe_pyramid_1775002737385.png'
]

dest_images = []
for idx, src in enumerate(source_images):
    dest_name = f'wireframe_{idx}.png'
    dest_path = os.path.join(images_dir, dest_name)
    shutil.copy2(src, dest_path)
    dest_images.append(f'images/{dest_name}')

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace colors
new_colors = """colors: {
              "surface-dim": "#1F1E1B",
              "surface": "#1F1E1B",
              "background": "#1F1E1B",
              "surface-container-low": "#2E2C27",
              "surface-container": "#2E2C27",
              "surface-container-high": "#3A3832",
              "surface-container-highest": "#403D37",
              "on-surface": "#F1EFE8",
              "on-surface-variant": "#888681",
              "primary": "#003CD8",
              "on-primary": "#F1EFE8",
              "primary-container": "#102D7A",
              "outline": "#464555",
              "outline-variant": "#3A3832",
              "secondary": "#888681",
              "tertiary": "#003CD8"
            }"""
content = re.sub(r'colors:\s*\{[^}]+\}', new_colors, content)

# Fonts
content = re.sub(r'"headline":\s*\["[^"]+"\]', '"headline": ["Inter"]', content)
content = re.sub(r'"body":\s*\["[^"]+"\]', '"body": ["Inter"]', content)
content = re.sub(r'"label":\s*\["[^"]+"\]', '"label": ["Inter"]', content)

# Fix fonts import string in head (all templates)
# <link href="https://fonts.googleapis.com/css2?..." rel="stylesheet">
content = re.sub(r'<link href="https://fonts\.googleapis\.com/css2\?[^"]+" rel="stylesheet"/?>', '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>', content)


# Gradients and rounded corners
content = content.replace('bg-gradient-to-br from-primary to-primary-container', 'bg-primary hover:bg-primary-container')
content = content.replace('primary-gradient', 'bg-primary hover:bg-primary-container')
content = content.replace('rounded-xl', 'rounded-2xl')

# Images substitution function
def image_replacer(match):
    return f'src="{random.choice(dest_images)}"'

# Replace all <img src="..."> that start with https://lh3.googleusercontent.com
content = re.sub(r'src="https://lh3\.googleusercontent\.com[^"]+"', image_replacer, content)

# To ensure images look like wireframes on #1F1E1B, remove grayscale/opacity overrides from images if any, 
# The wireframes are already dark with thin blue lines
content = content.replace('grayscale opacity-60 group-hover:grayscale-0', 'opacity-90 group-hover:opacity-100')
content = content.replace('grayscale opacity-40 group-hover:grayscale-0', 'opacity-80 group-hover:opacity-100')
content = content.replace('mix-blend-luminosity', 'mix-blend-screen')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Updated {html_file} successfully. Replaced colors, fonts, and copied local vector images!")
