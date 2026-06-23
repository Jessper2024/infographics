#!/usr/bin/env python3
"""Generate 昨日的世界 ch013-ch016 infographics (zh + en)."""
import os, pathlib

OUT = pathlib.Path(os.path.expanduser("~/.openclaw/workspace/infographics/books"))
BOOK = "昨日的世界"

# ── Shared CSS ──────────────────────────────────────────────
CSS = r"""@font-face{font-family:'FZXPYZS';src:url('../方正屏显雅宋简体.TTF') format('truetype');font-weight:normal;font-style:normal;}
*{margin:0;padding:0;box-sizing:border-box;}
body{background:#f5f1eb;font-family:'FZXPYZS','PingFang SC','Noto Serif SC','STSong',Georgia,serif;display:flex;justify-content:center;align-items:flex-start;min-height:100vh;padding:40px 20px 60px;}
.container{max-width:880px;width:100%;}
h1{font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif;font-size:32px;color:#1a1a1a;text-align:center;line-height:1.4;margin-bottom:8px;font-weight:normal;letter-spacing:1.5px;}
.subtitle{text-align:center;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif;font-size:14px;color:#888;margin-bottom:24px;line-height:1.7;max-width:640px;margin-left:auto;margin-right:auto;}
.divider{width:60px;height:3px;background:linear-gradient(90deg,#dc2626,#ea580c);margin:0 auto 28px;border-radius:2px;}
.chapter-overview{background:#fff;border-left:4px solid #4f46e5;border-radius:12px;padding:22px 26px;margin-bottom:24px;font-size:15px;color:#555;line-height:2.0;box-shadow:0 1px 3px rgba(0,0,0,0.04);}
.chapter-overview strong{color:#4f46e5;}
.kpi-row{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:24px;}
.kpi{background:#fff;border-radius:12px;padding:14px 10px;text-align:center;box-shadow:0 1px 3px rgba(0,0,0,0.04);}
.kpi-num{font-family:'FZXPYZS',serif;font-size:26px;font-weight:bold;}
.kpi-label{font-size:12px;color:#888;margin-top:4px;}
.c01{color:#dc2626;}.c02{color:#ea580c;}.c03{color:#ca8a04;}.c04{color:#4f46e5;}
.section{background:#fff;border-radius:14px;margin-bottom:18px;padding:24px 28px;box-shadow:0 1px 3px rgba(0,0,0,0.04);display:flex;gap:20px;align-items:flex-start;border-left:4px solid transparent;}
.section-01{border-left-color:#dc2626;}.section-02{border-left-color:#ea580c;}.section-03{border-left-color:#ca8a04;}.section-04{border-left-color:#4f46e5;}.section-05{border-left-color:#db2777;}
.section-num{flex-shrink:0;width:42px;height:42px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:17px;font-weight:bold;margin-top:2px;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif;}
.num-01{background:#fef2f2;color:#dc2626;}.num-02{background:#fff7ed;color:#ea580c;}.num-03{background:#fefce8;color:#ca8a04;}.num-04{background:#eef2ff;color:#4f46e5;}.num-05{background:#fdf2f8;color:#db2777;}
.section-body{flex:1;}
.tag{display:inline-block;font-size:11px;font-weight:bold;padding:2px 10px;border-radius:10px;margin-bottom:8px;letter-spacing:1px;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif;}
.tag-01{background:#fef2f2;color:#dc2626;}.tag-02{background:#fff7ed;color:#ea580c;}.tag-03{background:#fefce8;color:#ca8a04;}.tag-04{background:#eef2ff;color:#4f46e5;}.tag-05{background:#fdf2f8;color:#db2777;}
.section-title{font-size:18px;margin-bottom:10px;font-weight:bold;line-height:1.4;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif;}
.t-01{color:#dc2626;}.t-02{color:#ea580c;}.t-03{color:#ca8a04;}.t-04{color:#4f46e5;}.t-05{color:#db2777;}
.section-desc{font-size:14px;color:#555;line-height:1.9;margin-bottom:14px;}
.flow-row{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-top:6px;}
.flow-step{background:#fff7ed;border:1px solid #fed7aa;border-radius:10px;padding:10px 12px;text-align:center;min-width:80px;flex:1;font-size:13px;color:#9a3412;line-height:1.5;font-weight:bold;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif;}
.flow-arrow{font-size:18px;color:#ea580c;flex-shrink:0;}
.dual-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:10px;}
.dual-card{border-radius:12px;padding:18px 20px;display:flex;gap:12px;align-items:flex-start;}
.dual-card.yes{background:#fef2f2;border:1px solid #fecaca;}
.dual-card.no{background:#f0fdf4;border:1px solid #bbf7d0;}
.dual-icon{font-size:24px;flex-shrink:0;line-height:1;}
.dual-text h4{font-size:14px;color:#1a1a1a;margin-bottom:4px;font-family:'FZXPYZS','PingFang SC','Noto Serif SC',serif;}
.dual-text p{font-size:12px;color:#777;line-height:1.6;}
.timeline{border-left:3px solid #ca8a04;padding-left:18px;margin-top:10px;}
.timeline-item{margin-bottom:12px;position:relative;}
.timeline-item::before{content:'';position:absolute;left:-23px;top:6px;width:10px;height:10px;border-radius:50%;background:#ca8a04;}
.timeline-year{font-weight:bold;color:#ca8a04;font-size:13px;font-family:'FZXPYZS',serif;}
.timeline-text{font-size:13px;color:#555;line-height:1.7;}
.quote-card{background:#fdf2f8;border-left:4px solid #db2777;border-radius:10px;padding:16px 20px;margin-top:10px;font-style:italic;font-size:14px;color:#666;line-height:1.8;}
.quote-card .author{display:block;text-align:right;font-style:normal;font-size:12px;color:#db2777;margin-top:8px;}
.icon-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:10px;}
.icon-item{background:#fefce8;border:1px solid #fde68a;border-radius:10px;padding:12px;text-align:center;}
.icon-item .icon-emoji{font-size:22px;margin-bottom:4px;}
.icon-item .icon-label{font-size:12px;color:#92400e;font-weight:bold;}
.icon-item .icon-desc{font-size:11px;color:#b45309;margin-top:2px;}
.data-row{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:10px;}
.data-cell{background:#eef2ff;border:1px solid #c7d2fe;border-radius:10px;padding:12px;text-align:center;}
.data-cell .data-num{font-family:'FZXPYZS',serif;font-size:22px;font-weight:bold;color:#4f46e5;}
.data-cell .data-label{font-size:11px;color:#6366f1;margin-top:2px;}
.takeaway{background:#fff;border-left:4px solid #dc2626;border-radius:12px;padding:22px 26px;margin-bottom:24px;font-size:15px;color:#555;line-height:2.0;box-shadow:0 1px 3px rgba(0,0,0,0.04);}
.takeaway strong{color:#dc2626;}
.footer{text-align:center;font-size:12px;color:#aaa;margin-top:40px;padding-top:20px;border-top:1px solid #e8e0d5;line-height:1.8;}
@media(max-width:768px){body{padding:20px 12px 40px;}.kpi-row{grid-template-columns:repeat(2,1fr);}.dual-grid{grid-template-columns:1fr;}.icon-grid{grid-template-columns:1fr;}.data-row{grid-template-columns:1fr;}.flow-row{flex-direction:column;}.flow-arrow{transform:rotate(90deg);}.section{flex-direction:column;gap:12px;}}"""

