"""Check built pages, local links, fragments, image text, and core metadata."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import sys
root=Path(sys.argv[1] if len(sys.argv)>1 else 'dist').resolve()
base=sys.argv[2].rstrip('/') if len(sys.argv)>2 else ''
class Page(HTMLParser):
 def __init__(self):super().__init__();self.ids=[];self.links=[];self.h1=0;self.main=0;self.description=False;self.errors=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='main':self.main+=1
  if tag=='meta' and a.get('name')=='description':self.description=bool(a.get('content'))
  if tag=='img' and not a.get('alt'):self.errors.append('Missing image alt text')
  for k in ('href','src'):
   if k in a:self.links.append(a[k])
pages={}
for f in root.rglob('*.html'):
 p=Page();p.feed(f.read_text());pages[f]=p
errors=[]
for f,p in pages.items():
 for issue in p.errors:errors.append(f'{f.relative_to(root)}: {issue}')
 if p.h1!=1 or p.main!=1 or not p.description:errors.append(f'{f.name}: heading/main/description issue')
 if len(p.ids)!=len(set(p.ids)):errors.append(f'{f.name}: duplicate IDs')
 for link in p.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  path=unquote(u.path)
  if path.startswith('/'):
   if base and not (path==base or path.startswith(base+'/')):errors.append(f'{f.name}: missing base in {link}');continue
   target=root/path[len(base):].lstrip('/')
  elif path:target=(f.parent/path).resolve()
  else:target=f
  if target.is_dir():target=target/'index.html'
  if not target.exists():errors.append(f'{f.name}: missing {link}');continue
  if u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:errors.append(f'{f.name}: missing fragment {link}')
if errors:print('\n'.join(errors));sys.exit(1)
print(f'{len(pages)} pages passed: local links, fragments, image alt text, main headings, descriptions, and unique IDs.')
