import re

with open('emerald-clinical.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. SUMMARY
content = content.replace('<span class="ec-divider-label">OVERVIEW</span>', '<span class="ec-divider-label">SUMMARY</span>')
content = content.replace('<p>Emerald Clinical is a clinical research organisation dedicated to bridging the gap between patients and life-changing therapies. They needed a visual identity that felt credible, human, and forward-looking — without falling into the sterile clichés of the medical industry.</p>\n                    <p>The challenge was to craft something that could live comfortably in both a hospital corridor and a digital product — a brand that communicates scientific rigour while remaining warm and accessible.</p>', '<p><span class="text-green">Emerald Clinical</span> Trials were launching a new brand direction and needed a visual system to support it across all channels.</p>\n                    <p class="ec-caption-text">A fast-paced project focused on clarity, trust and long-term scalability.</p>')

# 2. THE BRIEF
brief_old = '''<p>[Paste business goals copy here.]</p>
                </div>
                <div class="ec-col-right">
                    <span class="ec-green-label">PROBLEM</span>
                    <p>[Paste problem statement copy here.]</p>'''
brief_new = '''<p>Establish Emerald Clinical Trials as a credible and recognizable healthcare brand.</p>
                    <p>Build trust through a clear and consistent visual identity across all channels.</p>
                </div>
                <div class="ec-col-right">
                    <span class="ec-green-label">PROBLEM</span>
                    <p>The existing identity lacked consistency and differentiation, resulting in low brand recall.</p>
                    <p>Disconnected visual applications weakened trust across digital and print touch points.</p>'''
content = content.replace(brief_old, brief_new)

# 3. 01 DISCOVERY
disc_old = '''<div class="ec-divider ec-divider--split">
                <span class="ec-divider-label">BRAND DISCOVERY</span>
                <span class="ec-divider-label ec-divider-label--right">RESEARCH & METHODS</span>
            </div>
            <p class="ec-intro-paragraph">Initial discovery focused on understanding brand perception, visual gaps, and the competitive landscape — without over-complicating the process.</p>
            <div class="ec-subsection-label">
                <span class="ec-green-label">METHODS USED</span>
                <p>[List methods here.]</p>
            </div>'''
disc_new = '''<div class="ec-divider ec-divider--split">
                <span class="ec-divider-label">DESIGN APPROACH</span>
                <span class="ec-divider-label ec-divider-label--right text-green">01 DISCOVERY</span>
            </div>
            <p class="ec-intro-paragraph">Initial discovery focused on understanding brand perception, visual gaps and the competitive landscape, without over complicating the process.</p>
            <div class="ec-subsection-label">
                <span class="ec-green-label" style="font-size: 1.2rem;">METHODS USED</span>
                <p>Focused on speed and clarity rather than exhaustive documentation.</p>
                <p style="margin-top: 0.5rem;">Customer journey &nbsp;&middot;&nbsp; Market research analysis &nbsp;&middot;&nbsp; Persona &nbsp;&middot;&nbsp; Prototype testing</p>
            </div>'''
content = content.replace(disc_old, disc_new)

# 4. 02 RESEARCH & INSIGHTS
res_old = '''<div class="ec-divider">
                <span class="ec-divider-label">KEY INSIGHTS</span>
            </div>
            <p class="ec-intro-paragraph ec-intro-paragraph--large">Research revealed low brand recall, visual inconsistency, and a gap between clinical credibility and human connection.</p>
            <div class="ec-stats-row">
                <div class="ec-stat-block">
                    <span class="ec-stat-number">42%</span>
                    <span class="ec-stat-caption">[Caption for first stat]</span>
                </div>
                <div class="ec-stat-block">
                    <span class="ec-stat-number">65%</span>
                    <span class="ec-stat-caption">[Caption for second stat]</span>
                </div>
                <div class="ec-stat-block">
                    <span class="ec-stat-number">54%</span>
                    <span class="ec-stat-caption">[Caption for third stat]</span>
                </div>
            </div>'''
res_new = '''<div class="ec-divider ec-divider--split">
                <span class="ec-divider-label">DESIGN APPROACH</span>
                <span class="ec-divider-label ec-divider-label--right text-green">02 RESEARCH & INSIGHTS</span>
            </div>
            <p class="ec-intro-paragraph ec-intro-paragraph--large">Research revealed low brand recall, visual inconsistency and a gap between clinical credibility and human connection.</p>
            <div class="ec-stats-row">
                <div class="ec-stat-block">
                    <span class="ec-stat-number">42%</span>
                    <span class="ec-stat-caption">Couldn’t recall the brand after 24h</span>
                </div>
                <div class="ec-stat-block">
                    <span class="ec-stat-number">65%</span>
                    <span class="ec-stat-caption">Visual inconsistency across assets</span>
                </div>
                <div class="ec-stat-block">
                    <span class="ec-stat-number">54%</span>
                    <span class="ec-stat-caption">Described the brand as “cold” or “too corporate”</span>
                </div>
            </div>'''
content = content.replace(res_old, res_new)

# 5. 03 STRATEGY
strat_old = '''<div class="ec-divider">
                <span class="ec-divider-label">STRATEGY</span>
            </div>
            <p class="ec-intro-paragraph ec-intro-paragraph--large">The strategy focused on building a visual system that balances scientific precision with warmth and accessibility.</p>
            <div class="ec-pillars">
                <span class="ec-green-label">THREE STRATEGIC PILLARS</span>
                <ul class="ec-pillar-list ec-pillar-list--row">
                    <li><strong>TRUST</strong> — [pillar copy]</li>
                    <li><strong>CLARITY</strong> — [pillar copy]</li>
                    <li><strong>HUMAN APPROACH</strong> — [pillar copy]</li>
                </ul>
            </div>'''
strat_new = '''<div class="ec-divider ec-divider--split">
                <span class="ec-divider-label">DESIGN APPROACH</span>
                <span class="ec-divider-label ec-divider-label--right text-green">03 STRATEGY & DIRECTION</span>
            </div>
            <p class="ec-intro-paragraph ec-intro-paragraph--large">The strategy focused on building a visual system that balances scientific precision with warmth and accessibility.</p>
            <p class="ec-caption-text ec-caption-text--top" style="margin-top:-1rem; margin-bottom: 3rem;">The goal wasn’t to redesign for aesthetics, but to reshape how the brand feels at first contact.</p>
            <div class="ec-pillars">
                <span class="text-green" style="display: block; font-size: 1rem; font-weight: 600; margin-bottom: 1rem;">Three strategic pillars guided every design decision</span>
                <ul class="ec-pillar-list ec-pillar-list--row">
                    <li><strong>TRUST</strong> &nbsp;&middot;&nbsp; Clear hierarchy and professional tone.</li>
                    <li><strong>CLARITY</strong> &nbsp;&middot;&nbsp; Simplified visuals and strong contrast.</li>
                    <li><strong>HUMAN APPROACH</strong> &nbsp;&middot;&nbsp; Warmth, empathy and real people.</li>
                </ul>
            </div>'''
content = content.replace(strat_old, strat_new)

# 6. 04 CONCEPT DEVELOPMENT
concept_old = '''<div class="ec-divider">
                <span class="ec-divider-label">CONCEPT EXPLORATION</span>
            </div>
            <p class="ec-intro-paragraph ec-intro-paragraph--large">The new concept was inspired by the Emerald structure — clarity, precision, and value.</p>
            <div class="ec-image-pair">
                <div class="ec-placeholder ec-placeholder--concept">
                    <span>Concept board 1</span>
                </div>
                <div class="ec-placeholder ec-placeholder--concept">
                    <span>Concept board 2</span>
                </div>
            </div>
            <p class="ec-caption-text">[Description of how concepts were tested and refined.]</p>'''
concept_new = '''<div class="ec-divider ec-divider--split">
                <span class="ec-divider-label">DESIGN APPROACH</span>
                <span class="ec-divider-label ec-divider-label--right text-green">04 CONCEPT DEVELOPMENT</span>
            </div>
            <p class="ec-intro-paragraph ec-intro-paragraph--large">The core concept was inspired by the Emerald structure: clarity, precision and value.</p>
            <div class="ec-image-pair">
                <div class="ec-placeholder ec-placeholder--concept">
                    <span>Concept board 1</span>
                </div>
                <div class="ec-placeholder ec-placeholder--concept">
                    <span>Concept board 2</span>
                </div>
            </div>
            <div style="margin-top: 3rem;">
                <p class="ec-intro-paragraph">The core concept was inspired by the Emerald structure, balancing transparency, precision and care.<br>
                The previous logo lacked recognisability and felt cold and outdated, which raised concerns for the client.</p>
                <div class="ec-two-col ec-two-col--brief" style="gap: 3rem; margin-top: 2rem;">
                    <div class="ec-col-left">
                        <p>During early exploration, the brand tested different names, visual languages and colour directions. Instead of committing to a final look too early, the logo development focused on structure and meaning.</p>
                    </div>
                    <div class="ec-col-right">
                        <p>The final mark uses a modular grid that subtly forms both an “E” and a cross, referencing Emerald while signalling healthcare, care and clinical trust. This kept the identity flexible without losing recognisability.</p>
                    </div>
                </div>
            </div>'''
content = content.replace(concept_old, concept_new)

# 7. 05 BRAND SYSTEM DESIGN
brand_sys_old = '''<div class="ec-divider ec-divider--split">
                    <span class="ec-divider-label">COLOR SYSTEM</span>
                    <span class="ec-divider-label ec-divider-label--right">VISUAL IDENTITY</span>
                </div>'''
brand_sys_new = '''<div class="ec-divider ec-divider--split">
                    <span class="ec-divider-label">DESIGN APPROACH</span>
                    <span class="ec-divider-label ec-divider-label--right text-green">05 BRAND SYSTEM DESIGN</span>
                </div>
                <div class="ec-divider ec-divider--split" style="border-bottom: none; margin-bottom: 1.5rem; margin-top: 2rem;">
                    <span class="ec-divider-label">COLOR SYSTEM</span>
                </div>'''
content = content.replace(brand_sys_old, brand_sys_new)

content = content.replace('<strong class="ec-type-name">Plus Jakarta Sans</strong>', '<strong class="ec-type-name">Sinter</strong>')

# 8. 06 APPLICATIONS
content = content.replace('The brand system was designed to <strong>work in real-world and digital environments</strong>, from print materials to UI foundations.', 'The brand system was designed to work in real-world and digital environments, from print materials to UI foundations.')

# 9. 07 RESULTS
content = content.replace('<span class="ec-result-sub">shift towards "trustworthy" and "human" attributes</span>', '<span class="ec-result-sub">shift towards “trustworthy” and “human” attributes</span>')

# 10. 08 TAKEAWAYS
takeaway_old = '''<p class="ec-takeaway-text">This project reminded me that <strong>good branding isn't about looking good</strong>; it's about <strong>making people feel safe</strong>, confident and understood from the first interaction.</p>'''
takeaway_new = '''<p class="ec-takeaway-text">This project reminded me that good branding isn’t about looking good; it’s about making people feel safe, confident and understood from the first interaction.</p>'''
content = content.replace(takeaway_old, takeaway_new)

# 11. 2 things after the image in 08
takeaway_img_old = '''<div class="ec-placeholder ec-placeholder--takeaway">
                    <span>Takeaway image placeholder</span>
                </div>'''
takeaway_img_new = '''<div class="ec-placeholder ec-placeholder--takeaway">
                    <span>Takeaway image placeholder</span>
                </div>
                
                <div style="margin-top: 6rem; display: flex; flex-direction: column; align-items: center; gap: 3rem;">
                    <a href="humanly.html" style="text-decoration: none; width: 100%; max-width: 500px;">
                        <div class="proj-card" style="min-height: 180px; align-items: center; justify-content: center; display: flex; padding: 2rem;">
                            <div style="text-align: center;">
                                <span class="proj-card-cat" style="display: block; margin-bottom: 0.5rem;">NEXT PROJECT</span>
                                <h3 class="proj-card-name" style="font-size: 2rem;">Humanly</h3>
                            </div>
                        </div>
                    </a>
                    
                    <button onclick="window.scrollTo({top: 0, behavior: 'smooth'})" class="btn-pill" style="cursor: pointer; background: transparent;">
                        Go back to the top
                    </button>
                </div>'''
content = content.replace(takeaway_img_old, takeaway_img_new)

with open('emerald-clinical.html', 'w', encoding='utf-8') as f:
    f.write(content)
