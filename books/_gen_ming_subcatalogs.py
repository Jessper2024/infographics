#!/usr/bin/env python3
"""Generate per-emperor catalog pages for 明朝那些事儿"""
import os, json

BOOKS_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BOOKS_DIR, '_ming_data.json')

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

CSS = '''<style>
@font-face{font-family:"FZXPYZS";src:url("../方正屏显雅宋简体.TTF") format("truetype");}
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
body{background:#f5f1eb;font-family:"FZXPYZS","PingFang SC","Noto Serif SC","STSong",Georgia,serif;color:#1a1a1a;display:flex;justify-content:center;padding:48px 20px 64px;-webkit-font-smoothing:antialiased}
.container{max-width:880px;width:100%;}
.header{text-align:center;margin-bottom:32px}
.header h1{font-size:32px;font-weight:normal;color:#1a1a1a;letter-spacing:.04em;line-height:1.3}
.header .count{font-size:13px;color:#bbb;margin-top:6px}
.divider{width:60px;height:3px;margin:24px auto 28px;border-radius:2px;background:linear-gradient(90deg,#dc2626,#ea580c)}
.chapter-list{list-style:none;padding:0;margin:0}
.chapter-item{background:#fff;border:1px solid #e8e0d5;border-radius:10px;padding:14px 20px;margin-bottom:10px;display:flex;align-items:center;gap:14px;transition:box-shadow .15s}
.chapter-item:hover{box-shadow:0 2px 10px rgba(0,0,0,.05)}
.chapter-num{width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:bold;color:#fff;flex-shrink:0}
.chapter-info{flex:1;min-width:0}
.chapter-title{font-size:15px;font-weight:bold;color:#1a1a1a;margin-bottom:2px}
.chapter-meta{font-size:12px;color:#888}
.chapter-links{display:flex;gap:6px;flex-shrink:0}
.ch-link{display:inline-block;padding:5px 12px;border-radius:6px;font-size:12px;text-decoration:none;font-weight:500}
.ch-link.zh{background:#fef2f2;color:#dc2626;border:1px solid #fecaca}
.ch-link.en{background:#eef2ff;color:#4f46e5;border:1px solid #c7d2fe}
.back-link{display:inline-block;font-size:14px;color:#888;text-decoration:none;margin-bottom:16px}
.back-link:hover{color:#555}
.footer{text-align:center;font-size:13px;color:#bbb;margin-top:32px}
@media(max-width:600px){.chapter-item{flex-direction:column;align-items:flex-start;gap:10px}.chapter-links{width:100%}.ch-link{flex:1;text-align:center}}
</style>'''

COLORS = ['#dc2626','#ea580c','#ca8a04','#4f46e5','#db2777']

for section in data['sections']:
    emperor = section['emperor']
    chapters = section['chapters']
    count = len(chapters)

    items = []
    for idx, ch in enumerate(chapters):
        info_num = ch['info_num']
        title = ch['title']
        color = COLORS[idx % len(COLORS)]
        items.append(f'''<li class="chapter-item">
  <div class="chapter-num" style="background:{color};">{idx+1}</div>
  <div class="chapter-info">
    <div class="chapter-title">{title}</div>
    <div class="chapter-meta">第 {idx+1} 章 · {emperor}</div>
  </div>
  <div class="chapter-links">
    <a class="ch-link zh" target="_blank" href="明朝那些事儿-{emperor}-{info_num}-info-zh.html">中文</a>
    <a class="ch-link en" target="_blank" href="明朝那些事儿-{emperor}-{info_num}-info-en.html">EN</a>
  </div>
</li>''')

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>明朝那些事儿 · {emperor} · 章节目录</title>
{CSS}
</head>
<body>
<div class="container">
<a class="back-link" href="明朝那些事儿-catalog.html" target="_blank">&larr; 返回总目录</a>
<div class="header">
<h1>📖 明朝那些事儿 · {emperor}</h1>
<div class="count">共 {count} 章</div>
</div>
<div class="divider"></div>
<ul class="chapter-list">
{''.join(items)}
</ul>
<div class="footer">方正屏显雅宋简体</div>
</div>
</body>
</html>'''

    out_path = os.path.join(BOOKS_DIR, f'明朝那些事儿-{emperor}-catalog.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Generated: 明朝那些事儿-{emperor}-catalog.html ({count} chapters)')

print(f'\nTotal: {len(data["sections"])} emperor catalogs generated')