def build_html(lang, ch_num, ch_title_zh, ch_title_en, data):
    """Build a complete infographic HTML file."""
    is_zh = lang == "zh"
    lang_label = "中文 / English"
    lang_file = f"{BOOK}-ch{ch_num:03d}-info-en.html" if is_zh else f"{BOOK}-ch{ch_num:03d}-info-zh.html"
    title = f"{BOOK} · 第{ch_num}章「{ch_title_zh}」" if is_zh else f"The World of Yesterday · Chapter {ch_num}: \"{ch_title_en}\""
    subtitle = data["subtitle_zh"] if is_zh else data["subtitle_en"]
    overview = data["overview_zh"] if is_zh else data["overview_en"]
    kpis = data["kpis_zh"] if is_zh else data["kpis_en"]
    sections = data["sections_zh"] if is_zh else data["sections_en"]
    takeaway = data["takeaway_zh"] if is_zh else data["takeaway_en"]

    # Build KPI HTML
    kpi_html = '<div class="kpi-row">\n'
    colors = ["c01","c02","c03","c04"]
    for i, (num, label) in enumerate(kpis):
        kpi_html += f'  <div class="kpi"><div class="kpi-num {colors[i]}">{num}</div><div class="kpi-label">{label}</div></div>\n'
    kpi_html += '</div>'

    # Build sections HTML
    sec_html = ""
    for i, sec in enumerate(sections):
        sn = f"0{i+1}"
        sec_html += f'<div class="section section-{sn}">\n'
        sec_html += f'  <div class="section-num num-{sn}">{i+1}</div>\n'
        sec_html += f'  <div class="section-body">\n'
        sec_html += f'    <span class="tag tag-{sn}">{sec["tag"]}</span>\n'
        sec_html += f'    <div class="section-title t-{sn}">{sec["title"]}</div>\n'
        sec_html += f'    <div class="section-desc">{sec["desc"]}</div>\n'
        if "viz" in sec:
            sec_html += sec["viz"] + "\n"
        sec_html += '  </div>\n</div>\n'

    # Footer
    footer_zh = f'<div class="footer">{BOOK} · 上海译文出版社 · 茨威格 著 · 徐友敬 译<br>信息图生成 © 2026</div>'
    footer_en = f'<div class="footer">The World of Yesterday · Stefan Zweig · Trans. Xu Youjing<br>Infographic © 2026</div>'
    footer = footer_zh if is_zh else footer_en

    html = f"""<!DOCTYPE html>
<html lang="{"zh-CN" if is_zh else "en"}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>{CSS}</style>
</head>
<body>
<div class="container">

<div style="text-align:right;margin-bottom:4px;">
  <a href="{BOOK}-catalog.html" style="font-size:12px;color:#888;text-decoration:none;font-family:'FZXPYZS','PingFang SC',serif;">← {"章节目录" if is_zh else "Chapter Catalog"}</a>
</div>
<div class="lang-switch" style="text-align:right;margin-bottom:12px;">
  <a class="lang-btn" href="{lang_file}" target="_blank" style="font-size:13px;color:#4f46e5;text-decoration:none;font-family:'FZXPYZS','PingFang SC',serif;">{lang_label}</a>
</div>

<h1>{title}</h1>
<p class="subtitle">{subtitle}</p>
<div class="divider"></div>

<div class="chapter-overview"><strong>{"概述" if is_zh else "Overview"}：</strong>{overview}</div>

{kpi_html}

{sec_html}

<div class="takeaway"><strong>{"核心结论" if is_zh else "Key Takeaway"}：</strong>{takeaway}</div>

{footer}

</div>
</body>
</html>"""
    return html

