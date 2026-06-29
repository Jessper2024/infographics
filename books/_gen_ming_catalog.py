#!/usr/bin/env python3
"""Generate catalog page for 明朝那些事儿"""
import os, json

BOOKS_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BOOKS_DIR, '_ming_data.json')

with open(DATA_PATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

entries = []
for section in data['sections']:
    emperor = section['emperor']
    prefix = section['prefix']
    chapters = section['chapters']
    count = len(chapters)

    icon_emojis = {
        '朱元璋': '👑', '朱允炆': '🏛️', '朱棣': '🐉', '朱高炽': '📜',
        '朱瞻基': '🎭', '朱祁镇pt1': '⚔️', '朱祁钰': '🛡️', '朱祁镇pt2': '👁️',
        '朱见深': '🌙', '朱祐樘': '⭐', '朱厚照': '🔥', '朱厚熜pt1': '🏔️',
        '朱厚熜pt2': '⛩️', '朱载垕': '⚖️', '朱翊钧pt1': '🎯', '朱翊钧pt2': '📚',
        '朱常洛': '🌸', '朱由校pt1': '🔧', '朱由校pt2': '⚔️', '朱由检': '💔'
    }
    icon = icon_emojis.get(emperor, '📖')
    first_ch = chapters[0]['title'] if chapters else ''
    last_ch = chapters[-1]['title'] if chapters else ''
    desc = f'从{first_ch}到{last_ch}，共{count}章。当年明月笔下的{emperor}，波澜壮阔的历史画卷。'
    catalog_href = f'明朝那些事儿-{emperor}-catalog.html'

    entry = f'''<div class="entry">
  <div class="entry-icon" style="background:#fef2f2;color:#dc2626;">{icon}</div>
  <div class="entry-info">
    <div class="entry-title">明朝那些事儿 · {emperor}</div>
    <div class="entry-meta">当年明月 · {count} 章节</div>
    <div class="entry-desc">{desc}</div>
  </div>
  <div class="entry-links">
    <a class="entry-link zh" target="_blank" href="{catalog_href}">📋 目录</a>
  </div>
</div>'''
    entries.append(entry)

css = '''<style>
@font-face{font-family:"FZXPYZS";src:url("../方正屏显雅宋简体.TTF") format("truetype");}
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
body{background:#f5f1eb;font-family:"FZXPYZS","PingFang SC","Noto Serif SC","STSong",Georgia,serif;color:#1a1a1a;display:flex;justify-content:center;padding:48px 20px 64px;-webkit-font-smoothing:antialiased}
.container{max-width:880px;width:100%;}
.header{text-align:center;margin-bottom:32px}
.header h1{font-size:32px;font-weight:normal;color:#1a1a1a;letter-spacing:.04em;line-height:1.3}
.header .count{font-size:13px;color:#bbb;margin-top:6px}
.divider{width:60px;height:3px;margin:24px auto 28px;border-radius:2px;background:linear-gradient(90deg,#dc2626,#ea580c)}
.entry{background:#fff;border:1px solid #e8e0d5;border-radius:14px;padding:22px 28px;margin-bottom:14px;box-shadow:0 1px 8px rgba(0,0,0,.03);display:flex;gap:20px;align-items:flex-start;transition:box-shadow .15s}
.entry:hover{box-shadow:0 2px 14px rgba(0,0,0,.06)}
.entry-icon{width:52px;height:52px;border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:24px;flex-shrink:0}
.entry-info{flex:1;min-width:0}
.entry-title{font-size:18px;font-weight:bold;color:#1a1a1a;margin-bottom:4px;letter-spacing:.03em}
.entry-meta{font-size:13px;color:#888;margin-top:2px;letter-spacing:.02em}
.entry-desc{font-size:14px;color:#555;margin-top:8px;line-height:1.8}
.entry-links{display:flex;gap:8px;flex-shrink:0;flex-wrap:wrap;align-items:flex-start}
.entry-link{display:inline-block;padding:7px 16px;border-radius:8px;font-size:13px;text-decoration:none;letter-spacing:.03em;transition:opacity .15s}
.entry-link:hover{opacity:.8}
.entry-link.zh{background:#fef2f2;color:#dc2626;border:1px solid #fecaca}
.footer{text-align:center;font-size:13px;color:#bbb;margin-top:32px}
@media(max-width:600px){.entry{flex-direction:column;align-items:flex-start}.entry-links{width:100%}.entry-link{flex:1;text-align:center}}
</style>'''

html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>明朝那些事儿 · 图书信息图目录</title>
{css}
</head>
<body>
<div class="container">
<div class="header">
<h1>📚 明朝那些事儿 · 图书信息图</h1>
<div class="count">共 {len(data['sections'])} 个皇帝篇，{data['total_chapters']} 章</div>
</div>
<div class="divider"></div>
{''.join(entries)}
<div class="footer">方正屏显雅宋简体</div>
</div>
</body>
</html>'''

out_path = os.path.join(BOOKS_DIR, '明朝那些事儿-catalog.html')
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Generated: {out_path}')
print(f'Total entries: {len(entries)}')
