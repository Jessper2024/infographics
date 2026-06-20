#!/usr/bin/env python3
"""Generate 东坡志林 ch009-012 infographic HTML (zh+en, 8 files).
Uses template functions with data defined in triple-quoted strings to avoid quoting issues."""

import os

OUT = os.path.dirname(os.path.abspath(__file__))

CSS = '''  @font-face{font-family:'FZXPYZS';src:url('../TTF/方正屏显雅宋简体.TTF') format('truetype');font-weight:normal;font-style:normal}
  *{margin:0;padding:0;box-sizing:border-box}
  body{background:#f5f1eb;font-family:'PingFang SC','Noto Serif SC','STSong',Georgia,serif;display:flex;justify-content:center;align-items:flex-start;min-height:100vh;padding:40px 20px 60px}
  .container{max-width:880px;width:100%}
  h1{font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif;font-size:36px;color:#1a1a1a;text-align:center;line-height:1.4;margin-bottom:8px;font-weight:normal;letter-spacing:1.5px}
  .subtitle{text-align:center;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif;font-size:14px;color:#888;margin-bottom:24px;line-height:1.7;max-width:640px;margin-left:auto;margin-right:auto}
  .divider{width:60px;height:3px;background:linear-gradient(90deg,#dc2626,#ea580c);margin:0 auto 28px;border-radius:2px}
  .section{background:#fff;border-radius:14px;margin-bottom:18px;padding:24px 28px;box-shadow:0 1px 3px rgba(0,0,0,.04);display:flex;gap:20px;align-items:flex-start;border-left:4px solid transparent}
  .section-01{border-left-color:#dc2626}.section-02{border-left-color:#ea580c}.section-03{border-left-color:#ca8a04}.section-04{border-left-color:#4f46e5}.section-05{border-left-color:#db2777}
  .section-num{flex-shrink:0;width:42px;height:42px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:17px;font-weight:bold;margin-top:2px;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif}
  .num-01{background:#fef2f2;color:#dc2626}.num-02{background:#fff7ed;color:#ea580c}.num-03{background:#fefce8;color:#ca8a04}.num-04{background:#eef2ff;color:#4f46e5}.num-05{background:#fdf2f8;color:#db2777}
  .section-body{flex:1}
  .tag{display:inline-block;font-size:11px;font-weight:bold;padding:2px 10px;border-radius:10px;margin-bottom:8px;letter-spacing:1px;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif}
  .tag-01{background:#fef2f2;color:#dc2626}.tag-02{background:#fff7ed;color:#ea580c}.tag-03{background:#fefce8;color:#ca8a04}.tag-04{background:#eef2ff;color:#4f46e5}.tag-05{background:#fdf2f8;color:#db2777}
  .section-title{font-size:18px;margin-bottom:10px;font-weight:bold;line-height:1.4;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif}
  .t-01{color:#dc2626}.t-02{color:#ea580c}.t-03{color:#ca8a04}.t-04{color:#4f46e5}.t-05{color:#db2777}
  .section-desc{font-size:14px;color:#555;line-height:1.9;margin-bottom:14px}
  .dual-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:10px}
  .dual-card{border-radius:12px;padding:18px 20px;display:flex;gap:12px;align-items:flex-start}
  .dual-card.yes{background:#fef2f2;border:1px solid #fecaca}
  .dual-card.no{background:#f0fdf4;border:1px solid #bbf7d0}
  .dual-icon{font-size:24px;flex-shrink:0;line-height:1}
  .dual-text h4{font-size:14px;color:#1a1a1a;margin-bottom:4px;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif}
  .dual-text p{font-size:12px;color:#777;line-height:1.6}
  .flow-row{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-top:6px}
  .flow-step{background:#eef2ff;border:1px solid #c7d2fe;border-radius:10px;padding:10px 12px;text-align:center;min-width:80px;flex:1;font-size:13px;color:#3730a3;line-height:1.5;font-weight:bold}
  .flow-arrow{font-size:20px;color:#4f46e5;flex-shrink:0;font-weight:bold}
  .flow-step.end{background:#fef2f2;border-color:#fecaca;color:#991b1b}
  .quote-block{background:#f8f6f3;border-radius:12px;padding:18px 22px;margin-top:10px;border:1px solid #e8e0d5}
  .quote-text{font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif;font-size:15px;color:#1a1a1a;line-height:1.9;font-style:italic;margin-bottom:6px}
  .quote-source{font-size:12px;color:#aaa;text-align:right}
  .confusion-table{margin-top:10px}
  .confusion-row{display:flex;align-items:center;gap:12px;margin-bottom:8px;background:#fffbeb;border:1px solid #fde68a;border-radius:10px;padding:10px 16px}
  .confusion-left{flex:1;text-align:right;font-size:13px;color:#92400e;font-weight:bold;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif}
  .confusion-arrow{flex-shrink:0;font-size:18px;color:#ca8a04;font-weight:bold}
  .confusion-right{flex:1;font-size:13px;color:#713f12}
  .kpi-row{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:28px}
  .kpi-card{background:#fff;border-radius:12px;padding:18px 14px;text-align:center;box-shadow:0 1px 3px rgba(0,0,0,.04);border-top:3px solid transparent}
  .kpi-card.c01{border-top-color:#dc2626}.kpi-card.c02{border-top-color:#ea580c}.kpi-card.c03{border-top-color:#ca8a04}.kpi-card.c04{border-top-color:#4f46e5}
  .kpi-num{font-size:28px;font-weight:bold;margin-bottom:4px;font-family:'FZXPYZS','PingFang SC',serif}
  .kpi-num.c01{color:#dc2626}.kpi-num.c02{color:#ea580c}.kpi-num.c03{color:#ca8a04}.kpi-num.c04{color:#4f46e5}
  .kpi-label{font-size:12px;color:#888;line-height:1.5}
  .takeaway{background:#fff;border:1px solid #e8e0d5;border-radius:14px;padding:24px 32px;margin-bottom:18px;box-shadow:0 1px 3px rgba(0,0,0,.04);border-left:4px solid #dc2626}
  .takeaway-label{font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif;font-size:12px;color:#dc2626;letter-spacing:2px;margin-bottom:6px;font-weight:bold}
  .takeaway-text{font-size:16px;color:#1a1a1a;line-height:1.9;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif}
  .footer{text-align:center;margin-top:32px;padding-top:20px;border-top:1px solid #e8e0d5;color:#bbb;font-size:13px;line-height:1.8}
  .lang-switch{text-align:right;margin-bottom:16px}
  .lang-btn{display:inline-block;padding:6px 16px;border-radius:8px;font-size:13px;text-decoration:none;letter-spacing:.03em;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif;background:#fef2f2;color:#dc2626;border:1px solid #fecaca;transition:opacity .15s}
  .lang-btn:hover{opacity:.75}
  .chapter-overview{background:#f8f6f3;border-left:3px solid #4f46e5;border-radius:8px;padding:16px 20px;margin:12px 0 24px;font-size:14px;color:#555;line-height:1.8;font-family:'FZXPYZS','PingFang SC',serif}
  .chapter-overview p{margin:0}
  .back-catalog{text-align:right;margin-bottom:4px}
  .back-catalog-btn{display:inline-block;padding:5px 14px;border-radius:8px;font-size:12px;text-decoration:none;letter-spacing:.02em;background:#eef2ff;color:#4f46e5;border:1px solid #c7d2fe;transition:opacity .15s}
  .back-catalog-btn:hover{opacity:.75}
  @media(max-width:640px){.section{flex-direction:column;align-items:center;text-align:center;border-left:none;border-top:4px solid transparent;padding-top:20px}.section-01{border-top-color:#dc2626}.section-02{border-top-color:#ea580c}.section-03{border-top-color:#ca8a04}.section-04{border-top-color:#4f46e5}.section-05{border-top-color:#db2777}.dual-grid,.kpi-row{grid-template-columns:1fr}.flow-row{flex-direction:column}.flow-arrow{transform:rotate(90deg)}.confusion-row{flex-direction:column;align-items:stretch}.confusion-left{text-align:center}.container{padding:0 8px}h1{font-size:26px}}'''

def build_page(lang, ch_num, h1_text, subtitle, overview, kpis, sections, takeaway, footer_text):
    """Build complete HTML page. lang = 'zh' or 'en'."""
    if lang == 'zh':
        back_text = '← 返回章节目录'
        lang_text = '中文 / English'
        lang_href = f'东坡志林-ch{ch_num}-info-en.html'
        scqa_label = 'SCQA · 情境 → 冲突 → 问题 → 回答'
        takeaway_label = '核心启悟'
        footer_src = f'来源：《东坡志林》卷五·论古/人物　|　（宋）苏轼 著　|　万卷出版公司　|　信息图生成于 2026-06-20'
        html_lang = 'zh-CN'
        title = f'东坡志林 · 第{ch_num}章'
    else:
        back_text = '← Back to Chapter Catalog'
        lang_text = 'English / 中文'
        lang_href = f'东坡志林-ch{ch_num}-info-zh.html'
        scqa_label = 'SCQA · Situation → Complication → Question → Answer'
        takeaway_label = 'KEY INSIGHT'
        footer_src = 'Source: Dongpo\'s Jottings, Scroll 5 · Historical Discourses &amp; Character Sketches | By Su Shi (Song Dynasty) | Wanjuan Publishing | Infographic generated 2026-06-20'
        html_lang = 'en'
        title = f'Dongpo\'s Jottings · Chapter {ch_num}'

    # Build KPI cards
    kpi_html = ''
    kpi_colors = ['c01', 'c02', 'c03', 'c04']
    for i, (val, label) in enumerate(kpis):
        kpi_html += f'''    <div class="kpi-card {kpi_colors[i]}">
      <div class="kpi-num {kpi_colors[i]}">{val}</div>
      <div class="kpi-label">{label}</div>
    </div>
'''

    # Build sections
    sec_html = ''
    sec_styles = [
        ('section-01', 'num-01', 'tag-01', 't-01'),
        ('section-02', 'num-02', 'tag-02', 't-02'),
        ('section-03', 'num-03', 'tag-03', 't-03'),
        ('section-04', 'num-04', 'tag-04', 't-04'),
        ('section-05', 'num-05', 'tag-05', 't-05'),
    ]
    for i, (tag_label, sec_title, sec_desc, extra_html) in enumerate(sections):
        ei = i if i < 5 else 4
        ss, sn, st, stt = sec_styles[ei]
        extra = extra_html if extra_html else ''
        sec_html += f'''<div class="section {ss}">
  <div class="section-num {sn}">{i+1:02d}</div>
  <div class="section-body">
    <div class="tag {st}">{tag_label}</div>
    <div class="section-title {stt}">{sec_title}</div>
    <div class="section-desc">{sec_desc}</div>
    {extra}
  </div>
</div>
'''

    page = f'''<!DOCTYPE html>
<html lang="{html_lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
{CSS}
</style>
</head>
<body>
<div class="container">
<div class="back-catalog"><a class="back-catalog-btn" href="东坡志林-catalog.html">{back_text}</a></div>
<div class="lang-switch">
  <a class="lang-btn" target="_blank" href="{lang_href}">{lang_text}</a>
</div>

<h1>{h1_text}</h1>
<p class="subtitle">
  <span style="display:block;margin-bottom:6px;color:#dc2626;font-weight:bold;font-size:12px;letter-spacing:2px;">{scqa_label}</span>
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
  <div class="takeaway-label">{takeaway_label}</div>
  <div class="takeaway-text">{takeaway}</div>
</div>

<div class="footer">{footer_text}</div>

</div>
</body>
</html>'''
    return page


def write_ch(ch_num, zh_h1, zh_sub, zh_over, zh_kpis, zh_sections, zh_take, zh_foot,
                    en_h1, en_sub, en_over, en_kpis, en_sections, en_take, en_foot):
    zh_html = build_page('zh', ch_num, zh_h1, zh_sub, zh_over, zh_kpis, zh_sections, zh_take, zh_foot)
    en_html = build_page('en', ch_num, en_h1, en_sub, en_over, en_kpis, en_sections, en_take, en_foot)
    zh_path = os.path.join(OUT, f'东坡志林-ch{ch_num}-info-zh.html')
    en_path = os.path.join(OUT, f'东坡志林-ch{ch_num}-info-en.html')
    with open(zh_path, 'w', encoding='utf-8') as f:
        f.write(zh_html)
    with open(en_path, 'w', encoding='utf-8') as f:
        f.write(en_html)
    print(f'  ✅ 东坡志林-ch{ch_num}-info-zh.html ({len(zh_html.encode("utf-8"))//1024} KB)')
    print(f'  ✅ 东坡志林-ch{ch_num}-info-en.html ({len(en_html.encode("utf-8"))//1024} KB)')


# ════════════════════════════════════════
# CHAPTER 9 DATA
# ════════════════════════════════════════

ch09_zh_h1 = '东坡志林 · 第九章「战略与兴衰——迁都·伐国·养士」'
ch09_zh_sub = '面对王朝的兴衰成败，苏轼从《史记》《左传》中抽丝剥茧。周平王为什么一迁都就亡了国？秦始皇为什么在灭楚之战中险象环生？六国为什么能长久存在而秦朝却二世而亡？三个看似不相干的问题，被苏轼串联成一套地缘政治学的完整论述——迁都即是放弃根基、伐国不可急于求成、养士方能维持社会稳定。这些来自千年前的洞见，至今仍在叩问每一个治世者。'
ch09_zh_over = '本章汇集苏轼《论古》三篇长文——「周东迁失计」「秦拙取楚」「游士失职之祸」。三篇合在一起，构成了苏轼对王朝兴衰的三维分析：地理维（迁都即弃田宅）、军事维（取国当如拔龆齿）、社会维（失士则失天下）。苏轼以史家之眼、策士之笔，在千年之后，为后世治者留下了不可不察的镜鉴。'
ch09_zh_kpis = [('3', '篇长文<br>周东迁·秦取楚·游士论'),
                ('8+9+∞', '迁都8例·养士<br>9诸侯·无穷士'),
                ('60万', '王翦伐楚<br>空国而战的冒险'),
                ('3维分析', '地理·军事·社会<br>王朝兴衰三维模型')]