# ═══════════════════════════════════════════════════════════
# CHAPTER 13: 又回到世界上 / Back to the World
# ═══════════════════════════════════════════════════════════
ch13 = {
    "subtitle_zh": "一九一九—一九三三：战后重建、通货膨胀与黄金十年",
    "subtitle_en": "1919–1933: Postwar Reconstruction, Hyperinflation, and the Golden Decade",
    "overview_zh": "茨威格从萨尔茨堡的隐居中走出，重新踏上旅途。在意大利受到热情接待，亲历威尼斯法西斯首次亮相；在德国目睹拉特瑙被暗杀后马克崩溃的疯狂通货膨胀；一九二四至一九三三年的短暂和平中，他的文学事业达到巅峰——作品被翻译最多、读者遍及全球，同时他以压缩与精炼的写作方法确立了独特的艺术风格。",
    "overview_en": "Zweig emerges from isolation in Salzburg and resumes traveling. Welcomed warmly in Italy, he witnesses the first Fascist march in Venice; in Germany he sees Rathenau's assassination trigger hyperinflation madness; during the brief peace of 1924–1933 his literary career peaks—most-translated author, global readership—while his compression-driven writing method defines his art.",
    "kpis_zh": [("1919–21", "战后隔绝三年"), ("1:1万亿", "马克贬值极限"), ("25万册", "《群星闪耀时》印数"), ("1924–33", "黄金十年")],
    "kpis_en": [("1919–21", "3 yrs postwar isolation"), ("1:1 Trillion", "Mark devaluation peak"), ("250K copies", "Stars of Humanity"), ("1924–33", "Golden decade")],
    "sections_zh": [
        {"tag": "重逢", "title": "越过国界：战争仇恨的幻灭",
         "desc": "<strong>战争宣传的仇恨从未触及真正的民众。</strong>茨威格鼓起勇气越过意奥边境，维罗纳门房惊喜地说"终于来了一个奥地利人"。在米兰重逢老友博尔盖塞，"敌国"友谊五分钟内恢复如初。佛罗伦萨街头画家旧友冲来拥抱。所有煽动和仇恨只是使头脑一时发热，欧洲真正的群众从未被触及。",
         "viz": '<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🤝</div><div class="dual-text"><h4>真实的人</h4><p>门房热情接待、老友真诚拥抱——民间友谊从未断裂</p></div></div><div class="dual-card no"><div class="dual-icon">📢</div><div class="dual-text"><h4>宣传的仇恨</h4><p>战时敌意只是表面，群众心底的善意始终存在</p></div></div></div>'},
        {"tag": "警钟", "title": "威尼斯法西斯：第一声警钟",
         "desc": "<strong>法西斯不是乌合之众，而是领导得非常好的力量。</strong>在威尼斯，茨威格第一次亲眼看到法西斯冲锋队——年轻人迈着训练有素的步伐，唱着《青年之歌》，挥舞棍棒闪电般冲过罢工人群，然后消失无踪。他从此意识到，和平还不是真正的和平，欧洲水面下潜藏着危险暗流。",
         "viz": '<div class="flow-row"><div class="flow-step">总罢工<br>城市瘫痪</div><div class="flow-arrow">→</div><div class="flow-step">冲锋队<br>闪电突袭</div><div class="flow-arrow">→</div><div class="flow-step">训练有素<br>全身而退</div><div class="flow-arrow">→</div><div class="flow-step">第一次<br>警钟敲响</div></div>'},
        {"tag": "疯狂", "title": "拉特瑙遇刺与通货膨胀",
         "desc": "<strong>通货膨胀使德国充满仇恨和杀机，这是永远的教训。</strong>拉特瑙在拉巴洛谈判中取得最好成果，却在柏林街头被暗杀。随后马克崩溃——早上五万买报纸，晚上十万；鞋带的钱过去能买一间鞋店；乞丐把十万马克扔进排水沟。整个社会道德沦丧，柏林成为罪恶渊薮。",
         "viz": '<div class="timeline"><div class="timeline-item"><span class="timeline-year">1922</span><div class="timeline-text">拉特瑙在柏林被暗杀，德国不幸开始</div></div><div class="timeline-item"><span class="timeline-year">1923</span><div class="timeline-text">马克贬值到万亿比一，物价每小时翻倍</div></div><div class="timeline-item"><span class="timeline-year">1923</span><div class="timeline-text">施廷内斯靠贬值吞并四分之一德国财富</div></div><div class="timeline-item"><span class="timeline-year">1924</span><div class="timeline-text">新马克发行，混乱结束，但仇恨已种下</div></div></div>'},
        {"tag": "巅峰", "title": "文学成就：世界建筑师",
         "desc": "<strong>成就来自对冗长的极度反感和对压缩的执着追求。</strong>《马来狂人》《一个陌生女人的来信》大获成功，《人类群星闪耀时》印数达二十五万册，高尔基为俄文全集作序。茨威格的写作方法是反复压缩——一千页留二百页精华，他的座右铭是"绝不能只看表面现象，重要的是了解事物的内情"。",
         "viz": '<div class="data-row"><div class="data-cell"><div class="data-num">全球第一</div><div class="data-label">被翻译最多的作家</div></div><div class="data-cell"><div class="data-num">50+国</div><div class="data-label">译本覆盖国家</div></div><div class="data-cell"><div class="data-num">2万册/日</div><div class="data-label">新书首日销量</div></div></div>'},
        {"tag": "自省", "title": "成就与自由：隐姓埋名的渴望",
         "desc": "<strong>成就是一把双刃剑，真正的自由在于保持匿名。</strong>茨威格对成就保持清醒——他把名字看作标记，一旦成名就脱离主体成为权力。他本能地拒绝抛头露面，总是坐在最后一排。他认为如果重新开始，会用笔名发表作品，"一箭双雕：既享受文学成就的幸福，又享受隐姓匿名的平静"。",
         "viz": '<div class="quote-card">"任何一个酷爱自由的人，如果到处刊登他的照片，他身上最美好的东西就会受到阻碍和歪曲。"<span class="author">——茨威格</span></div>'}
    ],
    "sections_en": [
        {"tag": "Reunion", "title": "Crossing the Border: The Illusion of Hatred",
         "desc": "<strong>Wartime propaganda never truly reached ordinary people.</strong> Zweig braves the Italian border, where a porter joyfully exclaims 'An Austrian at last!' In Milan, old friend Borghese embraces him within five minutes; in Florence, painter friend Stirlinga rushes to hug him on the street. All wartime animosity was superficial—European goodwill endured underneath.",
         "viz": '<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🤝</div><div class="dual-text"><h4>Real People</h4><p>Warm porters, sincere friends—cross-border friendship never broke</p></div></div><div class="dual-card no"><div class="dual-icon">📢</div><div class="dual-text"><h4>Propaganda Hatred</h4><p>Hostility was surface-deep; genuine goodwill persisted</p></div></div></div>'},
        {"tag": "Alarm", "title": "Venice Fascism: The First Warning Bell",
         "desc": "<strong>Fascism was no mob—it was superbly organized force.</strong> In Venice, Zweig witnessed Fascist squads march in disciplined formation, singing Giovinezza, striking through striking workers with lightning speed before vanishing. He realized peace was illusory—dangerous currents lurked beneath Europe's calm surface.",
         "viz": '<div class="flow-row"><div class="flow-step">General Strike<br>City paralyzed</div><div class="flow-arrow">→</div><div class="flow-step">Squad Storm<br>Lightning raid</div><div class="flow-arrow">→</div><div class="flow-step">Trained Retreat<br>No arrests</div><div class="flow-arrow">→</div><div class="flow-step">First Alarm<br>Sounded</div></div>'},
        {"tag": "Madness", "title": "Rathenau's Assassination & Hyperinflation",
         "desc": "<strong>Inflation filled Germany with hatred and murderous intent—a lasting lesson.</strong> Rathenau achieved brilliant results at Rapallo but was assassinated in Berlin. The Mark then collapsed: 50,000 for a morning paper, 100,000 by evening; a shoelace cost what once bought a shoe shop; beggars discarded 100,000-Mark notes. Society's moral fabric disintegrated.",
         "viz": '<div class="timeline"><div class="timeline-item"><span class="timeline-year">1922</span><div class="timeline-text">Rathenau assassinated in Berlin—Germany\'s tragedy begins</div></div><div class="timeline-item"><span class="timeline-year">1923</span><div class="timeline-text">Mark hits trillion-to-one; prices double hourly</div></div><div class="timeline-item"><span class="timeline-year">1923</span><div class="timeline-text">Stinnes swallows quarter of German wealth via inflation</div></div><div class="timeline-item"><span class="timeline-year">1924</div><div class="timeline-text">New Mark issued; chaos ends but hatred is planted</div></div></div>'},
        {"tag": "Peak", "title": "Literary Fame: Architect of the World",
         "desc": "<strong>Fame came from relentless hatred of verbosity and devotion to compression.</strong> The Amok Letter and Letter from a Stranger were huge successes; Star-Hour of Humanity reached 250,000 copies; Gorky wrote the preface to the Russian edition. Zweig's method was radical cutting—1,000 pages distilled to 200, seeking 'the inner truth behind appearances.'",
         "viz": '<div class="data-row"><div class="data-cell"><div class="data-num">#1 Global</div><div class="data-label">Most translated author</div></div><div class="data-cell"><div class="data-num">50+ Countries</div><div class="data-label">Translation coverage</div></div><div class="data-cell"><div class="data-num">20K/day</div><div class="data-label">New book first-day sales</div></div></div>'},
        {"tag": "Reflection", "title": "Fame vs. Freedom: The Longing for Anonymity",
         "desc": "<strong>Fame is a double-edged sword; true freedom lies in anonymity.</strong> Zweig stayed清醒 about success—seeing a name as a label that, once famous, detaches from the self and becomes a force. He instinctively avoided publicity, always sitting in the last row. He wished he had used a pen name: 'enjoying both literary happiness and the peace of anonymity.'",
         "viz": '<div class="quote-card">"Anyone who loves freedom, if his photograph is published everywhere, finds his finest qualities obstructed and distorted."<span class="author">— Stefan Zweig</span></div>'}
    ],
    "takeaway_zh": "战争宣传的仇恨是肤浅的，民众心底的善意从未消失；但法西斯的组织化暴力已预示未来的灾难。茨威格在短暂的和平十年中达到文学巅峰，却始终保持清醒——真正的自由不在名声之中，而在匿名的内心独立。",
    "takeaway_en": "Wartime hatred was superficial—genuine goodwill endured. But organized Fascist violence foreshadowed future catastrophe. Zweig reached his literary peak in the brief peaceful decade yet remained清醒: true freedom lies not in fame but in anonymous inner independence."
}

