import re

with open("neoscona.html", "r", encoding="utf-8") as f:
    text = f.read()

svg_files = [
    "images/wir-1.svg",
    "images/wir-2.svg",
    "images/wir-3.svg",
    "images/wir-4.svg",
    "images/wir-5.svg"
]

svg_idx = 0
def replacer(match):
    global svg_idx
    original_svg = match.group(0)
    
    class_match = re.search(r'class="([^"]+)"', original_svg)
    img_class = class_match.group(1) if class_match else "w-full h-full"
    
    img_class = img_class.replace('text-primary', '').replace('opacity-60', '').strip()
    
    img_src = svg_files[svg_idx % len(svg_files)]
    svg_idx += 1
    return f'<img src="{img_src}" class="{img_class} object-contain mix-blend-screen opacity-90 hover:opacity-100 transition-opacity" />'

new_text = re.sub(r'<svg viewBox="0 0 100 100".*?</svg>', replacer, text, flags=re.DOTALL)

with open("neoscona.html", "w", encoding="utf-8") as f:
    f.write(new_text)

print(f"Replaced {svg_idx} inline SVGs with user provided SVG images.")