ch09_zh_sections = [
    ('迁都之鉴',
     '周东迁失计——「一败而粥田宅」的地理宿命',
     '苏轼以一句惊人的比喻开篇：周平王放弃丰镐、东迁洛邑，好比一个富裕人家「一败而粥田宅」。夏商两朝，先王德业不如周，后王败落不亚于幽厉，却延续五六百年——因为它们从未放弃根基。苏轼列举了历史上八次迁都：盘庚迁殷是复旧地，古公迁岐是逐水草，齐晋迁都皆在盛时；而「其余避寇而迁都，未有不亡」。最精彩的案例是东晋苏峻之乱时王导力阻迁都——「金陵，王者之都也。王者不以丰俭移都」，终使晋室复安。苏轼感慨：若周平王有一个王导，定不迁之计，收丰镐遗民，修文武成康之政，齐晋虽强，「未敢贰也，而秦何自霸哉？」结论掷地有声：周之失计，未有如东迁之缪者。',
     '<div class="confusion-table"><div class="confusion-row"><div class="confusion-left">夏商：不迁都</div><div class="confusion-arrow">→</div><div class="confusion-right">延续五六百年，天下宗之</div></div><div class="confusion-row"><div class="confusion-left">周：东迁洛邑</div><div class="confusion-arrow">→</div><div class="confusion-right">名存实亡，终以不振</div></div><div class="confusion-row"><div class="confusion-left">8次避寇迁都</div><div class="confusion-arrow">→</div><div class="confusion-right">魏·楚·汉·李景，未有不亡</div></div></div><div class="quote-block"><div class="quote-text">使平王有一王导，定不迁之计……齐、晋虽强，未敢贰也，而秦何自霸哉？</div><div class="quote-source">——苏轼「周东迁失计」</div></div>'),
    ('伐国之术',
     '秦拙取楚——「如取龆齿，必以渐」的军事哲学',
     '苏轼分析秦始皇统一六国的时间线：十八年取韩，二十二年取魏，二十五年取赵取楚，二十六年取燕取齐。他认为秦的胜利「非有道也，特巧耳，非幸也」。真正精彩的是「巧于取齐而拙于取楚」的辩证：秦人用四十年不加兵于齐来麻痹齐国、瓦解三晋联盟——这是「巧」；却在伐楚时以李信二十万人不克，再以王翦六十万人「空国而战」——这是「拙」。苏轼的比喻妙绝：「古之取国者必有数，如取龆齿也，必以渐，故齿脱而儿不知。今秦易楚，以为龆齿也，可拔，遂抉其口，一拔而取之，儿必伤，吾指为啮。」吴国三年迭出方入郢都，晋平吴、隋平陈皆用此法。而苻坚不懂此理，虽有百倍之众，终败于淝水。结论：始皇幸胜，而坚不幸。',
     '<div class="flow-row"><div class="flow-step">秦麻痹齐国<br>40年不加兵</div><div class="flow-arrow">→</div><div class="flow-step">瓦解三晋<br>逐一击破</div><div class="flow-arrow">→</div><div class="flow-step">巧取天下<br>非道也，特巧耳</div></div><div class="quote-block" style="margin-top:12px"><div class="quote-text">如取龆齿也，必以渐，故齿脱而儿不知。</div><div class="quote-source">——苏轼「秦拙取楚」</div></div>'),
    ('养士之道',
     '游士失职之祸——「纵百万虎狼于山林」的社会动力学',
     '苏轼从战国养士之风入手——越王勾践有君子六千人，战国四公子各有客三千，田文招任侠六万家于薛，稷下谈者千人——「度其余，当倍官吏而半农夫」。他的核心论点石破天惊：六国虐民不亚于秦，为何百姓无人叛？因为「凡民之秀杰者多以客养之，不失其职也。其力耕以奉上，皆椎鲁无能为者，虽欲怨叛，而莫为之先」。秦始皇的致命错误是并天下后以客为无用，「堕名城，杀豪杰，民之秀异者散而归田亩」。苏轼将这一政策比作「纵百万虎狼于山林而饥渴之」——「不知其将噬人，世以始皇为智，吾不信也」。秦之亡不在二世，而在始皇使天下士人失业的那一刻。',
     '<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🏛️</div><div class="dual-text"><h4>六国养士：社会稳定器</h4><p>「凡民之秀杰者多以客养之，不失其职也。」六国之君虐民不减始皇，然百姓无一人叛——因为精英阶层被养士制度容纳。</p></div></div><div class="dual-card no"><div class="dual-icon">⚡</div><div class="dual-text"><h4>秦驱士归田：社会定时炸弹</h4><p>「堕名城，杀豪杰，民之秀异者散而归田亩。」纵百万虎狼于山林而饥渴之——秦之亡不在二世，而在始皇。</p></div></div></div>'),
    ('史家之道',
     '苏轼的三维分析模型——一个超前千年的系统思维',
     '将三篇分开来看，它们分别是独立的历史分析；合在一起，却构成了一个完整的王朝兴衰诊断框架。地理维（迁都即弃田宅）：周平王放弃丰镐意味着放弃了文武成康四代建立的地理资本，正如夏商两朝「不粥田宅」而延续五六百年。军事维（取国当如拔龆齿）：秦始皇用二十万人伐楚不克，再以六十万人「空国而战」——苏轼的「龆齿之喻」道出了渐进主义的军事智慧，而这个比喻在苻坚淝水之败中得到了最残酷的印证。社会维（失士则失天下）：六国养士制度容纳了社会的精英阶层，而秦朝「堕名城、杀豪杰」则将精英推向了对立面。苏轼的三维思维在千年前就已超越了道德化的历史叙事——他不问「昏君还是明君」，而问「地理根基是否动摇、军事节奏是否得当、社会精英是否被容纳」。',
     '<div class="flow-row"><div class="flow-step">地理维<br>迁都=弃田宅</div><div class="flow-arrow">+</div><div class="flow-step">军事维<br>伐国=拔龆齿</div><div class="flow-arrow">+</div><div class="flow-step">社会维<br>驱士=纵虎狼</div><div class="flow-arrow">=</div><div class="flow-step end">三维模型<br>王朝兴衰诊断</div></div><div class="quote-block" style="margin-top:12px"><div class="quote-text">凡有血气必争，争必以利，利莫大于封建。封建者，争之端而乱之始也。</div><div class="quote-source">——苏轼「秦废封建」（附于本章）</div></div>'),
    ('东坡之眼',
     '从《论古》看苏轼——一个被诗词才华掩盖的战略思想家',
     '世人皆知苏轼是词人、书画家、美食家，却很少有人注意到他作为战略分析家的深度。《东坡志林》中的《论古》诸篇，展现了一个被文学才华遮蔽的政治头脑。他不是皓首穷经的考据家——他考证周东迁用了「粥田宅」这一个民间比喻，分析秦伐楚用了「拔龆齿」这一个儿童经验，论述游士用了「纵虎狼于山林」这一个猎人常识。他用最直白的人间经验，拆解了最复杂的国家命运。他的结论也从不模棱两可：「周之失计，未有如东迁之缪者也」「秦之巧，亦创智伯而已」「始皇，吾不信也」——每一句都斩钉截铁。这就是苏轼：他从不假装中立，从不掩饰判断。他的史学不是冰冷的考据，而是一个活生生的人，用自己的全部生命经验，去丈量千年前那些帝国命运的尺度。而这，恰恰是他比任何专业史学家都更令人信服的原因。',
     '<div class="quote-block"><div class="quote-text">吾以是知二秦之一律也：始皇幸胜；而坚不幸耳。</div><div class="quote-source">——苏轼「秦拙取楚」· 千年史家最精炼的断语</div></div>'),
]
ch09_zh_take = '三篇长文，三个维度。周东迁失计是地理维——放弃根基则名存实亡；秦拙取楚是军事维——急于求成则反伤自身；游士失职之祸是社会维——精英失业则天下必乱。苏轼用看似散漫的随笔，构建了一套完整的王朝兴衰分析模型：一个国家的存亡，不在于某个君王的道德高下，而在于能否守住地理根基、把握军事节奏、容纳社会精英。这三件事，比任何道德说教都更接近历史的真相。'
ch09_zh_foot = '来源：《东坡志林》卷五·论古　|　（宋）苏轼 著　|　万卷出版公司　|　信息图生成于 2026-06-20'

ch09_en_h1 = 'Dongpo\'s Jottings · Chapter 9 · Strategy &amp; Fate — Relocation, Conquest &amp; Talent'
ch09_en_sub = 'Facing the rise and fall of dynasties, Su Shi drew insights from the Records of the Grand Historian and the Zuo Tradition. Why did the Zhou dynasty collapse after moving east? Why did Qin nearly lose its war against Chu? Why did the Six Kingdoms endure for centuries while Qin fell within two generations? Three seemingly unrelated questions form a complete geopolitical thesis: relocate your capital and you abandon your roots; conquer a kingdom hastily and you wound yourself; lose your elite talent and you lose the world. These millennium-old insights still challenge every ruler today.'
ch09_en_over = 'This chapter brings together three major essays from Su Shi\'s Historical Discourses: "The Zhou\'s Fatal Eastward Move," "Qin\'s Clumsy Conquest of Chu," and "The Calamity of Unemployed Scholars." Together they form a three-dimensional analysis of dynastic rise and fall: the geographic dimension (relocation = selling ancestral property), the military dimension (conquest must be gradual like pulling a baby tooth), and the social dimension (lose the elite and lose the state). With a historian\'s eye and a strategist\'s pen, Su Shi leaves posterity an indispensable mirror.'
ch09_en_kpis = [('3', 'Major Essays<br>Zhou·Qin·Scholar Crisis'),
                ('8+∞', '8 Capital Relocations<br>Countless Unemployed'),
                ('600K', 'Wang Jian\'s Chu<br>Campaign gamble'),
                ('3D Model', 'Geographic·Military·Social<br>Dynastic Analysis')]

HQ = '&quot;'  # HTML double-quote entity

_XiaShang = f'<div class="confusion-table"><div class="confusion-row"><div class="confusion-left">Xia·Shang: Never moved</div><div class="confusion-arrow">→</div><div class="confusion-right">Endured 500-600 years, all submitted</div></div><div class="confusion-row"><div class="confusion-left">Zhou: Moved east</div><div class="confusion-arrow">→</div><div class="confusion-right">A name alive, a state dead</div></div><div class="confusion-row"><div class="confusion-left">8 wartime relocations</div><div class="confusion-arrow">→</div><div class="confusion-right">Wei·Chu·Han·Li Jing — all perished</div></div></div><div class="quote-block"><div class="quote-text">Had King Ping possessed one Wang Dao... Qi and Jin, however strong, would not dare rebel — and how could Qin ever have risen to hegemony?</div><div class="quote-source">— Su Shi, {HQ}The Zhou&rsquo;s Fatal Eastward Move{HQ}</div></div>'

_QinChu = f'<div class="flow-row"><div class="flow-step">Qin Lulls Qi<br>40 yrs no attack</div><div class="flow-arrow">→</div><div class="flow-step">Dissolves 3 Jin<br>Alliance collapses</div><div class="flow-arrow">→</div><div class="flow-step">World Unified<br>By cunning, not Dao</div></div><div class="quote-block" style="margin-top:12px"><div class="quote-text">Taking a kingdom was like pulling a baby tooth — gradually, so the tooth falls out without the child noticing.</div><div class="quote-source">— Su Shi, {HQ}Qin&rsquo;s Clumsy Conquest of Chu{HQ}</div></div>'

_Scholars = f'<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🏛️</div><div class="dual-text"><h4>Six Kingdoms: Retainer System as Social Stabilizer</h4><p>{HQ}The elite were all absorbed as retainers, never losing their station.{HQ} Though kings oppressed no less than Qin, none rebelled — because talent had its place.</p></div></div><div class="dual-card no"><div class="dual-icon">⚡</div><div class="dual-text"><h4>Qin: Driving Talent to the Fields</h4><p>{HQ}Destroyed famous cities, killed heroes, sent the talented back to the fields.{HQ} Loosing millions of tigers into starving mountains — Qin&rsquo;s collapse was ordered by the First Emperor himself.</p></div></div></div>'