# ═══════════════════════════════════════════════════════════
# CHAPTER 14: 日落 / Sunset
# ═══════════════════════════════════════════════════════════
ch14 = {
    "subtitle_zh": "黄金十年的旅行、俄国之行与萨尔茨堡的文艺盛会",
    "subtitle_en": "The Golden Decade: Travels, Russia, and Salzburg's Cultural Glory",
    "overview_zh": "一九二四至一九三三年，茨威格以世界主义作家身份游历各国，在布鲁塞尔、佛罗伦萨、美洲用当地语言演讲。一九二八年赴俄参加托尔斯泰纪念活动，目睹新旧俄国的矛盾；在索伦托与高尔基结下深厚友谊。萨尔茨堡成为世界艺术圣地，他的家成为欧洲文化名人的落脚处，名人手迹收藏也臻于巅峰。",
    "overview_en": "From 1924 to 1933, Zweig traveled widely as a cosmopolitan writer, lecturing in local languages across Europe and the Americas. In 1928 he attended Tolstoy's centenary in Russia, witnessing old and new Russia's contradictions; in Sorrento he forged deep friendship with Gorky. Salzburg became a world arts capital, his home a gathering place for cultural luminaries, and his autograph collection reached its peak.",
    "kpis_zh": [("14天", "苏维埃俄国之行"), ("3天", "索伦托与高尔基"), ("4000+册", "手迹收藏参考书"), ("1924–33", "萨尔茨堡艺术节黄金期")],
    "kpis_en": [("14 days", "Soviet Russia visit"), ("3 days", "Sorrento with Gorky"), ("4000+ vols", "Autograph reference"), ("1924–33", "Salzburg festival peak")],
    "sections_zh": [
        {"tag": "旅行", "title": "世界主义作家的欧洲之旅",
         "desc": "<strong>旅行从青年时代的好奇变成了传播欧洲精神统一的使命。</strong>茨威格在瑞士和荷兰演讲，用法语在布鲁塞尔艺术宫发言，用意大利语在佛罗伦萨演讲，用英语在美洲巡回。他不再籍籍无名，到处有朋友、出版人和读者。巴黎圣日耳曼的宫殿、费城古董商的店铺向他敞开大门，但他仍怀念青年时代无人等候的独自旅行。",
         "viz": '<div class="icon-grid"><div class="icon-item"><div class="icon-emoji">🇧🇪</div><div class="icon-label">布鲁塞尔</div><div class="icon-desc">法语演讲</div></div><div class="icon-item"><div class="icon-emoji">🇮🇹</div><div class="icon-label">佛罗伦萨</div><div class="icon-desc">意大利语演讲</div></div><div class="icon-item"><div class="icon-emoji">🇺🇸</div><div class="icon-label">美洲巡回</div><div class="icon-desc">英语演讲</div></div></div>'},
        {"tag": "俄国", "title": "苏维埃俄国：热情与矛盾的十四天",
         "desc": "<strong>俄国是一个有才能的心地善良的大孩子，急于求成却令人感动。</strong>茨威格穿越波兰到达莫斯科，目睹红场旁古老圣像与列宁水晶棺的并存。工人们第一次看到缝纫机就激动地以为是革命的发明。冬宫里，农民穿着沉重靴鞋缓缓穿过皇帝的殿堂，怯生生地抬头看伦勃朗的画。一切都是拔苗助长式的认真学习。",
         "viz": '<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">✨</div><div class="dual-text"><h4>新俄国的光芒</h4><p>人民热情、自豪、渴求知识，"这是我们自己做的"</p></div></div><div class="dual-card no"><div class="dual-icon">⚠️</div><div class="dual-text"><h4>旧俄国的阴影</h4><p>官僚臃肿、效率低下、奥勃洛摩夫式怠倦</p></div></div></div>'},
        {"tag": "友谊", "title": "高尔基：永恒民族的灵魂",
         "desc": "<strong>高尔基是世界文学中最有天才的叙述家，他身上集中体现了俄罗斯原型。</strong>在索伦托三天的相处中，茨威格发现高尔基叙述时会变成所描绘的人——脑袋耷拉、双肩下垂就变成了驼背老人。高尔基自称"流亡"，每天都想回国。俄国水兵来访时质问他为何住资产阶级的房子，他笑着解释，然后和他们拥抱告别。",
         "viz": '<div class="quote-card">"我们与他们是多么不同啊。我们不是畏首畏尾就是激烈无比，但从来不能把握自己。"<span class="author">——高尔基</span></div>'},
        {"tag": "圣地", "title": "萨尔茨堡：世界艺术的新奥林匹亚",
         "desc": "<strong>在自己的城市里，茨威格等于生活在欧洲的中心。</strong>萨尔茨堡从偏僻小城变成世界艺术朝拜圣地，各国最优秀的音乐家、演员竞相前来。托斯卡尼尼、理查德·施特劳斯、拉威尔、威尔斯、乔伊斯、罗曼·罗兰……茨威格的家成为欧洲文化名人的落脚处。从阳台上可以眺望对面贝希特斯加登山——希特勒就住在那座山上。",
         "viz": '<div class="icon-grid"><div class="icon-item"><div class="icon-emoji">🎵</div><div class="icon-label">音乐大师</div><div class="icon-desc">托斯卡尼尼·施特劳斯·拉威尔</div></div><div class="icon-item"><div class="icon-emoji">✍️</div><div class="icon-label">文学巨匠</div><div class="icon-desc">罗曼·罗兰·乔伊斯·威尔斯</div></div><div class="icon-item"><div class="icon-emoji">📜</div><div class="icon-label">手迹收藏</div><div class="icon-desc">莫扎特·贝多芬·歌德·巴尔扎克</div></div></div>'},
        {"tag": "收藏", "title": "名人手迹：不朽时刻的凝固",
         "desc": "<strong>收藏从追求签名升华到捕捉天才创作鼎盛时期的手稿。</strong>茨威格从十五岁开始收藏，最终拥有四千多册参考书和最珍贵的大师手稿：达芬奇笔记、拿破仑军令、巴尔扎克小说校样、尼采《悲剧的诞生》初稿、莫扎特十一岁手稿、歌德从九岁到八十二岁的十五件手稿。这些是"不朽巨人遗留下来的珍贵手稿"。",
         "viz": '<div class="data-row"><div class="data-cell"><div class="data-num">达·芬奇</div><div class="data-label">工作笔记手稿</div></div><div class="data-cell"><div class="data-num">莫扎特</div><div class="data-label">十一岁至逝世前</div></div><div class="data-cell"><div class="data-num">歌德</div><div class="data-label">9岁→82岁全生涯</div></div></div>'}
    ],
    "sections_en": [
        {"tag": "Travel", "title": "A Cosmopolitan Writer's European Journey",
         "desc": "<strong>Travel evolved from youthful curiosity into a mission to spread European spiritual unity.</strong> Zweig lectured in Switzerland, Holland, Brussels (in French), Florence (in Italian), and the Americas (in English). No longer unknown, he had friends, publishers, and readers everywhere. Paris palaces and Philadelphia antique shops opened their doors, yet he still longed for the solitary travels of youth.",
         "viz": '<div class="icon-grid"><div class="icon-item"><div class="icon-emoji">🇧🇪</div><div class="icon-label">Brussels</div><div class="icon-desc">French lecture</div></div><div class="icon-item"><div class="icon-emoji">🇮🇹</div><div class="icon-label">Florence</div><div class="icon-desc">Italian lecture</div></div><div class="icon-item"><div class="icon-emoji">🇺🇸</div><div class="icon-label">Americas</div><div class="icon-desc">English lecture</div></div></div>'},
        {"tag": "Russia", "title": "Soviet Russia: Fourteen Days of Passion and Paradox",
         "desc": "<strong>Russia was a talented, good-hearted child—earnest but impatient.</strong> Zweig crossed Poland to Moscow, witnessing Red Square's ancient icons alongside Lenin's crystal coffin. Workers激动 over a sewing machine, believing it a革命 invention. In the Winter Palace, peasants in heavy boots shuffled past Rembrandt paintings, looking up shyly—diligent learning, but拔苗助长.",
         "viz": '<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">✨</div><div class="dual-text"><h4>New Russia's Light</h4><p>People热情, proud, eager to learn: "We made this ourselves"</p></div></div><div class="dual-card no"><div class="dual-icon">⚠️</div><div class="dual-text"><h4>Old Russia's Shadow</h4><p>Bloated bureaucracy, inefficiency, Oblomov-like inertia</p></div></div></div>'},
        {"tag": "Friendship", "title": "Gorky: Soul of an Eternal Nation",
         "desc": "<strong>Gorky was literature's greatest narrator—he became what he described.</strong> During three days in Sorrento, Zweig saw Gorky physically transform into a hunched old man while narrating. Gorky called his exile a daily torment. When young sailors visited and批评 his bourgeois house, he laughed, explained, then embraced them goodbye.",
         "viz": '<div class="quote-card">"How different we are from them! We were either timid or extreme, but never able to hold ourselves in balance."<span class="author">— Gorky</span></div>'},
        {"tag": "Mecca", "title": "Salzburg: The New Olympia of Art",
         "desc": "<strong>In his own city, Zweig lived at the center of Europe.</strong> Salzburg transformed from a provincial town into a world arts pilgrimage site. Toscanini, Richard Strauss, Ravel, Wells, Joyce, Romain Rolland—Zweig's home became a gathering place. From his balcony he could see Berchtesgaden mountain, where Hitler lived.",
         "viz": '<div class="icon-grid"><div class="icon-item"><div class="icon-emoji">🎵</div><div class="icon-label">Music Masters</div><div class="icon-desc">Toscanini · Strauss · Ravel</div></div><div class="icon-item"><div class="icon-emoji">✍️</div><div class="icon-label">Literary Giants</div><div class="icon-desc">Rolland · Joyce · Wells</div></div><div class="icon-item"><div class="icon-emoji">📜</div><div class="icon-label">Autographs</div><div class="icon-desc">Mozart · Beethoven · Goethe</div></div></div>'},
        {"tag": "Collection", "title": "Autographs: Frozen Moments of Genius",
         "desc": "<strong>Collecting evolved from signatures to capturing masters' creative peaks.</strong> Starting at fifteen, Zweig amassed 4,000+ reference volumes and priceless manuscripts: da Vinci's notebooks, Napoleon's battle orders, Balzac's galley proofs, Nietzsche's Birth of Tragedy draft, Mozart's age-11 manuscript, Goethe's papers spanning ages 9 to 82—'precious manuscripts left by immortal giants.'",
         "viz": '<div class="data-row"><div class="data-cell"><div class="data-num">Da Vinci</div><div class="data-label">Work notebook</div></div><div class="data-cell"><div class="data-num">Mozart</div><div class="data-label">Age 11 to deathbed</div></div><div class="data-cell"><div class="data-num">Goethe</div><div class="data-label">Full life: age 9→82</div></div></div>'}
    ],
    "takeaway_zh": "黄金十年是茨威格一生最珍贵的时光——旅行、交友、创作、收藏齐头并进，萨尔茨堡成为世界文化中心。但在这表面的繁荣之下，贝希特斯加登山上的阴影正在逼近，"我们不知道，在对面住着一个要破坏这一切的人"。",
    "takeaway_en": "The golden decade was Zweig's most precious time—travel, friendship, creation, and collecting flourished together, with Salzburg as Europe's cultural center. But beneath this prosperity, the shadow from Berchtesgaden was closing in: 'We did not know that across the mountain lived a man who would destroy all of this.'"
}

