import os
from bs4 import BeautifulSoup
import re

with open("neoscona.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# 1. HERO SECTION
h1 = soup.find('h1', class_=lambda c: c and 'hero-gradient-text' in c)
if h1:
    h1.string = "Build Scalable Web2 & Web3 Products — Without the Guesswork"

p_hero = soup.find('p', class_=lambda c: c and 'text-lg md:text-xl text-on-surface-variant' in c)
if p_hero:
    p_hero.string = "We partner with startups and businesses to design, develop, and launch high-performance web applications, mobile apps, and blockchain products — from MVP to scale."

buttons = soup.find_all('button')
for btn in buttons:
    if "View Our Work" in btn.text:
        btn.string = "Book a Call"

# 2. HERO SPLIT (ABOUT)
h1_split = soup.find('h1', text=re.compile(r'Trust is the\s*bottleneck', re.I))
# the h1 contains a span for the red text
for split_header in soup.find_all('h1'):
    if 'Trust is the' in split_header.text:
        split_header.clear()
        split_header.append("About ")
        new_span = soup.new_tag("span")
        new_span['class'] = "text-primary-fixed-dim"
        new_span.string = "Us."
        split_header.append(new_span)
        
        # Also update the P tag next to it
        p_about = split_header.find_next_sibling('p')
        if p_about:
            p_about.string = "We are a product engineering studio focused on building modern digital products across Web2 and Web3. Our goal is simple — help founders and businesses turn ideas into scalable, high-quality products. We combine engineering, product thinking, and blockchain expertise to deliver solutions that are not only functional, but built to last."
        
        # Update the small label above it
        div_label = split_header.find_previous_sibling('div')
        if div_label and div_label.find('span'):
            div_label.find('span', class_=lambda c: 'font-label' in c).string = "ORGANIZATION"

# 3. BENEFITS -> PORTFOLIO
benefits_h3 = soup.find_all('h3')
benefit_idx = 0
portfolio_data = [
    {
        "title": "SaaS Analytics Platform",
        "desc": "Designed and developed a scalable dashboard platform handling real-time data visualization and user management.",
        "icon": "dashboard"
    },
    {
        "title": "NFT Minting Platform",
        "desc": "Built a secure, high-performance minting platform with wallet integration and smart contract deployment.",
        "icon": "account_balance_wallet"
    },
    {
        "title": "Startup MVP",
        "desc": "Took a startup from idea to launch with a full-stack application and mobile-ready experience.",
        "icon": "rocket_launch"
    }
]

for h3 in benefits_h3:
    if h3.text in ["Private Data", "Verifiable Execution", "Programmable Policies"]:
        h3.string = portfolio_data[benefit_idx]["title"]
        p = h3.find_next_sibling('p')
        if p:
            p.string = portfolio_data[benefit_idx]["desc"]
        
        icon = h3.find_previous_sibling('div').find('span', class_='material-symbols-outlined')
        if icon:
            icon.string = portfolio_data[benefit_idx]["icon"]
        benefit_idx += 1

# 4. CORE ENGINEERING -> PROCESS
core_h2 = soup.find('h2', text=re.compile(r'Core Engineering Services', re.I))
if core_h2:
    core_h2.string = "How We Work (Process)"

process_data = [
    ("Discovery & Strategy", "We understand your idea, users, and business goals — then define a clear product roadmap.", "explore"),
    ("Product Design", "We design intuitive, high-performance user experiences and interfaces.", "design_services"),
    ("Development", "Our engineers build scalable, secure systems using modern technologies.", "code"),
    ("Testing & Security", "We rigorously test everything — including smart contract security where applicable.", "bug_report"),
    ("Launch & Scale", "We deploy, monitor, and help you scale your product post-launch.", "flight_takeoff")
]

core_h3 = soup.find_all('h3')
proc_idx = 0
for h3 in core_h3:
    if h3.text in ["Web Platforms", "Blockchain", "AI & Automation", "UI/UX Engineering", "Infrastructure"]:
        if proc_idx < 5:
            h3.string = f"{proc_idx+1}. {process_data[proc_idx][0]}"
            p = h3.find_next_sibling('p')
            if p:
                p.string = process_data[proc_idx][1]
            icon = h3.find_previous_sibling('span', class_='material-symbols-outlined')
            if icon:
                icon.string = process_data[proc_idx][2]
                icon['data-icon'] = process_data[proc_idx][2]
            proc_idx += 1

# 5. STRATEGIC USE CASES -> WHY CHOOSE US
usecase_h2 = soup.find('h2', text=re.compile(r'Strategic Use Cases', re.I))
if usecase_h2:
    usecase_h2.string = "Why Work With Us"

why_data = [
    ("Web2 + Web3 Expertise", "Seamlessly combine traditional software with blockchain infrastructure.", "diversity_3"),
    ("Startup-Focused", "We understand speed, iteration, and building under uncertainty.", "speed"),
    ("Security-First", "Especially critical for smart contracts and blockchain systems.", "verified_user"),
    ("Fast & Scalable", "We build MVPs quickly — and architect for long-term growth.", "trending_up"),
    ("Clear Communication", "No black box. You always know what’s happening and why.", "forum")
]

why_h4 = soup.find_all('h4')
why_idx = 0
for h4 in why_h4:
    if h4.text in ["Digital Identity", "Tokenized Assets", "Private DeFi", "Trustless Agents", "Verified Payments"]:
        if why_idx < 5:
            h4.string = why_data[why_idx][0]
            p = h4.find_next_sibling('p')
            if p:
                p.string = why_data[why_idx][1]
            icon = h4.find_previous_sibling('div').find('span', class_='material-symbols-outlined')
            if icon:
                icon.string = why_data[why_idx][2]
            why_idx += 1

# 6. CAPABILITIES (BENTO) -> SERVICES
cap_h2 = soup.find('h2', text=re.compile(r'Precision instruments for digital dominance', re.I))
if cap_h2:
    cap_h2.string = "We build end-to-end digital products"

cap_p = soup.find('p', text=re.compile(r'A multi-disciplinary approach.*'))
if cap_p:
    cap_p.string = "Combining modern software engineering with blockchain expertise."

bento_h3 = soup.find_all('h3')
for h3 in bento_h3:
    if h3.text == "Web Platforms":
        h3.string = "Web2 Development"
        p = h3.find_next_sibling('p')
        if p:
            p.string = "• Full-stack web application development\n• Mobile app development (iOS & Android)\n• SaaS product development\n• Backend & API architecture\n• Internal tools"
    elif h3.text == "Blockchain":
        h3.string = "Web3 Development"
        p = h3.find_next_sibling('p')
        if p:
            p.string = "• Smart contract development (secure, scalable)\n• Smart contract auditing (security-first approach)\n• Token creation (ERC-20, ERC-721)\n• NFT platforms & minting\n• dApp & wallet integrations"

# 7. JOURNAL & INSIGHTS -> SOCIAL PROOF
jour_h2 = soup.find('h2', text=re.compile(r'Journal.*Archive', re.I))
if jour_h2:
    jour_h2.string = "Built with a Product Mindset"

proof_data = [
    ("Track Record", "Multiple products successfully designed and developed from scratch."),
    ("Ecosystem Mastery", "Deep experience launching projects across both Web2 and Web3 ecosystems."),
    ("Built to Scale", "Unrelenting focus on performance, usability, and long-term scalability.")
]

proof_h4 = soup.find_all('h4')
proof_idx = 0
for h4 in proof_h4:
    if "Zero-Knowledge" in h4.text or "Post-Quantum" in h4.text or "Neural" in h4.text:
        if proof_idx < 3:
            h4.string = proof_data[proof_idx][0]
            p = h4.find_next_sibling('p')
            if p:
                p.string = proof_data[proof_idx][1]
            proof_idx += 1

# 8. FINAL CTA
cta_h2 = soup.find('h2', text=re.compile(r'Let’s Build Something', re.I))
if cta_h2:
    cta_h2.clear()
    cta_h2.append("Let's Build Something ")
    span = soup.new_tag("span")
    span['class'] = "text-primary italic"
    span.string = "That Matters."
    cta_h2.append(span)

cta_p = soup.find('p', text=re.compile(r'Ready to transform your technical vision.*'))
if cta_p:
    cta_p.string = "Whether you're starting from an idea or scaling an existing product, we can help you move faster and build smarter. Book a call to discuss your project, timeline, and next steps."

with open("neoscona.html", "w", encoding="utf-8") as f:
    f.write(str(soup))

print("Injected new copy successfully!")