ch09_en_sections = [
    ('Relocation Folly',
     'The Zhou\'s Fatal Eastward Move — \u2018One Defeat, Sold the Family Estate\u2019',
     'Su Shi opens with a stunning metaphor: King Ping of Zhou abandoning Fenghao for Luoyang is like a wealthy family \u2018selling their ancestral estate at the first setback.\u2019 Xia and Shang, whose founding kings\u2019 virtue was no greater than Zhou\u2019s and whose later rulers\u2019 decadence matched You and Li, each lasted five or six centuries — because they never abandoned their roots. Su Shi catalogs eight historical relocations: Pangeng returned to Yin\u2019s old territory, Gugong moved to Qishan among nomads, Qi and Jin relocated at their zenith; but \u2018those who moved their capital to escape invaders — none escaped destruction.\u2019 The highlight: during the Su Jun Rebellion, Wang Dao blocked the relocation plan with \u2018Jinling is the city of kings; a king does not move his capital for wealth or poverty\u2019 — and Jin survived. Su Shi laments: had King Ping had a Wang Dao, with an unshaken capital, recovering Fenghao\u2019s remnants, restoring Wen-Wu-Cheng-Kang\u2019s governance, \u2018Qi and Jin, however strong, would not dare rebel — and how could Qin ever have risen to hegemony?\u2019',
     _XiaShang),
    ('Conquest Strategy',
     'Qin\u2019s Clumsy Conquest of Chu — \u2018Like Pulling a Baby Tooth\u2019',
     'Su Shi traces Qin\u2019s unification timeline: year 18 took Han, year 22 Wei, year 25 Zhao and Chu, year 26 Yan and Qi. Qin\u2019s victory, he argues, was \u2018not by the Dao, only by cunning, and not even luck.\u2019 The brilliant dialectic: Qin was \u2018clever in taking Qi\u2019 — forty years without attacking, lulling Qi into dissolving the Three Jin alliance — yet \u2018clumsy in taking Chu,\u2019 first sending Li Xin with 200,000 men (failed), then Wang Jian with 600,000 (\u2018emptying the state for battle\u2019). The metaphor is exquisite: \u2018In ancient times, taking a kingdom was like pulling a baby tooth — gradually, so the tooth falls out without the child noticing. Qin treated Chu as a loose tooth, pried open the mouth, yanked it out — the child must be hurt, the fingers bitten.\u2019 Wu attacked Chu in waves for three years before entering Ying. Jin pacified Wu, Sui pacified Chen, all using this method. Only Fu Jian, with a hundred-fold larger army, failed at Feishui. Conclusion: the First Emperor won by luck; Fu Jian was simply unlucky.',
     _QinChu),
    ('Talent Retention',
     'The Calamity of Unemployed Scholars — \u2018Loosing Millions of Tigers into Starving Mountains\u2019',
     'Su Shi begins with the Warring States patronage system: King Goujian kept 6,000 gentlemen; the Four Lords each maintained 3,000 retainers; Tian Wen gathered 60,000 knights-errant in Xue; the Jixia Academy hosted a thousand debaters — \u2018estimating the remainder, they would double the officials and equal half the farmers.\u2019 His core argument is shocking: the Six Kings oppressed their people no less than Qin, yet no peasant rebelled — because \u2018the elite were all absorbed as retainers, never losing their station. Those who farmed were dullards incapable of leadership; even if they resented their lot, none could lead.\u2019 The First Emperor\u2019s fatal error: after unification, he deemed retainers useless, \u2018destroyed famous cities, killed heroes, and sent the talented back to the fields.\u2019 Su Shi compares this to \u2018loosing millions of tigers and wolves into starving mountains\u2019 — \u2018not knowing they would devour men, the world considers the First Emperor wise; I do not believe it.\u2019 Qin\u2019s fall began not under the Second Emperor but the moment the First Emperor rendered the entire elite class unemployed.',
     _Scholars),
    ('The Historian\u2019s Way',
     'Su Shi\u2019s Three-Dimensional Model — Systems Thinking a Millennium Ahead',
     'Read separately, these three essays are independent historical analyses; together, they form a complete diagnostic framework for dynastic rise and fall. Geographic axis (relocation = selling ancestral property): King Ping abandoning Fenghao meant forfeiting the geographic capital built by four generations of Zhou kings — just as Xia and Shang \u2018never sold their estate\u2019 and endured five to six centuries. Military axis (conquest = pulling a baby tooth): the First Emperor sent 200,000 against Chu and failed, then gambled with 600,000 — Su Shi\u2019s \u2018baby tooth\u2019 metaphor crystallizes gradualism as military wisdom, cruelly vindicated by Fu Jian\u2019s defeat at Feishui. Social axis (lose the elite = lose the state): the Six Kingdoms\u2019 retainer system absorbed society\u2019s best talent, while Qin\u2019s \u2018destroying famous cities and killing heroes\u2019 drove the elite into opposition. Su Shi\u2019s three-dimensional thinking transcended moralized historiography a thousand years ago: he never asked \u2018was the ruler good or bad?\u2019 but \u2018is the geographic foundation shaken, is the military tempo right, are the social elites accommodated?\u2019',
     '<div class="flow-row"><div class="flow-step">Geographic<br>Relocation = Root Loss</div><div class="flow-arrow">+</div><div class="flow-step">Military<br>Conquest = Tooth Pull</div><div class="flow-arrow">+</div><div class="flow-step">Social<br>Driving Talent = Loosing Tigers</div><div class="flow-arrow">=</div><div class="flow-step end">3D Model<br>Dynastic Diagnosis</div></div><div class="quote-block" style="margin-top:12px"><div class="quote-text">All with blood and breath must contend; contention must spring from profit; and no profit exceeds feudal investiture. Feudal investiture is the genesis of contention and the beginning of chaos.</div><div class="quote-source">— Su Shi, &quot;Qin Abolished Feudalism&quot; (appended)</div></div>'),
    ('Dongpo\u2019s Eye',
     'Seeing Su Shi in the Historical Discourses — A Strategic Thinker Hidden by Poetic Genius',
     'The world knows Su Shi as a lyric poet, calligrapher, painter, and gourmand, but few notice his depth as a strategic analyst. The Historical Discourses in Dongpo\u2019s Jottings reveal a political mind obscured by literary brilliance. He was no dusty textual scholar — he analyzed the Zhou eastward move with a folk metaphor of \u2018selling the family estate,\u2019 Qin\u2019s Chu conquest with a child\u2019s experience of \u2018pulling a baby tooth,\u2019 the scholars\u2019 crisis with a hunter\u2019s common sense of \u2018loosing tigers into starving mountains.\u2019 He used the plainest human experiences to deconstruct the most complex national fates. His conclusions were never ambiguous: \u2018No mistake of the Zhou equaled the folly of the eastward move,\u2019 \u2018Qin\u2019s cunning merely copied Zhibo,\u2019 \u2018the First Emperor wise? I do not believe it\u2019 — each judgment cut decisively. This is Su Shi: he never feigned neutrality, never hid his verdict. His historiography is not cold textual criticism but a living human, measuring the fate of millennia-old empires with the full scale of his own life experience. And this is precisely why he is more persuasive than any professional historian.',
     '<div class="quote-block"><div class="quote-text">Thus I know the two Qins followed one law: the First Emperor won by luck; Fu Jian was simply unlucky.</div><div class="quote-source">— Su Shi, &quot;Qin\u2019s Clumsy Conquest of Chu&quot; · History\u2019s most distilled verdict across a millennium</div></div>'),
]
ch09_en_take = 'Three essays, three dimensions. The Zhou\'s eastward move is the geographic dimension — abandon your roots and your name outlives your substance. Qin\'s clumsy conquest of Chu is the military dimension — haste wounds the conqueror. The unemployed scholars\' calamity is the social dimension — lose the elite and lose the state. Su Shi, through seemingly casual jottings, constructed a complete model of dynastic rise and fall: a state\'s survival depends not on the morality of any single ruler, but on maintaining geographic foundations, military pacing, and elite social integration. These three truths come closer to history\'s reality than any moral sermon.'
ch09_en_foot = 'Source: Dongpo\u2019s Jottings, Scroll 5 · Historical Discourses | By Su Shi (Song Dynasty) | Wanjuan Publishing | Infographic generated 2026-06-20'


# ════════════════════════════════════════
# CHAPTER 10 DATA
# ════════════════════════════════════════

ch10_zh_h1 = '东坡志林 · 第十章「权力与人性——君臣之间的生死棋局」'
ch10_zh_sub = '在权力的棋盘上，君臣之间的关系从来不是简单的忠诚与背叛。苏轼用三篇精妙的论说——「论子胥种蠡」「赵高李斯」「隐公不幸」——剖开了权力游戏中最幽暗的角落。从春秋到秦朝，从楚国到咸阳宫，忠诚是什么？背叛又是什么？当扬雄用道德教条丈量历史人物时，苏轼一把撕开所有的标签：问题从来不是忠奸与否，而是智慧与愚蠢的较量。在权力面前，智者的忠诚可能是逃跑，愚者的忠诚可能是送死。'
ch10_zh_over = '本章汇集苏轼三篇权力分析——「论子胥种蠡」谈功成身退与忠诚的定义，「赵高李斯」谈制度之恶如何催生背叛，「隐公不幸」谈政治中智与愚的生死分界。三篇从不同角度解剖同一个命题：在绝对权力面前，个人的道德选择空间何其狭窄；但正因如此，智慧的选择才弥足珍贵。'
ch10_zh_kpis = [('6', '位历史人物<br>子胥·种·蠡·赵高<br>李斯·鲁隐公'),
                ('5', '起弑君事件<br>从春秋到秦二世'),
                ('3', '篇论说<br>子胥种蠡·赵高李斯<br>隐公不幸'),
                ('权力棋局', '忠诚·背叛·智慧<br>愚蠢·生·死')]
ch10_zh_sections = [
    ('功成身退',
     '论子胥种蠡——范蠡的智慧与扬雄的愚见',
     '苏轼开篇即做惊人之论：范蠡虽知勾践「长颈鸟喙，可与共患难，不可与共逸乐」，功成之后浮海而去，但苏轼说「以吾相蠡，蠡亦鸟喙也」——范蠡也是这样的人。他耕于海滨、力作营千金，「屡散而复积」——「岂非才有余而道不足」？苏轼以鲁仲连为对照：鲁连退秦军后，平原君欲以千金为寿，他笑而辞去、终身不复见——「所贵于天下士者，为人排难解纷而无所取也。」范蠡虽知进退，却放不下财富。更精彩的是苏轼对扬雄的批驳：扬雄以三谏不去、鞭尸籍馆来苛责伍子胥，苏轼怒斥——「三谏而去，为人臣交浅者言也。至于子胥，吴之宗臣，与国存亡者也，去将安往哉？百谏不听，继之以死可也。」他反问：「父不受诛，子复仇，礼也。生则斩首，死则鞭尸，发其至痛，无所择也。扬雄独非人子乎？」对大夫种和范蠡，扬雄又以不強谏勾践来苛责，苏轼一笑——「此皆儿童之见。」',
     '<div class="flow-row"><div class="flow-step">范蠡浮海<br>功成身退</div><div class="flow-arrow">→</div><div class="flow-step">耕于海滨<br>屡散复积</div><div class="flow-arrow">→</div><div class="flow-step end">才有余<br>而道不足</div></div><div class="quote-block" style="margin-top:12px"><div class="quote-text">三谏而去，为人臣交浅者言也。至于子胥，吴之宗臣，与国存亡者也。</div><div class="quote-source">——苏轼「论子胥种蠡」</div></div>'),
    ('制度之恶',
     '赵高李斯——法家严刑如何制造背叛',
     '苏轼追问一个千古谜题：李斯何等聪明，为何听信赵高，葬送了大秦帝国？他的回答深刻：不是李斯智不足，而是秦国的法家制度已经把所有正常的人性反应都杀死了。秦始皇的权威「如雷电鬼神，不可测也」——商鞅「立信于徙木，立威于弃灰，刑其亲戚师傅」，积累了无与伦比的威信。到了始皇，「秦人视其君如雷电鬼神」，以至于荆轲行刺时「持兵者熟视始皇环柱而走，莫之救者，以秦法重故也」。在这样的制度下，扶苏接到赐死诏书「宁死而不请」——因为他知道请了也没用。李斯之所以不畏惧扶苏、蒙恬，正是因为「知威令之素行，而臣子不敢复请也」。苏轼的结论震耳欲聋：「夫以法毒天下者，未有不反中其身及其子孙者也。」他以周公、孔子为对照：「以忠恕为心而以平易为政，则上易知而下易达。」法家的极致效率，最终反噬了法家的创造者。',
     '<div class="confusion-table"><div class="confusion-row"><div class="confusion-left">商鞅立信·立威·刑亲</div><div class="confusion-arrow">→</div><div class="confusion-right">秦人视君「如雷电鬼神」</div></div><div class="confusion-row"><div class="confusion-left">扶苏接到伪诏</div><div class="confusion-arrow">→</div><div class="confusion-right">「宁死而不请」——知请亦无用</div></div><div class="confusion-row"><div class="confusion-left">李斯不惧蒙恬扶苏</div><div class="confusion-arrow">→</div><div class="confusion-right">「知威令之素行，臣子不敢复请」</div></div></div><div class="quote-block"><div class="quote-text">夫以法毒天下者，未有不反中其身及其子孙者也。</div><div class="quote-source">——苏轼「赵高李斯」</div></div>'),
    ('智愚生死',
     '隐公不幸——政治场上的愚蠢比背叛更致命',
     '鲁隐公是苏轼笔下最令人唏嘘的悲剧人物。当公子翚向他请求去杀桓公、以换取太宰之位时，隐公的回答充满了仁者的温情：「为其少故也，吾将授之矣。使营菟裘，吾将老焉。」——桓公还年幼，我本来就要把王位还给他，我已经在菟裘建造退休的居所了。但这句话非但没有感化公子翚，反而使他「惧，反谮公于桓公而弑之」。苏轼的叹息锋利如刀：「隐公之智，曾不若是涂人也，哀哉！」——路边行人看到盗贼都知道捕击，因为若不击则盗将并杀自己，隐公的智慧竟不如路人。苏轼以骊姬、里克和赵高、李斯两组对照案例说明一个规律：小人之为乱，总是先找到最脆弱的环节下手。李斯本可以「召百官、陈六师而斩之」，却选择了另一条路——「非下愚而何！」结尾以郑小同（被司马师毒杀）和王允之（以醉吐避祸）的对比收束——乱臣如蝮蛇，其所螫草木犹足以杀人。',
     '<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🛡️</div><div class="dual-text"><h4>王允之：醉吐避祸的智者</h4><p>夜饮闻王敦密谋造反，大吐污衣面。王敦见其「卧吐中」，果不疑。岌岌乎危矣，以智全生。</p></div></div><div class="dual-card no"><div class="dual-icon">💀</div><div class="dual-text"><h4>郑小同：诚实致死的愚者</h4><p>诣司马师，师密疏未屏。师问：「见吾疏乎？」答曰：「不见。」师曰：「宁我负卿，无卿负我。」遂鸩之。哀哉！</p></div></div></div><div class="quote-block"><div class="quote-text">隐公之智，曾不若是涂人也，哀哉！</div><div class="quote-source">——苏轼「隐公不幸」</div></div>'),
    ('权力之镜',
     '六位历史人物的灵魂透视——苏轼的权力人类学',
     '将伍子胥、范蠡、文种、赵高、李斯、鲁隐公六人放在一起观看，苏轼实际上完成了一部微型权力人类学。伍子胥代表的是「不可选择的忠诚」——他是吴国的宗臣，与国家共存亡，没有地方可以逃离。范蠡代表的是「智慧的逃离」——他知道勾践的为人，功成之后浮海而去，但苏轼尖锐地指出：范蠡仍放不下财富，所以「才有余而道不足」。赵高和李斯代表的则是「制度的共谋」——不是李斯愚蠢，而是秦国的法家制度已经让他没有任何正常的决策空间。鲁隐公代表的是「善良的愚蠢」——他以善意揣度公子翚，却因这种善良而丧命。苏轼没有给出一个简单的道德公式，因为权力场中没有这样的公式——他给出的是一面镜子，每个人在这面镜子中，都能看到自己的处境。',
     '<div class="confusion-table"><div class="confusion-row"><div class="confusion-left">伍子胥：不可选择的忠诚</div><div class="confusion-arrow">→</div><div class="confusion-right">「吴之宗臣，与国存亡者也，去将安往哉？」</div></div><div class="confusion-row"><div class="confusion-left">范蠡：智慧但未完全的逃离</div><div class="confusion-arrow">→</div><div class="confusion-right">「才有余而道不足」——功成身退却放不下财富</div></div><div class="confusion-row"><div class="confusion-left">鲁隐公：善良导致的死亡</div><div class="confusion-arrow">→</div><div class="confusion-right">「隐公之智，曾不若是涂人也，哀哉！」</div></div></div>'),
    ('生存法则',
     '「危邦不入，乱邦不居」——苏轼留给所有权力人的最后箴言',
     '苏轼在「隐公不幸」的结尾引用了孔子的话：「危邦不入，乱邦不居。」这不是道德说教，而是在权力游戏中存活下来的最基本的生存指南。伍子胥无法逃离吴国——因为他没有选择；范蠡逃离了越国——但他仍然被困在财富的执念中；鲁隐公既没有逃离也没有防备——所以他死了。苏轼用这六个人的命运告诉所有权力场中的人：第一，认清你所处的制度和局面——在秦始皇的制度下，李斯注定无法做出正常选择；第二，判断你的对手——公子翚来请求杀桓公，这本身就是最危险的信号；第三，在你还有选择的时候做出选择——范蠡和鲁隐公的区别就在于：一个在灭吴后就离开了，一个在公子翚亮出匕首时还在谈退休计划。这三条法则，是苏轼用六个生命换来的权力生存课。',
     '<div class="flow-row"><div class="flow-step">认清制度<br>秦法之下<br>李斯无路</div><div class="flow-arrow">→</div><div class="flow-step">判断对手<br>公子翚亮刀<br>隐公谈退休</div><div class="flow-arrow">→</div><div class="flow-step">抓住时机<br>范蠡早逃离<br>隐公来不及</div><div class="flow-arrow">=</div><div class="flow-step end">危邦不入<br>乱邦不居<br>孔子最后的警告</div></div>'),
]
ch10_zh_take = '六位历史人物，三种权力悲剧。伍子胥、范蠡、文种的命运告诉我们：忠诚不是一个固定的姿势，而是一种审时度势的智慧——子胥死得壮烈，范蠡逃得聪明，而扬雄用道德教条去丈量他们，「此皆儿童之见」。赵高和李斯的剧本则揭示了制度的结构性暴力：当法律成为绝对的恐怖，连聪明的李斯也只能走上愚蠢的绝路——「夫以法毒天下者，未有不反中其身及其子孙者也。」隐公、里克、李斯、郑小同、王允之这五人，生与死的分界线不是道德上的善恶，而是智慧上的高下——在乱世中，「危邦不入，乱邦不居」，孔子的这句警告，是苏轼留给我们的终极安全法则。'
ch10_zh_foot = '来源：《东坡志林》卷五·论古　|　（宋）苏轼 著　|　万卷出版公司　|　信息图生成于 2026-06-20'

