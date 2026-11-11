exec(open('build.py').read())
import re,glob
IMG=lambda n,p="":f"--img:url({p}assets/images/{n}.webp)"
def qform():
    sv="".join(f'<option value="{s[2]}">{s[2]}</option>' for s in S)+"<option>Not sure yet</option>"
    return f'''<div class="qcard" id="enquire"><h2>Talk to an energy specialist</h2><p class="sm">Tell us what you need. We reply by email.</p><form class="lead" novalidate action="#"><div class="g">
<div class="f"><label for="qn">Full name</label><input id="qn" name="name" autocomplete="name"><span class="err"></span></div>
<div class="f"><label for="qc">Company</label><input id="qc" name="company" autocomplete="organization"><span class="err"></span></div>
<div class="f"><label for="qe">Work email</label><input id="qe" name="email" type="email" autocomplete="email"><span class="err"></span></div>
<div class="f"><label for="qp">Phone</label><input id="qp" name="phone" type="tel" autocomplete="tel"><span class="err"></span></div>
<div class="f w"><label for="qs">I need help with</label><select id="qs" name="service"><option value="">Select a service</option>{sv}</select><span class="err"></span></div>
<div class="f w"><label for="qm">Your requirement</label><textarea id="qm" name="message" rows="2"></textarea><span class="err"></span></div></div>
<input type="text" name="_gotcha" tabindex="-1" autocomplete="off" style="position:absolute;left:-999px" aria-hidden="true">
<p style="margin:14px 0 0"><button class="btn" type="submit">Book a Consultation</button></p><div class="status" role="status" aria-live="polite"></div>
<p class="alt-contact">Or email <a class="mailfb" href="mailto:{EMAIL}">{EMAIL}</a> <a id="wa" href="#" hidden>&middot; WhatsApp</a></p></form></div>'''
NEEDS=[("My electricity bills feel too high",1,"Have your bill reviewed","We analyse your bill, check calculations and look at sanctioned load and contract demand, then explore options to optimise expenditure. No savings are promised; findings depend on your site."),
("I need an energy or safety audit",0,"Audit your installation","Find where energy is wasted and where electrical safety hazards exist, with clear recommendations."),
("I'm planning a power project",2,"Plan your infrastructure","Design, equipment sourcing, delivery and installation coordination from one team."),
("I have compliance gaps to close",3,"Close compliance gaps","Assess regulatory and safety gaps, then coordinate the work needed to close them."),
("I want solar, EV or Open Access",4,"Explore cleaner energy","Evaluate solar, Open Access electricity and EV charging for your premises.")]
tabs="".join(f'<button role="tab" aria-selected="false">{ic(S[n[1]][10],"")}{n[0]}</button>' for n in NEEDS)
panels="".join(f'<div class="npanel" role="tabpanel"><div><h3>{n[2]}</h3><p>{n[3]}</p></div><div><a class="btn" href="contact.html?service={S[n[1]][2].replace(" ","%20").replace("&","%26")}#enquire">{S[n[1]][6]}</a> <p style="margin-top:14px"><a href="services/{S[n[1]][0]}.html">Learn more about this service</a></p></div></div>' for n in NEEDS)
names=["svc-audit","svc-bill","svc-infra","svc-compliance","svc-renewable"]
order=[(1,"big"),(0,""),(2,""),(3,"mid"),(4,"mid")]
tiles="".join(f'<a class="tile ph {c}" style="{IMG(names[i])}" href="services/{S[i][0]}.html">{ic(S[i][10],"bg")}<h3>{S[i][1]}</h3><p>{S[i][3]}</p><span class="go">Explore service</span></a>' for i,c in order)
inames=["ind-datacentre","ind-developers","ind-hotels","ind-hospitals","ind-restaurants","ind-itparks","ind-commercial","ind-industrial"]
itiles="".join(f'<div class="ph" style="{IMG(n)}">{I[0]}</div>' for n,I in zip(inames,IND))
home=head("","GRIDENCE | Energy & Power Advisory for Businesses","GRIDENCE provides electricity bill optimisation, energy audits, power infrastructure consulting, regulatory compliance and renewable energy solutions for businesses.","index.html")
home+=f'''<section class="hero2" style="{IMG("hero")}"><div class="wrap"><div><h1>Intelligent Energy Solutions for a More Efficient Business.</h1>
<p class="lead">From electricity bill optimisation and energy audits to power infrastructure and renewable energy solutions, GRIDENCE helps businesses build more efficient, reliable and compliant energy operations.</p>
<div class="ctas"><a class="btn" href="#enquire">Book a Consultation</a><a class="btn ghost" href="#services">Explore Our Solutions</a></div>
<ul class="chips"><li>100+ years of collective director experience</li><li>Experience at Reliance Energy and Adani Electricity</li><li>Works with MSEDCL and Adani Electricity</li></ul></div>{qform()}</div></section>
<div class="strip"><div class="wrap"><span>Data Centres</span><span>Developers</span><span>Hotels</span><span>Hospitals</span><span>Restaurant Chains</span><span>IT Parks</span><span>Commercial Complexes</span><span>Industry</span></div></div>
<section><div class="wrap"><h2>What do you need help with today?</h2><p class="lead">Choose the closest match. We will take you to the right specialist.</p>
<div data-tabs><div class="needs" role="tablist">{tabs}</div>{panels}</div></div></section>
<section class="dark"><div class="wrap split r"><div><h2>Are You Paying More Than You Should for Electricity?</h2><p class="lead">Send us a recent bill. We review how it is calculated and whether your sanctioned load and contract demand suit how you use power.</p>
<ul class="tick" style="color:#c9d6e3"><li>Bill analysis and calculation review</li><li>Coordination with MSEDCL and Adani Electricity</li><li>Application, documentation and site inspection support</li><li>Ongoing monitoring</li></ul><p><a class="btn" href="contact.html?service=Electricity%20Bill%20Optimization#enquire">Get Your Electricity Bill Reviewed</a></p></div>
<div class="bill" aria-hidden="true"><h4><span>Electricity bill</span><span>Review</span></h4><div><span>Energy charges<i></i></span><span>&#10003;</span></div><div><span>Demand charges<i></i></span><span>&#10003;</span></div><div class="flag"><span>Sanctioned load and contract demand</span><span>Check</span></div><div><span>Fixed charges<i></i></span><span>&#10003;</span></div><div><span>Duties and taxes<i></i></span><span>&#10003;</span></div></div></div></section>
<section id="services"><div class="wrap"><h2>Comprehensive Energy Expertise. One Strategic Partner.</h2><div class="bento">{tiles}</div></div></section>
<section class="bigstats"><div class="wrap"><h2 style="color:#fff;max-width:20ch">Led by people who have worked inside the utilities.</h2><div class="stats"><div><strong>100+</strong><span>years of collective industry experience among our directors</span></div><div><strong>4</strong><span>directors</span></div><div><strong>25+</strong><span>years of expertise each</span></div></div></div></section>
<section class="alt"><div class="wrap"><h2>Energy Expertise Across Diverse Business Environments.</h2><div class="itiles">{itiles}</div></div></section>
<div class="band"><div class="wrap"><h2>Not sure where to start? Tell us your requirement.</h2><a class="btn light" href="#enquire">Book a Consultation</a></div></div>
<section><div class="wrap"><h2>Technical Expertise. Commercial Perspective.</h2><div class="why">{"".join(f"<div><h3>{a}</h3><p>{b}</p></div>" for a,b in why)}</div></div></section>
<section class="alt"><div class="wrap"><h2>Our approach</h2><p class="lead">A general engagement journey. The steps vary by service.</p><ol class="steps">{"".join(f"<li><span>{s}</span></li>" for s in steps)}</ol></div></section>
<section><div class="wrap split"><div><h2>Frequently asked questions</h2><p class="lead">Still unsure? <a href="contact.html">Ask our team</a>.</p></div><div>{faq()}</div></div></section>
{cta_band("")}'''+foot("")
write("index.html",home)
for s,n in zip(S,names):
    f=f"services/{s[0]}.html";t=open(f,encoding="utf-8").read()
    t=t.replace('<section class="hero sub">',f'<section class="hero sub imgd" style="{IMG(n,"../")}">',1)
    t=t.replace('<section class="alt"><div class="wrap"><h2>How we work',f'<div class="band"><div class="wrap"><h2>{s[6]}</h2><a class="btn light" href="#enquire">Send an Enquiry</a></div></div><section class="alt"><div class="wrap"><h2>How we work',1)
    write(f,t)
