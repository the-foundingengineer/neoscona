import os

html_path = "neoscona.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Accent color replacements (Blue -> Purple)
html = html.replace('"primary": "#003CD8"', '"primary": "#7C3AED"')
html = html.replace('"tertiary": "#003CD8"', '"tertiary": "#7C3AED"')
html = html.replace('"primary-container": "#102D7A"', '"primary-container": "#4C1D95"')
html = html.replace('text-[#c0c1ff]', 'text-[#d8b4fe]') 
html = html.replace('bg-[#c0c1ff]', 'bg-[#d8b4fe]')
html = html.replace('border-[#c0c1ff]', 'border-[#d8b4fe]')

# 2. SVGs creation (White and Purple alternatives)
for i in range(1, 6):
    svg_path = f"images/wir-{i}.svg"
    if os.path.exists(svg_path):
        with open(svg_path, "r", encoding="utf-8") as f:
            svg_data = f.read()
        
        # White version
        white_svg = svg_data.replace('#2E2C27', '#FFFFFF')
        with open(f"images/wir-{i}-white.svg", "w", encoding="utf-8") as f:
            f.write(white_svg)
            
        # Purple version
        purple_svg = svg_data.replace('#2E2C27', '#7C3AED')
        with open(f"images/wir-{i}-purple.svg", "w", encoding="utf-8") as f:
            f.write(purple_svg)

# 3. Apply White/Purple cards to the Capabilities Bento Grid

# Service 1 (md:col-span-8)
html = html.replace(
    '<div class="md:col-span-8 group relative overflow-hidden rounded-2xl bg-surface-container-high p-10 hover:bg-surface-container-highest transition-all">',
    '<div class="md:col-span-8 group relative overflow-hidden rounded-2xl bg-[#F1EFE8] text-[#1F1E1B] p-10 hover:shadow-[0_20px_50px_rgba(124,58,237,0.15)] transition-all">',
    1
)
html = html.replace('<h3 class="font-headline text-3xl font-bold text-on-surface mb-4">Web Platforms</h3>', '<h3 class="font-headline text-3xl font-bold text-[#1F1E1B] mb-4">Web Platforms</h3>')
html = html.replace('<p class="font-body text-on-surface-variant max-w-md">Building high-performance', '<p class="font-body text-[#3A3832] max-w-md">Building high-performance')
html = html.replace('<img src="images/wir-2.svg"', '<img src="images/wir-2-purple.svg"')

# Service 2 & 3 (md:col-span-4)
html = html.replace(
    '<div class="md:col-span-4 group relative overflow-hidden rounded-2xl bg-surface-container-low p-10 border border-outline-variant/10">',
    '<div class="md:col-span-4 group relative overflow-hidden rounded-2xl bg-[#7C3AED] text-[#F1EFE8] p-10 border-none shadow-[inset_0_0_40px_rgba(255,255,255,0.1)]">'
)
# For the small cards, we used bg-primary. By hardcoding #7C3AED it will match regardless.
html = html.replace('<h3 class="font-headline text-2xl font-bold text-on-surface mb-4">AI Engineering</h3>', '<h3 class="font-headline text-2xl font-bold text-[#F1EFE8] mb-4">AI Engineering</h3>')
html = html.replace('<p class="font-body text-sm text-on-surface-variant">Deploying LLMs', '<p class="font-body text-sm text-[#F1EFE8]/90">Deploying LLMs')
html = html.replace('<h3 class="font-headline text-2xl font-bold text-on-surface mb-4">Blockchain</h3>', '<h3 class="font-headline text-2xl font-bold text-[#F1EFE8] mb-4">Blockchain</h3>')
html = html.replace('<p class="font-body text-sm text-on-surface-variant">Smart contract', '<p class="font-body text-sm text-[#F1EFE8]/90">Smart contract')
html = html.replace('<span class="material-symbols-outlined text-primary text-5xl mb-8">memory</span>', '<span class="material-symbols-outlined text-[#F1EFE8] text-5xl mb-8">memory</span>')
html = html.replace('<span class="material-symbols-outlined text-primary text-5xl mb-8">currency_bitcoin</span>', '<span class="material-symbols-outlined text-[#F1EFE8] text-5xl mb-8">currency_bitcoin</span>')


# Service 4 (md:col-span-8)
old_s4 = '<div class="md:col-span-8 group relative overflow-hidden rounded-2xl bg-surface-container-high p-10 hover:bg-surface-container-highest transition-all">\n<div class="flex flex-col md:flex-row gap-10 items-center">\n<div class="flex-1">\n<span class="material-symbols-outlined text-primary text-5xl mb-8">auto_awesome_motion</span>\n<h3 class="font-headline text-3xl font-bold text-on-surface mb-4">UI/UX Engineering</h3>\n<p class="font-body text-on-surface-variant">Crafting immersive digital'
new_s4 = '<div class="md:col-span-8 group relative overflow-hidden rounded-2xl bg-[#F1EFE8] text-[#1F1E1B] p-10 hover:shadow-[0_20px_50px_rgba(124,58,237,0.15)] transition-all">\n<div class="flex flex-col md:flex-row gap-10 items-center">\n<div class="flex-1">\n<span class="material-symbols-outlined text-primary text-5xl mb-8">auto_awesome_motion</span>\n<h3 class="font-headline text-3xl font-bold text-[#1F1E1B] mb-4">UI/UX Engineering</h3>\n<p class="font-body text-[#3A3832]">Crafting immersive digital'

html = html.replace(old_s4, new_s4)

# Replace remaining images globally
html = html.replace('<img src="images/wir-3.svg"', '<img src="images/wir-3-white.svg"')
html = html.replace('<img src="images/wir-4.svg"', '<img src="images/wir-4-white.svg"')
html = html.replace('<img src="images/wir-5.svg"', '<img src="images/wir-5-white.svg"')
html = html.replace('<img src="images/wir-1.svg"', '<img src="images/wir-1-purple.svg"')

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Bento grid and accents updated successfully!")