ch10_en_h1 = 'Dongpo\u2019s Jottings · Chapter 10 · Power &amp; Humanity — The Life-or-Death Chessboard Between Sovereign and Subject'
ch10_en_sub = 'On the chessboard of power, the relationship between ruler and minister has never been simply loyalty versus betrayal. Su Shi dissects power\u2019s darkest corners through three exquisite discourses: \u2018On Wu Zixu, Wen Zhong, and Fan Li,\u2019 \u2018Zhao Gao and Li Si,\u2019 and \u2018The Misfortune of Duke Yin of Lu.\u2019 From the Spring and Autumn period to the Qin dynasty, from Chu to the Xianyang Palace — what is loyalty? What is betrayal? When Yang Xiong measured historical figures with moral yardsticks, Su Shi tore away every label: the real question is never loyalty versus betrayal, but wisdom versus folly. Before absolute power, a wise man\u2019s loyalty may be escape; a fool\u2019s loyalty may be suicide.'
ch10_en_over = 'This chapter brings together three of Su Shi\u2019s power analyses: \u2018On Wu Zixu, Wen Zhong, and Fan Li\u2019 examines timely withdrawal and the definition of loyalty; \u2018Zhao Gao and Li Si\u2019 reveals how institutional evil manufactures betrayal; \u2018The Misfortune of Duke Yin\u2019 maps the life-or-death boundary between political wisdom and stupidity. From three angles, one proposition: before absolute power, the space for individual moral choice is terrifyingly narrow — which is precisely why wise choices are so precious.'
ch10_en_kpis = [('6', 'Historical Figures<br>Zixu·Zhong·Li·Zhao<br>Li Si·Duke Yin'),
                ('5', 'Regicides<br>Spring &amp; Autumn \u2192 Qin II'),
                ('3', 'Discourses<br>Zixu·Zhao-Li<br>Duke Yin'),
                ('Power Mat', 'Loyalty·Betrayal·Wisdom<br>Folly·Life·Death')]

_HQ = '&quot;'

_Zixu = f'<div class="flow-row"><div class="flow-step">Fan Li Sails Away<br>Timely Withdrawal</div><div class="flow-arrow">→</div><div class="flow-step">Farms by Sea<br>Amasses Wealth</div><div class="flow-arrow">→</div><div class="flow-step end">Talent Exceeds<br>Dao — Incomplete</div></div><div class="quote-block" style="margin-top:12px"><div class="quote-text">{_HQ}Three remonstrations then leave{_HQ} — that is for ministers of shallow ties. Zixu was a founding minister, living and dying with the state.</div><div class="quote-source">— Su Shi, {_HQ}On Wu Zixu, Wen Zhong, and Fan Li{_HQ}</div></div>'

_ZhaoLi = f'<div class="confusion-table"><div class="confusion-row"><div class="confusion-left">Shang Yang: Trust·Awe·Punished Kin</div><div class="confusion-arrow">→</div><div class="confusion-right">Qin people saw ruler as {_HQ}thunder, ghosts, gods{_HQ}</div></div><div class="confusion-row"><div class="confusion-left">Fusu received forged edict</div><div class="confusion-arrow">→</div><div class="confusion-right">{_HQ}Chose death rather than appeal{_HQ} — knew useless</div></div><div class="confusion-row"><div class="confusion-left">Li Si feared no one</div><div class="confusion-arrow">→</div><div class="confusion-right">{_HQ}Knew terror was habitual; subjects dared not question{_HQ}</div></div></div><div class="quote-block"><div class="quote-text">Those who poison the world with law invariably find it rebounding upon themselves and their descendants.</div><div class="quote-source">— Su Shi, {_HQ}Zhao Gao and Li Si{_HQ}</div></div>'

_DukeYin = f'<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🛡️</div><div class="dual-text"><h4>Wang Yunzhi: Feigned Drunkenness Saved Him</h4><p>Overheard Wang Dun plotting rebellion at a night banquet, vomited profusely, face and clothes soiled. Wang Dun saw him {_HQ}lying in vomit{_HQ} and dismissed suspicion. Saved by wits at the brink.</p></div></div><div class="dual-card no"><div class="dual-icon">💀</div><div class="dual-text"><h4>Zheng Xiaotong: Honesty Killed Him</h4><p>Visited Sima Shi, who left a secret memo unguarded. Shi asked: {_HQ}Did you see my memo?{_HQ} Answered honestly: {_HQ}No.{_HQ} Shi: {_HQ}Better I betray you than you betray me.{_HQ} Poisoned. Tragedy!</p></div></div></div><div class="quote-block"><div class="quote-text">Duke Yin\u2019s wisdom could not match a passerby on the road — how sad!</div><div class="quote-source">— Su Shi, {_HQ}Duke Yin\u2019s Misfortune{_HQ}</div></div>'

