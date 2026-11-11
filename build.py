import os
SITE="https://ecomaura.github.io/gridence/"
EMAIL="sales.powerhelp@gmail.com"
S=[
("energy-audits","Energy Audits & Electricity Safety Audits","Energy Audits","Identify energy inefficiencies, improve electrical safety and strengthen operational performance.",
 "Improve Energy Efficiency. Strengthen Electrical Safety.","Identify energy inefficiencies, uncover electrical safety concerns and improve the performance of your business's energy infrastructure.","Request an Energy Audit Consultation",
 "Energy audits and electricity safety audits give a business a clear technical picture of how electricity is used and where the installation may carry risk. They support decisions on efficiency, safety and regulatory readiness for hotels, restaurants and other commercial and industrial operations.",
 [("Energy audits","Review how electrical energy is consumed across your premises and identify inefficiencies that increase waste."),("Electricity safety audits","Inspect the installation for electrical safety hazards and gaps against applicable regulatory requirements."),("Reducing energy waste","Translate findings into practical recommendations that improve operational efficiency."),("Regulatory requirements","Understand which electrical safety obligations apply to your type of establishment.")],
 ["Clearer visibility of how your facility uses electricity","Early identification of electrical safety hazards","Recommendations to reduce energy waste","Better regulatory readiness for hotels, restaurants and other businesses"],"audit"),
("electricity-bill-optimization","Electricity Bill Optimization","Electricity Bill Optimization","Review electricity bills, identify potential discrepancies and explore opportunities to optimise electricity expenditure.",
 "Are You Paying More Than You Should for Electricity?","Understand your electricity costs, review billing calculations and identify opportunities to improve your electricity expenditure.","Get Your Electricity Bill Reviewed",
 "GRIDENCE reviews how your electricity bill is built and whether your supply arrangements suit the way you use power. Our directors bring experience from utilities including Reliance Energy and Adani Electricity, and we work with distribution companies such as MSEDCL and Adani Electricity. Outcomes depend on each site; we do not promise guaranteed savings.",
 [("Bill analysis","Examine tariff category, charges and consumption patterns line by line."),("Calculation review","Check billing calculations and flag potential discrepancies for follow-up."),("Collaboration with utilities","Coordinate with distribution utilities such as MSEDCL and Adani Electricity."),("Cost reduction","Explore opportunities to optimise expenditure, including sanctioned load and contract demand."),("Regulatory compliance","Ensure any changes follow applicable regulatory procedure."),("Ongoing monitoring","Keep reviewing bills so changes in usage or billing are noticed.")],
 ["Application processing with the utility","Documentation preparation","Site inspection coordination","Support through the full utility process"],"bill"),
("power-infrastructure","Power Infrastructure Design & Supply Solutions","Power Infrastructure","Plan, design and coordinate reliable power infrastructure and equipment supply.",
 "Build Reliable Power Infrastructure for Your Next Project.","Technical planning, infrastructure design and coordinated supply solutions for commercial and infrastructure requirements.","Discuss Your Infrastructure Project",
 "From early consultation to delivery, GRIDENCE supports developers and operators with the planning, design and procurement of power distribution infrastructure, with one team coordinating each stage.",
 [("Comprehensive design services","Technical design of power distribution networks for your project."),("Expert consultation & planning","Early advice on requirements, capacity and approvals."),("Quality assurance","Equipment and design reviewed against technical standards."),("Integrated supply chain","Sourcing of infrastructure equipment through a coordinated supply chain."),("Timely execution","Delivery and installation coordination aligned to your project programme."),("End-to-end support","A single point of coordination from planning to handover.")],
 ["Power distribution networks","Infrastructure equipment sourcing","Delivery and installation coordination"],"grid"),
("regulatory-compliance","Regulatory Compliance & Closure Services","Regulatory Compliance","Help businesses identify electrical safety and regulatory gaps and coordinate compliance-related requirements.",
 "Stay Compliant. Operate Safely. Reduce Risk.","Identify electrical safety concerns, address compliance gaps and improve regulatory readiness across your business operations.","Discuss Your Compliance Requirements",
 "Electrical faults are a recognised cause of fire and operational risk. GRIDENCE assesses your installation against safety standards and regulatory requirements, then helps close the gaps so legal and operational exposure is reduced for hotels, restaurants, hospitals and industries.",
 [("Fire hazards","Identify electrical conditions that can contribute to fire risk."),("Compliance assessments","Assess your installation against applicable regulatory requirements."),("Risk identification","Document legal and operational risks in plain terms."),("Closure of compliance gaps","Coordinate the work and paperwork needed to close identified gaps."),("Safety standards","Align electrical practices to accepted safety standards.")],
 ["Hotels and restaurants","Hospitals and healthcare facilities","Industrial establishments"],"shield"),
("renewable-energy","Eco-Friendly Power Solutions","Renewable Energy Solutions","Explore solar power, Open Access electricity and EV charging solutions.",
 "Smarter, Cleaner and More Cost-Effective Energy Solutions.","Explore renewable and alternative energy solutions that support business efficiency and long-term sustainability.","Explore Energy Solutions",
 "Renewable and alternative energy can reduce electricity expenditure, improve energy efficiency and lower the carbon footprint of an operation. GRIDENCE helps developers, industries and commercial establishments evaluate and adopt the right options within regulatory requirements.",
 [("Solar power","Evaluate rooftop and on-site solar for your premises."),("Open Access","Explore sourcing electricity through Open Access where eligible."),("Electric vehicle charging","Plan EV charging infrastructure for commercial and residential developments.")],
 ["Potential reduction in electricity expenditure","Improved energy efficiency","Sustainability and carbon footprint reduction","Regulatory compliance throughout"],"leaf"),
]
IND=[("Data Centres","Reliable, well-planned power is central to uptime."),("Developers & Builders","Power infrastructure planning for new projects."),("Hotels","Safety, compliance and electricity cost control."),("Hospitals","Electrical safety and dependable supply."),("Restaurant Chains","Multi-site bill review and safety compliance."),("IT Parks","Large connected loads and demand planning."),("Commercial Complexes","Shared infrastructure and consumption oversight."),("Industrial Establishments","Contract demand, safety and efficiency.")]
FAQ=[("What is electricity bill optimisation?","It is a review of your electricity bills, tariff category and supply arrangements to identify billing discrepancies and opportunities to optimise expenditure. Results depend on your site."),
("What is sanctioned load?","Sanctioned load is the maximum electrical load your connection is approved for by the utility. If it does not match actual needs, you may be paying for more than you use, or risk exceeding limits."),
("What is contract demand?","Contract demand is the demand level agreed with the utility for certain commercial and industrial connections. It influences demand-related charges on your bill."),
("What is Open Access electricity?","Open Access allows eligible large consumers to source electricity from suppliers other than their local distribution company, subject to regulations."),
("Why do I need an energy audit?","An energy audit shows where electricity is being wasted and what can be improved in efficiency and operations."),
("What is an electrical safety audit?","It is an inspection of your electrical installation for hazards and gaps against regulatory requirements and safety standards."),
("What renewable energy solutions can GRIDENCE help with?","Solar power, Open Access electricity and electric vehicle charging infrastructure.")]
ICON={
"audit":'<circle cx="42" cy="42" r="24"/><path d="M60 60l26 26M30 42h24M42 30v24"/>',
"bill":'<rect x="20" y="10" width="60" height="80"/><path d="M32 30h36M32 44h36M32 58h20M32 72h28"/>',
"grid":'<circle cx="20" cy="20" r="6"/><circle cx="80" cy="20" r="6"/><circle cx="50" cy="50" r="6"/><circle cx="20" cy="80" r="6"/><circle cx="80" cy="80" r="6"/><path d="M26 20h48M20 26v48M80 26v48M26 80h48M24 24l22 22M76 24L54 46M24 76l22-22M76 76L54 54"/>',
"shield":'<path d="M50 8l36 14v28c0 22-16 36-36 42C30 86 14 72 14 50V22z"/><path d="M34 50l12 12 22-24"/>',
"leaf":'<circle cx="50" cy="40" r="16"/><path d="M50 12v8M50 60v8M22 40h8M70 40h8M30 20l6 6M64 54l6 6M70 20l-6 6M36 54l-6 6M50 68v24M36 92h28"/>'}
def ic(k,cls="ic"):return f'<svg class="{cls}" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="square" aria-hidden="true">{ICON[k]}</svg>'
MARK='<svg width="34" height="34" viewBox="0 0 34 34" aria-hidden="true"><g stroke="#2689D8" stroke-width="1.6" fill="none"><path d="M5 5h24M5 17h24M5 29h24M5 5v24M17 5v24M29 5v24"/></g><g fill="currentColor"><rect x="2" y="2" width="6" height="6"/><rect x="14" y="14" width="6" height="6" fill="#2689D8"/><rect x="26" y="26" width="6" height="6"/></g></svg>'
def logo(p):return f'<a class="logo" href="{p}index.html" aria-label="GRIDENCE home">{MARK}<span><b>GRIDENCE</b><small>ENERGY &amp; POWER ADVISORY</small></span></a>'
def head(p,title,desc,path):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{SITE}{path}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:type" content="website"><meta property="og:url" content="{SITE}{path}"><meta property="og:site_name" content="GRIDENCE">
<meta name="theme-color" content="#0A1728"><link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@600;700;800&display=swap">
<link rel="stylesheet" href="{p}assets/css/style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"GRIDENCE","description":"Energy & Power Advisory","email":"{EMAIL}","url":"{SITE}"}}</script>
</head><body><a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="wrap bar">{logo(p)}<button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
<nav class="main" aria-label="Primary"><ul><li><a href="{p}index.html">Home</a></li><li><a href="{p}about.html">About</a></li>
<li class="dd"><button aria-expanded="false" aria-haspopup="true">Services &#9662;</button><ul class="menu">{"".join(f'<li><a href="{p}services/{s[0]}.html">{s[2]}</a></li>' for s in S)}</ul></li>
<li><a href="{p}industries.html">Industries</a></li><li><a href="{p}blog/index.html">Insights</a></li><li><a href="{p}contact.html">Contact</a></li>
<li><a class="btn" href="{p}contact.html">Discuss Your Energy Requirements</a></li></ul></nav></div></header><main id="main">'''
def foot(p):
    return f'''</main><footer class="site"><div class="wrap"><div class="cols"><div>{logo(p)}<p style="margin-top:18px;max-width:34ch">GRIDENCE helps businesses make smarter energy decisions through electricity cost optimisation, technical audits, power infrastructure consulting, regulatory compliance and renewable energy solutions.</p>
