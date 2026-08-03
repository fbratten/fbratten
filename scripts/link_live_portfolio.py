from pathlib import Path

path = Path('README.md')
text = path.read_text(encoding='utf-8')

marker = (
    'I combine applied AI with more than 20 years in enterprise IT, automation, operations and cybersecurity. '
    'My work focuses on systems that are useful in practice: searchable knowledge, controlled agent actions, '
    'product-facing AI workflows, auditability and operational safeguards.\n'
)

block = '''

<p align="center">
  <a href="https://fbratten.github.io/"><img src="https://img.shields.io/badge/Public_Portfolio-Proof_Packages_%26_Showcases-14b8a6?style=for-the-badge" alt="Public portfolio"/></a>
  <a href="https://fbratten.github.io/methods/"><img src="https://img.shields.io/badge/Methods_%26_Protocols-Interactive_Profiles-8b5cf6?style=for-the-badge" alt="Methods and protocols"/></a>
</p>

<p align="center">
  <strong><a href="https://fbratten.github.io/">Start with the live portfolio landing page</a></strong><br/>
  Recruiter proof packages, method profiles, supporting evidence and earlier showcases in one public route.
</p>
'''

if 'https://fbratten.github.io/">Start with the live portfolio landing page' not in text:
    if marker not in text:
        raise SystemExit('Profile introduction marker not found')
    text = text.replace(marker, marker + block, 1)

for old in ('\u2011', '\u2012', '\u2013', '\u2014', '\u2015', '\u2212'):
    text = text.replace(old, '-')
for old in ('&mdash;', '&ndash;', '&#8212;', '&#8211;', '&#x2014;', '&#x2013;'):
    text = text.replace(old, '-')

path.write_text(text, encoding='utf-8')
print('Profile README updated.')