ch10_en_sections = [
    ('Timely Withdrawal',
     'On Wu Zixu, Wen Zhong, and Fan Li — Fan Li\u2019s Wisdom vs. Yang Xiong\u2019s Folly',
     'Su Shi opens with a startling judgment: Fan Li recognized Goujian\u2019s \u2018long neck and bird beak — share hardship but not pleasure,\u2019 and sailed away after victory. Yet Su Shi says, \u2018if I physiognomize Fan Li, Fan Li too had a bird beak.\u2019 Fan Li farmed by the sea, labored to amass a thousand gold pieces, \u2018repeatedly dispersing and accumulating wealth\u2019 — \u2018is this not talent exceeding Dao?\u2019 Su Shi contrasts with Lu Zhonglian: after Lu forced Qin\u2019s retreat, Lord Pingyuan offered him a thousand gold pieces; Lu laughed and declined, vanishing forever — \u2018what the world honors in a scholar is resolving difficulties without taking anything.\u2019 Fan Li knew when to leave but could not let go of wealth. Even better: Su Shi demolishes Yang Xiong\u2019s criticism of Wu Zixu for not leaving after three remonstrations: \u2018Three remonstrations then leave — that is for ministers of shallow ties. As for Zixu, he was a founding minister of Wu, living and dying with the state. Where could he go? Remonstrate a hundred times unheard, then die — that is acceptable.\u2019 He asks: \u2018A father unjustly killed, a son takes revenge — this is ritual propriety. Alive, behead him; dead, whip his corpse, venting extreme grief, with no alternative. Is Yang Xiong alone not someone\u2019s son?\u2019',
     _Zixu),
    ('Institutional Evil',
     'Zhao Gao and Li Si — How Legalist Terror Manufactures Betrayal',
     'Su Shi probes an eternal puzzle: Li Si was so brilliant — why did he listen to Zhao Gao and bury the Qin empire? His answer is profound: not that Li Si lacked wisdom, but that Qin\u2019s Legalist system had killed every normal human response. The First Emperor\u2019s authority was \u2018like thunder, lightning, ghosts, and gods — unfathomable.\u2019 Shang Yang \u2018built trust by paying a man to move a log, built awe by amputating a man who dumped ashes, punished his own relatives and teachers,\u2019 accumulating ultimate prestige. By the First Emperor\u2019s reign, \u2018Qin people viewed their ruler as thunder, ghosts, and gods\u2019 — so much so that during Jing Ke\u2019s assassination attempt, \u2018armed guards watched the First Emperor run circles around pillars, none daring to help — because Qin\u2019s laws were too severe.\u2019 Under such a system, Fusu received a forged suicide edict and \u2018chose death rather than appeal\u2019 — knowing appeal was useless. Li Si did not fear Fusu and Meng Tian precisely because he \u2018knew the terror of commands was habitual, and subjects dared not question.\u2019 Su Shi\u2019s conclusion thunders: \u2018Those who poison the world with law invariably find it rebounding upon themselves and their descendants.\u2019',
     _ZhaoLi),
    ('Wisdom or Death',
     'Duke Yin\u2019s Misfortune — Political Stupidity Kills More Surely Than Betrayal',
     'Duke Yin of Lu is Su Shi\u2019s most heartbreaking tragic figure. When Gongzi Hui asked permission to kill Duke Huan in exchange for the Grand Steward post, Duke Yin replied with a benevolent man\u2019s warmth: \u2018He is still young; I intended to yield the throne to him. I am building my retirement home at Tuqiu.\u2019 But instead of moving Hui, these words made him \u2018fear, then slander Duke Yin to Duke Huan, and assassinate him.\u2019 Su Shi\u2019s lament cuts like a knife: \u2018Duke Yin\u2019s wisdom could not match a passerby on the road — how sad!\u2019 A bystander seeing a bandit would capture and strike him, knowing otherwise the bandit would kill them too. Su Shi presents paired cases: Lady Li and Li Ke; Zhao Gao and Li Si — villains always target the weakest link first. Li Si could have \u2018summoned the hundred officials, arrayed the six divisions, and beheaded Gao\u2019 — he chose otherwise. \u2018If that is not utter stupidity, what is?\u2019 The chapter ends with the contrast between Zheng Xiaotong (poisoned by Sima Shi for honesty) and Wang Yunzhi (saved by feigning drunken vomiting) — treacherous ministers are like pit vipers; even the grass they bite can kill.',
     _DukeYin),
    ('The Mirror of Power',
     'A Soul Perspective on Six Figures — Su Shi\u2019s Anthropology of Power',
     'Place Wu Zixu, Fan Li, Wen Zhong, Zhao Gao, Li Si, and Duke Yin together, and Su Shi has completed a miniature anthropology of power. Wu Zixu represents \u2018unchoosable loyalty\u2019 — he was a founding minister of Wu, living and dying with the state, with nowhere to flee. Fan Li represents \u2018wise escape\u2019 — he recognized Goujian\u2019s character and sailed away after victory, but Su Shi sharply notes: Fan Li still could not release wealth, so \u2018his talent exceeded his Dao.\u2019 Zhao Gao and Li Si represent \u2018institutional complicity\u2019 — not that Li Si was stupid, but that Qin\u2019s Legalist system had left him no normal decision space. Duke Yin represents \u2018kind-hearted stupidity\u2019 — he judged Gongzi Hui with good intentions and died from that goodness. Su Shi offers no simple moral formula, because no such formula exists in the arena of power — he offers a mirror in which everyone can see their own situation.',
     '<div class="confusion-table"><div class="confusion-row"><div class="confusion-left">Wu Zixu: Unchoosable Loyalty</div><div class="confusion-arrow">→</div><div class="confusion-right">\u201cFounding minister, living and dying with the state — where could he go?\u201d</div></div><div class="confusion-row"><div class="confusion-left">Fan Li: Wise But Incomplete Escape</div><div class="confusion-arrow">→</div><div class="confusion-right">\u201cTalent exceeded Dao\u201d — withdrew but could not release wealth</div></div><div class="confusion-row"><div class="confusion-left">Duke Yin: Kindness That Killed</div><div class="confusion-arrow">→</div><div class="confusion-right">\u201cHis wisdom could not match a passerby — how sad!\u201d</div></div></div>'),
    ('Survival Rules',
     '\u201cDo Not Enter a Dangerous State\u201d — Su Shi\u2019s Final Admonition for Power Players',
     'Su Shi ends Duke Yin\u2019s Misfortune with Confucius\u2019s words: \u201cDo not enter a dangerous state; do not dwell in a chaotic state.\u201d This is not moral preaching but the most basic survival guide for anyone in the game of power. Wu Zixu could not flee Wu — he had no choice. Fan Li fled Yue — but remained trapped in the obsession with wealth. Duke Yin neither fled nor defended himself — so he died. Through these six fates, Su Shi tells all power players: first, recognize the system and situation you\u2019re in — under the First Emperor\u2019s system, Li Si was destined to make no normal choices. Second, assess your opponent — Gongzi Hui coming to ask permission to kill Duke Huan was itself the most dangerous signal. Third, choose while you still have a choice — the difference between Fan Li and Duke Yin is that one left right after Wu was destroyed, while the other was still discussing retirement plans after Gongzi Hui had shown his dagger. These three rules are the power-survival lesson Su Shi bought with six lives.',
     '<div class="flow-row"><div class="flow-step">Recognize System<br>Under Qin Law<br>Li Si Had No Path</div><div class="flow-arrow">→</div><div class="flow-step">Assess Opponent<br>Hui Drew Dagger<br>Yin Discussed Retirement</div><div class="flow-arrow">→</div><div class="flow-step">Seize the Moment<br>Fan Li Fled Early<br>Yin Never Had Time</div><div class="flow-arrow">=</div><div class="flow-step end">Don\u2019t Enter<br>Dangerous State<br>Confucius\u2019s Final Warning</div></div>'),
]
ch10_en_take = 'Six historical figures, three types of power tragedy. The fates of Wu Zixu, Fan Li, and Wen Zhong teach us: loyalty is not a fixed posture but wisdom in reading the times — Zixu died heroically, Fan Li escaped cleverly, and Yang Xiong\u2019s moral yardsticks measured none of them, \u2018these are all childish views.\u2019 The Zhao Gao-Li Si drama reveals structural violence of institutions: when law becomes absolute terror, even the brilliant Li Si can only march down a stupid dead-end path — \u2018those who poison the world with law invariably find it rebounding upon themselves and their descendants.\u2019 Duke Yin, Li Ke, Li Si, Zheng Xiaotong, Wang Yunzhi — the line between life and death is not moral goodness versus evil, but wisdom versus folly. In turbulent times, \u2018do not enter a dangerous state, do not dwell in a chaotic state\u2019 — Confucius\u2019s warning is Su Shi\u2019s ultimate safety rule for us all.'
ch10_en_foot = 'Source: Dongpo\u2019s Jottings, Scroll 5 · Historical Discourses | By Su Shi (Song Dynasty) | Wanjuan Publishing | Infographic generated 2026-06-20'


# ════════════════════════════════════════
# CHAPTER 11 DATA
# ════════════════════════════════════════

ch11_zh_h1 = '东坡志林 · 第十一章「礼法与制度——孔子的治世理想与制度之辩」'
ch11_zh_sub = '当孔子面对鲁国三桓的跋扈时，他能做什么？当摄主制度在秦汉以后被母后摄政取代时，丢失了什么？当管仲「九合诸侯不以兵车」时，为什么孔子仍对他略有微词？苏轼在「论鲁三桓」「摄主」「七德八戒」三篇中，用纵横捭阖的史笔，将礼法制度这个抽象命题变得血肉丰满——他从孔子的政治实践出发，追问什么才是真正有效的治理之道：不是杀伐果断，不是权谋机变，而是以礼法为框架的制度之善。'
ch11_zh_over = '本章汇集苏轼三篇制度论——「论鲁三桓」讲孔子如何在权力夹缝中以礼法约束强卿，「摄主」辨古代理摄主制度与后世母后摄政的根本差异，「七德八戒」以七位「盛德」之人和八位「嗜杀」之人做对照，提出「治国如养生，未病而服药则药杀人」的终极政治哲学。'
ch11_zh_kpis = [('3', '篇制度论<br>鲁三桓·摄主<br>七德八戒'),
                ('7+8', '位历史案例<br>7盛德之人<br>8嗜杀之人'),
                ('礼法', '核心命题<br>制度之善<br>胜于杀伐之威'),
                ('治道', '治国如养生<br>未病而服药<br>则药杀人')]
ch11_zh_sections = [
    ('孔子治鲁',
     '论鲁三桓——孔子如何在权力夹缝中推行礼法',
     '鲁定公十三年，孔子提出「臣无藏甲，大夫无百雉之城」——堕三都。叔孙氏先堕郈，季氏将堕费时公山不狃叛乱，最终堕成时公敛处父以成叛——孔子的改革面临巨大阻力。苏轼指出关键悖论：季氏曾亲自驱逐鲁昭公使其死于国外，「忌刻忮害」不亚于曹操，孔子怎能在此时毁其都城、削其军队？答案是孔子有一种「不言而信，不怒而威」的力量——「孔子以羁旅之臣得政期月，而能举治世之礼，以律亡国之臣，堕名都，出藏甲，而三桓不疑其害」。苏轼又用晏婴作对比：晏婴知「田氏之僭，惟礼可以已之」，但「婴能知之而不能为之」——其浩然之气「不及孔孟」。孔子晚年沐浴而朝告哀公请讨齐陈恒——此时他已七十一岁，距去世仅两年，仍不忘以《春秋》之法治理列国，「至于老且死而不忘」。',
     '<div class="confusion-table"><div class="confusion-row"><div class="confusion-left">晏婴知礼</div><div class="confusion-arrow">→</div><div class="confusion-right">「能知之而不能为之」——浩然之气不及孔孟</div></div><div class="confusion-row"><div class="confusion-left">孔子执政</div><div class="confusion-arrow">→</div><div class="confusion-right">「不言而信，不怒而威」——三桓不疑其害</div></div><div class="confusion-row"><div class="confusion-left">孔子晚年</div><div class="confusion-arrow">→</div><div class="confusion-right">七十一岁沐浴而朝请讨陈恒——「老且死而不忘」</div></div></div><div class="quote-block"><div class="quote-text">孔子以羁旅之臣得政期月，而能举治世之礼……此必有不言而信、不怒而威者矣。</div><div class="quote-source">——苏轼「论鲁三桓」</div></div>'),
    ('摄主之制',
     '摄主——秦汉以后丢失的制度智慧',
     '欧阳修认为鲁隐公是正式即位而非摄政，苏轼不同意——他引孔子与曾子的对话来论证「摄主」制度的存在。孔子解释：若国君去世时世子尚未出生，则由国君之弟或其兄弟之子暂代摄主；若遗腹子是女孩则摄主正式即位，若是男孩则摄主退位。苏轼认为这是「先王之令典，孔子之法言」——它的精髓在于确保权力始终留在先君血脉中，而非如后世母后摄政那样易引发异姓篡夺。苏轼列举：母后摄政而国安者仅有君王后、曹后、高后、向后等「千一」之人；而吕后、胡武灵、武则天之类「不胜其乱」。他发出追问：若母后可信则摄主亦可信；若均不可信，则摄主「犹吾先君之子孙也，不犹愈于异姓之取哉？」',
     '<div class="flow-row"><div class="flow-step">古制摄主<br>先王子孙继</div><div class="flow-arrow">→</div><div class="flow-step">世子生男<br>摄主退位</div><div class="flow-arrow">→</div><div class="flow-step">权力永在<br>先君血脉</div></div><div class="dual-grid" style="margin-top:10px"><div class="dual-card yes"><div class="dual-icon">👑</div><div class="dual-text"><h4>摄主制：权力在血脉之内</h4><p>季康子摄政，南孺子生男即退位——「古之道也，孔子行之。」确保权力不出先君子孙。</p></div></div><div class="dual-card no"><div class="dual-icon">⚠️</div><div class="dual-text"><h4>母后摄政：权力易落异姓</h4><p>「牝鸡之晨，惟家之索。」吕后、武氏「不胜其乱」，王莽杨坚「遂因以易姓」。</p></div></div></div>'),
    ('七德八戒',
     '七德八戒——「治国如养生」的终极政治哲学',
     '这是苏轼笔下最有方法论价值的一篇。他读史得出两组人：七位「盛德」之人——楚成王不杀重耳、汉高祖不杀吴王濞、晋武帝不杀刘元海、苻坚不杀慕容垂、唐明皇不杀安禄山等；但他们最终都遭遇了这些人的叛乱。八位「嗜杀」之人——汉景帝杀周亚夫、曹操杀孔融、晋文帝杀嵇康、唐太宗杀李君羡、武后杀裴炎等。「世之论者」皆以七人不杀为失，八人杀之为当。苏轼断然反对：「七人者皆自有以致败亡，非不杀之过也。」他的逻辑如手术刀般精准：齐景公不繁刑重赋，虽有田氏齐不可取；楚成王不用子玉，虽有晋文公兵不败……明皇不用李林甫杨国忠，「虽有安禄山，亦何能为？」最后以养生喻治国——「养生者不过慎起居饮食、节声色而已，节慎在未病之前，而服药于已病之后。今吾忧寒疾而先服乌喙……则病未作而药杀人矣。彼八人者，皆未病而服药者也。」杀无罪之人以求防患，是政治智慧的最低级形态。',
     '<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🏆</div><div class="dual-text"><h4>七位盛德之人：不妄杀</h4><p>楚成王不杀重耳、汉高祖不杀吴王濞、唐明皇不杀安禄山——「非不杀之过也」。国乱之因不在不杀，而在其他政策的失误。</p></div></div><div class="dual-card no"><div class="dual-icon">💀</div><div class="dual-text"><h4>八位嗜杀之人：未病服药</h4><p>汉景帝杀周亚夫、曹操杀孔融、晋文帝杀嵇康——「皆未病而服药者也」。以杀无罪求防患，乃「政治智慧的最低级形态」。</p></div></div></div><div class="quote-block"><div class="quote-text">治国如养生……忧寒疾而先服乌喙，忧热疾而先服甘遂，则病未作而药杀人矣。</div><div class="quote-source">——苏轼「七德八戒」</div></div>'),
    ('制度之善',
     '礼法高于刀剑——苏轼政治哲学的最后答案',
     '三篇制度论读下来，苏轼的政治哲学逐渐清晰。他不是法家——法家相信法律的绝对威慑力，但苏轼在「赵高李斯」中已经论证了「夫以法毒天下者，未有不反中其身及其子孙者也」。他也不是道家——道家主张无为而治，但苏轼在「论鲁三桓」中盛赞孔子「得政期月而能举治世之礼」。他也不是纯粹的儒家——他批评扬雄的道德教条主义「此皆儿童之见」。苏轼的政治哲学自成一体：核心是礼法制度的建设，但礼法不是僵硬的教条，而是一种「不言而信、不怒而威」的无形力量。他在「七德八戒」中给出了最终答案：治国如养生，真正的高明不是等病变了再下猛药（杀伐），也不是在没病时乱吃药（杀无罪以预防），而是在未病之前建立健康的制度肌体——「节慎在未病之前」。这是一个被贬谪半生的人，用生命的代价悟出的政治智慧。',
     '<div class="flow-row"><div class="flow-step">法家<br>以法毒天下<br>反中其身</div><div class="flow-arrow">≠</div><div class="flow-step">道家<br>无为而治<br>不够积极</div><div class="flow-arrow">≠</div><div class="flow-step">僵化儒家<br>道德教条<br>儿童之见</div><div class="flow-arrow">=</div><div class="flow-step end">苏轼之道<br>礼法制度<br>节慎在未病之前</div></div>'),
    ('千年回响',
     '苏轼留给治者的最后箴言——制度健康比任何个人权威都重要',
     '苏轼的「七德八戒」有一种惊人的现代感。他论证的核心命题——杀无辜者以求防患是政治的最低级形态——在二十世纪的极权政治中得到了最惨烈的印证。他列举的七位「盛德」之人和八位「嗜杀」之人，实际上是在提出一个永恒的政治伦理学问题：政治的手段能不能正当化政治的目的？苏轼的回答是断然的「不能」。他举的例子跨越千年——从汉景帝到武后——而这些例子共同指向一个结论：以暴力和恐惧为基础的统治，最终都会被暴力和恐惧反噬。「夫以法毒天下者，未有不反中其身及其子孙者也」——这句写于九百多年前的话，至今仍是所有治者最不该忘记的箴言。',
     '<div class="quote-block"><div class="quote-text">世之以成败为是非也！故夫嗜杀人者，必以邓侯不杀楚子为口实。</div><div class="quote-source">——苏轼「七德八戒」· 批判以成败论英雄的历史观</div></div>'),
]
ch11_zh_take = '三篇制度论构成苏轼政治哲学的三重奏。孔子堕三都的实践说明：真正的权威不是来自刀剑而是来自信义——「不言而信、不怒而威」，三桓不疑其害。摄主之制的思考揭示：好的制度设计远比依赖个体道德可靠——权力留在血脉之内，胜过寄托于不可靠的母后。七德八戒的辨析则抵达了最高层次的政治智慧：治国如养生，真正的高明不是杀人防患，而是在未病之前建立健康的制度肌体——「节慎在未病之前，而服药于已病之后」。那些因为恐惧未来叛乱而杀害无罪之人者，「皆未病而服药者也」——毒药入腹，病变未至，人已先死。这就是苏轼留给所有治者的最后箴言。'
ch11_zh_foot = '来源：《东坡志林》卷五·论古　|　（宋）苏轼 著　|　万卷出版公司　|　信息图生成于 2026-06-20'

