import re

with open("neoscona.html", "r", encoding="utf-8") as f:
    text = f.read()

# Separate the templates
templates = text.split("<!-- Neoscona")
# templates[0] is empty. 1=Insight, 2=Official, 3=Trust, 4=Services, 5=Home Hero

print(f"Found {len(templates)-1} templates.")

# We want: 
# Head from T1 (they are all identical)
head_match = re.search(r'<head>.*?</head>', templates[1], re.DOTALL)
head = head_match.group(0) if head_match else "<head></head>"

# Nav from T5 (Official Landing Page has a better nav? Let's use T2's Nav which has Start a Project inside a proper <nav>)
nav_match = re.search(r'<nav.*?</nav>', templates[2], re.DOTALL)
nav = nav_match.group(0) if nav_match else ""

# Footer from T2
footer_match = re.search(r'<footer.*?</footer>', templates[2], re.DOTALL)
footer = footer_match.group(0) if footer_match else ""

# Now extract sections.
# We want: 
# 1. T5 Hero: <section ... min-h-screen ...>
hero_match = re.search(r'<section[^>]*min-h-screen.*?</section>', templates[5], re.DOTALL)
hero = hero_match.group(0) if hero_match else ""

# 2. T3 Trust/Benefits (lines with Architectural Crisis)
# T3 contains exactly <main> ... </main> which wraps the sections we want
t3_main = re.search(r'<main[^>]*>(.*?)</main>', templates[3], re.DOTALL)
crisis_benefits = t3_main.group(1) if t3_main else ""

# 3. T4 System Architecture (Header + Core + Use Cases)
t4_main = re.search(r'<main[^>]*>(.*?)</main>', templates[4], re.DOTALL)
sys_arch = t4_main.group(1) if t4_main else ""

# 4. T2 Capabilities Bento Grid, Insights, CTA
# T2 has <section> tags. The first is Hero, second is Trust, third is Capabilities, fourth is Insights/Newsletter, fifth is CTA
t2_sections = re.findall(r'<section.*?</section>', templates[2], re.DOTALL)
capabilities = t2_sections[2] if len(t2_sections) > 2 else ""
insights = t2_sections[3] if len(t2_sections) > 3 else ""
cta = t2_sections[4] if len(t2_sections) > 4 else ""

unified = f"""<!DOCTYPE html>
<html class="dark" lang="en">
{head}
<body class="bg-surface text-on-surface font-body selection:bg-primary/30 selection:text-primary">
{nav}

<main class="relative z-10 pt-32 pb-20">
<!-- Hero -->
{hero}

<!-- Trust & Benefits -->
{crisis_benefits}

<!-- System Architecture -->
{sys_arch}

<!-- Capabilities -->
{capabilities}

<!-- Journal & Insights -->
{insights}

<!-- Final CTA -->
{cta}
</main>

{footer}
</body>
</html>
"""

with open("neoscona.html", "w", encoding="utf-8") as f:
    f.write(unified)

print("Unified HTML written, length:", len(unified))
print("DOCTYPE count:", unified.count("DOCTYPE"))
print("FOOTER count:", unified.count("<footer"))
