# GRIDENCE website
Static HTML/CSS/JS site for GitHub Pages. Regenerate pages with `python3 build.py`.

## Deploy
Repo Settings > Pages > Deploy from branch `main`, folder `/ (root)`. Live at https://ecomaura.github.io/gridence/

## Form setup (Formspree)
1. Create a form at formspree.io, copy its ID.
2. Edit `assets/js/config.js`: set `formspree` to `https://formspree.io/f/<ID>`.
3. Optional: set `whatsapp` to a verified number (digits with country code). Until then the form shows an email fallback.

## Content still to migrate (powerhelp.in blocked automated access)
- Full original blog articles and their detail pages (blog/ currently shows an empty state)
- Exact original FAQ answers (current FAQs are neutral drafts, verify)
- Client logos, original photography, phone/address, legal text for Privacy and Terms
- Enrovison LLP legal entity wording is subject to client confirmation