ch11_en_h1 = 'Dongpo\u2019s Jottings · Chapter 11 · Ritual &amp; Institutions — Confucius\u2019s Governance Ideal and the Debate on Systems'
ch11_en_sub = 'When Confucius faced the arrogance of Lu\u2019s Three Huan families, what could he do? When the \u2018regent\u2019 institution was replaced by empress-dowager regencies after Qin-Han, what was lost? When Guan Zhong \u2018united the feudal lords nine times without military force,\u2019 why did Confucius still find him wanting? In three discourses — \u2018On Lu\u2019s Three Huan,\u2019 \u2018The Regent System,\u2019 and \u2018Seven Virtues, Eight Warnings\u2019 — Su Shi uses sweeping historical analysis to give flesh and blood to the abstract question of ritual institutions. Starting from Confucius\u2019s political practice, he asks what truly constitutes effective governance: not decisive killing, not strategic cunning, but institutional goodness framed by ritual propriety.'
ch11_en_over = 'This chapter brings together three institutional discourses: \u2018On Lu\u2019s Three Huan\u2019 shows how Confucius constrained powerful ministers through ritual in impossible circumstances; \u2018The Regent System\u2019 distinguishes the ancient regent institution from later empress-dowager regencies; \u2018Seven Virtues, Eight Warnings\u2019 contrasts seven virtuous figures with eight murderous ones, arriving at the ultimate political philosophy: \u2018governing a state is like nurturing health — taking medicine before illness strikes means the medicine kills you.\u2019'
ch11_en_kpis = [('3', 'Institutional<br>Discourses'),
                ('7+8', 'Historical Cases<br>7 Virtuous<br>8 Murderous'),
                ('Ritual', 'Core Thesis<br>Institutional Good<br>Over Terror'),
                ('Governance', 'State as Body<br>Pre-illness Care<br>Not Preemptive Kill')]

_Confucius = f'<div class="confusion-table"><div class="confusion-row"><div class="confusion-left">Yan Ying: Knew ritual</div><div class="confusion-arrow">→</div><div class="confusion-right">{_HQ}Could know it without enacting it{_HQ} — spirit unmatched</div></div><div class="confusion-row"><div class="confusion-left">Confucius: Governed</div><div class="confusion-arrow">→</div><div class="confusion-right">{_HQ}Trusting without speaking, awe without anger{_HQ} — Three Huan unsuspicious</div></div><div class="confusion-row"><div class="confusion-left">Confucius at 71</div><div class="confusion-arrow">→</div><div class="confusion-right">Bathed, came to court, asked to punish Chen Heng — {_HQ}not forgetting until old age and death{_HQ}</div></div></div><div class="quote-block"><div class="quote-text">As a wandering minister who gained power for barely a month, Confucius could implement governance rituals... This must come from trusting without speaking, commanding awe without anger.</div><div class="quote-source">— Su Shi, {_HQ}On Lu&rsquo;s Three Huan{_HQ}</div></div>'

_Regent = f'<div class="flow-row"><div class="flow-step">Ancient Regent<br>Descendant of Ruler</div><div class="flow-arrow">→</div><div class="flow-step">If Heir is Boy<br>Regent Steps Down</div><div class="flow-arrow">→</div><div class="flow-step">Power Remains<br>in Bloodline</div></div><div class="dual-grid" style="margin-top:10px"><div class="dual-card yes"><div class="dual-icon">👑</div><div class="dual-text"><h4>Regent System: Power in the Bloodline</h4><p>Ji Kangzi regency — stepped down when Nan Ruzi bore a boy. {_HQ}The ancient way, practiced by Confucius.{_HQ} Power never leaves the former ruler&rsquo;s descendants.</p></div></div><div class="dual-card no"><div class="dual-icon">⚠️</div><div class="dual-text"><h4>Empress-Dowager Regency: Power Falls to Strangers</h4><p>{_HQ}When the hen crows at dawn, the household faces ruin.{_HQ} Empress L\u00fc, Wu Zetian — {_HQ}uncontainable chaos.{_HQ} Wang Mang, Yang Jian {_HQ}changed the surname.{_HQ}</p></div></div></div>'

_SevenVirtues = f'<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🏆</div><div class="dual-text"><h4>7 Virtuous: Did Not Kill Recklessly</h4><p>King Cheng spared Chong\u2019er, Han Gaozu spared the King of Wu, Tang Minghuang spared An Lushan — {_HQ}not the fault of not killing.{_HQ} The cause of chaos lay elsewhere.</p></div></div><div class="dual-card no"><div class="dual-icon">💀</div><div class="dual-text"><h4>8 Murderous: Took Medicine Before Illness</h4><p>Han Jingdi killed Zhou Yafu, Cao Cao killed Kong Rong, Jin Wendi killed Ji Kang — {_HQ}all took medicine before falling ill.{_HQ} Killing innocents preemptively is {_HQ}the lowest form of political wisdom.{_HQ}</p></div></div></div><div class="quote-block"><div class="quote-text">Governing a state is like nurturing health... Fearing cold, one first takes aconite; fearing heat, kansui root — illness has not struck, but the medicine has killed.</div><div class="quote-source">— Su Shi, {_HQ}Seven Virtues, Eight Warnings{_HQ}</div></div>'

ch11_en_sections = [
    ('Confucius in Lu',
     'On Lu\u2019s Three Huan — How Confucius Advanced Ritual Amid a Power Vise',
     'In Duke Ding\u2019s 13th year, Confucius proposed \u2018ministers shall not hoard arms, grandees shall not have hundred-zhang city walls\u2019 — tear down the three capitals. Shusun first demolished Hou. When the Ji clan was about to demolish Fei, Gongshan Buniu rebelled. When they moved to demolish Cheng, Gonglian Chufu rebelled with Cheng — Confucius\u2019s reform faced immense resistance. Su Shi identifies the key paradox: the Ji clan had personally driven Duke Zhao into exile where he died, their \u2018jealous cruelty\u2019 matching Cao Cao\u2019s — how could Confucius destroy their cities and disarm them at such a moment? The answer: Confucius possessed a power of \u2018trusting without speaking, commanding awe without anger.\u2019 \u2018As a wandering minister who gained power for barely a month, Confucius could implement governance rituals, discipline ministers who would destroy a state, demolish famous cities, remove hidden arms — and the Three Huan never suspected him of harming them.\u2019 Su Shi contrasts with Yan Ying: Yan Ying knew \u2018the Tian usurpation can only be stopped by ritual,\u2019 but \u2018Ying could know it without enacting it\u2019 — his vast spirit \u2018could not match Confucius and Mencius.\u2019 In his twilight years, Confucius bathed and came to court asking Duke Ai to punish Chen Heng of Qi — at seventy-one, two years from death, still \u2018not forgetting until old age and death.\u2019',
     _Confucius),
    ('The Regent System',
     'The Regent — Institutional Wisdom Lost After Qin-Han',
     'Ouyang Xiu argued Duke Yin of Lu was a formal ruler, not a regent. Su Shi disagrees — he cites Confucius\u2019s dialogue with Zengzi to prove the \u2018regent\u2019 institution existed. Confucius explained: if the heir is unborn when the ruler dies, the ruler\u2019s younger brother or nephew serves as regent; if the posthumous child is a girl, the regent formally ascends; if a boy, the regent steps down. Su Shi calls this \u2018the ancient kings\u2019 canonical code, Confucius\u2019s legal doctrine\u2019 — its essence is keeping power always within the former ruler\u2019s bloodline, unlike later empress-dowager regencies that invited usurpation by other surnames. Su Shi catalogs: empress-dowager regencies producing stable rule — only Junwang Hou, Empress Cao, Empress Gao, Empress Xiang, \u2018one in a thousand\u2019; while Empress L\u00fc, Hu Wuling, Wu Zetian brought \u2018uncontainable chaos,\u2019 and Wang Mang and Yang Jian \u2018changed the dynastic surname.\u2019 He asks: if empress-dowagers are trustworthy, regents too are trustworthy; if neither is, then a regent is \u2018still a descendant of our former ruler — is that not better than another surname seizing power?\u2019',
     _Regent),
    ('Seven Virtues, Eight Warnings',
     'Seven Virtues, Eight Warnings — \u2018Governing a State Is Like Nurturing Health\u2019',
     'This is Su Shi\u2019s most methodologically valuable essay. From history he derives two groups: seven figures of \u2018flourishing virtue\u2019 — King Cheng of Chu did not kill Chong\u2019er, Han Gaozu did not kill the King of Wu, Emperor Wu of Jin did not kill Liu Yuanhai, Fu Jian did not kill Murong Chui, Tang Minghuang did not kill An Lushan — yet all later faced rebellions from these very people. Eight \u2018murder-loving\u2019 figures — Han Jingdi killed Zhou Yafu, Cao Cao killed Kong Rong, Jin Wendi killed Ji Kang, Tang Taizong killed Li Junxian, Empress Wu killed Pei Yan, etc. \u2018Contemporary commentators\u2019 all said the seven erred by not killing and the eight were right to kill. Su Shi flatly rejects this: \u2018These seven each had their own causes of defeat — it was not the fault of not killing.\u2019 His logic is surgically precise: had Qi Jinggong not imposed harsh punishments and heavy taxes, even with the Tian clan Qi could not be taken; had Chu Chengwang not employed Ziyu, even with Jin Wengong his army would not have been defeated... had Minghuang not employed Li Linfu and Yang Guozhong, \u2018even with An Lushan, what could he have done?\u2019 The essay culminates in the healthcare metaphor: \u2018Nurturing health is merely caution in food, drink, and daily habits, moderating sensual pleasures. Caution comes before illness; medicine comes after. Now if I, fearing a cold illness, first take aconite... illness has not arrived but the medicine has killed me. Those eight persons all took medicine before falling ill.\u2019 Killing the innocent to preempt danger is the lowest form of political wisdom.',
     _SevenVirtues),
    ('The Good of Institutions',
     'Ritual Over the Sword — Su Shi\u2019s Final Answer in Political Philosophy',
     'Reading the three institutional discourses, Su Shi\u2019s political philosophy crystallizes. He is no Legalist — Legalists believe in law\u2019s absolute deterrent power, but in Zhao Gao and Li Si, Su Shi already proved that \u2018those who poison the world with law invariably find it rebounding upon themselves and their descendants.\u2019 He is no Daoist — Daoists advocate governance through non-action, but in On Lu\u2019s Three Huan, Su Shi praises Confucius for \u2018gaining power for barely a month and implementing governance rituals.\u2019 He is no pure Confucian — he criticizes Yang Xiong\u2019s moral dogmatism as \u2018childish views.\u2019 Su Shi\u2019s political philosophy stands on its own: its core is the construction of ritual institutions, but ritual is not rigid dogma — it is an invisible power that \u2018trusts without speaking, commands awe without anger.\u2019 In Seven Virtues, Eight Warnings, he gives the final answer: governing is nurturing health; true mastery is not administering harsh medicine once illness has struck (slaughter), nor swallowing medicine when not yet sick (killing innocents preventively), but building healthy institutional bodies before illness — \u2018caution before illness.\u2019 This is political wisdom earned by a man exiled for half his life, at the cost of that very life.',
     '<div class="flow-row"><div class="flow-step">Legalist<br>Poison world with law<br>Rebounds on self</div><div class="flow-arrow">\u2260</div><div class="flow-step">Daoist<br>Govern by non-action<br>Too passive</div><div class="flow-arrow">\u2260</div><div class="flow-step">Rigid Confucian<br>Moral dogma<br>Childish views</div><div class="flow-arrow">=</div><div class="flow-step end">Su Shi\u2019s Way<br>Ritual Institutions<br>Caution before illness</div></div>'),
    ('Echoes Across a Millennium',
     'Su Shi\u2019s Final Admonition — Institutional Health Matters More Than Any Individual Authority',
     'Su Shi\u2019s Seven Virtues, Eight Warnings possesses an astonishingly modern resonance. His core thesis — killing the innocent to preempt danger is the lowest form of politics — found its most horrific vindication in 20th-century totalitarianism. The seven figures of flourishing virtue and eight murder-loving figures he catalogs are actually posing an eternal question of political ethics: can political means justify political ends? Su Shi\u2019s answer is a categorical No. His examples span a millennium — from Han Jingdi to Empress Wu — and they all point to one conclusion: rule founded on violence and fear is ultimately devoured by violence and fear. \u2018Those who poison the world with law invariably find it rebounding upon themselves and their descendants\u2019 — written over nine hundred years ago, this remains the admonition that every ruler should least afford to forget.',
     '<div class="quote-block"><div class="quote-text">The world judges right and wrong by success and failure! Therefore those who love killing invariably cite Marquis Deng not killing the Viscount of Chu as precedent.</div><div class="quote-source">— Su Shi, &quot;Seven Virtues, Eight Warnings&quot; · A critique of success-worshipping historiography</div></div>'),
]
ch11_en_take = 'Three institutional discourses form Su Shi\u2019s political-philosophical trilogy. Confucius\u2019s destruction of the three capitals demonstrates: true authority comes not from swords but from trust — \u2018trusting without speaking, commanding awe without anger,\u2019 the Three Huan never suspected harm. The regent-system analysis reveals: good institutional design is far more reliable than reliance on individual virtue — keeping power in the bloodline surpasses entrusting it to unreliable empress-dowagers. The Seven Virtues, Eight Warnings dialectic reaches the highest level of political wisdom: governing is like nurturing health; true mastery is not killing to prevent disaster, but building healthy institutional bodies before illness — \u2018caution before illness, medicine after.\u2019 Those who killed innocents from fear of future rebellion \u2018all took medicine before falling ill\u2019 — poison swallowed, illness not yet arrived, but the person already dead. This is Su Shi\u2019s final admonition to all rulers.'
ch11_en_foot = 'Source: Dongpo\u2019s Jottings, Scroll 5 · Historical Discourses | By Su Shi (Song Dynasty) | Wanjuan Publishing | Infographic generated 2026-06-20'


