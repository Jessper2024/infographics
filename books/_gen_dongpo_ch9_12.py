#!/usr/bin/env python3
"""Generate infographic HTML for 东坡志林 ch009~ch012 (zh+en, 8 files)"""
import os, sys

OUT = os.path.dirname(os.path.abspath(__file__))

def zh_page(ch_num, ch_title_short, ch_title_full, subtitle, overview, kpis, sections, takeaway, footer_title):
    kpi_html = ""
    colors = ['c01','c02','c03','c04']
    for i, (icon, val, label) in enumerate(kpis):
        kpi_html += f'''    <div class="kpi-card {colors[i]}">
      <div class="kpi-num {colors[i]}">{val}</div>
      <div class="kpi-label">{label}</div>
    </div>\n'''

    sec_html = ""
    sec_styles = [('section-01','num-01','tag-01','t-01'),
                  ('section-02','num-02','tag-02','t-02'),
                  ('section-03','num-03','tag-03','t-03'),
                  ('section-04','num-04','tag-04','t-04'),
                  ('section-05','num-05','tag-05','t-05')]
    for i, (tag_label, sec_title, sec_desc, extra_html) in enumerate(sections):
        ei = i if i < 5 else 4
        ss, sn, st, stt = sec_styles[ei]
        extra = extra_html if extra_html else ""
        sec_html += f'''<div class="section {ss}">
  <div class="section-num {sn}">{i+1:02d}</div>
  <div class="section-body">
    <div class="tag {st}">{tag_label}</div>
    <div class="section-title {stt}">{sec_title}</div>
    <div class="section-desc">{sec_desc}</div>
    {extra}
  </div>
</div>\n'''

    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>东坡志林 · 第{ch_num}章</title>