# ═══════════════════════════════════════════════════════════
# CHAPTER 15: 希特勒的崛起 / Hitler's Rise
# ═══════════════════════════════════════════════════════════
ch15 = {
    "subtitle_zh": "从啤酒馆小丑到独裁者：一个时代的沦陷",
    "subtitle_en": "From Beer-Hall Agitator to Dictator: The Fall of an Era",
    "overview_zh": "茨威格以亲历者的视角，追溯希特勒从无名小卒到独裁者的崛起过程。德国人因学历崇拜而低估他，各党派都以为能利用他。纳粹上台后，从焚书到迫害犹太人，步步升级。茨威格与理查德·施特劳斯合写歌剧《沉默的女人》，在纳粹禁令与艺术自由之间上演了一场荒诞的拉锯战。",
    "overview_en": "From a witness's perspective, Zweig traces Hitler's rise from nobody to dictator. Germans低估 him due to学历崇拜; every party thought it could use him. After the Nazis took power, escalation went from book-burning to persecution. Zweig's opera collaboration with Richard Strauss on The Silent Woman上演了一场 absurd tug-of-war between Nazi bans and artistic freedom.",
    "kpis_zh": [("1933.1", "希特勒上台"), ("1部歌剧", "与施特劳斯合写"), ("数百位", "被焚书作家"), ("2.5小时", "萨尔茨堡到慕尼黑")],
    "kpis_en": [("Jan 1933", "Hitler takes power"), ("1 opera", "With Strauss"), ("Hundreds", "Authors banned"), ("2.5 hrs", "Salzburg to Munich")],
    "sections_zh": [
        {"tag": "崛起", "title": "啤酒馆里的煽动者",
         "desc": "<strong>德国的学历崇拜使知识分子把希特勒看作啤酒馆小丑，这是一个致命的错误。</strong>在德国，所有高级职务都由受过高等教育的人担任。一个没读完中学、在收容所过夜的人竟能觊觎俾斯麦的位子？知识分子嗤之以鼻。但希特勒的冲锋队装备精良——簇新的军服、汽车、摩托车——背后必有军方和大资本的支持。",
         "viz": '<div class="dual-grid"><div class="dual-card no"><div class="dual-icon">🎓</div><div class="dual-text"><h4>知识分子的判断</h4><p>"啤酒馆小丑"，不可能成为危险人物</p></div></div><div class="dual-card yes"><div class="dual-icon">⚡</div><div class="dual-text"><h4>实际情况</h4><p>有组织、有资金、有军事训练的准军事力量</p></div></div></div>'},
        {"tag": "欺骗", "title": "各取所需的集体幻觉",
         "desc": "<strong>希特勒对所有阶层和政党都许过愿——每个人都以为他是自己的朋友。</strong>君主主义者认为他是皇帝的先锋，工业家以为能借他抵御布尔什维克，小市民期待他"打破利息的桎梏"，军方喜欢他的军国主义，社会民主党希望他消灭共产党，甚至犹太人也自欺欺人地认为"当上部长的雅各宾派"会温和行事。",
         "viz": '<div class="icon-grid"><div class="icon-item"><div class="icon-emoji">👑</div><div class="icon-label">君主派</div><div class="icon-desc">"他是皇帝的先锋"</div></div><div class="icon-item"><div class="icon-emoji">🏭</div><div class="icon-label">工业家</div><div class="icon-desc">"抵御布尔什维克"</div></div><div class="icon-item"><div class="icon-emoji">🏪</div><div class="icon-label">小市民</div><div class="icon-desc">"打破利息桎梏"</div></div><div class="icon-item"><div class="icon-emoji">⚔️</div><div class="icon-label">军方</div><div class="icon-desc">"痛骂和平主义"</div></div><div class="icon-item"><div class="icon-emoji">🚩</div><div class="icon-label">社民党</div><div class="icon-desc">"消灭共产党"</div></div><div class="icon-item"><div class="icon-emoji">✡️</div><div class="icon-label">犹太人</div><div class="icon-desc">"部长不会极端"</div></div></div>'},
        {"tag": "升级", "title": "试探与升级：纳粹的投毒策略",
         "desc": "<strong>纳粹像用药一样逐步加大剂量，直到毒死整个欧洲。</strong>国会纵火案后一切法律化为乌有，集中营设在和平环境中。禁书没有法律依据，先唆使大学生焚书，再逐步禁止出版和销售。茨威格的《灼人的秘密》电影因片名被联想为嘲笑纵火案而遭禁映。世界良知总是"与己无关"，剂量便越来越大。",
         "viz": '<div class="flow-row"><div class="flow-step">国会纵火案<br>法律消失</div><div class="flow-arrow">→</div><div class="flow-step">大学生焚书<br>"民众愤怒"</div><div class="flow-arrow">→</div><div class="flow-step">禁止出版<br>全面封锁</div><div class="flow-arrow">→</div><div class="flow-step">集中营<br>恐怖统治</div></div>'},
        {"tag": "歌剧", "title": "《沉默的女人》：一场荒诞的拉锯战",
         "desc": "<strong>茨威格的作品让希特勒本人都陷入了恼怒的尴尬境地。</strong>施特劳斯不顾禁令坚持与犹太人茨威格合作。纳粹想禁止歌剧却找不到借口——剧本没有伤风败俗，也没有政治内容。最终希特勒不得不亲自阅读三幕歌剧，破例批准演出。但施特劳斯一封坦率的信被盖世太保截获后，歌剧遭禁，施特劳斯被迫辞职。",
         "viz": '<div class="timeline"><div class="timeline-item"><span class="timeline-year">1933</span><div class="timeline-text">施特劳斯坚持与茨威格合作，无视种族禁令</div></div><div class="timeline-item"><span class="timeline-year">1934</span><div class="timeline-text">纳粹各部门互相推诿，无人敢决定</div></div><div class="timeline-item"><span class="timeline-year">1934</span><div class="timeline-text">希特勒亲自破例批准——出于政治算计</div></div><div class="timeline-item"><span class="timeline-year">1934</span><div class="timeline-text">施特劳斯的信被截获，歌剧遭永久禁演</div></div></div>'},
        {"tag": "流亡", "title": "萨尔茨堡的最后日子",
         "desc": "<strong>住在德奥边境的茨威格，比维也纳的朋友更清楚地看到危险。</strong>他的老朋友在街上假装没看见他，打电话来又说不出重要的话——友谊在恐惧中蒸发。奥地利人互相打气"那边的事不会长久"，就像当年俄国出版者说"委员会共和国不会超过两星期"。一九三三年十月，茨威格离开萨尔茨堡，没想到那是永别。",
         "viz": '<div class="quote-card">"那边的事不会长久的。"——奥地利人的口头禅，与当年俄国人说"委员会不会超过两星期"如出一辙。<span class="author">——茨威格</span></div>'}
    ],
    "sections_en": [
        {"tag": "Rise", "title": "The Beer-Hall Agitator",
         "desc": "<strong>Germany's学历崇拜 led intellectuals to dismiss Hitler as a clown—a fatal error.</strong> In Germany, all top positions went to university graduates. A man who never finished secondary school and slept in shelters aspiring to Bismarck's chair? Intellectuals scoffed. But Hitler's SA had brand-new uniforms, cars, motorcycles—clearly backed by military and big money.",
         "viz": '<div class="dual-grid"><div class="dual-card no"><div class="dual-icon">🎓</div><div class="dual-text"><h4>Intellectuals' Judgment</h4><p>"Beer-hall clown"—impossible to become dangerous</p></div></div><div class="dual-card yes"><div class="dual-icon">⚡</div><div class="dual-text"><h4>Reality</h4><p>Organized, funded, militarily trained paramilitary force</p></div></div></div>'},
        {"tag": "Deception", "title": "Collective Delusion: Everyone's Friend",
         "desc": "<strong>Hitler made promises to every class and party—each believed he was their friend.</strong> Monarchists saw皇帝's vanguard; industrialists wanted him against Bolshevism; small shopkeepers期待 him to 'break the shackles of interest'; the military liked his militarism; Social Democrats hoped he'd crush Communists; even Jews deceived themselves that a 'minister Jacobin' would be温和.",
         "viz": '<div class="icon-grid"><div class="icon-item"><div class="icon-emoji">👑</div><div class="icon-label">Monarchists</div><div class="icon-desc">"Emperor\'s先锋"</div></div><div class="icon-item"><div class="icon-emoji">🏭</div><div class="icon-label">Industrialists</div><div class="icon-desc">"Against Bolshevism"</div></div><div class="icon-item"><div class="icon-emoji">🏪</div><div class="icon-label">Shopkeepers</div><div class="icon-desc">"Break interest shackles"</div></div><div class="icon-item"><div class="icon-emoji">⚔️</div><div class="icon-label">Military</div><div class="icon-desc">"Anti-pacifism"</div></div><div class="icon-item"><div class="icon-emoji">🚩</div><div class="icon-label">Social Democrats</div><div class="icon-desc">"Crush Communists"</div></div><div class="icon-item"><div class="icon-emoji">✡️</div><div class="icon-label">Jews</div><div class="icon-desc">"Minister won\'t be extreme"</div></div></div>'},
        {"tag": "Escalation", "title": "Testing and Escalating: The Poisoning Strategy",
         "desc": "<strong>Nazis increased dosage like medicine until they poisoned all of Europe.</strong> After the Reichstag fire, all laws vanished; concentration camps appeared in peaceful neighborhoods. Book bans had no legal basis—they first incited students to burn books, then逐步禁止 publishing. Zweig's film 'Burning Secret' was banned because the title was联想为 mocking the fire. Europe's conscience said 'not our concern,' so dosage kept rising.",
         "viz": '<div class="flow-row"><div class="flow-step">Reichstag Fire<br>Laws vanish</div><div class="flow-arrow">→</div><div class="flow-step">Student Book-Burning<br>"Public anger"</div><div class="flow-arrow">→</div><div class="flow-step">Publishing Ban<br>Full blockade</div><div class="flow-arrow">→</div><div class="flow-step">Concentration Camps<br>Reign of Terror</div></div>'},
        {"tag": "Opera", "title": "The Silent Woman: An Absurd Tug-of-War",
         "desc": "<strong>Zweig's work put Hitler himself in an embarrassing predicament.</strong> Strauss defied racial bans to collaborate with Jewish Zweig. Nazis wanted to ban the opera but found no excuse—no indecency, no politics. Hitler personally read the three-act opera and granted an exception. But when Strauss's candid letter was intercepted by the Gestapo, the opera was permanently banned and Strauss forced to resign.",
         "viz": '<div class="timeline"><div class="timeline-item"><span class="timeline-year">1933</span><div class="timeline-text">Strauss insists on collaborating with Zweig despite racial ban</div></div><div class="timeline-item"><span class="timeline-year">1934</span><div class="timeline-text">Nazi departments pass the buck—no one dares decide</div></div><div class="timeline-item"><span class="timeline-year">1934</span><div class="timeline-text">Hitler personally grants exception—political calculation</div></div><div class="timeline-item"><span class="timeline-year">1934</span><div class="timeline-text">Strauss\'s letter intercepted; opera permanently banned</div></div></div>'},
        {"tag": "Exile", "title": "Last Days in Salzburg",
         "desc": "<strong>Living on the German-Austrian border, Zweig saw danger more clearly than Vienna friends.</strong> An old friend pretended not to see him on the street, then called saying nothing important—friendship evaporated in fear. Austrians reassured each other 'it won't last,' just as the Russian publisher once said 'the committee republic won\'t last two weeks.' In October 1933, Zweig left Salzburg, not knowing it was farewell.",
         "viz": '<div class="quote-card">"It won\'t last on that side"—Austria\'s mantra, echoing the Russian who said "the committee won\'t last two weeks."<span class="author">— Stefan Zweig</span></div>'}
    ],
    "takeaway_zh": "希特勒的崛起不是偶然——每个阶层都因自私的算计而成为帮凶。纳粹的"试探与升级"策略利用了欧洲良知的冷漠。茨威格与施特劳斯的歌剧之争，是艺术自由与极权暴力之间最荒诞的缩影：连希特勒本人都被一个犹太作家的作品难住了。",
    "takeaway_en": "Hitler's rise was no accident—every class became complicit through selfish calculation. The Nazi 'test and escalate' strategy exploited Europe's indifferent conscience. The Zweig-Strauss opera saga was the most absurd epitome of artistic freedom vs. totalitarian power: even Hitler himself was stumped by a Jewish writer's work."
}

# ═══════════════════════════════════════════════════════════
# CHAPTER 16: 和平的濒死状态 / The Agony of Peace
# ═══════════════════════════════════════════════════════════
ch16 = {
    "subtitle_zh": "流亡、绥靖与弗洛伊德的最后时光",
    "subtitle_en": "Exile, Appeasement, and Freud's Final Days",
    "overview_zh": "茨威格在伦敦开始半流亡生活，目睹奥地利沦陷、绥靖政策的失败与慕尼黑协定的虚幻和平。他与弗洛伊德在伦敦的最后交往，成为黑暗时代最珍贵的精神慰藉。无国籍者的屈辱、犹太人的悲剧、欧洲文明的崩塌，最终在二战爆发那天汇成一个时代的终结。",
    "overview_en": "Zweig begins semi-exile in London, witnessing Austria's fall, the failure of appeasement, and Munich's illusory peace. His final encounters with Freud in London become the most precious spiritual comfort in dark times. The humiliation of statelessness, the Jewish tragedy, and European文明's collapse converge in WWII's outbreak as an era ends.",
    "kpis_zh": [("1938.3", "奥地利沦陷"), ("1938.9", "慕尼黑协定"), ("1939.9", "二战爆发"), ("83岁", "弗洛伊德在伦敦")],
    "kpis_en": [("Mar 1938", "Austria falls"), ("Sep 1938", "Munich Agreement"), ("Sep 1939", "WWII begins"), ("Age 83", "Freud in London")],
    "sections_zh": [
        {"tag": "流亡", "title": "伦敦的半流亡：失去祖国的痛楚",
         "desc": "<strong>一个人随着祖国的灭亡所失去的，要比那一片有限的国土大得多。</strong>茨威格在伦敦租了一间小公寓，恍如三十年前维也纳的学生房间——同样的大小，同样的布莱克画作。他已五十岁，又要重新开始。无国籍者的白卡是一种经申请得来的照顾，随时可能被收回。护照上的图章犹如犯人脸上的烙印。",
         "viz": '<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🏠</div><div class="dual-text"><h4>三十年前</h4><p>维也纳小房间，充满希望的起点</p></div></div><div class="dual-card no"><div class="dual-icon">📦</div><div class="dual-text"><h4>三十年后</h4><p>伦敦同样大小的房间，流亡者的临时栖身</p></div></div></div>'},
        {"tag": "沦陷", "title": "奥地利沦陷：最后的告别",
         "desc": "<strong>一九三八年三月十三日，奥地利以及全欧洲都成了赤裸裸的暴力的战利品。</strong>茨威格最后一次回维也纳，朋友们无忧无虑地聚会、吸香烟、买圣诞礼物——他们不知道几个月后会被关进集中营。老母亲去世时，他感到的不是悲痛而是宽慰——她不必再遭受"不准犹太人坐在长椅上"的侮辱。女看护因种族法律拒绝在临终老人身旁过夜。",
         "viz": '<div class="timeline"><div class="timeline-item"><span class="timeline-year">1937 秋</span><div class="timeline-text">最后一次回维也纳，感到"永别"的情感</div></div><div class="timeline-item"><span class="timeline-year">1938.3</span><div class="timeline-text">奥地利沦陷，暴力横行，犹太人遭系统迫害</div></div><div class="timeline-item"><span class="timeline-year">1938</span><div class="timeline-text">母亲去世，茨威格感到宽慰而非悲痛</div></div><div class="timeline-item"><span class="timeline-year">1938</span><div class="timeline-text">旧奥地利护照失效，沦为无国籍者</div></div></div>'},
        {"tag": "绥靖", "title": "慕尼黑协定：虚幻的和平",
         "desc": "<strong>张伯伦到慕尼黑不是去争取和平，而是去乞求和平。</strong>一九三八年九月，英国国会听到慕尼黑会议的消息时爆发出前所未有的欢呼。张伯伦挥动"为了我们时代的和平"的文件，电影院观众起立欢呼。茨威格自己也激动不已，在街上走得越来越快。但几天后真相大白：这是一次彻底的投降。",
         "viz": '<div class="flow-row"><div class="flow-step">戈德斯贝格<br>绥靖失败</div><div class="flow-arrow">→</div><div class="flow-step">慕尼黑会议<br>举国欢腾</div><div class="flow-arrow">→</div><div class="flow-step">条约墨迹未干<br>希特勒违约</div><div class="flow-arrow">→</div><div class="flow-step">幻想破灭<br>战争逼近</div></div>'},
        {"tag": "弗洛伊德", "title": "弗洛伊德：黑暗时代的精神灯塔",
         "desc": "<strong>弗洛伊德是道德勇气的象征——世界上唯一不要求别人牺牲的英雄主义。</strong>八十三岁的弗洛伊德从维也纳逃到伦敦，比以前更开朗、精神更饱满。他每天用清晰的字体写作，拒绝服用安眠药——"宁愿清醒地被病痛折磨，也不愿被麻木"。达利为他画了速写，画面上的死神已经清晰可见。弗洛伊德像罗马英雄一样，要求医生结束他的痛苦。",
         "viz": '<div class="quote-card">"很少有百分之百的真理，就像没有百分之百的酒精一样！"<span class="author">——弗洛伊德</span></div>'},
        {"tag": "终结", "title": "战争又降临：一个时代的终结",
         "desc": "<strong>我们命该遇到这样的时代。</strong>一九三九年九月一日，茨威格正在巴斯登记结婚，官员突然冲进来喊道："德国人入侵波兰，战争爆发了！"英国向德国宣战，茨威格从外国人变为"敌邦的外国人"。他走到小镇上，最后一次看一眼和平的景象——阳光和煦，鸟儿啾啾，"大自然，古老的母亲，又一次无法体会她的造物的苦痛"。",
         "viz": '<div class="quote-card">"每一个影子毕竟还是光明的产儿，而且，只有经历了光明和黑暗、和平与战争、兴盛和衰败的人，才算是真正生活过。"<span class="author">——茨威格</span></div>'}
    ],
    "sections_en": [
        {"tag": "Exile", "title": "London Semi-Exile: The Pain of Losing祖国",
         "desc": "<strong>What one loses with祖国's fall far exceeds a有限 piece of land.</strong> Zweig rented a small London flat, eerily similar to his Vienna student room—same size, same Blake painting. At fifty, he must start over. The stateless white card was a revocable favor. Passport stamps felt like prisoner's brands on the face.",
         "viz": '<div class="dual-grid"><div class="dual-card yes"><div class="dual-icon">🏠</div><div class="dual-text"><h4>30 Years Ago</h4><p>Vienna student room—hopeful beginning</p></div></div><div class="dual-card no"><div class="dual-icon">📦</div><div class="dual-text"><h4>30 Years Later</h4><p>Same-size London room—exile\'s temporary shelter</p></div></div></div>'},
        {"tag": "Fall", "title": "Austria Falls: The Final Farewell",
         "desc": "<strong>On March 13, 1938, Austria and all Europe became prizes of naked violence.</strong> Zweig's last visit to Vienna: friends partying carelessly, smoking, buying Christmas gifts—months before concentration camps. When his mother died, he felt relief, not grief—she need not endure 'Jews may not sit on benches.' A nurse refused to stay overnight near a dying老人 due to racial laws.",
         "viz": '<div class="timeline"><div class="timeline-item"><span class="timeline-year">Autumn 1937</span><div class="timeline-text">Last visit to Vienna—feeling of "final farewell"</div></div><div class="timeline-item"><span class="timeline-year">Mar 1938</span><div class="timeline-text">Austria falls; systematic Jewish persecution</div></div><div class="timeline-item"><span class="timeline-year">1938</span><div class="timeline-text">Mother dies—Zweig feels relief, not grief</div></div><div class="timeline-item"><span class="timeline-year">1938</span><div class="timeline-text">Austrian passport expires; becomes stateless</div></div></div>'},
        {"tag": "Appeasement", "title": "Munich Agreement: Illusory Peace",
         "desc": "<strong>Chamberlain went to Munich not to争取 peace but to乞求 it.</strong> In September 1938, Parliament erupted in unprecedented cheers at news of the Munich conference. Chamberlain waved 'Peace for our time'; cinema audiences stood and cheered. Zweig himself felt elated, walking faster and faster through London. Days later the truth emerged: it was total surrender.",
         "viz": '<div class="flow-row"><div class="flow-step">Godesberg<br>Appeasement fails</div><div class="flow-arrow">→</div><div class="flow-step">Munich Conference<br>National euphoria</div><div class="flow-arrow">→</div><div class="flow-step">Ink Not Dry<br>Hitler breaks treaty</div><div class="flow-arrow">→</div><div class="flow-step">Illusion Shatters<br>War approaches</div></div>'},
        {"tag": "Freud", "title": "Freud: A Spiritual Lighthouse in Darkness",
         "desc": "<strong>Freud embodied moral courage—heroism that demands no sacrifice from others.</strong> At 83, Freud fled Vienna to London, more cheerful than before. He wrote daily in clear script, refusing sleeping pills—'I prefer清醒 suffering to numbness.' Dalí sketched him with death already visible. Like a Roman hero, Freud asked his doctor to end his suffering.",
         "viz": '<div class="quote-card">"There are few truths as certain as there is no 100% alcohol!"<span class="author">— Sigmund Freud</span></div>'},
        {"tag": "End", "title": "War Returns: The End of an Era",
         "desc": "<strong>"We are destined to live in such times."</strong> On September 1, 1939, Zweig was registering his marriage in Bath when an official burst in: "Germany has invaded Poland—war has begun!" Britain declared war; Zweig became an 'enemy alien.' He walked through town for a last glimpse of peace—sunshine, birdsong—'Nature, the ancient mother, once again cannot feel her creatures\' suffering.'",
         "viz": '<div class="quote-card">"Every shadow is after all a child of light, and only those who have experienced light and darkness, peace and war, rise and fall, have truly lived."<span class="author">— Stefan Zweig</span></div>'}
    ],
    "takeaway_zh": "和平的死亡不是一瞬间的事——它在绥靖政策的自欺欺人中慢慢窒息。茨威格在失去祖国后才明白：失去的远不止一片国土，而是整个自我存在的根基。弗洛伊德以清醒的意志面对死亡，成为黑暗时代最后的精神灯塔。"只有经历了光明和黑暗的人，才算是真正生活过。"",
    "takeaway_en": "Peace did not die in an instant—it suffocated slowly in appeasement's self-deception. Zweig learned after losing his homeland: what's lost far exceeds land—it's the very foundation of existence. Freud faced death with清醒 will, becoming the last spiritual lighthouse. 'Only those who have experienced light and darkness have truly lived.'"
}

# ── Generate all files ──
chapters = [
    (13, "又回到世界上", "Back to the World", ch13),
    (14, "日落", "Sunset", ch14),
    (15, "希特勒的崛起", "Hitler's Rise", ch15),
    (16, "和平的濒死状态", "The Agony of Peace", ch16),
]

for ch_num, zh_title, en_title, data in chapters:
    for lang in ("zh", "en"):
        fname = f"{BOOK}-ch{ch_num:03d}-info-{lang}.html"
        html = build_html(lang, ch_num, zh_title, en_title, data)
        (OUT / fname).write_text(html, encoding="utf-8")
        print(f"✅ {fname}")

print("\nDone! All 8 files generated.")