# ════════════════════════════════════════
# CHAPTER 12 DATA
# ════════════════════════════════════════

ch12_zh_h1 = '东坡志林 · 第十二章「士人风骨——苏轼品评历代人物的智慧之光」'
ch12_zh_sub = '如果前十一章是苏轼放眼江山、纵论古今的大文章，那么这一章是他俯身拾取的人性碎片——十二则短小精悍的人物点评，从汉武帝到李后主，从颜蠋到刘伶，从张仪到房琯。没有长篇大论，只有一针见血的洞见。苏轼在这些碎片中展现了他最令人倾倒的才华：在几百字之内，用一句比喻、一个反问、一次历史对照，就能穿透一个人的灵魂。这些人物品评，不是史家的冷眼旁观，而是一个历经沧桑的智者，用自己的人生经验去丈量每一个人物的灵魂深度。'
ch12_zh_over = '本章精选苏轼《人物》卷中最精彩的十二则人物品评——颜蠋的「晚食当肉」、汉武帝踞厕见卫青、李后主的亡国之泪、刘伶的「死便埋我」、荀卿的「青出于蓝」之谬、张仪的欺楚之术……每一则都是几百字的微缩传记，却闪耀着比长篇传记更锐利的人性洞察。'
ch12_zh_kpis = [('29', '则人物<br>品评短文'),
                ('12', '则精选<br>本章重点呈现'),
                ('千年', '跨度<br>从尧舜到五代'),
                ('人性光谱', '圣贤·帝王·隐士<br>枭雄·名士·败者')]
ch12_zh_sections = [
    ('隐士风骨',
     '颜蠋·刘伶——何为真正的达观？',
     '苏轼对隐士的态度极其挑剔。颜蠋辞齐王而去，说「晚食以当肉，安步以当车，无罪以当贵，清静贞正以自娱」——战国之士中难得有如此贤者。但苏轼偏不买账：「晚食以当肉，安步以当车，是犹有意于肉于车也。晚食自美，安步自适，取其美与适足矣，何以当肉与车为哉！」——你还在想着肉和车，就不是真正的达观。但他又忍不住补了一句：「虽然，蠋可谓巧于居贫者也……非我之久于贫，不能知蠋之巧也。」——这是谪居黄州的苏轼才能写出的补充。对刘伶，他更加不留情面：「刘伯伦常以锸自随，曰死即埋我。苏子曰，伯伦非达者也，棺椁衣衾，不害为达。苟为不然，死则已矣，何必更埋！」——死都死了，还惦记着让人用锸埋你，这不是执着是什么？',
     '<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🍃</div><div class="dual-text"><h4>颜蠋：近乎达观的居贫之巧</h4><p>「晚食自美，安步自适，取其美与适足矣，何以当肉与车为哉！」苏轼挑剔其有意于肉车，却又承认：「非我之久于贫，不能知蠋之巧。」</p></div></div><div class="dual-card no"><div class="dual-icon">🍶</div><div class="dual-text"><h4>刘伶：连死亡都执着</h4><p>「死即埋我」——苏轼说：「伯伦非达者也。苟为不然，死则已矣，何必更埋！」连死后怎么处理都要操心，谈何放达？</p></div></div></div>'),
    ('帝王之相',
     '汉武帝·李后主·晋惠帝——帝王的灵魂切片',
     '苏轼看帝王，只看一个小动作，一个表情，一句话。汉武帝——「踞厕见卫青，不冠不见汲长孺」：蹲在厕所接见大将军卫青，不戴帽子却不敢见汲黯。苏轼只说一句话：「若青奴才，雅宜舐痔，踞厕见之，正其宜也。」——卫青这种奴才本就该舔痔疮，蹲厕所里见他刚好合适。对李后主，苏轼引其绝命词「最是仓惶辞庙日，教坊犹奏别离歌，挥泪对宫娥」——然后一刀劈下：「后主既为樊若水所卖，举国与人，故当恸哭于九庙之外，谢其民而后行，顾乃挥泪宫娥，听教坊离曲！」亡国之时不对祖宗和百姓哭泣，却对着宫女流泪！晋惠帝太子时，晋武帝以探策卜其命运，「惠帝不肖，得一」——苏轼评：「盖神以实告。」神用最诚实的方式预告了晋朝的灭亡——一个「一」字，就是「不肖」的全部答案。',
     '<div class="confusion-table"><div class="confusion-row"><div class="confusion-left">汉武帝踞厕见卫青</div><div class="confusion-arrow">→</div><div class="confusion-right">「若青奴才，雅宜舐痔，踞厕见之，正其宜也。」</div></div><div class="confusion-row"><div class="confusion-left">李后主挥泪对宫娥</div><div class="confusion-arrow">→</div><div class="confusion-right">「当恸哭于九庙之外，谢其民而后行」——亡国哭错了对象</div></div><div class="confusion-row"><div class="confusion-left">晋惠帝探策得「一」</div><div class="confusion-arrow">→</div><div class="confusion-right">「盖神以实告」——一个数字预告了整个王朝的命运</div></div></div>'),
    ('智者之智',
     '荀卿·张仪·房琯——智者为何犯错？',
     '苏轼对一些公认的「智者」进行了不留情面的解剖。荀卿说「青出于蓝而青于蓝，冰生于水而寒于水」，世人以此证明弟子可胜于师。苏轼冷笑：「青即蓝也，冰即水也。酿米为酒……曰酒甘于米，膳羞美于羊，虽儿童必笑之，而荀卿以是为辨，信其醉梦颠倒之言！」——把本体和衍生物混为一谈，儿童都不会犯的逻辑错误。关于张仪欺楚以商於六百里：「此与儿戏无异，天下无不疾张子之诈而笑楚王之愚也。」但苏轼更关心的是另一种欺骗：后世的臣子欺君说「行吾言，天下举安，四夷皆服，礼乐兴而刑罚措」——「其君之所欲得者，非特六百里也，而卒无丝毫之获」。这种华而不实的承诺，比张仪的六百里有更大的杀伤力。房琯以刘秩为将，败于陈涛斜，杀四万人——苏轼叹：「挟区区之辨以待热洛河，疏矣。」一个纸上谈兵的书生以口辩代替军事常识，四万人的生命只证明了理论的空洞。',
     '<div class="quote-block"><div class="quote-text">后世之臣欺其君，曰：「行吾言，天下举安，四夷皆服，礼乐兴而刑罚措。」其君之所欲得者，非特六百里也，而卒无丝毫之获。</div><div class="quote-source">——苏轼评张仪欺楚</div></div>'),
    ('乱世相人',
     '司马懿·吕后·王衍——识破人的面具',
     '苏轼的人物洞察力在最阴暗的历史场景中最锋利。司马懿讨曹爽，桓范往奔之，蒋济说「驽马恋栈豆，必不能用也」——果然曹爽不听桓范之计，身死族灭。曹操擒陈宫、吕布后问陈宫：「公台平生自谓智有余，今日何如？」陈宫答：「此子不用宫言，不然未可知也！」苏轼评：「吕布、曹爽，何人也？而为之用，尚何言知！」——伺候这种蠢货主子，还有什么脸谈智慧！王衍降石勒后「自解无罪，且劝僭号」，苏轼不说王衍，而说他的女儿惠风：「刘曜陷洛，以惠风赐其将乔属。将妻之，惠风杖剑大骂而死。」一句感叹：「乃知王夷甫之死，非独惭见晋公卿，乃当羞见其女也。」——父亲劝降求活，女儿以死殉节，父亲的死不仅愧对同僚，更无颜见自己的女儿。王济以人乳蒸豚，王恺使妓吹笛「小失声韵便杀之」——苏轼评：「时武帝在也，而贵戚敢如此，知晋室之乱也久矣。」',
     '<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🗡️</div><div class="dual-text"><h4>王衍之女惠风</h4><p>「杖剑大骂而死」——父亲劝石勒僭号求生，女儿面对敌将从容赴死。苏轼：「乃当羞见其女也。」</p></div></div><div class="dual-card no"><div class="dual-icon">😈</div><div class="dual-text"><h4>王济·王恺</h4><p>「以人乳蒸豚」「小失声韵便杀之」——「时武帝在也，而贵戚敢如此，知晋室之乱也久矣。」</p></div></div></div>'),
    ('处世之道',
     '刘凝之·沈麟士——同一件事，两种境界',
     '两个人的鞋被认错了。刘凝之：被认错即与之，失主得鞋送还不肯复取。沈麟士：被认错也与之，失主送还，笑而受之。苏轼一语定高下：「此虽小事，然处事当如麟士，不当如凝之也。」为什么？刘凝之的「不肯复取」是一种道德洁癖——我不愿意有任何被误解的可能，所以宁可不拿回自己的鞋。沈麟士的「笑而受之」是一种通透——鞋是我的就是我的，别人搞错了还回来，我就笑着收下。前者是紧绷的道德表演，后者是松弛的智慧境界。在苏轼看来，真正的君子从不刻意展示自己的道德优越感——「笑而受之」，四字即是全部的人生哲学。',
     '<div class="quote-block"><div class="quote-text">此虽小事，然处事当如麟士，不当如凝之也。</div><div class="quote-source">——苏轼评刘凝之与沈麟士</div></div>'),
]
ch12_zh_take = '二十九则人物品评，苏轼在这片人性的碎片之海中展现了他最自由的才华。他不做道德裁决——汉武帝踞厕见卫青，「正其宜也」；李后主挥泪对宫娥，「当恸哭于九庙之外」；王衍之女杖剑而死，「乃当羞见其女也」。他也不迷信任何既有标签——荀卿的辩证是「醉梦颠倒之言」，范蠡的功成身退「才有余而道不足」，刘伶的死便埋我「非达者也」。他唯一的标准是「通透」——沈麟士的「笑而受之」之所以高于刘凝之的「不肯复取」，因为前者不需要通过拒绝来证明操守。人物的高下，不在道德标签，而在灵魂的通透程度。这就是苏轼人物品评的终极尺度。'
ch12_zh_foot = '来源：《东坡志林》·人物　|　（宋）苏轼 著　|　万卷出版公司　|　信息图生成于 2026-06-20'

ch12_en_h1 = 'Dongpo\u2019s Jottings · Chapter 12 · The Spirit of the Scholar — Su Shi\u2019s Piercing Character Sketches'
ch12_en_sub = 'If the previous eleven chapters are Su Shi surveying landscapes and history with sweeping vision, this chapter is him bending down to gather fragments of human nature — twelve terse, razor-sharp character sketches, from Emperor Wu of Han to the Last Ruler of Southern Tang, from Yan Zhu to Liu Ling, from Zhang Yi to Fang Guan. No lengthy treatises, only needle-point insights. In these fragments, Su Shi displays his most captivating talent: within a few hundred words, with a single metaphor, a rhetorical question, a historical contrast, he penetrates a person\u2019s soul. These character sketches are not a historian\u2019s cold observations, but a weathered sage measuring each figure\u2019s spiritual depth with his own hard-won life experience.'
ch12_en_over = 'This chapter selects twelve of Su Shi\u2019s most brilliant character sketches from the Personages scroll — Yan Zhu\u2019s \u2018late meals as meat,\u2019 Emperor Wu receiving Wei Qing from the toilet, the Last Ruler of Southern Tang\u2019s tears for palace ladies, Liu Ling\u2019s \u2018bury me when I die,\u2019 Xun Qing\u2019s fallacy of \u2018blue from indigo,\u2019 Zhang Yi\u2019s deceit of the King of Chu... each a miniature biography in a few hundred words, yet radiating sharper human insight than any full-length biography.'
ch12_en_kpis = [('29', 'Character<br>Sketches Total'),
                ('12', 'Selected<br>In This Chapter'),
                ('3,000 yrs', 'Timespan<br>Yao-Shun \u2192 Five Dynasties'),
                ('Human Spectrum', 'Sages·Emperors·Hermits<br>Warlords·Literati·Losers')]