<style>
  @font-face {{font-family:'FZXPYZS';src:url('../TTF/方正屏显雅宋简体.TTF') format('truetype');font-weight:normal;font-style:normal}}
  *{{margin:0;padding:0;box-sizing:border-box}}
  body{{background:#f5f1eb;font-family:'PingFang SC','Noto Serif SC','STSong',Georgia,serif;display:flex;justify-content:center;align-items:flex-start;min-height:100vh;padding:40px 20px 60px}}
  .container{{max-width:880px;width:100%}}
  h1{{font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif;font-size:36px;color:#1a1a1a;text-align:center;line-height:1.4;margin-bottom:8px;font-weight:normal;letter-spacing:1.5px}}
  .subtitle{{text-align:center;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif;font-size:14px;color:#888;margin-bottom:24px;line-height:1.7;max-width:640px;margin-left:auto;margin-right:auto}}
  .divider{{width:60px;height:3px;background:linear-gradient(90deg,#dc2626,#ea580c);margin:0 auto 28px;border-radius:2px}}
  .section{{background:#fff;border-radius:14px;margin-bottom:18px;padding:24px 28px;box-shadow:0 1px 3px rgba(0,0,0,.04);display:flex;gap:20px;align-items:flex-start;border-left:4px solid transparent}}
  .section-01{{border-left-color:#dc2626}}.section-02{{border-left-color:#ea580c}}.section-03{{border-left-color:#ca8a04}}.section-04{{border-left-color:#4f46e5}}.section-05{{border-left-color:#db2777}}
  .section-num{{flex-shrink:0;width:42px;height:42px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:17px;font-weight:bold;margin-top:2px;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif}}
  .num-01{{background:#fef2f2;color:#dc2626}}.num-02{{background:#fff7ed;color:#ea580c}}.num-03{{background:#fefce8;color:#ca8a04}}.num-04{{background:#eef2ff;color:#4f46e5}}.num-05{{background:#fdf2f8;color:#db2777}}
  .section-body{{flex:1}}
  .tag{{display:inline-block;font-size:11px;font-weight:bold;padding:2px 10px;border-radius:10px;margin-bottom:8px;letter-spacing:1px;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif}}
  .tag-01{{background:#fef2f2;color:#dc2626}}.tag-02{{background:#fff7ed;color:#ea580c}}.tag-03{{background:#fefce8;color:#ca8a04}}.tag-04{{background:#eef2ff;color:#4f46e5}}.tag-05{{background:#fdf2f8;color:#db2777}}
  .section-title{{font-size:18px;margin-bottom:10px;font-weight:bold;line-height:1.4;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif}}
  .t-01{{color:#dc2626}}.t-02{{color:#ea580c}}.t-03{{color:#ca8a04}}.t-04{{color:#4f46e5}}.t-05{{color:#db2777}}
  .section-desc{{font-size:14px;color:#555;line-height:1.9;margin-bottom:14px}}
  .dual-grid{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:10px}}
  .dual-card{{border-radius:12px;padding:18px 20px;display:flex;gap:12px;align-items:flex-start}}
  .dual-card.yes{{background:#fef2f2;border:1px solid #fecaca}}
  .dual-card.no{{background:#f0fdf4;border:1px solid #bbf7d0}}
  .dual-icon{{font-size:24px;flex-shrink:0;line-height:1}}
  .dual-text h4{{font-size:14px;color:#1a1a1a;margin-bottom:4px;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif}}
  .dual-text p{{font-size:12px;color:#777;line-height:1.6}}
  .flow-row{{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-top:6px}}
  .flow-step{{background:#eef2ff;border:1px solid #c7d2fe;border-radius:10px;padding:10px 12px;text-align:center;min-width:80px;flex:1;font-size:13px;color:#3730a3;line-height:1.5;font-weight:bold}}
  .flow-arrow{{font-size:20px;color:#4f46e5;flex-shrink:0;font-weight:bold}}
  .flow-step.end{{background:#fef2f2;border-color:#fecaca;color:#991b1b}}
  .quote-block{{background:#f8f6f3;border-radius:12px;padding:18px 22px;margin-top:10px;border:1px solid #e8e0d5}}
  .quote-text{{font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif;font-size:15px;color:#1a1a1a;line-height:1.9;font-style:italic;margin-bottom:6px}}
  .quote-source{{font-size:12px;color:#aaa;text-align:right}}
  .confusion-table{{margin-top:10px}}
  .confusion-row{{display:flex;align-items:center;gap:12px;margin-bottom:8px;background:#fffbeb;border:1px solid #fde68a;border-radius:10px;padding:10px 16px}}
  .confusion-left{{flex:1;text-align:right;font-size:13px;color:#92400e;font-weight:bold;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif}}
  .confusion-arrow{{flex-shrink:0;font-size:18px;color:#ca8a04;font-weight:bold}}
  .confusion-right{{flex:1;font-size:13px;color:#713f12}}
  .kpi-row{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:28px}}
  .kpi-card{{background:#fff;border-radius:12px;padding:18px 14px;text-align:center;box-shadow:0 1px 3px rgba(0,0,0,.04);border-top:3px solid transparent}}
  .kpi-card.c01{{border-top-color:#dc2626}}.kpi-card.c02{{border-top-color:#ea580c}}.kpi-card.c03{{border-top-color:#ca8a04}}.kpi-card.c04{{border-top-color:#4f46e5}}
  .kpi-num{{font-size:28px;font-weight:bold;margin-bottom:4px;font-family:'FZXPYZS','PingFang SC',serif}}
  .kpi-num.c01{{color:#dc2626}}.kpi-num.c02{{color:#ea580c}}.kpi-num.c03{{color:#ca8a04}}.kpi-num.c04{{color:#4f46e5}}
  .kpi-label{{font-size:12px;color:#888;line-height:1.5}}
  .takeaway{{background:#fff;border:1px solid #e8e0d5;border-radius:14px;padding:24px 32px;margin-bottom:18px;box-shadow:0 1px 3px rgba(0,0,0,.04);border-left:4px solid #dc2626}}
  .takeaway-label{{font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif;font-size:12px;color:#dc2626;letter-spacing:2px;margin-bottom:6px;font-weight:bold}}
  .takeaway-text{{font-size:16px;color:#1a1a1a;line-height:1.9;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif}}
  .footer{{text-align:center;margin-top:32px;padding-top:20px;border-top:1px solid #e8e0d5;color:#bbb;font-size:13px;line-height:1.8}}
  .lang-switch{{text-align:right;margin-bottom:16px}}
  .lang-btn{{display:inline-block;padding:6px 16px;border-radius:8px;font-size:13px;text-decoration:none;letter-spacing:.03em;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif;background:#fef2f2;color:#dc2626;border:1px solid #fecaca;transition:opacity .15s}}
  .lang-btn:hover{{opacity:.75}}
  .chapter-overview{{background:#f8f6f3;border-left:3px solid #4f46e5;border-radius:8px;padding:16px 20px;margin:12px 0 24px;font-size:14px;color:#555;line-height:1.8;font-family:'FZXPYZS','PingFang SC',serif}}
  .chapter-overview p{{margin:0}}
  .back-catalog{{text-align:right;margin-bottom:4px}}
  .back-catalog-btn{{display:inline-block;padding:5px 14px;border-radius:8px;font-size:12px;text-decoration:none;letter-spacing:.02em;background:#eef2ff;color:#4f46e5;border:1px solid #c7d2fe;transition:opacity .15s}}
  .back-catalog-btn:hover{{opacity:.75}}
  @media(max-width:640px){{.section{{flex-direction:column;align-items:center;text-align:center;border-left:none;border-top:4px solid transparent;padding-top:20px}}.section-01{{border-top-color:#dc2626}}.section-02{{border-top-color:#ea580c}}.section-03{{border-top-color:#ca8a04}}.section-04{{border-top-color:#4f46e5}}.section-05{{border-top-color:#db2777}}.dual-grid,.kpi-row{{grid-template-columns:1fr}}.flow-row{{flex-direction:column}}.flow-arrow{{transform:rotate(90deg)}}.confusion-row{{flex-direction:column;align-items:stretch}}.confusion-left{{text-align:center}}.container{{padding:0 8px}}h1{{font-size:26px}}}}
</style>
</head>
<body>
<div class="container">
<div class="back-catalog"><a class="back-catalog-btn" href="东坡志林-catalog.html">← 返回章节目录</a></div>
<div class="lang-switch">
  <a class="lang-btn" target="_blank" href="东坡志林-ch{ch_num}-info-en.html">中文 / English</a>
</div>

<h1>东坡志林 · 第{ch_num}章「{ch_title_full}」</h1>
<p class="subtitle">
  <span style="display:block;margin-bottom:6px;color:#dc2626;font-weight:bold;font-size:12px;letter-spacing:2px;">SCQA · 情境 → 冲突 → 问题 → 回答</span>
  {subtitle}
</p>
<div class="divider"></div>
<div class="chapter-overview">
  <p>{overview}</p>
</div>

<div class="kpi-row">
{kpi_html}</div>

{sec_html}
<div class="takeaway">
  <div class="takeaway-label">核心启悟</div>
  <div class="takeaway-text">{takeaway}</div>
</div>

<div class="footer">来源：《东坡志林》卷五·论古/人物　|　（宋）苏轼 著　|　万卷出版公司　|　信息图生成于 2026-06-20</div>

</div>
</body>
</html>'''


def en_page(ch_num, ch_title_short, ch_title_full_en, subtitle, overview, kpis, sections, takeaway, footer_title):
    kpi_html = ""
    colors = ['c01','c02','c03','c04']
    for i, (icon, val, label) in enumerate(kpis):
        kpi_html += f'''    <div class="kpi-card {colors[i]}">
      <div class="kpi-num {colors[i]}">{val}</div>
      <div class="kpi-label">{label}</div>
    </div>\n'''

    sec_html = ""
    sec_styles = [('section-01','num-01','tag-01','t-01'),
                  ('section-02','num-02','tag-02','t-02'),
                  ('section-03','num-03','tag-03','t-03'),
                  ('section-04','num-04','tag-04','t-04'),
                  ('section-05','num-05','tag-05','t-05')]
    for i, (tag_label, sec_title, sec_desc, extra_html) in enumerate(sections):
        ei = i if i < 5 else 4
        ss, sn, st, stt = sec_styles[ei]
        extra = extra_html if extra_html else ""
        sec_html += f'''<div class="section {ss}">
  <div class="section-num {sn}">{i+1:02d}</div>
  <div class="section-body">
    <div class="tag {st}">{tag_label}</div>
    <div class="section-title {stt}">{sec_title}</div>
    <div class="section-desc">{sec_desc}</div>
    {extra}
  </div>
</div>\n'''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dongpo's Jottings · Chapter {ch_num}</title>
<style>
  @font-face {{font-family:'FZXPYZS';src:url('../TTF/方正屏显雅宋简体.TTF') format('truetype');font-weight:normal;font-style:normal}}
  *{{margin:0;padding:0;box-sizing:border-box}}
  body{{background:#f5f1eb;font-family:'PingFang SC','Noto Serif SC','STSong',Georgia,serif;display:flex;justify-content:center;align-items:flex-start;min-height:100vh;padding:40px 20px 60px}}
  .container{{max-width:880px;width:100%}}
  h1{{font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif;font-size:36px;color:#1a1a1a;text-align:center;line-height:1.4;margin-bottom:8px;font-weight:normal;letter-spacing:1.5px}}
  .subtitle{{text-align:center;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif;font-size:14px;color:#888;margin-bottom:24px;line-height:1.7;max-width:640px;margin-left:auto;margin-right:auto}}
  .divider{{width:60px;height:3px;background:linear-gradient(90deg,#dc2626,#ea580c);margin:0 auto 28px;border-radius:2px}}
  .section{{background:#fff;border-radius:14px;margin-bottom:18px;padding:24px 28px;box-shadow:0 1px 3px rgba(0,0,0,.04);display:flex;gap:20px;align-items:flex-start;border-left:4px solid transparent}}
  .section-01{{border-left-color:#dc2626}}.section-02{{border-left-color:#ea580c}}.section-03{{border-left-color:#ca8a04}}.section-04{{border-left-color:#4f46e5}}.section-05{{border-left-color:#db2777}}
  .section-num{{flex-shrink:0;width:42px;height:42px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:17px;font-weight:bold;margin-top:2px;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif}}
  .num-01{{background:#fef2f2;color:#dc2626}}.num-02{{background:#fff7ed;color:#ea580c}}.num-03{{background:#fefce8;color:#ca8a04}}.num-04{{background:#eef2ff;color:#4f46e5}}.num-05{{background:#fdf2f8;color:#db2777}}
  .section-body{{flex:1}}
  .tag{{display:inline-block;font-size:11px;font-weight:bold;padding:2px 10px;border-radius:10px;margin-bottom:8px;letter-spacing:1px;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif}}
  .tag-01{{background:#fef2f2;color:#dc2626}}.tag-02{{background:#fff7ed;color:#ea580c}}.tag-03{{background:#fefce8;color:#ca8a04}}.tag-04{{background:#eef2ff;color:#4f46e5}}.tag-05{{background:#fdf2f8;color:#db2777}}
  .section-title{{font-size:18px;margin-bottom:10px;font-weight:bold;line-height:1.4;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif}}
  .t-01{{color:#dc2626}}.t-02{{color:#ea580c}}.t-03{{color:#ca8a04}}.t-04{{color:#4f46e5}}.t-05{{color:#db2777}}
  .section-desc{{font-size:14px;color:#555;line-height:1.9;margin-bottom:14px}}
  .dual-grid{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:10px}}
  .dual-card{{border-radius:12px;padding:18px 20px;display:flex;gap:12px;align-items:flex-start}}
  .dual-card.yes{{background:#fef2f2;border:1px solid #fecaca}}
  .dual-card.no{{background:#f0fdf4;border:1px solid #bbf7d0}}
  .dual-icon{{font-size:24px;flex-shrink:0;line-height:1}}
  .dual-text h4{{font-size:14px;color:#1a1a1a;margin-bottom:4px;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif}}
  .dual-text p{{font-size:12px;color:#777;line-height:1.6}}
  .flow-row{{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-top:6px}}
  .flow-step{{background:#eef2ff;border:1px solid #c7d2fe;border-radius:10px;padding:10px 12px;text-align:center;min-width:80px;flex:1;font-size:13px;color:#3730a3;line-height:1.5;font-weight:bold}}
  .flow-arrow{{font-size:20px;color:#4f46e5;flex-shrink:0;font-weight:bold}}
  .flow-step.end{{background:#fef2f2;border-color:#fecaca;color:#991b1b}}
  .quote-block{{background:#f8f6f3;border-radius:12px;padding:18px 22px;margin-top:10px;border:1px solid #e8e0d5}}
  .quote-text{{font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif;font-size:15px;color:#1a1a1a;line-height:1.9;font-style:italic;margin-bottom:6px}}
  .quote-source{{font-size:12px;color:#aaa;text-align:right}}
  .confusion-table{{margin-top:10px}}
  .confusion-row{{display:flex;align-items:center;gap:12px;margin-bottom:8px;background:#fffbeb;border:1px solid #fde68a;border-radius:10px;padding:10px 16px}}
  .confusion-left{{flex:1;text-align:right;font-size:13px;color:#92400e;font-weight:bold;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif}}
  .confusion-arrow{{flex-shrink:0;font-size:18px;color:#ca8a04;font-weight:bold}}
  .confusion-right{{flex:1;font-size:13px;color:#713f12}}
  .kpi-row{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:28px}}
  .kpi-card{{background:#fff;border-radius:12px;padding:18px 14px;text-align:center;box-shadow:0 1px 3px rgba(0,0,0,.04);border-top:3px solid transparent}}
  .kpi-card.c01{{border-top-color:#dc2626}}.kpi-card.c02{{border-top-color:#ea580c}}.kpi-card.c03{{border-top-color:#ca8a04}}.kpi-card.c04{{border-top-color:#4f46e5}}
  .kpi-num{{font-size:28px;font-weight:bold;margin-bottom:4px;font-family:'FZXPYZS','PingFang SC',serif}}
  .kpi-num.c01{{color:#dc2626}}.kpi-num.c02{{color:#ea580c}}.kpi-num.c03{{color:#ca8a04}}.kpi-num.c04{{color:#4f46e5}}
  .kpi-label{{font-size:12px;color:#888;line-height:1.5}}
  .takeaway{{background:#fff;border:1px solid #e8e0d5;border-radius:14px;padding:24px 32px;margin-bottom:18px;box-shadow:0 1px 3px rgba(0,0,0,.04);border-left:4px solid #dc2626}}
  .takeaway-label{{font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif;font-size:12px;color:#dc2626;letter-spacing:2px;margin-bottom:6px;font-weight:bold}}
  .takeaway-text{{font-size:16px;color:#1a1a1a;line-height:1.9;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif}}
  .footer{{text-align:center;margin-top:32px;padding-top:20px;border-top:1px solid #e8e0d5;color:#bbb;font-size:13px;line-height:1.8}}
  .lang-switch{{text-align:right;margin-bottom:16px}}
  .lang-btn{{display:inline-block;padding:6px 16px;border-radius:8px;font-size:13px;text-decoration:none;letter-spacing:.03em;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif;background:#fef2f2;color:#dc2626;border:1px solid #fecaca;transition:opacity .15s}}
  .lang-btn:hover{{opacity:.75}}
  .chapter-overview{{background:#f8f6f3;border-left:3px solid #4f46e5;border-radius:8px;padding:16px 20px;margin:12px 0 24px;font-size:14px;color:#555;line-height:1.8;font-family:'FZXPYZS','PingFang SC',serif}}
  .chapter-overview p{{margin:0}}
  .back-catalog{{text-align:right;margin-bottom:4px}}
  .back-catalog-btn{{display:inline-block;padding:5px 14px;border-radius:8px;font-size:12px;text-decoration:none;letter-spacing:.02em;background:#eef2ff;color:#4f46e5;border:1px solid #c7d2fe;transition:opacity .15s}}
  .back-catalog-btn:hover{{opacity:.75}}
  @media(max-width:640px){{.section{{flex-direction:column;align-items:center;text-align:center;border-left:none;border-top:4px solid transparent;padding-top:20px}}.section-01{{border-top-color:#dc2626}}.section-02{{border-top-color:#ea580c}}.section-03{{border-top-color:#ca8a04}}.section-04{{border-top-color:#4f46e5}}.section-05{{border-top-color:#db2777}}.dual-grid,.kpi-row{{grid-template-columns:1fr}}.flow-row{{flex-direction:column}}.flow-arrow{{transform:rotate(90deg)}}.confusion-row{{flex-direction:column;align-items:stretch}}.confusion-left{{text-align:center}}.container{{padding:0 8px}}h1{{font-size:26px}}}}
</style>
</head>
<body>
<div class="container">
<div class="back-catalog"><a class="back-catalog-btn" href="东坡志林-catalog.html">← Back to Chapter Catalog</a></div>
<div class="lang-switch">
  <a class="lang-btn" target="_blank" href="东坡志林-ch{ch_num}-info-zh.html">English / 中文</a>
</div>

<h1>Dongpo's Jottings · {ch_title_full_en}</h1>
<p class="subtitle">
  <span style="display:block;margin-bottom:6px;color:#dc2626;font-weight:bold;font-size:12px;letter-spacing:2px;">SCQA · Situation → Complication → Question → Answer</span>
  {subtitle}
</p>
<div class="divider"></div>
<div class="chapter-overview">
  <p>{overview}</p>
</div>

<div class="kpi-row">
{kpi_html}</div>

{sec_html}
<div class="takeaway">
  <div class="takeaway-label">KEY INSIGHT</div>
  <div class="takeaway-text">{takeaway}</div>
</div>

<div class="footer">Source: Dongpo's Jottings, Scroll 5 · Historical Discourses & Character Sketches | By Su Shi (Song Dynasty) | Wanjuan Publishing | Infographic generated 2026-06-20</div>

</div>
</body>
</html>'''


# ════════════════════════════════════════
# CHAPTER 9: 战略与兴衰 — 迁都·伐国·养士
# ════════════════════════════════════════

ch09_zh = zh_page("9",
    "迁都·伐国·养士",
    "战略与兴衰——苏轼的地缘政治学",
    # subtitle (SCQA)
    "面对王朝的兴衰成败，苏轼从《史记》《左传》中抽丝剥茧。周平王为什么一迁都就亡了国？秦始皇为什么在灭楚之战中险象环生？六国为什么能长久存在而秦朝却二世而亡？三个看似不相干的问题，被苏轼串联成一套地缘政治学的完整论述——迁都即是放弃根基、伐国不可急于求成、养士方能维持社会稳定。这些来自千年前的洞见，至今仍在叩问每一个治世者。",
    # overview
    "本章汇集苏轼《论古》三篇长文——「周东迁失计」「秦拙取楚」「游士失职之祸」。三篇合在一起，构成了苏轼对王朝兴衰的三维分析：地理维（迁都即弃田宅）、军事维（取国当如拔龆齿）、社会维（失士则失天下）。苏轼以史家之眼、策士之笔，在千年之后，为后世治者留下了不可不察的镜鉴。",
    # kpis
    [("🏛️", "3", "篇长文<br>周东迁·秦取楚·游士论"),
     ("📊", "8+9+∞", "迁都8例·养士<br>9诸侯·无穷士"),
     ("⚔️", "60万", "王翦伐楚<br>空国而战的冒险"),
     ("🧭", "3维分析", "地理·军事·社会<br>王朝兴衰三维模型")],
    # sections
    [("迁都之鉴",
      "周东迁失计——「一败而粥田宅」的地理宿命",
      "苏轼以一句惊人的比喻开篇：周平王放弃丰镐、东迁洛邑，好比一个富裕人家「一败而粥田宅」。夏商两朝，先王德业不如周，后王败落不亚于幽厉，却延续五六百年——因为它们从未放弃根基。苏轼列举了历史上八次迁都：盘庚迁殷是复旧地，古公迁岐是逐水草，齐晋迁都皆在盛时；而「其余避寇而迁都，未有不亡」。最精彩的案例是东晋苏峻之乱时王导力阻迁都——「金陵，王者之都也。王者不以丰俭移都」，终使晋室复安。苏轼感慨：若周平王有一个王导，定不迁之计，收丰镐遗民，修文武成康之政，齐晋虽强，「未敢贰也，而秦何自霸哉？」结论掷地有声：周之失计，未有如东迁之缪者。",
      '<div class="confusion-table"><div class="confusion-row"><div class="confusion-left">夏商：不迁都</div><div class="confusion-arrow">→</div><div class="confusion-right">延续五六百年，天下宗之</div></div><div class="confusion-row"><div class="confusion-left">周：东迁洛邑</div><div class="confusion-arrow">→</div><div class="confusion-right">名存实亡，终以不振</div></div><div class="confusion-row"><div class="confusion-left">8次避寇迁都</div><div class="confusion-arrow">→</div><div class="confusion-right">魏·楚·汉·李景，未有不亡</div></div></div><div class="quote-block"><div class="quote-text">使平王有一王导，定不迁之计……齐、晋虽强，未敢贰也，而秦何自霸哉？</div><div class="quote-source">——苏轼「周东迁失计」</div></div>'),
     ("伐国之术",
      "秦拙取楚——「如取龆齿，必以渐」的军事哲学",
      "苏轼分析秦始皇统一六国的时间线：十八年取韩，二十二年取魏，二十五年取赵取楚，二十六年取燕取齐。他认为秦的胜利「非有道也，特巧耳，非幸也」。真正精彩的是「巧于取齐而拙于取楚」的辩证：秦人用四十年不加兵于齐来麻痹齐国、瓦解三晋联盟——这是「巧」；却在伐楚时以李信二十万人不克，再以王翦六十万人「空国而战」——这是「拙」。苏轼的比喻妙绝：「古之取国者必有数，如取龆齿也，必以渐，故齿脱而儿不知。今秦易楚，以为龆齿也，可拔，遂抉其口，一拔而取之，儿必伤，吾指为啮。」吴国三年迭出方入郢都，晋平吴、隋平陈皆用此法。而苻坚不懂此理，虽有百倍之众，终败于淝水。结论：始皇幸胜，而坚不幸。",
      '<div class="flow-row"><div class="flow-step">秦麻痹齐国<br>40年不加兵</div><div class="flow-arrow">→</div><div class="flow-step">瓦解三晋<br>逐一击破</div><div class="flow-arrow">→</div><div class="flow-step">巧取天下<br>非道也，特巧耳</div></div><div class="quote-block" style="margin-top:12px"><div class="quote-text">如取龆齿也，必以渐，故齿脱而儿不知。</div><div class="quote-source">——苏轼「秦拙取楚」</div></div>'),
     ("养士之道",
      "游士失职之祸——「纵百万虎狼于山林」的社会动力学",
      "苏轼从战国养士之风入手——越王勾践有君子六千人，战国四公子各有客三千，田文招任侠六万家于薛，稷下谈者千人——「度其余，当倍官吏而半农夫」。他的核心论点石破天惊：六国虐民不亚于秦，为何百姓无人叛？因为「凡民之秀杰者多以客养之，不失其职也。其力耕以奉上，皆椎鲁无能为者，虽欲怨叛，而莫为之先」。秦始皇的致命错误是并天下后以客为无用，「堕名城，杀豪杰，民之秀异者散而归田亩」。苏轼将这一政策比作「纵百万虎狼于山林而饥渴之」——「不知其将噬人，世以始皇为智，吾不信也」。秦之亡不在二世，而在始皇使天下士人失业的那一刻。",
      '<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🏛️</div><div class="dual-text"><h4>六国养士：社会稳定器</h4><p>「凡民之秀杰者多以客养之，不失其职也。」六国之君虐民不减始皇，然百姓无一人叛——因为精英阶层被养士制度容纳。</p></div></div><div class="dual-card no"><div class="dual-icon">⚡</div><div class="dual-text"><h4>秦驱士归田：社会定时炸弹</h4><p>「堕名城，杀豪杰，民之秀异者散而归田亩。」纵百万虎狼于山林而饥渴之——秦之亡不在二世，而在始皇。</p></div></div></div>')],
    # takeaway
    "三篇长文，三个维度。周东迁失计是地理维——放弃根基则名存实亡；秦拙取楚是军事维——急于求成则反伤自身；游士失职之祸是社会维——精英失业则天下必乱。苏轼用看似散漫的随笔，构建了一套完整的王朝兴衰分析模型：一个国家的存亡，不在于某个君王的道德高下，而在于能否守住地理根基、把握军事节奏、容纳社会精英。这三件事，比任何道德说教都更接近历史的真相。",
    "战略与兴衰——迁都·伐国·养士"
)

ch09_en = en_page("9",
    "Relocation·Conquest·Talent",
    "Chapter 9 · Strategy & Fate — Su Shi's Geopolitics",
    "Facing the rise and fall of dynasties, Su Shi drew insights from the Records of the Grand Historian and the Zuo Tradition. Why did the Zhou dynasty collapse after moving east? Why did Qin nearly lose its war against Chu? Why did the Six Kingdoms endure for centuries while Qin fell within two generations? Three seemingly unrelated questions form a complete geopolitical thesis: relocate your capital and you abandon your roots; conquer a kingdom hastily and you wound yourself; lose your elite talent and you lose the world. These millennium-old insights still challenge every ruler today.",
    "This chapter brings together three major essays from Su Shi's 'Historical Discourses': 'The Zhou&rsquo;s Fatal Eastward Move,' 'Qin&rsquo;s Clumsy Conquest of Chu,' and 'The Calamity of Unemployed Scholars.' Together they form a three-dimensional analysis of dynastic rise and fall: the geographic dimension (relocation = selling ancestral property), the military dimension (conquest must be gradual like pulling a baby tooth), and the social dimension (lose the elite and lose the state). With a historian's eye and a strategist's pen, Su Shi leaves posterity an indispensable mirror.",
    [("🏛️", "3", "Major Essays\nZhou·Qin·Scholar Crisis"),
     ("📊", "8+∞", "8 Capital Relocations\nCountless Unemployed"),
     ("⚔️", "600K", "Wang Jian's Chu\nCampaign gamble"),
     ("🧭", "3D Model", "Geographic·Military·Social\nDynastic Analysis")],
    [("Relocation Folly",
      "The Zhou&rsquo;s Fatal Eastward Move — 'One Defeat, Sold the Family Estate'",
      "Su Shi opens with a stunning metaphor: King Ping of Zhou abandoning Fenghao for Luoyang is like a wealthy family 'selling their ancestral estate at the first setback.' Xia and Shang, whose founding kings' virtue was no greater than Zhou&rsquo;s and whose later rulers' decadence matched You and Li, each lasted five or six centuries — because they never abandoned their roots. Su Shi catalogs eight historical relocations: Pangeng returned to Yin's old territory, Gugong moved to Qishan among nomads, Qi and Jin relocated at their zenith; but 'those who moved their capital to escape invaders — none escaped destruction.' The highlight: during the Su Jun Rebellion, Wang Dao blocked the relocation plan with 'Jinling is the city of kings; a king does not move his capital for wealth or poverty' — and Jin survived. Su Shi laments: had King Ping had a Wang Dao, with an unshaken capital, recovering Fenghao's remnants, restoring Wen-Wu-Cheng-Kang's governance, 'Qi and Jin, however strong, would not dare rebel — and how could Qin ever have risen to hegemony?'",
      '<div class="confusion-table"><div class="confusion-row"><div class="confusion-left">Xia·Shang: Never moved</div><div class="confusion-arrow">→</div><div class="confusion-right">Endured 500-600 years, all submitted</div></div><div class="confusion-row"><div class="confusion-left">Zhou: Moved east</div><div class="confusion-arrow">→</div><div class="confusion-right">A name alive, a state dead</div></div><div class="confusion-row"><div class="confusion-left">8 wartime relocations</div><div class="confusion-arrow">→</div><div class="confusion-right">Wei·Chu·Han·Li Jing — all perished</div></div></div><div class="quote-block"><div class="quote-text">Had King Ping possessed one Wang Dao... Qi and Jin, however strong, would not dare rebel — and how could Qin ever have risen to hegemony?</div><div class="quote-source">— Su Shi, &quot;The Zhou&rsquo;s Fatal Eastward Move&quot;</div></div>'),
     ("Conquest Strategy",
      "Qin&rsquo;s Clumsy Conquest of Chu — 'Like Pulling a Baby Tooth'",
      "Su Shi traces Qin&rsquo;s unification timeline: year 18 took Han, year 22 Wei, year 25 Zhao and Chu, year 26 Yan and Qi. Qin&rsquo;s victory, he argues, was 'not by the Dao, only by cunning, and not even luck.' The brilliant dialectic: Qin was 'clever in taking Qi' — forty years without attacking, lulling Qi into dissolving the Three Jin alliance — yet 'clumsy in taking Chu,' first sending Li Xin with 200,000 men (failed), then Wang Jian with 600,000 ('emptying the state for battle'). The metaphor is exquisite: 'In ancient times, taking a kingdom was like pulling a baby tooth — gradually, so the tooth falls out without the child noticing. Qin treated Chu as a loose tooth, pried open the mouth, yanked it out — the child must be hurt, the fingers bitten.' Wu attacked Chu in waves for three years before entering Ying. Jin pacified Wu, Sui pacified Chen, all using this method. Only Fu Jian, with a hundred-fold larger army, failed at Feishui. Conclusion: the First Emperor won by luck; Fu Jian was simply unlucky.",
      '<div class="flow-row"><div class="flow-step">Qin Lulls Qi\n40 yrs no attack</div><div class="flow-arrow">→</div><div class="flow-step">Dissolves 3 Jin\nAlliance collapses</div><div class="flow-arrow">→</div><div class="flow-step">World Unified\nBy cunning, not Dao</div></div><div class="quote-block" style="margin-top:12px"><div class="quote-text">Taking a kingdom was like pulling a baby tooth — gradually, so the tooth falls out without the child noticing.</div><div class="quote-source">— Su Shi, &quot;Qin&rsquo;s Clumsy Conquest of Chu&quot;</div></div>'),
     ("Talent Retention",
      "The Calamity of Unemployed Scholars — 'Loosing Millions of Tigers into Starving Mountains'",
      "Su Shi begins with the Warring States patronage system: King Goujian kept 6,000 gentlemen; the Four Lords each maintained 3,000 retainers; Tian Wen gathered 60,000 knights-errant in Xue; the Jixia Academy hosted a thousand debaters — 'estimating the remainder, they would double the officials and equal half the farmers.' His core argument is shocking: the Six Kings oppressed their people no less than Qin, yet no peasant rebelled — because 'the elite were all absorbed as retainers, never losing their station. Those who farmed were dullards incapable of leadership; even if they resented their lot, none could lead.' The First Emperor's fatal error: after unification, he deemed retainers useless, 'destroyed famous cities, killed heroes, and sent the talented back to the fields.' Su Shi compares this to 'loosing millions of tigers and wolves into starving mountains' — 'not knowing they would devour men, the world considers the First Emperor wise; I do not believe it.' Qin&rsquo;s fall began not under the Second Emperor but the moment the First Emperor rendered the entire elite class unemployed.",
      '<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🏛️</div><div class="dual-text"><h4>Six Kingdoms: Retainer System as Social Stabilizer</h4><p>&quot;The elite were all absorbed as retainers, never losing their station." Though kings oppressed no less than Qin, none rebelled — because talent had its place.</p></div></div><div class="dual-card no"><div class="dual-icon">⚡</div><div class="dual-text"><h4>Qin: Driving Talent to the Fields</h4><p>&quot;Destroyed famous cities, killed heroes, sent the talented back to the fields." Loosing millions of tigers into starving mountains — Qin&rsquo;s collapse was ordered by the First Emperor himself.</p></div></div></div>')],
    "Three essays, three dimensions. The Zhou&rsquo;s eastward move is the geographic dimension — abandon your roots and your name outlives your substance. Qin&rsquo;s clumsy conquest of Chu is the military dimension — haste wounds the conqueror. The unemployed scholars' calamity is the social dimension — lose the elite and lose the state. Su Shi, through seemingly casual jottings, constructed a complete model of dynastic rise and fall: a state's survival depends not on the morality of any single ruler, but on maintaining geographic foundations, military pacing, and elite social integration. These three truths come closer to history's reality than any moral sermon.",
    "Strategy & Fate — Relocation, Conquest & Talent"
)


# ════════════════════════════════════════
# CHAPTER 10: 权力与忠奸 — 君臣之间
# ════════════════════════════════════════

ch010_zh = zh_page("10",
    "君臣·忠奸·智愚",
    "权力与人性——君臣之间的生死棋局",
    "在权力的棋盘上，君臣之间的关系从来不是简单的忠诚与背叛。苏轼用三篇精妙的论说——「论子胥种蠡」「赵高李斯」「隐公不幸」——剖开了权力游戏中最幽暗的角落。从春秋到秦朝，从楚国到咸阳宫，忠诚是什么？背叛又是什么？当扬雄用道德教条丈量历史人物时，苏轼一把撕开所有的标签：问题从来不是忠奸与否，而是智慧与愚蠢的较量。在权力面前，智者的忠诚可能是逃跑，愚者的忠诚可能是送死。",
    "本章汇集苏轼三篇权力分析——「论子胥种蠡」谈功成身退与忠诚的定义，「赵高李斯」谈制度之恶如何催生背叛，「隐公不幸」谈政治中智与愚的生死分界。三篇从不同角度解剖同一个命题：在绝对权力面前，个人的道德选择空间何其狭窄；但正因如此，智慧的选择才弥足珍贵。",
    [("👥", "6", "位历史人物<br>子胥·种·蠡·赵高<br>李斯·鲁隐公"),
     ("🔪", "5", "起弑君事件<br>从春秋到秦二世"),
     ("📜", "3", "篇论说<br>子胥种蠡·赵高李斯<br>隐公不幸"),
     ("♟️", "权力棋局", "忠诚·背叛·智慧<br>愚蠢·生·死")],
    [("功成身退",
      "论子胥种蠡——范蠡的智慧与扬雄的愚见",
      "苏轼开篇即做惊人之论：范蠡虽知勾践「长颈鸟喙，可与共患难，不可与共逸乐」，功成之后浮海而去，但苏轼说「以吾相蠡，蠡亦鸟喙也」——范蠡也是这样的人。他耕于海滨、力作营千金，「屡散而复积」——「岂非才有余而道不足」？苏轼以鲁仲连为对照：鲁连退秦军后，平原君欲以千金为寿，他笑而辞去、终身不复见——「所贵于天下士者，为人排难解纷而无所取也。」范蠡虽知进退，却放不下财富。更精彩的是苏轼对扬雄的批驳：扬雄以三谏不去、鞭尸籍馆来苛责伍子胥，苏轼怒斥——「三谏而去，为人臣交浅者言也。至于子胥，吴之宗臣，与国存亡者也，去将安往哉？百谏不听，继之以死可也。」他反问：「父不受诛，子复仇，礼也。生则斩首，死则鞭尸，发其至痛，无所择也。扬雄独非人子乎？」对大夫种和范蠡，扬雄又以不強谏勾践来苛责，苏轼一笑——「此皆儿童之见。」",
      '<div class="flow-row"><div class="flow-step">范蠡浮海<br>功成身退</div><div class="flow-arrow">→</div><div class="flow-step">耕于海滨<br>屡散复积</div><div class="flow-arrow">→</div><div class="flow-step end">才有余<br>而道不足</div></div><div class="quote-block" style="margin-top:12px"><div class="quote-text">三谏而去，为人臣交浅者言也。至于子胥，吴之宗臣，与国存亡者也。</div><div class="quote-source">——苏轼「论子胥种蠡」</div></div>'),
     ("制度之恶",
      "赵高李斯——法家严刑如何制造背叛",
      "苏轼追问一个千古谜题：李斯何等聪明，为何听信赵高，葬送了大秦帝国？他的回答深刻：不是李斯智不足，而是秦国的法家制度已经把所有正常的人性反应都杀死了。秦始皇的权威「如雷电鬼神，不可测也」——商鞅「立信于徙木，立威于弃灰，刑其亲戚师傅」，积累了无与伦比的威信。到了始皇，「秦人视其君如雷电鬼神」，以至于荆轲行刺时「持兵者熟视始皇环柱而走，莫之救者，以秦法重故也」。在这样的制度下，扶苏接到赐死诏书「宁死而不请」——因为他知道请了也没用。李斯之所以不畏惧扶苏、蒙恬，正是因为「知威令之素行，而臣子不敢复请也」。苏轼的结论震耳欲聋：「夫以法毒天下者，未有不反中其身及其子孙者也。」他以周公、孔子为对照：「以忠恕为心而以平易为政，则上易知而下易达。」法家的极致效率，最终反噬了法家的创造者。",
      '<div class="confusion-table"><div class="confusion-row"><div class="confusion-left">商鞅立信·立威·刑亲</div><div class="confusion-arrow">→</div><div class="confusion-right">秦人视君「如雷电鬼神」</div></div><div class="confusion-row"><div class="confusion-left">扶苏接到伪诏</div><div class="confusion-arrow">→</div><div class="confusion-right">「宁死而不请」——知请亦无用</div></div><div class="confusion-row"><div class="confusion-left">李斯不惧蒙恬扶苏</div><div class="confusion-arrow">→</div><div class="confusion-right">「知威令之素行，臣子不敢复请」</div></div></div><div class="quote-block"><div class="quote-text">夫以法毒天下者，未有不反中其身及其子孙者也。</div><div class="quote-source">——苏轼「赵高李斯」</div></div>'),
     ("智愚生死",
      "隐公不幸——政治场上的愚蠢比背叛更致命",
      "鲁隐公是苏轼笔下最令人唏嘘的悲剧人物。当公子翚向他请求去杀桓公、以换取太宰之位时，隐公的回答充满了仁者的温情：「为其少故也，吾将授之矣。使营菟裘，吾将老焉。」——桓公还年幼，我本来就要把王位还给他，我已经在菟裘建造退休的居所了。但这句话非但没有感化公子翚，反而使他「惧，反谮公于桓公而弑之」。苏轼的叹息锋利如刀：「隐公之智，曾不若是涂人也，哀哉！」——路边行人看到盗贼都知道捕击，因为若不击则盗将并杀自己，隐公的智慧竟不如路人。苏轼以骊姬、里克和赵高、李斯两组对照案例说明一个规律：小人之为乱，总是先找到最脆弱的环节下手。李斯本可以「召百官、陈六师而斩之」，却选择了另一条路——「非下愚而何！」结尾以郑小同（被司马师毒杀）和王允之（以醉吐避祸）的对比收束——乱臣如蝮蛇，其所螫草木犹足以杀人。",
      '<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🛡️</div><div class="dual-text"><h4>王允之：醉吐避祸的智者</h4><p>夜饮闻王敦密谋造反，大吐污衣面。王敦见其「卧吐中」，果不疑。岌岌乎危矣，以智全生。</p></div></div><div class="dual-card no"><div class="dual-icon">💀</div><div class="dual-text"><h4>郑小同：诚实致死的愚者</h4><p>诣司马师，师密疏未屏。师问：「见吾疏乎？」答曰：「不见。」师曰：「宁我负卿，无卿负我。」遂鸩之。哀哉！</p></div></div></div><div class="quote-block"><div class="quote-text">隐公之智，曾不若是涂人也，哀哉！</div><div class="quote-source">——苏轼「隐公不幸」</div></div>')],
    # takeaway
    "六位历史人物，三种权力悲剧。伍子胥、范蠡、文种的命运告诉我们：忠诚不是一个固定的姿势，而是一种审时度势的智慧——子胥死得壮烈，范蠡逃得聪明，而扬雄用道德教条去丈量他们，「此皆儿童之见」。赵高和李斯的剧本则揭示了制度的结构性暴力：当法律成为绝对的恐怖，连聪明的李斯也只能走上愚蠢的绝路——「夫以法毒天下者，未有不反中其身及其子孙者也。」隐公、里克、李斯、郑小同、王允之这五人，生与死的分界线不是道德上的善恶，而是智慧上的高下——在乱世中，「危邦不入，乱邦不居」，孔子的这句警告，是苏轼留给我们的终极安全法则。",
    "权力与人性——君臣之间的生死棋局"
)

ch010_en = en_page("10",
    "Loyalty·Betrayal·Wisdom",
    "Chapter 10 · Power & Humanity — The Life-or-Death Chessboard Between Sovereign and Subject",
    "On the chessboard of power, the relationship between ruler and minister has never been simply loyalty versus betrayal. Su Shi dissects power's darkest corners through three exquisite discourses: 'On Wu Zixu, Wen Zhong, and Fan Li,' 'Zhao Gao and Li Si,' and 'The Misfortune of Duke Yin of Lu.' From the Spring and Autumn period to the Qin dynasty, from Chu to the Xianyang Palace — what is loyalty? What is betrayal? When Yang Xiong measured historical figures with moral yardsticks, Su Shi tore away every label: the real question is never loyalty versus betrayal, but wisdom versus folly. Before absolute power, a wise man's loyalty may be escape, a fool's loyalty may be suicide.",
    "This chapter brings together three of Su Shi's power analyses: 'On Wu Zixu, Wen Zhong, and Fan Li' examines timely withdrawal and the definition of loyalty; 'Zhao Gao and Li Si' reveals how institutional evil manufactures betrayal; 'The Misfortune of Duke Yin' maps the life-or-death boundary between political wisdom and stupidity. From three angles, one proposition: before absolute power, the space for individual moral choice is terrifyingly narrow — which is precisely why wise choices are so precious.",
    [("👥", "6", "Historical Figures\nZixu·Zhong·Li·Zhao\nLi Si·Duke Yin"),
     ("🔪", "5", "Regicides\nSpring & Autumn → Qin II"),
     ("📜", "3", "Discourses\nZixu·Zhao-Li\nDuke Yin"),
     ("♟️", "Power Mat", "Loyalty·Betrayal·Wisdom\nFolly·Life·Death")],
    [("Timely Withdrawal",
      "On Wu Zixu, Wen Zhong, and Fan Li — Fan Li's Wisdom vs. Yang Xiong's Folly",
      "Su Shi opens with a startling judgment: Fan Li recognized Goujian's 'long neck and bird beak — share hardship but not pleasure,' and sailed away after victory. Yet Su Shi says, 'if I physiognomize Fan Li, Fan Li too had a bird beak.' Fan Li farmed by the sea, labored to amass a thousand gold pieces, 'repeatedly dispersing and accumulating wealth' — 'is this not talent exceeding Dao?' Su Shi contrasts with Lu Zhonglian: after Lu forced Qin&rsquo;s retreat, Lord Pingyuan offered him a thousand gold pieces; Lu laughed and declined, vanishing forever — 'what the world honors in a scholar is resolving difficulties without taking anything.' Fan Li knew when to leave but could not let go of wealth. Even better: Su Shi demolishes Yang Xiong's criticism of Wu Zixu for not leaving after three remonstrations: 'Three remonstrations then leave — that is for ministers of shallow ties. As for Zixu, he was a founding minister of Wu, living and dying with the state. Where could he go? Remonstrate a hundred times unheard, then die — that is acceptable.' He asks: 'A father unjustly killed, a son takes revenge — this is ritual propriety. Alive, behead him; dead, whip his corpse, venting extreme grief, with no alternative. Is Yang Xiong alone not someone&rsquo;s son?'",
      '<div class="flow-row"><div class="flow-step">Fan Li Sails Away\nTimely Withdrawal</div><div class="flow-arrow">→</div><div class="flow-step">Farms by Sea\nAmasses Wealth</div><div class="flow-arrow">→</div><div class="flow-step end">Talent Exceeds\nDao — Incomplete</div></div><div class="quote-block" style="margin-top:12px"><div class="quote-text">&quot;Three remonstrations then leave&quot; — that is for ministers of shallow ties. Zixu was a founding minister, living and dying with the state.</div><div class="quote-source">— Su Shi, &quot;On Wu Zixu, Wen Zhong, and Fan Li&quot;</div></div>'),
     ("Institutional Evil",
      "Zhao Gao and Li Si — How Legalist Terror Manufactures Betrayal",
      "Su Shi probes an eternal puzzle: Li Si was so brilliant — why did he listen to Zhao Gao and bury the Qin empire? His answer is profound: not that Li Si lacked wisdom, but that Qin&rsquo;s Legalist system had killed every normal human response. The First Emperor's authority was 'like thunder, lightning, ghosts, and gods — unfathomable.' Shang Yang 'built trust by paying a man to move a log, built awe by amputating a man who dumped ashes, punished his own relatives and teachers,' accumulating ultimate prestige. By the First Emperor's reign, 'Qin people viewed their ruler as thunder, ghosts, and gods' — so much so that during Jing Ke's assassination attempt, 'armed guards watched the First Emperor run circles around pillars, none daring to help — because Qin&rsquo;s laws were too severe.' Under such a system, Fusu received a forged suicide edict and 'chose death rather than appeal' — knowing appeal was useless. Li Si did not fear Fusu and Meng Tian precisely because he 'knew the terror of commands was habitual, and subjects dared not question.' Su Shi's conclusion thunders: 'Those who poison the world with law invariably find it rebounding upon themselves and their descendants.'",
      '<div class="confusion-table"><div class="confusion-row"><div class="confusion-left">Shang Yang: Trust·Awe·Punished Kin</div><div class="confusion-arrow">→</div><div class="confusion-right">Qin people saw ruler as &quot;thunder, ghosts, gods&quot;</div></div><div class="confusion-row"><div class="confusion-left">Fusu received forged edict</div><div class="confusion-arrow">→</div><div class="confusion-right">"Chose death rather than appeal" — knew useless</div></div><div class="confusion-row"><div class="confusion-left">Li Si feared no one</div><div class="confusion-arrow">→</div><div class="confusion-right">"Knew terror was habitual; subjects dared not question"</div></div></div><div class="quote-block"><div class="quote-text">Those who poison the world with law invariably find it rebounding upon themselves and their descendants.</div><div class="quote-source">— Su Shi, "Zhao Gao and Li Si"</div></div>'),
     ("Wisdom or Death",
      "Duke Yin's Misfortune — Political Stupidity Kills More Surely Than Betrayal",
      "Duke Yin of Lu is Su Shi's most heartbreaking tragic figure. When Gongzi Hui asked permission to kill Duke Huan in exchange for the Grand Steward post, Duke Yin replied with a benevolent man's warmth: 'He is still young; I intended to yield the throne to him. I am building my retirement home at Tuqiu.' But instead of moving Hui, these words made him 'fear, then slander Duke Yin to Duke Huan, and assassinate him.' Su Shi's lament cuts like a knife: 'Duke Yin's wisdom could not match a passerby on the road — how sad!' A bystander seeing a bandit would capture and strike him, knowing otherwise the bandit would kill them too. Su Shi presents paired cases: Lady Li and Li Ke; Zhao Gao and Li Si — villains always target the weakest link first. Li Si could have 'summoned the hundred officials, arrayed the six divisions, and beheaded Gao' — he chose otherwise. 'If that is not utter stupidity, what is?' The chapter ends with the contrast between Zheng Xiaotong (poisoned by Sima Shi for honesty) and Wang Yunzhi (saved by feigning drunken vomiting) — treacherous ministers are like pit vipers; even the grass they bite can kill.",
      '<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🛡️</div><div class="dual-text"><h4>Wang Yunzhi: Feigned Drunkenness Saved Him</h4><p>Overheard Wang Dun plotting rebellion at a night banquet, vomited profusely, face and clothes soiled. Wang Dun saw him "lying in vomit" and dismissed suspicion. Saved by wits at the brink.</p></div></div><div class="dual-card no"><div class="dual-icon">💀</div><div class="dual-text"><h4>Zheng Xiaotong: Honesty Killed Him</h4><p>Visited Sima Shi, who left a secret memo unguarded. Shi asked: "Did you see my memo?" Answered honestly: "No." Shi: "Better I betray you than you betray me." Poisoned. Tragedy!</p></div></div></div><div class="quote-block"><div class="quote-text">Duke Yin's wisdom could not match a passerby on the road — how sad!</div><div class="quote-source">— Su Shi, "Duke Yin's Misfortune"</div></div>')],
    "Six historical figures, three types of power tragedy. The fates of Wu Zixu, Fan Li, and Wen Zhong teach us: loyalty is not a fixed posture but wisdom in reading the times — Zixu died heroically, Fan Li escaped cleverly, and Yang Xiong's moral yardsticks measured none of them, 'these are all childish views.' The Zhao Gao-Li Si drama reveals structural violence of institutions: when law becomes absolute terror, even the brilliant Li Si can only march down a stupid dead-end path — 'those who poison the world with law invariably find it rebounding upon themselves and their descendants.' Duke Yin, Li Ke, Li Si, Zheng Xiaotong, Wang Yunzhi — the line between life and death is not moral goodness versus evil, but wisdom versus folly. In turbulent times, 'do not enter a dangerous state, do not dwell in a chaotic state' — Confucius&rsquo;s warning is Su Shi's ultimate safety rule for us all.",
    "Power & Humanity — The Life-or-Death Chessboard Between Sovereign and Subject"
)


# ════════════════════════════════════════
# CHAPTER 11: 孔子与治道 — 礼法制度之辨
# ════════════════════════════════════════

ch011_zh = zh_page("11",
    "礼法·孔子·制度",
    "礼法与制度——孔子的治世理想与制度之辩",
    "当孔子面对鲁国三桓的跋扈时，他能做什么？当摄主制度在秦汉以后被母后摄政取代时，丢失了什么？当管仲「九合诸侯不以兵车」时，为什么孔子仍对他略有微词？苏轼在「论鲁三桓」「摄主」「七德八戒」三篇中，用纵横捭阖的史笔，将礼法制度这个抽象命题变得血肉丰满——他从孔子的政治实践出发，追问什么才是真正有效的治理之道：不是杀伐果断，不是权谋机变，而是以礼法为框架的制度之善。",
    "本章汇集苏轼三篇制度论——「论鲁三桓」讲孔子如何在权力夹缝中以礼法约束强卿，「摄主」辨古代理摄主制度与后世母后摄政的根本差异，「七德八戒」以七位「盛德」之人和八位「嗜杀」之人做对照，提出「治国如养生，未病而服药则药杀人」的终极政治哲学。",
    [("📖", "3", "篇制度论<br>鲁三桓·摄主<br>七德八戒"),
     ("🏛️", "7+8", "位历史案例<br>7盛德之人<br>8嗜杀之人"),
     ("🎯", "礼法", "核心命题<br>制度之善<br>胜于杀伐之威"),
     ("⚖️", "治道", "治国如养生<br>未病而服药<br>则药杀人")],
    [("孔子治鲁",
      "论鲁三桓——孔子如何在权力夹缝中推行礼法",
      "鲁定公十三年，孔子提出「臣无藏甲，大夫无百雉之城」——堕三都。叔孙氏先堕郈，季氏将堕费时公山不狃叛乱，最终堕成时公敛处父以成叛——孔子的改革面临巨大阻力。苏轼指出关键悖论：季氏曾亲自驱逐鲁昭公使其死于国外，「忌刻忮害」不亚于曹操，孔子怎能在此时毁其都城、削其军队？答案是孔子有一种「不言而信，不怒而威」的力量——「孔子以羁旅之臣得政期月，而能举治世之礼，以律亡国之臣，堕名都，出藏甲，而三桓不疑其害」。苏轼又用晏婴作对比：晏婴知「田氏之僭，惟礼可以已之」，但「婴能知之而不能为之」——其浩然之气「不及孔孟」。孔子晚年沐浴而朝告哀公请讨齐陈恒——此时他已七十一岁，距去世仅两年，仍不忘以《春秋》之法治理列国，「至于老且死而不忘」。",
      '<div class="confusion-table"><div class="confusion-row"><div class="confusion-left">晏婴知礼</div><div class="confusion-arrow">→</div><div class="confusion-right">「能知之而不能为之」——浩然之气不及孔孟</div></div><div class="confusion-row"><div class="confusion-left">孔子执政</div><div class="confusion-arrow">→</div><div class="confusion-right">「不言而信，不怒而威」——三桓不疑其害</div></div><div class="confusion-row"><div class="confusion-left">孔子晚年</div><div class="confusion-arrow">→</div><div class="confusion-right">七十一岁沐浴而朝请讨陈恒——「老且死而不忘」</div></div></div><div class="quote-block"><div class="quote-text">孔子以羁旅之臣得政期月，而能举治世之礼……此必有不言而信、不怒而威者矣。</div><div class="quote-source">——苏轼「论鲁三桓」</div></div>'),
     ("摄主之制",
      "摄主——秦汉以后丢失的制度智慧",
      "欧阳修认为鲁隐公是正式即位而非摄政，苏轼不同意——他引孔子与曾子的对话来论证「摄主」制度的存在。孔子解释：若国君去世时世子尚未出生，则由国君之弟或其兄弟之子暂代摄主；若遗腹子是女孩则摄主正式即位，若是男孩则摄主退位。苏轼认为这是「先王之令典，孔子之法言」——它的精髓在于确保权力始终留在先君血脉中，而非如后世母后摄政那样易引发异姓篡夺。苏轼列举：母后摄政而国安者仅有君王后、曹后、高后、向后等「千一」之人；而吕后、胡武灵、武则天之类「不胜其乱」。他发出追问：若母后可信则摄主亦可信；若均不可信，则摄主「犹吾先君之子孙也，不犹愈于异姓之取哉？」",
      '<div class="flow-row"><div class="flow-step">古制摄主<br>先王子孙继</div><div class="flow-arrow">→</div><div class="flow-step">世子生男<br>摄主退位</div><div class="flow-arrow">→</div><div class="flow-step">权力永在<br>先君血脉</div></div><div class="dual-grid" style="margin-top:10px"><div class="dual-card yes"><div class="dual-icon">👑</div><div class="dual-text"><h4>摄主制：权力在血脉之内</h4><p>季康子摄政，南孺子生男即退位——「古之道也，孔子行之。」确保权力不出先君子孙。</p></div></div><div class="dual-card no"><div class="dual-icon">⚠️</div><div class="dual-text"><h4>母后摄政：权力易落异姓</h4><p>「牝鸡之晨，惟家之索。」吕后、武氏「不胜其乱」，王莽杨坚「遂因以易姓」。</p></div></div></div>'),
     ("七德八戒",
      "七德八戒——「治国如养生」的终极政治哲学",
      "这是苏轼笔下最有方法论价值的一篇。他读史得出两组人：七位「盛德」之人——楚成王不杀重耳、汉高祖不杀吴王濞、晋武帝不杀刘元海、苻坚不杀慕容垂、唐明皇不杀安禄山等；但他们最终都遭遇了这些人的叛乱。八位「嗜杀」之人——汉景帝杀周亚夫、曹操杀孔融、晋文帝杀嵇康、唐太宗杀李君羡、武后杀裴炎等。「世之论者」皆以七人不杀为失，八人杀之为当。苏轼断然反对：「七人者皆自有以致败亡，非不杀之过也。」他的逻辑如手术刀般精准：齐景公不繁刑重赋，虽有田氏齐不可取；楚成王不用子玉，虽有晋文公兵不败……明皇不用李林甫杨国忠，「虽有安禄山，亦何能为？」最后以养生喻治国——「养生者不过慎起居饮食、节声色而已，节慎在未病之前，而服药于已病之后。今吾忧寒疾而先服乌喙……则病未作而药杀人矣。彼八人者，皆未病而服药者也。」杀无罪之人以求防患，是政治智慧的最低级形态。",
      '<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🏆</div><div class="dual-text"><h4>七位盛德之人：不妄杀</h4><p>楚成王不杀重耳、汉高祖不杀吴王濞、唐明皇不杀安禄山——「非不杀之过也」。国乱之因不在不杀，而在其他政策的失误。</p></div></div><div class="dual-card no"><div class="dual-icon">💀</div><div class="dual-text"><h4>八位嗜杀之人：未病服药</h4><p>汉景帝杀周亚夫、曹操杀孔融、晋文帝杀嵇康——「皆未病而服药者也」。以杀无罪求防患，乃「政治智慧的最低级形态」。</p></div></div></div><div class="quote-block"><div class="quote-text">治国如养生……忧寒疾而先服乌喙，忧热疾而先服甘遂，则病未作而药杀人矣。</div><div class="quote-source">——苏轼「七德八戒」</div></div>')],
    # takeaway
    "三篇制度论构成苏轼政治哲学的三重奏。孔子堕三都的实践说明：真正的权威不是来自刀剑而是来自信义——「不言而信、不怒而威」，三桓不疑其害。摄主之制的思考揭示：好的制度设计远比依赖个体道德可靠——权力留在血脉之内，胜过寄托于不可靠的母后。七德八戒的辨析则抵达了最高层次的政治智慧：治国如养生，真正的高明不是杀人防患，而是在未病之前建立健康的制度肌体——「节慎在未病之前，而服药于已病之后」。那些因为恐惧未来叛乱而杀害无罪之人者，「皆未病而服药者也」——毒药入腹，病变未至，人已先死。这就是苏轼留给所有治者的最后箴言。",
    "礼法与制度——孔子的治世理想与制度之辩"
)

ch011_en = en_page("11",
    "Ritual·Confucius·Institutions",
    "Chapter 11 · Ritual & Institutions — Confucius&rsquo;s Governance Ideal and the Debate on Systems",
    "When Confucius faced the arrogance of Lu&rsquo;s Three Huan families, what could he do? When the 'regent' institution was replaced by empress-dowager regencies after Qin-Han, what was lost? When Guan Zhong 'united the feudal lords nine times without military force,' why did Confucius still find him wanting? In three discourses — 'On Lu&rsquo;s Three Huan,' 'The Regent System,' and 'Seven Virtues, Eight Warnings' — Su Shi uses sweeping historical analysis to give flesh and blood to the abstract question of ritual institutions. Starting from Confucius&rsquo;s political practice, he asks what truly constitutes effective governance: not decisive killing, not strategic cunning, but institutional goodness framed by ritual propriety.",
    "This chapter brings together three institutional discourses: 'On Lu&rsquo;s Three Huan' shows how Confucius constrained powerful ministers through ritual in impossible circumstances; 'The Regent System' distinguishes the ancient regent institution from later empress-dowager regencies; 'Seven Virtues, Eight Warnings' contrasts seven virtuous figures with eight murderous ones, arriving at the ultimate political philosophy: 'governing a state is like nurturing health — taking medicine before illness strikes means the medicine kills you.'",
    [("📖", "3", "Institutional\nDiscourses"),
     ("🏛️", "7+8", "Historical Cases\n7 Virtuous\n8 Murderous"),
     ("🎯", "Ritual", "Core Thesis\nInstitutional Good\nOver Terror"),
     ("⚖️", "Governance", "State as Body\nPre-illness Care\nNot Preemptive Kill")],
    [("Confucius in Lu",
      "On Lu&rsquo;s Three Huan — How Confucius Advanced Ritual Amid a Power Vise",
      "In Duke Ding's 13th year, Confucius proposed 'ministers shall not hoard arms, grandees shall not have hundred-zhang city walls' — tear down the three capitals. Shusun first demolished Hou. When the Ji clan was about to demolish Fei, Gongshan Buniu rebelled. When they moved to demolish Cheng, Gonglian Chufu rebelled with Cheng — Confucius&rsquo;s reform faced immense resistance. Su Shi identifies the key paradox: the Ji clan had personally driven Duke Zhao into exile where he died, their 'jealous cruelty' matching Cao Cao's — how could Confucius destroy their cities and disarm them at such a moment? The answer: Confucius possessed a power of 'trusting without speaking, commanding awe without anger.' 'As a wandering minister who gained power for barely a month, Confucius could implement governance rituals, discipline ministers who would destroy a state, demolish famous cities, remove hidden arms — and the Three Huan never suspected him of harming them.' Su Shi contrasts with Yan Ying: Yan Ying knew 'the Tian usurpation can only be stopped by ritual,' but 'Ying could know it without enacting it' — his vast spirit 'could not match Confucius and Mencius.' In his twilight years, Confucius bathed and came to court asking Duke Ai to punish Chen Heng of Qi — at seventy-one, two years from death, still 'not forgetting until old age and death.'",
      '<div class="confusion-table"><div class="confusion-row"><div class="confusion-left">Yan Ying: Knew ritual</div><div class="confusion-arrow">→</div><div class="confusion-right">"Could know it without enacting it" — spirit unmatched</div></div><div class="confusion-row"><div class="confusion-left">Confucius: Governed</div><div class="confusion-arrow">→</div><div class="confusion-right">"Trusting without speaking, awe without anger" — Three Huan unsuspicious</div></div><div class="confusion-row"><div class="confusion-left">Confucius at 71</div><div class="confusion-arrow">→</div><div class="confusion-right">Bathed, came to court, asked to punish Chen Heng — &quot;not forgetting until old age and death&quot;</div></div></div><div class="quote-block"><div class="quote-text">As a wandering minister who gained power for barely a month, Confucius could implement governance rituals... This must come from trusting without speaking, commanding awe without anger.</div><div class="quote-source">— Su Shi, &quot;On Lu&rsquo;s Three Huan&quot;</div></div>'),
     ("The Regent System",
      "The Regent — Institutional Wisdom Lost After Qin-Han",
      "Ouyang Xiu argued Duke Yin of Lu was a formal ruler, not a regent. Su Shi disagrees — he cites Confucius&rsquo;s dialogue with Zengzi to prove the 'regent' institution existed. Confucius explained: if the heir is unborn when the ruler dies, the ruler&rsquo;s younger brother or nephew serves as regent; if the posthumous child is a girl, the regent formally ascends; if a boy, the regent steps down. Su Shi calls this 'the ancient kings' canonical code, Confucius&rsquo;s legal doctrine' — its essence is keeping power always within the former ruler&rsquo;s bloodline, unlike later empress-dowager regencies that invited usurpation by other surnames. Su Shi catalogs: empress-dowager regencies producing stable rule — only Junwang Hou, Empress Cao, Empress Gao, Empress Xiang, 'one in a thousand'; while Empress Lü, Hu Wuling, Wu Zetian brought 'uncontainable chaos,' and Wang Mang and Yang Jian 'changed the dynastic surname.' He asks: if empress-dowagers are trustworthy, regents too are trustworthy; if neither is, then a regent is 'still a descendant of our former ruler — is that not better than another surname seizing power?'",
      '<div class="flow-row"><div class="flow-step">Ancient Regent\nDescendant of Ruler</div><div class="flow-arrow">→</div><div class="flow-step">If Heir is Boy\nRegent Steps Down</div><div class="flow-arrow">→</div><div class="flow-step">Power Remains\nin Bloodline</div></div><div class="dual-grid" style="margin-top:10px"><div class="dual-card yes"><div class="dual-icon">👑</div><div class="dual-text"><h4>Regent System: Power in the Bloodline</h4><p>Ji Kangzi regency — stepped down when Nan Ruzi bore a boy. "The ancient way, practiced by Confucius." Power never leaves the former ruler&rsquo;s descendants.</p></div></div><div class="dual-card no"><div class="dual-icon">⚠️</div><div class="dual-text"><h4>Empress-Dowager Regency: Power Falls to Strangers</h4><p>"When the hen crows at dawn, the household faces ruin." Empress Lü, Wu Zetian — "uncontainable chaos." Wang Mang, Yang Jian "changed the surname."</p></div></div></div>'),
     (&quot;Seven Virtues, Eight Warnings&quot;,
      "Seven Virtues, Eight Warnings — 'Governing a State Is Like Nurturing Health'",
      "This is Su Shi's most methodologically valuable essay. From history he derives two groups: seven figures of 'flourishing virtue' — King Cheng of Chu did not kill Chong'er, Han Gaozu did not kill the King of Wu, Emperor Wu of Jin did not kill Liu Yuanhai, Fu Jian did not kill Murong Chui, Tang Minghuang did not kill An Lushan — yet all later faced rebellions from these very people. Eight 'murder-loving' figures — Han Jingdi killed Zhou Yafu, Cao Cao killed Kong Rong, Jin Wendi killed Ji Kang, Tang Taizong killed Li Junxian, Empress Wu killed Pei Yan, etc. 'Contemporary commentators' all said the seven erred by not killing and the eight were right to kill. Su Shi flatly rejects this: 'These seven each had their own causes of defeat — it was not the fault of not killing.' His logic is surgically precise: had Qi Jinggong not imposed harsh punishments and heavy taxes, even with the Tian clan Qi could not be taken; had Chu Chengwang not employed Ziyu, even with Jin Wengong his army would not have been defeated... had Minghuang not employed Li Linfu and Yang Guozhong, 'even with An Lushan, what could he have done?' The essay culminates in the healthcare metaphor: 'Nurturing health is merely caution in food, drink, and daily habits, moderating sensual pleasures. Caution comes before illness; medicine comes after. Now if I, fearing a cold illness, first take aconite... illness has not arrived but the medicine has killed me. Those eight persons all took medicine before falling ill.' Killing the innocent to preempt danger is the lowest form of political wisdom.",
      '<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🏆</div><div class="dual-text"><h4>7 Virtuous: Did Not Kill Recklessly</h4><p>King Cheng spared Chong\'er, Han Gaozu spared the King of Wu, Tang Minghuang spared An Lushan — "not the fault of not killing." The cause of chaos lay elsewhere.</p></div></div><div class="dual-card no"><div class="dual-icon">💀</div><div class="dual-text"><h4>8 Murderous: Took Medicine Before Illness</h4><p>Han Jingdi killed Zhou Yafu, Cao Cao killed Kong Rong, Jin Wendi killed Ji Kang — &quot;all took medicine before falling ill.&quot; Killing innocents preemptively is &quot;the lowest form of political wisdom.&quot;</p></div></div></div><div class="quote-block"><div class="quote-text">Governing a state is like nurturing health... Fearing cold, one first takes aconite; fearing heat, kansui root — illness has not struck, but the medicine has killed.</div><div class="quote-source">— Su Shi, &quot;Seven Virtues, Eight Warnings&quot;</div></div>')],
    "Three institutional discourses form Su Shi's political-philosophical trilogy. Confucius&rsquo;s destruction of the three capitals demonstrates: true authority comes not from swords but from trust — 'trusting without speaking, commanding awe without anger,' the Three Huan never suspected harm. The regent-system analysis reveals: good institutional design is far more reliable than reliance on individual virtue — keeping power in the bloodline surpasses entrusting it to unreliable empress-dowagers. The Seven Virtues, Eight Warnings dialectic reaches the highest level of political wisdom: governing is like nurturing health; true mastery is not killing to prevent disaster, but building healthy institutional bodies before illness — 'caution before illness, medicine after.' Those who killed innocents from fear of future rebellion 'all took medicine before falling ill' — poison swallowed, illness not yet arrived, but the person already dead. This is Su Shi's final admonition to all rulers.",
    "Ritual & Institutions — Confucius&rsquo;s Governance Ideal and the Debate on Systems"
)


# ════════════════════════════════════════
# CHAPTER 12: 士人风骨——人物品评
# ════════════════════════════════════════

ch012_zh = zh_page("12",
    "人物·风骨·世相",
    "士人风骨——苏轼品评历代人物的智慧之光",
    "如果前十一章是苏轼放眼江山、纵论古今的大文章，那么这一章是他俯身拾取的人性碎片——几十则短小精悍的人物点评，从尧舜禹到刘伶阮籍，从颜回到司马懿，从汉武帝到李后主。没有长篇大论，只有一针见血的洞见。苏轼在这些碎片中展现了他最令人倾倒的才华：在几百字甚至几十字之内，用一句比喻、一个反问、一次历史对照，就能穿透一个人的灵魂。这些人物品评，不是史家的冷眼旁观，而是一个历经沧桑的智者，用自己的人生经验去丈量每一个人物的灵魂深度。",
    "本章精选苏轼《人物》卷中最精彩的十二则人物品评——颜蠋的「晚食当肉」、汉武帝踞厕见卫青、李后主的亡国之泪、刘伶的「死便埋我」、荀卿的「青出于蓝」之谬、张仪的欺楚之术……每一则都是几百字的微缩传记，却闪耀着比长篇传记更锐利的人性洞察。",
    [("👤", "29", "则人物<br>品评短文"),
     ("📏", "12", "则精选<br>本章重点呈现"),
     ("✨", "千年", "跨度<br>从尧舜到五代"),
     ("🎭", "人性光谱", "圣贤·帝王·隐士<br>枭雄·名士·败者")],
    [("隐士风骨",
      "颜蠋·刘伶——何为真正的达观？",
      "苏轼对隐士的态度极其挑剔。颜蠋辞齐王而去，说「晚食以当肉，安步以当车，无罪以当贵，清静贞正以自娱」——战国之士中难有如此贤者。但苏轼偏不买账：「晚食以当肉，安步以当车，是犹有意于肉于车也。晚食自美，安步自适，取其美与适足矣，何以当肉与车为哉！」——你还在想着肉和车，就不是真正的达观。但他又忍不住补了一句：「虽然，蠋可谓巧于居贫者也……非我之久于贫，不能知蠋之巧也。」——这是谪居黄州的苏轼才能写出的补充。对刘伶，他更加不留情面：「刘伯伦常以锸自随，曰死即埋我。苏子曰，伯伦非达者也，棺椁衣衾，不害为达。苟为不然，死则已矣，何必更埋！」——死都死了，还惦记着让人用锸埋你，这不是执着是什么？",
      '<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🍃</div><div class="dual-text"><h4>颜蠋：近乎达观的居贫之巧</h4><p>「晚食自美，安步自适，取其美与适足矣，何以当肉与车为哉！」苏轼挑剔其有意于肉车，却又承认：「非我之久于贫，不能知蠋之巧。」</p></div></div><div class="dual-card no"><div class="dual-icon">🍶</div><div class="dual-text"><h4>刘伶：连死亡都执着</h4><p>「死即埋我」——苏轼说：「伯伦非达者也。苟为不然，死则已矣，何必更埋！」连死后怎么处理都要操心，谈何放达？</p></div></div></div>'),
     ("帝王之相",
      "汉武帝·李后主·晋惠帝——帝王的灵魂切片",
      "苏轼看帝王，只看一个小动作，一个表情，一句话。汉武帝——「踞厕见卫青，不冠不见汲长孺」：蹲在厕所接见大将军卫青，不戴帽子却不敢见汲黯。苏轼只说一句话：「若青奴才，雅宜舐痔，踞厕见之，正其宜也。」——卫青这种奴才本就该舔痔疮，蹲厕所里见他刚好合适。对李后主，苏轼引其绝命词「最是仓惶辞庙日，教坊犹奏别离歌，挥泪对宫娥」——然后一刀劈下：「后主既为樊若水所卖，举国与人，故当恸哭于九庙之外，谢其民而后行，顾乃挥泪宫娥，听教坊离曲！」亡国之时不对祖宗和百姓哭泣，却对着宫女流泪！晋惠帝太子时，晋武帝以探策卜其命运，「惠帝不肖，得一」——苏轼评：「盖神以实告。」神用最诚实的方式预告了晋朝的灭亡——一个「一」字，就是「不肖」的全部答案。",
      '<div class="confusion-table"><div class="confusion-row"><div class="confusion-left">汉武帝踞厕见卫青</div><div class="confusion-arrow">→</div><div class="confusion-right">「若青奴才，雅宜舐痔，踞厕见之，正其宜也。」</div></div><div class="confusion-row"><div class="confusion-left">李后主挥泪对宫娥</div><div class="confusion-arrow">→</div><div class="confusion-right">「当恸哭于九庙之外，谢其民而后行」——亡国哭错了对象</div></div><div class="confusion-row"><div class="confusion-left">晋惠帝探策得「一」</div><div class="confusion-arrow">→</div><div class="confusion-right">「盖神以实告」——一个数字预告了整个王朝的命运</div></div></div>'),
     ("智者之智",
      "荀卿·张仪·房琯——智者为何犯错？",
      "苏轼对一些公认的「智者」进行了不留情面的解剖。荀卿说「青出于蓝而青于蓝，冰生于水而寒于水」，世人以此证明弟子可胜于师。苏轼冷笑：「青即蓝也，冰即水也。酿米为酒……曰酒甘于米，膳羞美于羊，虽儿童必笑之，而荀卿以是为辨，信其醉梦颠倒之言！」——把本体和衍生物混为一谈，儿童都不会犯的逻辑错误。关于张仪欺楚以商於六百里：「此与儿戏无异，天下无不疾张子之诈而笑楚王之愚也。」但苏轼更关心的是另一种欺骗：后世的臣子欺君说「行吾言，天下举安，四夷皆服，礼乐兴而刑罚措」——「其君之所欲得者，非特六百里也，而卒无丝毫之获」。这种华而不实的承诺，比张仪的六百里有更大的杀伤力。房琯以刘秩为将，败于陈涛斜，杀四万人——苏轼叹：「挟区区之辨以待热洛河，疏矣。」一个纸上谈兵的书生以口辩代替军事常识，四万人的生命只证明了理论的空洞。",
      '<div class="quote-block"><div class="quote-text">后世之臣欺其君，曰：「行吾言，天下举安，四夷皆服，礼乐兴而刑罚措。」其君之所欲得者，非特六百里也，而卒无丝毫之获。</div><div class="quote-source">——苏轼评张仪欺楚</div></div>'),
     ("乱世相人",
      "司马懿·吕后·王衍——识破人的面具",
      "苏轼的人物洞察力在最阴暗的历史场景中最锋利。司马懿讨曹爽，桓范往奔之，蒋济说「驽马恋栈豆，必不能用也」——果然曹爽不听桓范之计，身死族灭。曹操擒陈宫、吕布后问陈宫：「公台平生自谓智有余，今日何如？」陈宫答：「此子不用宫言，不然未可知也！」苏轼评：「吕布、曹爽，何人也？而为之用，尚何言知！」——伺候这种蠢货主子，还有什么脸谈智慧！王衍降石勒后「自解无罪，且劝僭号」，苏轼不说王衍，而说他的女儿惠风：「刘曜陷洛，以惠风赐其将乔属。将妻之，惠风杖剑大骂而死。」一句感叹：「乃知王夷甫之死，非独惭见晋公卿，乃当羞见其女也。」——父亲劝降求活，女儿以死殉节，父亲的死不仅愧对同僚，更无颜见自己的女儿。王济以人乳蒸豚，王恺使妓吹笛「小失声韵便杀之」——苏轼评：「时武帝在也，而贵戚敢如此，知晋室之乱也久矣。」",
      '<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🗡️</div><div class="dual-text"><h4>王衍之女惠风</h4><p>「杖剑大骂而死」——父亲劝石勒僭号求生，女儿面对敌将从容赴死。苏轼：「乃当羞见其女也。」</p></div></div><div class="dual-card no"><div class="dual-icon">😈</div><div class="dual-text"><h4>王济·王恺</h4><p>「以人乳蒸豚」「小失声韵便杀之」——「时武帝在也，而贵戚敢如此，知晋室之乱也久矣。」</p></div></div></div>'),
     ("处世之道",
      "刘凝之·沈麟士——同一件事，两种境界",
      "两个人的鞋被认错了。刘凝之：被认错即与之，失主得鞋送还不肯复取。沈麟士：被认错也与之，失主送还，笑而受之。苏轼一语定高下：「此虽小事，然处事当如麟士，不当如凝之也。」为什么？刘凝之的「不肯复取」是一种道德洁癖——我不愿意有任何被误解的可能，所以宁可不拿回自己的鞋。沈麟士的「笑而受之」是一种通透——鞋是我的就是我的，别人搞错了还回来，我就笑着收下。前者是紧绷的道德表演，后者是松弛的智慧境界。在苏轼看来，真正的君子从不刻意展示自己的道德优越感——「笑而受之」，四字即是全部的人生哲学。",
      '<div class="quote-block"><div class="quote-text">此虽小事，然处事当如麟士，不当如凝之也。</div><div class="quote-source">——苏轼评刘凝之与沈麟士</div></div>')],
    # takeaway
    "二十九则人物品评，苏轼在这片人性的碎片之海中展现了他最自由的才华。他不做道德裁决——汉武帝踞厕见卫青，「正其宜也」；李后主挥泪对宫娥，「当恸哭于九庙之外」；王衍之女杖剑而死，「乃当羞见其女也」。他也不迷信任何既有标签——荀卿的辩证是「醉梦颠倒之言」，范蠡的功成身退「才有余而道不足」，刘伶的死便埋我「非达者也」。他唯一的标准是「通透」——沈麟士的「笑而受之」之所以高于刘凝之的「不肯复取」，因为前者不需要通过拒绝来证明操守。人物的高下，不在道德标签，而在灵魂的通透程度。这就是苏轼人物品评的终极尺度。",
    "士人风骨——苏轼品评历代人物的智慧之光"
)

ch012_en = en_page("12",
    "Character·Integrity·Society",
    "Chapter 12 · The Spirit of the Scholar — Su Shi's Piercing Character Sketches",
    "If the previous eleven chapters are Su Shi surveying landscapes and history with sweeping vision, this chapter is him bending down to gather fragments of human nature — dozens of terse, razor-sharp character sketches, from Yao, Shun, and Yu to Liu Ling and Ruan Ji, from Yan Hui to Sima Yi, from Emperor Wu of Han to the Last Ruler of Southern Tang. No lengthy treatises, only needle-point insights. In these fragments, Su Shi displays his most captivating talent: within a few hundred words, even a few dozen, with a single metaphor, a rhetorical question, a historical contrast, he penetrates a person's soul. These character sketches are not a historian's cold observations, but a weathered sage measuring each figure's spiritual depth with his own hard-won life experience.",
    "This chapter selects twelve of Su Shi's most brilliant character sketches from the 'Personages' scroll — Yan Zhu's 'late meals as meat,' Emperor Wu receiving Wei Qing from the toilet, the Last Ruler of Southern Tang's tears for palace ladies, Liu Ling's 'bury me when I die,' Xun Qing's fallacy of 'blue from indigo,' Zhang Yi's deceit of the King of Chu... each a miniature biography in a few hundred words, yet radiating sharper human insight than any full-length biography.",
    [("👤", "29", "Character\nSketches Total"),
     ("📏", "12", "Selected\nIn This Chapter"),
     ("✨", "3,000 yrs", "Timespan\nYao-Shun → Five Dynasties"),
     ("🎭", "Human Spectrum", "Sages·Emperors·Hermits\nWarlords·Literati·Losers")],
    [("The Hermit's Spirit",
      "Yan Zhu & Liu Ling — What Is True Detachment?",
      "Su Shi is extraordinarily demanding of hermits. Yan Zhu left the King of Qi, declaring: 'Late meals serve as meat, slow walks serve as carriage, innocence serves as nobility, quiet rectitude as self-delight' — among Warring States scholars, few matched such virtue. But Su Shi refuses to applaud: 'Late meals as meat, slow walks as carriage — this still shows attachment to meat and carriage. Late meals are delicious in themselves, slow walks are comfortable in themselves; take the deliciousness and comfort as enough — why compare them to meat and carriage!' You are still thinking about meat and carriages — that is not true detachment. Yet he cannot resist adding: 'Still, Yan Zhu can be called skillful at dwelling in poverty... had I not long endured poverty, I could not understand Zhu's skill.' Only Su Shi in Huangzhou exile could write that addendum. For Liu Ling, he is even more merciless: 'Liu Bolun always carried a spade, saying: "When I die, bury me." Su Shi says: Bolun was not a detached person. Coffin, shroud, grave-clothes — none harm detachment. Otherwise, dead is dead — why still need burying!' You're dead and still worried about someone digging you a grave — is that not attachment?",
      '<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🍃</div><div class="dual-text"><h4>Yan Zhu: Near-Detachment, Skillful in Poverty</h4><p>"Late meals are delicious in themselves, slow walks are comfortable — take the comfort as enough!" Su Shi critiques his lingering attachment to "meat and carriage," yet admits: "Had I not long endured poverty, I could not understand Zhu\'s skill."</p></div></div><div class="dual-card no"><div class="dual-icon">🍶</div><div class="dual-text"><h4>Liu Ling: Attached Even to Death</h4><p>"When I die, bury me" — Su Shi: "Bolun was not detached. Dead is dead — why still need burying!" Still worrying about post-mortem arrangements — what talk of freedom?</p></div></div></div>'),
     ("Emperors in Cross-Section",
      "Emperor Wu·Last Ruler of Tang·Emperor Hui — Soul Slices of Rulers",
      "Su Shi observes emperors through one gesture, one expression, one sentence. Emperor Wu of Han — 'squatting on the toilet to receive Wei Qing, yet not daring to meet Ji An without his cap.' Su Shi's single comment: 'Wei Qing, that slave, was well suited to licking hemorrhoids; receiving him squatting on the toilet was entirely appropriate.' For the Last Ruler of Southern Tang, Su Shi quotes his deathbed poem: 'Most harrowing, the day I fled the ancestral temple, musicians still played farewell songs, tears shed before palace ladies' — then cuts with a knife: 'The Last Ruler was betrayed by Fan Ruoshui, gave his entire state away — he should have wailed outside the Nine Temples, apologized to his people, then departed. Instead, he shed tears before palace ladies, listening to the academy play farewell songs!' Losing his kingdom, he wept before the wrong audience. When Crown Prince Hui of Jin drew a divination lot, the unworthy heir 'drew one' — Su Shi: 'The gods spoke truthfully.' A single number foretold an entire dynasty's doom.",
      '<div class="confusion-table"><div class="confusion-row"><div class="confusion-left">Emperor Wu, toilet, Wei Qing</div><div class="confusion-arrow">→</div><div class="confusion-right">"That slave suited licking hemorrhoids; receiving him from the toilet was entirely appropriate."</div></div><div class="confusion-row"><div class="confusion-left">Last Tang Ruler wept for palace ladies</div><div class="confusion-arrow">→</div><div class="confusion-right">"Should have wailed outside the Nine Temples, apologized to his people" — wept for the wrong audience</div></div><div class="confusion-row"><div class="confusion-left">Emperor Hui drew "One"</div><div class="confusion-arrow">→</div><div class="confusion-right">"The gods spoke truthfully" — one digit foretold a dynasty\'s doom</div></div></div>'),
     ("Why Smart People Err",
      "Xun Qing·Zhang Yi·Fang Guan — When the Brilliant Blunder",
      "Su Shi performs merciless dissection of recognized 'wise men.' Xun Qing said 'blue comes from indigo but surpasses indigo; ice forms from water but is colder than water' — the world took this as proof a student can surpass the teacher. Su Shi sneers: 'Blue IS indigo, ice IS water. Ferment rice into wine... to say wine is sweeter than rice, fine meat tastier than lamb — even a child would laugh, yet Xun Qing took this as dialectic. Truly the babblings of drunken dreams!' Conflating substance with derivative — a logical error even children avoid. On Zhang Yi deceiving the King of Chu with 600 li of territory: 'This was no different from child's play; the world condemns Zhang Yi's deceit and laughs at the Chu king&rsquo;s stupidity.' But Su Shi is more concerned with another deception: later ministers who tell their ruler 'Follow my words, the empire will be at peace, barbarians will submit, ritual and music will flourish, punishments shelved' — 'what their ruler desired was far more than 600 li, yet in the end, not a shred was gained.' Such grandiose empty promises are far deadlier than Zhang Yi's 600-li trick. Fang Guan appointed Liu Zhi as general, lost at Chentao Incline, 40,000 died — Su Shi sighs: 'Pitting mere rhetoric against the Reluo River — sloppy.' An armchair scholar substituting verbal cleverness for military common sense; 40,000 lives proved only the emptiness of theory.",
      '<div class="quote-block"><div class="quote-text">Later ministers who deceive their ruler say: "Follow my words, the empire will be at peace, barbarians will submit..." What their ruler desired was far more than 600 li, yet in the end, not a shred was gained.</div><div class="quote-source">— Su Shi, on Zhang Yi Deceiving Chu</div></div>'),
     ("Reading Faces in Chaos",
      "Sima Yi·Empress Lü·Wang Yan — Seeing Through the Mask",
      "Su Shi's character insight is sharpest in history's darkest scenes. Sima Yi attacked Cao Shuang; Huan Fan rushed to aid him, but Jiang Ji said 'A nag horse yearns for its stable beans — he cannot act on advice' — indeed, Cao Shuang ignored Huan Fan's strategy and perished. Cao Cao, having captured Chen Gong and Lü Bu, asked Chen Gong: 'You always claimed your wisdom exceeded others — how about today?' Chen Gong: 'This man would not heed my counsel; otherwise, who knows!' Su Shi's comment: 'Lü Bu, Cao Shuang — what kind of men? And you served them — what wisdom can you claim!' Serving idiot masters — what face to speak of intelligence! Wang Yan surrendered to Shi Le, 'excused himself of guilt and urged Shi Le to usurp the throne.' Su Shi does not discuss Wang Yan but his daughter Huifeng: 'When Liu Yao took Luoyang, he gave Huifeng to his general Qiao Shu. About to be forced into marriage, Huifeng seized a sword and died cursing.' One line: 'Thus we know Wang Yifu's death was not merely shame before Jin ministers, but shame before his own daughter.' Father urged usurpation to live; daughter chose death with honor — the father's death shames not only colleagues but his child. Wang Ji steamed pork in human milk; Wang Kai killed courtesans for 'slightly off-pitch flute notes' — Su Shi: 'Emperor Wu was alive then, yet nobles dared this — we know Jin's chaos had been brewing long.'",
      '<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🗡️</div><div class="dual-text"><h4>Wang Yan\'s Daughter Huifeng</h4><p>"Seized a sword and died cursing" — Father urged Shi Le to usurp to save his life; daughter faced the enemy general with death. Su Shi: "Shame before his own daughter."</p></div></div><div class="dual-card no"><div class="dual-icon">😈</div><div class="dual-text"><h4>Wang Ji·Wang Kai</h4><p>"Steamed pork in human milk" "Killed for slightly off-pitch flute" — "Emperor Wu was alive, yet nobles dared this — Jin\'s chaos had been brewing long."</p></div></div></div>'),
     ("The Art of Living",
      "Liu Ningzhi & Shen Linshi — Same Situation, Two States of Mind",
      "Two men had their shoes mistaken by others. Liu Ningzhi: his were taken by mistake, he gave them away; the real owner returned them, he refused to take them back. Shen Linshi: his were taken by mistake, he also gave them away; the real owner returned them, he laughed and accepted. Su Shi's judgment is swift: 'Though a small matter, in conducting oneself, one should be like Linshi, not Ningzhi.' Why? Liu's refusal was moral fastidiousness — I would rather not retrieve my shoes than risk being misunderstood. Shen's laughing acceptance was clarity — these are my shoes, someone made a mistake, they're returned, I laugh and take them. The former is tense moral performance; the latter is relaxed wisdom. In Su Shi's view, a true noble person never strains to display moral superiority — 'laughing, he accepted': four words containing an entire life philosophy.",
      '<div class="quote-block"><div class="quote-text">Though a small matter, in conducting oneself, one should be like Linshi, not Ningzhi.</div><div class="quote-source">— Su Shi, on Liu Ningzhi and Shen Linshi</div></div>')],
    "Twenty-nine character sketches — in this sea of human fragments, Su Shi displays his freest talent. He renders no moral verdicts — Emperor Wu receiving Wei Qing from the toilet: 'entirely appropriate'; the Last Tang Ruler weeping for palace ladies: 'should have wailed at the Nine Temples'; Wang Yan's daughter dying by the sword: 'shame before his own daughter.' He trusts no established labels — Xun Qing's dialectic is 'babblings of drunken dreams,' Fan Li's timely withdrawal shows 'talent exceeding Dao,' Liu Ling's 'bury me when I die' demonstrates 'not detachment.' His sole criterion is clarity — Shen Linshi's 'laughing, he accepted' surpasses Liu Ningzhi's 'refused to take them back' because the former needs no rejection to prove integrity. A person's stature lies not in moral labels but in spiritual clarity. This is Su Shi's ultimate measure in character judgment.",
    "The Spirit of the Scholar — Su Shi's Piercing Character Sketches"
)


# ═══════════════════ WRITE ALL FILES ═══════════════════

files = [
    ("东坡志林-ch009-info-zh.html", ch09_zh),
    ("东坡志林-ch009-info-en.html", ch09_en),
    ("东坡志林-ch010-info-zh.html", ch010_zh),
    ("东坡志林-ch010-info-en.html", ch010_en),
    ("东坡志林-ch011-info-zh.html", ch011_zh),
    ("东坡志林-ch011-info-en.html", ch011_en),
    ("东坡志林-ch012-info-zh.html", ch012_zh),
    ("东坡志林-ch012-info-en.html", ch012_en),
]

for fname, content in files:
    path = os.path.join(OUT, fname)
    with open(path, 'w', encoding='utf-8') as f:\n        f.write(content)\n    size_kb = len(content.encode('utf-8')) / 1024\n    print(f"✅ Written: {fname} ({size_kb:.1f} KB)")

print("\n🎉 All 8 files generated for 东坡志林 ch009~ch012!")