<p><a href="mailto:{EMAIL}">{EMAIL}</a></p><a class="btn" href="{p}contact.html">Request a Consultation</a></div>
<div><h4>Services</h4><ul>{"".join(f'<li><a href="{p}services/{s[0]}.html">{s[2]}</a></li>' for s in S)}</ul></div>
<div><h4>Company</h4><ul><li><a href="{p}about.html">About</a></li><li><a href="{p}industries.html">Industries</a></li><li><a href="{p}blog/index.html">Insights</a></li><li><a href="{p}contact.html">Contact</a></li></ul></div>
<div><h4>Legal</h4><ul><li><a href="{p}privacy-policy.html">Privacy Policy</a></li><li><a href="{p}terms.html">Terms and Conditions</a></li></ul></div></div>
<div class="legal"><span>&copy; 2026 GRIDENCE. Operated by Enrovison LLP (subject to client confirmation).</span><span>Intelligent Energy. Stronger Business.</span></div></div></footer>
<div class="sticky"><a class="btn" href="{p}contact.html">Book a Consultation</a></div><button id="top" aria-label="Back to top">&uarr;</button>
<script src="{p}assets/js/config.js"></script><script src="{p}assets/js/main.js"></script></body></html>'''
def form(p,pre="",title="Tell us about your requirement"):
    ind="".join(f"<option>{i[0]}</option>" for i in IND)+"<option>Other</option>"
    sv="".join(f'<option value="{s[2]}"{" selected" if s[0]==pre else ""}>{s[2]}</option>' for s in S)+"<option>Not sure yet</option>"
    return f'''<div class="formbox"><h3>{title}</h3><form class="lead" novalidate action="#">