_Hermit = f'<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🍃</div><div class="dual-text"><h4>Yan Zhu: Near-Detachment, Skillful in Poverty</h4><p>{_HQ}Late meals are delicious in themselves, slow walks are comfortable — take the comfort as enough!{_HQ} Su Shi critiques his lingering attachment to {_HQ}meat and carriage,{_HQ} yet admits: {_HQ}Had I not long endured poverty, I could not understand Zhu&rsquo;s skill.{_HQ}</p></div></div><div class="dual-card no"><div class="dual-icon">🍶</div><div class="dual-text"><h4>Liu Ling: Attached Even to Death</h4><p>{_HQ}When I die, bury me{HQ} — Su Shi: {_HQ}Bolun was not detached. Dead is dead — why still need burying!{_HQ} Still worrying about post-mortem arrangements — what talk of freedom?</p></div></div></div>'  # Note: intentional {HQ} without _ prefix - let me fix
# Actually let me fix the variable references
_Hermit_fixed = '<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🍃</div><div class="dual-text"><h4>Yan Zhu: Near-Detachment, Skillful in Poverty</h4><p>&quot;Late meals are delicious in themselves, slow walks are comfortable — take the comfort as enough!&quot; Su Shi critiques his lingering attachment to &quot;meat and carriage,&quot; yet admits: &quot;Had I not long endured poverty, I could not understand Zhu&rsquo;s skill.&quot;</p></div></div><div class="dual-card no"><div class="dual-icon">🍶</div><div class="dual-text"><h4>Liu Ling: Attached Even to Death</h4><p>&quot;When I die, bury me&quot; — Su Shi: &quot;Bolun was not detached. Dead is dead — why still need burying!&quot; Still worrying about post-mortem arrangements — what talk of freedom?</p></div></div></div>'

_Emperors = '<div class="confusion-table"><div class="confusion-row"><div class="confusion-left">Emperor Wu, toilet, Wei Qing</div><div class="confusion-arrow">→</div><div class="confusion-right">&quot;That slave suited licking hemorrhoids; receiving him from the toilet was entirely appropriate.&quot;</div></div><div class="confusion-row"><div class="confusion-left">Last Tang Ruler wept for palace ladies</div><div class="confusion-arrow">→</div><div class="confusion-right">&quot;Should have wailed outside the Nine Temples, apologized to his people&quot; — wept for the wrong audience</div></div><div class="confusion-row"><div class="confusion-left">Emperor Hui drew &quot;One&quot;</div><div class="confusion-arrow">→</div><div class="confusion-right">&quot;The gods spoke truthfully&quot; — one digit foretold a dynasty&rsquo;s doom</div></div></div>'

_WhyErr = '<div class="quote-block"><div class="quote-text">Later ministers who deceive their ruler say: &quot;Follow my words, the empire will be at peace, barbarians will submit...&quot; What their ruler desired was far more than 600 li, yet in the end, not a shred was gained.</div><div class="quote-source">— Su Shi, on Zhang Yi Deceiving Chu</div></div>'

_ChaosRead = '<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🗡️</div><div class="dual-text"><h4>Wang Yan&rsquo;s Daughter Huifeng</h4><p>&quot;Seized a sword and died cursing&quot; — Father urged Shi Le to usurp to save his life; daughter faced the enemy general with death. Su Shi: &quot;Shame before his own daughter.&quot;</p></div></div><div class="dual-card no"><div class="dual-icon">😈</div><div class="dual-text"><h4>Wang Ji · Wang Kai</h4><p>&quot;Steamed pork in human milk&quot; &quot;Killed for slightly off-pitch flute&quot; — &quot;Emperor Wu was alive, yet nobles dared this — Jin&rsquo;s chaos had been brewing long.&quot;</p></div></div></div>'

_Living = '<div class="quote-block"><div class="quote-text">Though a small matter, in conducting oneself, one should be like Linshi, not Ningzhi.</div><div class="quote-source">— Su Shi, on Liu Ningzhi and Shen Linshi</div></div>'

ch12_en_sections = [
    ("The Hermit\u2019s Spirit",
     "Yan Zhu &amp; Liu Ling — What Is True Detachment?",
     "Su Shi is extraordinarily demanding of hermits. Yan Zhu left the King of Qi, declaring: \u2018Late meals serve as meat, slow walks serve as carriage, innocence serves as nobility, quiet rectitude as self-delight\u2019 — among Warring States scholars, few matched such virtue. But Su Shi refuses to applaud: \u2018Late meals as meat, slow walks as carriage — this still shows attachment to meat and carriage. Late meals are delicious in themselves, slow walks are comfortable in themselves; take the deliciousness and comfort as enough — why compare them to meat and carriage!\u2019 You are still thinking about meat and carriages — that is not true detachment. Yet he cannot resist adding: \u2018Still, Yan Zhu can be called skillful at dwelling in poverty... had I not long endured poverty, I could not understand Zhu\u2019s skill.\u2019 Only Su Shi in Huangzhou exile could write that addendum. For Liu Ling, he is even more merciless: \u2018Liu Bolun always carried a spade, saying: \u201cWhen I die, bury me.\u201d Su Shi says: Bolun was not a detached person. Coffin, shroud, grave-clothes — none harm detachment. Otherwise, dead is dead — why still need burying!\u2019 You\u2019re dead and still worried about someone digging you a grave — is that not attachment?",
     _Hermit_fixed),
    ("Emperors in Cross-Section",
     "Emperor Wu · Last Ruler of Tang · Emperor Hui — Soul Slices of Rulers",
     "Su Shi observes emperors through one gesture, one expression, one sentence. Emperor Wu of Han — \u2018squatting on the toilet to receive Wei Qing, yet not daring to meet Ji An without his cap.\u2019 Su Shi\u2019s single comment: \u2018Wei Qing, that slave, was well suited to licking hemorrhoids; receiving him squatting on the toilet was entirely appropriate.\u2019 For the Last Ruler of Southern Tang, Su Shi quotes his deathbed poem: \u2018Most harrowing, the day I fled the ancestral temple, musicians still played farewell songs, tears shed before palace ladies\u2019 — then cuts with a knife: \u2018The Last Ruler was betrayed by Fan Ruoshui, gave his entire state away — he should have wailed outside the Nine Temples, apologized to his people, then departed. Instead, he shed tears before palace ladies, listening to the academy play farewell songs!\u2019 Losing his kingdom, he wept before the wrong audience. When Crown Prince Hui of Jin drew a divination lot, the unworthy heir \u2018drew one\u2019 — Su Shi: \u2018The gods spoke truthfully.\u2019 A single number foretold an entire dynasty\u2019s doom.",
     _Emperors),
    ("Why Smart People Err",
     "Xun Qing · Zhang Yi · Fang Guan — When the Brilliant Blunder",
     "Su Shi performs merciless dissection of recognized \u2018wise men.\u2019 Xun Qing said \u2018blue comes from indigo but surpasses indigo; ice forms from water but is colder than water\u2019 — the world took this as proof a student can surpass the teacher. Su Shi sneers: \u2018Blue IS indigo, ice IS water. Ferment rice into wine... to say wine is sweeter than rice, fine meat tastier than lamb — even a child would laugh, yet Xun Qing took this as dialectic. Truly the babblings of drunken dreams!\u2019 Conflating substance with derivative — a logical error even children avoid. On Zhang Yi deceiving the King of Chu with 600 li of territory: \u2018This was no different from child\u2019s play; the world condemns Zhang Yi\u2019s deceit and laughs at the Chu king\u2019s stupidity.\u2019 But Su Shi is more concerned with another deception: later ministers who tell their ruler \u2018Follow my words, the empire will be at peace, barbarians will submit, ritual and music will flourish, punishments shelved\u2019 — \u2018what their ruler desired was far more than 600 li, yet in the end, not a shred was gained.\u2019 Such grandiose empty promises are far deadlier than Zhang Yi\u2019s 600-li trick. Fang Guan appointed Liu Zhi as general, lost at Chentao Incline, 40,000 died — Su Shi sighs: \u2018Pitting mere rhetoric against the Reluo River — sloppy.\u2019 An armchair scholar substituting verbal cleverness for military common sense; 40,000 lives proved only the emptiness of theory.",
     _WhyErr),
    ("Reading Faces in Chaos",
     "Sima Yi · Empress L\u00fc · Wang Yan — Seeing Through the Mask",
     "Su Shi\u2019s character insight is sharpest in history\u2019s darkest scenes. Sima Yi attacked Cao Shuang; Huan Fan rushed to aid him, but Jiang Ji said \u2018A nag horse yearns for its stable beans — he cannot act on advice\u2019 — indeed, Cao Shuang ignored Huan Fan\u2019s strategy and perished. Cao Cao, having captured Chen Gong and L\u00fc Bu, asked Chen Gong: \u2018You always claimed your wisdom exceeded others — how about today?\u2019 Chen Gong: \u2018This man would not heed my counsel; otherwise, who knows!\u2019 Su Shi\u2019s comment: \u2018L\u00fc Bu, Cao Shuang — what kind of men? And you served them — what wisdom can you claim!\u2019 Serving idiot masters — what face to speak of intelligence! Wang Yan surrendered to Shi Le, \u2018excused himself of guilt and urged Shi Le to usurp the throne.\u2019 Su Shi does not discuss Wang Yan but his daughter Huifeng: \u2018When Liu Yao took Luoyang, he gave Huifeng to his general Qiao Shu. About to be forced into marriage, Huifeng seized a sword and died cursing.\u2019 One line: \u2018Thus we know Wang Yifu\u2019s death was not merely shame before Jin ministers, but shame before his own daughter.\u2019 Father urged usurpation to live; daughter chose death with honor — the father\u2019s death shames not only colleagues but his child. Wang Ji steamed pork in human milk; Wang Kai killed courtesans for \u2018slightly off-pitch flute notes\u2019 — Su Shi: \u2018Emperor Wu was alive then, yet nobles dared this — we know Jin\u2019s chaos had been brewing long.\u2019",
     _ChaosRead),
    ("The Art of Living",
     "Liu Ningzhi &amp; Shen Linshi — Same Situation, Two States of Mind",
     "Two men had their shoes mistaken by others. Liu Ningzhi: his were taken by mistake, he gave them away; the real owner returned them, he refused to take them back. Shen Linshi: his were taken by mistake, he also gave them away; the real owner returned them, he laughed and accepted. Su Shi\u2019s judgment is swift: \u2018Though a small matter, in conducting oneself, one should be like Linshi, not Ningzhi.\u2019 Why? Liu\u2019s refusal was moral fastidiousness — I would rather not retrieve my shoes than risk being misunderstood. Shen\u2019s laughing acceptance was clarity — these are my shoes, someone made a mistake, they\u2019re returned, I laugh and take them. The former is tense moral performance; the latter is relaxed wisdom. In Su Shi\u2019s view, a true noble person never strains to display moral superiority — \u2018laughing, he accepted\u2019: four words containing an entire life philosophy.",
     _Living),
]
ch12_en_take = "Twenty-nine character sketches — in this sea of human fragments, Su Shi displays his freest talent. He renders no moral verdicts — Emperor Wu receiving Wei Qing from the toilet: \u2018entirely appropriate\u2019; the Last Tang Ruler weeping for palace ladies: \u2018should have wailed at the Nine Temples\u2019; Wang Yan\u2019s daughter dying by the sword: \u2018shame before his own daughter.\u2019 He trusts no established labels — Xun Qing\u2019s dialectic is \u2018babblings of drunken dreams,\u2019 Fan Li\u2019s timely withdrawal shows \u2018talent exceeding Dao,\u2019 Liu Ling\u2019s \u2018bury me when I die\u2019 demonstrates \u2018not detachment.\u2019 His sole criterion is clarity — Shen Linshi\u2019s \u2018laughing, he accepted\u2019 surpasses Liu Ningzhi\u2019s \u2018refused to take them back\u2019 because the former needs no rejection to prove integrity. A person\u2019s stature lies not in moral labels but in spiritual clarity. This is Su Shi\u2019s ultimate measure in character judgment."
ch12_en_foot = "Source: Dongpo\u2019s Jottings · Personages | By Su Shi (Song Dynasty) | Wanjuan Publishing | Infographic generated 2026-06-20"


# ════════════════════════════════════════
# WRITE ALL FILES
# ════════════════════════════════════════

print("东坡志林 ch009-012 · 8-file generation")
print("=" * 60)

write_ch("009", ch09_zh_h1, ch09_zh_sub, ch09_zh_over, ch09_zh_kpis, ch09_zh_sections, ch09_zh_take, ch09_zh_foot,
                ch09_en_h1, ch09_en_sub, ch09_en_over, ch09_en_kpis, ch09_en_sections, ch09_en_take, ch09_en_foot)

write_ch("010", ch10_zh_h1, ch10_zh_sub, ch10_zh_over, ch10_zh_kpis, ch10_zh_sections, ch10_zh_take, ch10_zh_foot,
                ch10_en_h1, ch10_en_sub, ch10_en_over, ch10_en_kpis, ch10_en_sections, ch10_en_take, ch10_en_foot)

write_ch("011", ch11_zh_h1, ch11_zh_sub, ch11_zh_over, ch11_zh_kpis, ch11_zh_sections, ch11_zh_take, ch11_zh_foot,
                ch11_en_h1, ch11_en_sub, ch11_en_over, ch11_en_kpis, ch11_en_sections, ch11_en_take, ch11_en_foot)

write_ch("012", ch12_zh_h1, ch12_zh_sub, ch12_zh_over, ch12_zh_kpis, ch12_zh_sections, ch12_zh_take, ch12_zh_foot,
                ch12_en_h1, ch12_en_sub, ch12_en_over, ch12_en_kpis, ch12_en_sections, ch12_en_take, ch12_en_foot)

print()
print("🎉 All 8 files generated successfully!")