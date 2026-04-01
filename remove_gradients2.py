with open('neoscona.html', 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('bg-grid-lines', '')
text = text.replace('bg-dots', '')
text = text.replace('radial-glow', '')
text = text.replace('<div class="absolute inset-0 bg-gradient-to-t from-primary/5 to-transparent"></div>', '')
text = text.replace('<div class="absolute inset-0 bg-gradient-to-t from-surface-dim via-transparent to-transparent"></div>', '')
text = text.replace('<div class="absolute inset-0 bg-gradient-to-t from-surface via-transparent to-transparent"></div>', '')
with open('neoscona.html', 'w', encoding='utf-8', newline='') as f:
    f.write(text)
print("done")