<div class="g"><div class="f"><label for="n{pre}">Full name</label><input id="n{pre}" name="name" autocomplete="name" required><span class="err"></span></div>
<div class="f"><label for="c{pre}">Company name</label><input id="c{pre}" name="company" autocomplete="organization" required><span class="err"></span></div>
<div class="f"><label for="e{pre}">Work email</label><input id="e{pre}" name="email" type="email" autocomplete="email" required><span class="err"></span></div>
<div class="f"><label for="p{pre}">Phone number</label><input id="p{pre}" name="phone" type="tel" autocomplete="tel" required><span class="err"></span></div>
<div class="f"><label for="i{pre}">Industry</label><select id="i{pre}" name="industry" required><option value="">Select industry</option>{ind}</select><span class="err"></span></div>
<div class="f"><label for="s{pre}">Service required</label><select id="s{pre}" name="service" required><option value="">Select service</option>{sv}</select><span class="err"></span></div>
<div class="f w"><label for="m{pre}">Brief description of requirements</label><textarea id="m{pre}" name="message" rows="3" required></textarea><span class="err"></span></div></div>
<input type="text" name="_gotcha" tabindex="-1" autocomplete="off" style="position:absolute;left:-999px" aria-hidden="true">
<p style="margin:18px 0 0"><button class="btn" type="submit">Send Enquiry</button></p><div class="status" role="status" aria-live="polite"></div>
<p class="alt-contact">Prefer email? <a class="mailfb" href="mailto:{EMAIL}">{EMAIL}</a> <a id="wa" href="#" hidden>&middot; WhatsApp</a></p></form></div>'''
def faq(items=FAQ):return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in items)
def write(path,html):
    os.makedirs(os.path.dirname(path) or ".",exist_ok=True);open(path,"w",encoding="utf-8").write(html)
NET='''<svg class="net" viewBox="0 0 400 440" role="img" aria-label="Abstract power network diagram"><g class="ln"><path d="M40 60H200V180H360M200 180V320H80M200 320H340V400M40 220H200M360 60V180M360 180V260H300"/></g>
<g><path class="pulse" d="M40 60H200V180H360"/><path class="pulse" style="animation-delay:-3s" d="M200 180V320H340V400"/></g>
<g class="nd"><rect x="30" y="50" width="20" height="20"/><rect x="190" y="170" width="20" height="20"/><rect x="350" y="170" width="20" height="20"/><rect x="70" y="310" width="20" height="20"/><rect x="330" y="390" width="20" height="20"/><rect x="30" y="210" width="20" height="20"/><rect x="350" y="50" width="20" height="20"/></g>
<rect class="hot" x="193" y="173" width="14" height="14"/></svg>'''
def hero_sub(p,crumb,h1,sub,cta,svg=""):
    return f'<section class="hero sub"><div class="gridbg"></div><div class="wrap"><div><div class="crumb"><a href="{p}index.html">Home</a> / {crumb}</div><h1>{h1}</h1><p class="lead">{sub}</p><p><a class="btn" href="#enquire">{cta}</a></p></div><div>{svg}</div></div></section>'
def cta_band(p,pre=""):
    return f'<section class="cta" id="enquire"><div class="wrap split r"><div><h2>Let\'s Make Your Energy Operations More Efficient.</h2><p class="lead" style="color:#a9bbcd">Tell us about your energy requirements. Our team will help you explore the right technical and commercial solutions for your business.</p></div>{form(p,pre)}</div></section>'
# HOME
p=""
rows="".join(f'<a href="services/{s[0]}.html"><span>{c}</span><small>{s[2]}</small></a>' for c,s in zip(["Increasing electricity expenditure","Electricity billing discrepancies","Inefficient sanctioned load and contract demand","Electrical safety concerns","Regulatory compliance complexity","Power infrastructure planning challenges","Alternative energy adoption"],[S[1],S[1],S[1],S[0],S[3],S[2],S[4]]))
svcs="".join(f'<div class="svc">{ic(s[10])}<div><span class="n">Service {i+1}</span><h3>{s[1]}</h3><p>{s[3]}</p><p><a class="btn" href="services/{s[0]}.html">Explore Service</a></p></div><div><ul class="tick">{"".join(f"<li>{b}</li>" for b in s[9])}</ul></div></div>' for i,s in enumerate(S))
steps=["Understand business requirements","Review existing infrastructure and documentation","Identify optimisation and compliance opportunities","Recommend suitable solutions","Coordinate implementation and execution","Support ongoing efficiency and compliance"]
why=[("Industry-Leading Expertise","Our directors bring decades of combined experience from major utilities and power companies."),("Custom Solutions","Every business has a different load, site and regulatory context. We tailor recommendations to yours."),("Comprehensive Energy Strategy","From bills and audits to infrastructure and renewables, we look at energy as one connected system."),("Legal and Compliance Assurance","We keep regulatory requirements in view at every stage, so improvements are made the right way.")]
home=head(p,"GRIDENCE | Energy & Power Advisory for Businesses","GRIDENCE provides electricity bill optimisation, energy audits, power infrastructure consulting, regulatory compliance and renewable energy solutions for businesses.","index.html")
home+=f'''<section class="hero"><div class="gridbg"></div><div class="wrap"><div><h1>Intelligent Energy Solutions for a More Efficient Business.</h1><p class="lead">From electricity bill optimisation and energy audits to power infrastructure and renewable energy solutions, GRIDENCE helps businesses build more efficient, reliable and compliant energy operations.</p>
<div class="ctas"><a class="btn" href="contact.html">Book a Consultation</a><a class="btn ghost" href="#services">Explore Our Solutions</a></div></div><div>{NET}</div></div></section>
<section><div class="wrap"><div class="split"><div><h2>Led by people who have worked inside the utilities.</h2></div><div><p class="lead">Operated by Enrovison LLP, GRIDENCE brings together directors with experience at organisations including Reliance Energy and Adani Electricity.</p></div></div>
<div class="stats"><div><strong>100+</strong><span>years of collective industry experience among our directors</span></div><div><strong>4</strong><span>directors</span></div><div><strong>25+</strong><span>years of expertise each</span></div></div></div></section>
<section class="alt"><div class="wrap"><div class="split"><div><h2>Energy Challenges Shouldn't Hold Your Business Back.</h2><p class="lead">The problems we help address, and where to start with each.</p></div><div class="rows">{rows}</div></div></div></section>
<section id="services"><div class="wrap"><h2>Comprehensive Energy Expertise. One Strategic Partner.</h2>{svcs}</div></section>
<section class="dark"><div class="wrap"><h2>Energy Expertise Across Diverse Business Environments.</h2><div class="ind">{"".join(f"<div><h3>{a}</h3><p>{b}</p></div>" for a,b in IND)}</div><p style="margin-top:28px"><a class="btn light" href="industries.html">View Industries</a></p></div></section>
<section><div class="wrap"><h2>Technical Expertise. Commercial Perspective.</h2><div class="why">{"".join(f"<div><h3>{a}</h3><p>{b}</p></div>" for a,b in why)}</div></div></section>
<section class="alt"><div class="wrap"><h2>Our approach</h2><p class="lead">A general engagement journey. The steps vary by service.</p><ol class="steps">{"".join(f"<li><span>{s}</span></li>" for s in steps)}</ol></div></section>
<section><div class="wrap split"><div><h2>Frequently asked questions</h2></div><div>{faq()}</div></div></section>
<section class="alt"><div class="wrap"><h2>Insights</h2><div class="empty">Articles are being migrated from the original site. <a href="blog/index.html">Visit Insights</a>.</div></div></section>
{cta_band(p)}'''+foot(p)
write("index.html",home)
# SERVICES
for s in S:
    pth=f"services/{s[0]}.html";q="../"
    h=head(q,f"{s[1]} | GRIDENCE",s[5],pth)+hero_sub(q,f'<a href="{q}services.html">Services</a> / {s[2]}',s[4],s[5],s[6],ic(s[10],"net")) \
    +f'<section><div class="wrap split"><div><h2>{s[1]}</h2></div><div><p class="lead">{s[7]}</p></div></div></section>' \
    +f'<section class="alt"><div class="wrap"><h2>{"What We Review" if s[0]=="electricity-bill-optimization" else "What the service covers"}</h2><div class="why">{"".join(f"<div><h3>{a}</h3><p>{b}</p></div>" for a,b in s[8])}</div></div></section>' \
    +f'<section><div class="wrap split"><div><h2>Business benefits</h2></div><div><ul class="tick">{"".join(f"<li>{b}</li>" for b in s[9])}</ul></div></div></section>' \
    +f'<section class="alt"><div class="wrap"><h2>How we work</h2><ol class="steps">{"".join(f"<li><span>{x}</span></li>" for x in steps)}</ol></div></section>' \
    +f'<section><div class="wrap split"><div><h2>Questions on this service</h2></div><div>{faq(FAQ[:4] if s[0]=="electricity-bill-optimization" else FAQ[4:6] if s[0] in("energy-audits","regulatory-compliance") else FAQ[3:4]+FAQ[6:])}</div></div></section>'+cta_band(q,s[0])+foot(q)
    write(pth,h)
# overview
p=""
sv=head(p,"Services | GRIDENCE","Five energy and power advisory services: audits, bill optimisation, infrastructure, compliance and renewable energy.","services.html")+hero_sub(p,"Services","Comprehensive Energy Expertise. One Strategic Partner.","Five service areas, each with its own detailed approach.","Book a Consultation")+f'<section><div class="wrap">{svcs}</div></section>'+cta_band(p)+foot(p)
write("services.html",sv)
write("industries.html",head(p,"Industries | GRIDENCE","Energy expertise for data centres, developers, hotels, hospitals, restaurant chains, IT parks, commercial complexes and industry.","industries.html")+hero_sub(p,"Industries","Energy Expertise Across Diverse Business Environments.","Experience across commercial, infrastructure and industrial settings.","Discuss Your Requirements")+f'<section class="dark"><div class="wrap"><div class="ind">{"".join(f"<div><h3>{a}</h3><p>{b}</p></div>" for a,b in IND)}</div></div></section>'+cta_band(p)+foot(p))
write("about.html",head(p,"About GRIDENCE | Energy & Power Advisory","GRIDENCE is operated by Enrovison LLP, led by directors with over 100 years of collective experience including Reliance Energy and Adani Electricity.","about.html")+hero_sub(p,"About","Technical Expertise. Commercial Perspective.","GRIDENCE helps businesses make smarter energy decisions.","Book a Consultation")+f'<section><div class="wrap split"><div><h2>Who we are</h2></div><div class="prose"><p class="lead">Operated by Enrovison LLP (subject to client confirmation), GRIDENCE is led by four directors with over 25 years of expertise each and over 100 years of collective industry experience, including at Reliance Energy and Adani Electricity.</p></div></div><div class="wrap"><div class="why">{"".join(f"<div><h3>{a}</h3><p>{b}</p></div>" for a,b in why)}</div></div></section>'+cta_band(p)+foot(p))
write("contact.html",head(p,"Contact GRIDENCE","Discuss your electricity, audit, infrastructure, compliance or renewable energy requirements with GRIDENCE.","contact.html")+hero_sub(p,"Contact","Speak With Our Team","Tell us about your energy requirements.","Send an Enquiry")+f'<section id="enquire" class="alt"><div class="wrap split r"><div><h2>Contact details</h2><p>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p><p>Address and phone numbers to be confirmed from the original site.</p></div>{form(p)}</div></section>'+foot(p))
write("blog/index.html",head("../","Insights | GRIDENCE","Insights on electricity, energy efficiency and compliance from GRIDENCE.","blog/index.html")+hero_sub("../","Insights","Insights","Perspectives on electricity, compliance and energy efficiency.","Ask Our Team")+'<section id="enquire"><div class="wrap"><div class="empty"><h3>Articles are being migrated</h3><p>The original Powerhelp articles could not be accessed automatically and will be added with their original meaning intact. See README.</p></div></div></section>'+foot("../"))
leg=lambda t,f,d:head(p,f"{t} | GRIDENCE",d,f)+f'<section><div class="wrap prose"><h1 style="font-size:2.4rem">{t}</h1><p>Draft placeholder. Final legal text must be supplied or approved by the client and Enrovison LLP before launch.</p></div></section>'+foot(p)
write("privacy-policy.html",leg("Privacy Policy","privacy-policy.html","How GRIDENCE handles enquiry information."))
write("terms.html",leg("Terms and Conditions","terms.html","Terms of use for the GRIDENCE website."))
write("assets/favicon.svg",'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 34 34"><rect width="34" height="34" fill="#0A1728"/><path d="M5 5h24M5 17h24M5 29h24M5 5v24M17 5v24M29 5v24" stroke="#2689D8" stroke-width="1.6"/><rect x="14" y="14" width="6" height="6" fill="#fff"/></svg>')
pages=["index.html","about.html","services.html","industries.html","contact.html","blog/index.html","privacy-policy.html","terms.html"]+[f"services/{s[0]}.html" for s in S]
write("sitemap.xml",'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{SITE}{x}</loc></url>" for x in pages)+"</urlset>")
write("robots.txt",f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
write(".nojekyll","")
