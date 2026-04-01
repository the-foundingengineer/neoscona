import re

def build_blog():
    with open('neoscona.html', 'r', encoding='utf-8') as f:
        neo = f.read()

    # Extract sections from neoscona.html
    # 1. Everything up to the closing `</style>` tag
    style_end_idx = neo.find('</style>')
    head_css = neo[:style_end_idx]

    # Additional Blog specific CSS
    blog_css = """
    /* ─── BLOG PAGE SPECIFIC ────────────────────────────────────────────────────── */
    .nd-blog-hero { padding: 9rem 2rem 3rem; }
    .nd-featured-post {
      display: grid; grid-template-columns: 1fr 1fr;
      background: var(--bg-input); border: 1px solid var(--border);
      border-radius: 12px; overflow: hidden; margin-bottom: 5rem;
      transition: border-color 0.2s;
    }
    .nd-featured-post:hover { border-color: var(--primary); }
    .nd-featured-visual {
      border-right: 1px solid var(--border);
      background: var(--bg); display: flex; align-items: center; justify-content: center;
      padding: 3rem;
    }
    .nd-featured-visual img { width: 100%; height: 100%; object-fit: contain; opacity: 0.85; max-height: 400px; }
    .nd-featured-text { padding: 4rem 3.5rem; display: flex; flex-direction: column; justify-content: center; }
    .nd-featured-text h2 { font-size: clamp(1.8rem, 3.5vw, 2.5rem); margin-bottom: 1.25rem; line-height: 1.15; }
    .nd-featured-text p { font-size: 1.05rem; color: var(--copy-75); margin-bottom: 2rem; line-height: 1.7; }

    .nd-blog-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(330px, 1fr)); gap: 1.5rem; margin-bottom: 5rem;}
    .nd-blog-grid .nd-card { min-width: auto; scroll-snap-align: unset; }

    @media (max-width: 900px) {
      .nd-featured-post { grid-template-columns: 1fr; }
      .nd-featured-visual { border-right: none; border-bottom: 1px solid var(--border); padding: 2rem; }
      .nd-featured-text { padding: 3rem 2rem; }
    }
"""
    head_end = neo[style_end_idx: neo.find('<!-- ─── HERO')]
    # We want up to the <div class="nd-page-wrapper">
    page_wrapper_match = re.search(r'<div class="nd-page-wrapper">', neo)
    header_nav_wrapper = neo[style_end_idx:page_wrapper_match.end()]

    # Extract CTA and Footer
    cta_footer_start = neo.find('<!-- ─── CTA ───')
    cta_footer = neo[cta_footer_start:]

    # Blog content
    blog_content = """
  <!-- ─── BLOG PAGE CONTENT ────────────────────────────────────────────────── -->
  <section class="nd-blog-hero nd-container" id="blog-top">
    <div class="nd-section-head">
      <div class="nd-tag">Latest Updates</div>
      <h1><span class="nd-primary-accent">Logbook.</span> Insights &amp; News.</h1>
      <p>Dive into our engineering process, architectural decisions, and the future of scalable Web2 &amp; Web3 applications.</p>
    </div>

    <!-- FEATURED POST -->
    <a href="#" class="nd-featured-post">
      <div class="nd-featured-visual">
        <img src="images/wir-3-purple.svg" alt="Featured Visual" />
      </div>
      <div class="nd-featured-text">
        <div class="nd-card-meta">
          <span class="nd-card-label" style="color:var(--heading)">Featured Insight</span>
          <span class="nd-card-date">Mar 30, 2026</span>
        </div>
        <h2>Midas: Funding the Future of Onchain Finance</h2>
        <p>Oasis participates in Midas's Series A, backing the infrastructure bringing institutional assets onchain. Built with strict performance margins and security-first scaling.</p>
        <div class="nd-card-link">Read Full Article <span class="material-symbols-outlined" style="font-size:0.9rem">trending_flat</span></div>
      </div>
    </a>

    <hr class="nd-hr" style="margin-bottom: 4rem;">

    <div class="nd-section-head-split">
      <h2 class="nd-h2">Recent Posts</h2>
    </div>

    <!-- GRID OF POSTS -->
    <div class="nd-blog-grid">
      <a href="#" class="nd-card" style="display:block">
        <div class="nd-card-thumb" style="background:var(--bg); padding: 2.5rem;"><img src="images/wir-1-purple.svg" alt=""/></div>
        <div class="nd-card-body">
          <div class="nd-card-meta">
            <span class="nd-card-label" style="color:var(--heading)">Tutorial</span>
            <span class="nd-card-date">Mar 2, 2026</span>
          </div>
          <h4 style="margin-bottom:0.75rem; line-height:1.4">Vibe Code With Oasis</h4>
          <p>Dive into new tools and learn how to build verifiable AI-driven flows inside robust environments.</p>
          <div class="nd-card-link" style="margin-bottom:0;">Read Article <span class="material-symbols-outlined" style="font-size:0.9rem">trending_flat</span></div>
        </div>
      </a>

      <a href="#" class="nd-card" style="display:block">
        <div class="nd-card-thumb" style="background:var(--bg); padding: 2.5rem;"><img src="images/wir-2-purple.svg" alt=""/></div>
        <div class="nd-card-body">
          <div class="nd-card-meta">
            <span class="nd-card-label" style="color:var(--heading)">Architecture</span>
            <span class="nd-card-date">Jan 13, 2026</span>
          </div>
          <h4 style="margin-bottom:0.75rem; line-height:1.4">Attestation Is Not Enough</h4>
          <p>Exploring the nuances of remote attestation and what's required to make them genuinely useful within trust systems.</p>
          <div class="nd-card-link" style="margin-bottom:0;">Read Article <span class="material-symbols-outlined" style="font-size:0.9rem">trending_flat</span></div>
        </div>
      </a>

      <a href="#" class="nd-card" style="display:block">
        <div class="nd-card-thumb" style="background:var(--bg); padding: 2.5rem;"><img src="images/wir-1-purple.svg" alt="" style="transform: scaleX(-1)"/></div>
        <div class="nd-card-body">
          <div class="nd-card-meta">
            <span class="nd-card-label" style="color:var(--heading)">Case Study</span>
            <span class="nd-card-date">Dec 17, 2025</span>
          </div>
          <h4 style="margin-bottom:0.75rem; line-height:1.4">Verifiable Compute on Prop Trading</h4>
          <p>Integrating cryptographic attestation to verify high-frequency order execution and automated trader evaluation.</p>
          <div class="nd-card-link" style="margin-bottom:0;">Read Article <span class="material-symbols-outlined" style="font-size:0.9rem">trending_flat</span></div>
        </div>
      </a>

      <a href="#" class="nd-card" style="display:block">
        <div class="nd-card-thumb" style="background:var(--bg); padding: 2.5rem;"><img src="images/wir-3-purple.svg" alt="" style="transform: scaleX(-1)"/></div>
        <div class="nd-card-body">
          <div class="nd-card-meta">
            <span class="nd-card-label" style="color:var(--heading)">Web3 Standard</span>
            <span class="nd-card-date">Nov 10, 2025</span>
          </div>
          <h4 style="margin-bottom:0.75rem; line-height:1.4">x402: Internet-Native Payment Standard</h4>
          <p>Unlocking native micropayments and fueling the rise of an agentic economy natively within the browser stack.</p>
          <div class="nd-card-link" style="margin-bottom:0;">Read Article <span class="material-symbols-outlined" style="font-size:0.9rem">trending_flat</span></div>
        </div>
      </a>

      <a href="#" class="nd-card" style="display:block">
        <div class="nd-card-thumb" style="background:var(--bg); padding: 2.5rem;"><img src="images/wir-2-purple.svg" alt="" style="transform: scaleY(-1)"/></div>
        <div class="nd-card-body">
          <div class="nd-card-meta">
            <span class="nd-card-label" style="color:var(--heading)">R&amp;D</span>
            <span class="nd-card-date">Oct 9, 2025</span>
          </div>
          <h4 style="margin-bottom:0.75rem; line-height:1.4">ERC-8004: Trustless Agents</h4>
          <p>Proposed standards enabling autonomous models and applications to discover and transact completely trustlessly.</p>
          <div class="nd-card-link" style="margin-bottom:0;">Read Article <span class="material-symbols-outlined" style="font-size:0.9rem">trending_flat</span></div>
        </div>
      </a>

      <a href="#" class="nd-card" style="display:block">
        <div class="nd-card-thumb" style="background:var(--bg); padding: 2.5rem;"><img src="images/wir-1-purple.svg" alt="" style="transform: scaleY(-1)"/></div>
        <div class="nd-card-body">
          <div class="nd-card-meta">
            <span class="nd-card-label" style="color:var(--heading)">DevOps</span>
            <span class="nd-card-date">Oct 29, 2025</span>
          </div>
          <h4 style="margin-bottom:0.75rem; line-height:1.4">Proxy Support for Frontend Hosting</h4>
          <p>Automating robust frontend hosting, self-renewing TLS certificates, and custom domains inside strictly enforced TEEs.</p>
          <div class="nd-card-link" style="margin-bottom:0;">Read Article <span class="material-symbols-outlined" style="font-size:0.9rem">trending_flat</span></div>
        </div>
      </a>
    </div>
  </section>

  <hr class="nd-hr">
"""

    with open('oasis-blog.html', 'w', encoding='utf-8') as fout:
        fout.write(head_css + blog_css + header_nav_wrapper + blog_content + '\n\n' + cta_footer)

if __name__ == '__main__':
    build_blog()
