#!/usr/bin/env python3
"""Generate 8 ZH+EN info HTML files for Zen & Motorcycle Maintenance ch13-16."""
import json, os

BOOKDIR = os.path.expanduser("~/.openclaw/workspace/infographics/books")
SLUG = "zen-motorcycle"
BOOK_TITLE_ZH = "禅与摩托车维修艺术"
BOOK_TITLE_EN = "Zen and the Art of Motorcycle Maintenance"

with open(f"{BOOKDIR}/_zen_chapters_13_16.json", "r", encoding="utf-8") as f:
    chapters = json.load(f)

BASE_CSS = '''  @font-face {
    font-family: 'FZXPYZS';
    src: url('../方正屏显雅宋简体.TTF') format('truetype');
    font-weight: normal; font-style: normal;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    background: #f5f1eb;
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', 'STSong', Georgia, serif;
    display: flex; justify-content: center; align-items: flex-start;
    min-height: 100vh; padding: 40px 20px 60px;
  }
  .container { max-width: 880px; width: 100%; }

  h1 {
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
    font-size: 36px; color: #1a1a1a; text-align: center;
    line-height: 1.4; margin-bottom: 8px; font-weight: normal;
    letter-spacing: 1.5px;
  }
  .subtitle {
    text-align: center; font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
    font-size: 14px; color: #888; margin-bottom: 24px; line-height: 1.7;
    max-width: 640px; margin-left: auto; margin-right: auto;
  }
  .divider {
    width: 60px; height: 3px;
    background: linear-gradient(90deg, #dc2626, #ea580c);
    margin: 0 auto 28px; border-radius: 2px;
  }

  .section {
    background: #ffffff; border-radius: 14px;
    margin-bottom: 18px; padding: 24px 28px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    display: flex; gap: 20px; align-items: flex-start;
    border-left: 4px solid transparent;
  }
  .section-01 { border-left-color: #dc2626; }
  .section-02 { border-left-color: #ea580c; }
  .section-03 { border-left-color: #ca8a04; }
  .section-04 { border-left-color: #4f46e5; }
  .section-05 { border-left-color: #db2777; }

  .section-num {
    flex-shrink: 0; width: 42px; height: 42px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 17px; font-weight: bold; margin-top: 2px;
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
  }
  .num-01 { background: #fef2f2; color: #dc2626; }
  .num-02 { background: #fff7ed; color: #ea580c; }
  .num-03 { background: #fefce8; color: #ca8a04; }
  .num-04 { background: #eef2ff; color: #4f46e5; }
  .num-05 { background: #fdf2f8; color: #db2777; }

  .section-body { flex: 1; }
  .tag {
    display: inline-block; font-size: 11px; font-weight: bold;
    padding: 2px 10px; border-radius: 10px; margin-bottom: 8px;
    letter-spacing: 1px; font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
  }
  .tag-01 { background: #fef2f2; color: #dc2626; }
  .tag-02 { background: #fff7ed; color: #ea580c; }
  .tag-03 { background: #fefce8; color: #ca8a04; }
  .tag-04 { background: #eef2ff; color: #4f46e5; }
  .tag-05 { background: #fdf2f8; color: #db2777; }

  .section-title {
    font-size: 18px; margin-bottom: 10px; font-weight: bold; line-height: 1.4;
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
  }
  .t-01 { color: #dc2626; } .t-02 { color: #ea580c; }
  .t-03 { color: #ca8a04; } .t-04 { color: #4f46e5; }
  .t-05 { color: #db2777; }

  .section-desc {
    font-size: 14px; color: #555; line-height: 1.9; margin-bottom: 14px;
  }

  .dual-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 10px; }
  .dual-card {
    border-radius: 12px; padding: 18px 20px;
    display: flex; gap: 12px; align-items: flex-start;
    border: 1px solid;
  }
  .dual-card.a { background: #fef2f2; border-color: #fecaca; }
  .dual-card.b { background: #fff7ed; border-color: #fed7aa; }
  .dual-card.c { background: #eef2ff; border-color: #c7d2fe; }
  .dual-card.d { background: #fdf2f8; border-color: #fbcfe8; }

  .dual-icon { font-size: 28px; flex-shrink: 0; line-height: 1.2; }
  .dual-text h4 { font-size: 15px; margin-bottom: 6px; color: #1a1a1a;
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif; }
  .dual-text p { font-size: 13px; color: #555; line-height: 1.7; }

  .flow-row {
    display: flex; gap: 14px; align-items: center; margin-top: 14px;
    justify-content: center;
  }
  .flow-step {
    background: #fff7ed; border: 1px solid #fed7aa; border-radius: 10px;
    padding: 12px 18px; text-align: center; font-size: 13px;
    color: #9a3412; font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
    line-height: 1.6; min-width: 120px;
  }
  .flow-step.end {
    background: #fef2f2; border-color: #fecaca; color: #991b1b;
  }
  .flow-arrow { font-size: 20px; color: #ea580c; font-weight: bold; }

  .kpi-row {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 16px; margin: 24px 0;
  }
  .kpi-row.cols-4 { grid-template-columns: repeat(4, 1fr); }
  .kpi-card {
    background: #fff; border: 1px solid #e8e0d5; border-radius: 14px;
    padding: 24px 20px 18px; text-align: center;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    display: flex; flex-direction: column; align-items: center;
  }
  .kpi-value {
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
    font-size: 42px; font-weight: bold; color: #1a1a1a; line-height: 1.1;
    margin-bottom: 6px; letter-spacing: -0.5px;
  }
  .kpi-unit { font-size: 18px; font-weight: normal; color: #888; margin-left: 2px; }
  .kpi-label { font-size: 13px; color: #888; margin-bottom: 10px; letter-spacing: 0.5px; }
  .kpi-note { font-size: 11px; color: #bbb; line-height: 1.6;
    border-top: 1px solid #f0ebe0; padding-top: 10px; width: 100%; text-align: center; }
  .kpi-card.c01 { border-left: 3px solid #dc2626; } .kpi-card.c01 .kpi-value { color: #dc2626; }
  .kpi-card.c02 { border-left: 3px solid #ea580c; } .kpi-card.c02 .kpi-value { color: #ea580c; }
  .kpi-card.c03 { border-left: 3px solid #ca8a04; } .kpi-card.c03 .kpi-value { color: #ca8a04; }
  .kpi-card.c04 { border-left: 3px solid #4f46e5; } .kpi-card.c04 .kpi-value { color: #4f46e5; }

  .takeaway {
    background: #ffffff; border-radius: 14px;
    padding: 28px 32px; margin-top: 24px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    border: 1px solid #e8e0d5;
  }
  .takeaway-label {
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
    font-size: 16px; font-weight: bold; color: #dc2626; margin-bottom: 12px;
  }
  .takeaway-text {
    font-size: 15px; color: #555; line-height: 2.0;
  }

  .footer {
    text-align: center; margin-top: 32px; padding-top: 20px;
    border-top: 1px solid #e8e0d5; color: #bbb; font-size: 13px; line-height: 1.8;
  }

  .lang-switch { text-align: right; margin-bottom: 16px; }
  .lang-btn {
    display: inline-block; padding: 6px 16px; border-radius: 8px;
    font-size: 13px; text-decoration: none; letter-spacing: 0.03em;
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
    background: #fef2f2; color: #dc2626; border: 1px solid #fecaca;
    transition: opacity 0.15s;
  }
  .lang-btn:hover { opacity: 0.75; }

  .confusion-table { margin-top: 10px; }
  .confusion-row {
    display: flex; align-items: center; gap: 14px;
    padding: 10px 14px; border-bottom: 1px solid #f0ebe0;
  }
  .confusion-row:last-child { border-bottom: none; }
  .confusion-left {
    font-weight: bold; color: #1a1a1a; font-size: 14px;
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
    min-width: 110px;
  }
  .confusion-arrow { color: #ca8a04; font-size: 14px; flex-shrink: 0; }
  .confusion-right { color: #555; font-size: 13px; line-height: 1.6; }

  .data-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-top: 12px; }
  .data-card {
    background: #faf9f6; border: 1px solid #e8e0d5; border-radius: 12px;
    padding: 18px 16px; text-align: center;
  }
  .data-big {
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
    font-size: 24px; font-weight: bold; margin-bottom: 6px;
  }
  .d1 .data-big { color: #dc2626; } .d2 .data-big { color: #ea580c; }
  .d3 .data-big { color: #4f46e5; }
  .data-name { font-size: 14px; color: #1a1a1a; margin-bottom: 6px;
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif; }
  .data-sm { font-size: 12px; color: #888; line-height: 1.6; }

  @media (max-width: 640px) {
    .section { flex-direction: column; align-items: center; text-align: center;
      border-left: none; border-top: 4px solid transparent; padding-top: 20px; }
    .section-01 { border-top-color: #dc2626; } .section-02 { border-top-color: #ea580c; }
    .section-03 { border-top-color: #ca8a04; } .section-04 { border-top-color: #4f46e5; }
    .section-05 { border-top-color: #db2777; }
    .dual-grid, .data-row { grid-template-columns: 1fr; }
    .flow-row { flex-direction: column; }
    .flow-arrow { transform: rotate(90deg); }
    .confusion-row { flex-direction: column; align-items: stretch; }
    .confusion-left { text-align: center; }
    .container { padding: 0 8px; }
    h1 { font-size: 26px; }
    .kpi-row, .kpi-row.cols-4 { grid-template-columns: repeat(2, 1fr); }
    .kpi-value { font-size: 34px; }
  }
  @media (max-width: 400px) {
    .kpi-row, .kpi-row.cols-4 { grid-template-columns: 1fr; }
  }
  .back-catalog{text-align:right;margin-bottom:4px}.back-catalog-btn{display:inline-block;padding:5px 14px;border-radius:8px;font-size:12px;text-decoration:none;letter-spacing:.02em;background:#eef2ff;color:#4f46e5;border:1px solid #c7d2fe;transition:opacity .15s}.back-catalog-btn:hover{opacity:.75}
  .chapter-overview{background:#f8f6f3;border-left:3px solid #4f46e5;border-radius:8px;padding:16px 20px;margin:12px 0 24px;font-size:14px;color:#555;line-height:1.8;font-family:'FZXPYZS','PingFang SC',serif}.chapter-overview p{margin:0}
'''


def build_html(lang, ch_num, data):
    """Build a complete info HTML for one chapter in zh/en."""
    is_zh = (lang == "zh")
    lang_attr = "zh-CN" if is_zh else "en"
    book_title = BOOK_TITLE_ZH if is_zh else BOOK_TITLE_EN
    ch_title = data["zh_title"] if is_zh else data["en_title"]
    subtitle = data["zh_subtitle"] if is_zh else data["en_subtitle"]
    overview = data["zh_overview"] if is_zh else data["en_overview"]
    kpi_list = data["kpi_zh"] if is_zh else data["kpi_en"]
    sections = data["sections_zh"] if is_zh else data["sections_en"]
    takeaway = data["takeaway_zh"] if is_zh else data["takeaway_en"]

    # lang switch
    en_file = f"{SLUG}-ch{ch_num}-info-en.html"
    zh_file = f"{SLUG}-ch{ch_num}-info-zh.html"
    if is_zh:
        lang_text = "中文 / English"
        lang_href = en_file
    else:
        lang_text = "中文 / English"
        lang_href = zh_file

    # Build KPI HTML
    kpi_html = '<div class="kpi-row cols-4">\n'
    colors = ["c01", "c02", "c03", "c04"]
    for i, k in enumerate(kpi_list[:4]):
        ci = colors[i]
        unit_html = f'<span class="kpi-unit">{k["u"]}</span>' if k["u"] else ""
        kpi_html += f'''  <div class="kpi-card {ci}">
    <div class="kpi-value">{k["v"]}{unit_html}</div>
    <div class="kpi-label">{k["l"]}</div>
    <div class="kpi-note">{k["n"]}</div>
  </div>
'''
    kpi_html += '</div>\n'

    # Build sections HTML
    sec_html = ""
    for i, s in enumerate(sections):
        ni = i + 1
        # Choose visualization based on content
        viz_html = build_viz(ni, s, is_zh)

        sec_html += f'''<!-- {ni:02d}: {s["tag"]} -->
<div class="section section-{ni:02d}">
  <div class="section-num num-{ni:02d}">{ni:02d}</div>
  <div class="section-body">
    <div class="tag tag-{ni:02d}">{s["tag"]}</div>
    <div class="section-title t-{ni:02d}">{s["title"]}</div>
    <div class="section-desc">{s["desc"]}</div>
    {viz_html}
  </div>
</div>
'''

    # footer
    ch_label = f"第{int(ch_num)}章「{ch_title}」" if is_zh else f'Chapter {int(ch_num)} "{ch_title}"'
    source_zh = f"来源：罗伯特·M·波西格《禅与摩托车维修艺术》{ch_label} · 信息图 · 仅供学习参考"
    source_en = f'Source: Robert M. Pirsig, "Zen and the Art of Motorcycle Maintenance" {ch_label} · Infographic · For educational reference only'
    footer_text = source_zh if is_zh else source_en

    html = f'''<!DOCTYPE html>
<html lang="{lang_attr}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{book_title} · {ch_title}</title>
<style>
{BASE_CSS}
</style>
</head>
<body>
<div class="container">
<div class="back-catalog"><a class="back-catalog-btn" href="{SLUG}-catalog.html">← 返回章节目录</a></div>
<div class="lang-switch">
  <a class="lang-btn" target="_blank" href="{lang_href}">{lang_text}</a>
</div>

<h1>{book_title} · {ch_title}</h1>
<p class="subtitle">{subtitle}</p>
<div class="divider"></div>
<div class="chapter-overview">
  <p>{overview}</p>
</div>

{kpi_html}
{sec_html}
<!-- Key Takeaway -->
<div class="takeaway">
  <div class="takeaway-label">{"🔑 核心结论" if is_zh else "🔑 Key Takeaway"}</div>
  <div class="takeaway-text">{takeaway}</div>
</div>

<!-- Footer -->
<div class="footer">{footer_text}</div>

</div>
</body>
</html>'''
    return html


def build_viz(sec_num, s, is_zh):
    """Build appropriate visualization component for a section based on content."""
    tag = s["tag"]

    # Section 1 (red): Typically a flow/process - use dual-grid
    if sec_num == 1:
        left_title = "关键事件" if is_zh else "Key Events"
        left_text = ("极右派暴动·教授被禁演说·$8000不及格罚金·50人黑名单" if tag in ["校园政治","Campus Politics"] else
                     "从啤酒招牌到理性教会——斐德洛以教堂类比大学" if tag in ["核心理念","Core Idea"] else
                     "思薇雅三次回头张望·酒吧告别·叙述者保持距离" if tag in ["告别","Farewell"] else
                     "松针铺地·阳光如教堂光芒·75英里无人森林" if tag in ["登山","Ascent"] else
                     "描述要点A" if is_zh else "Key point A")
        right_title = "核心回应" if is_zh else "Core Response"
        right_text = ("斐德洛致信评鉴委员会·班上学生力主学术自由·公开呼吁调查" if tag in ["校园政治","Campus Politics"] else
                      "真正的大学不存在于任何特定建筑之内——撤销承认=被逐出教会" if tag in ["核心理念","Core Idea"] else
                      "「他们是我的朋友，并不是书中的人物」——斐德洛教书的紧张回忆浮现" if tag in ["告别","Farewell"] else
                      "斐德洛的良质探讨正是开拓一条到达灵性高峰的路径" if tag in ["登山","Ascent"] else
                      "描述要点B" if is_zh else "Key point B")
        return f'''    <div class="dual-grid">
      <div class="dual-card a">
        <div class="dual-icon">📋</div>
        <div class="dual-text">
          <h4>{left_title}</h4>
          <p>{left_text}</p>
        </div>
      </div>
      <div class="dual-card b">
        <div class="dual-icon">💡</div>
        <div class="dual-text">
          <h4>{right_title}</h4>
          <p>{right_text}</p>
        </div>
      </div>
    </div>'''

    # Section 2 (orange): typically a flow
    elif sec_num == 2:
        step_labels = ["问题", "转化", "答案"] if is_zh else ["Problem", "Shift", "Answer"]
        steps = [
            ("修辞学无逻辑可言" if is_zh else "Rhetoric has no logic"),
            ("教科书把修辞当作理性分支" if is_zh else "Textbook treats rhetoric as reason"),
            ("直接观察才是唯一的写作法" if is_zh else "Direct observation is the only way"),
        ]
        return f'''    <div class="flow-row">
      <div class="flow-step">{steps[0]}</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">{steps[1]}</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step end">{steps[2]}</div>
    </div>'''

    # Section 3 (gold): typically a process/results
    elif sec_num == 3:
        rows = [
            ("斐德洛 → 牧师 → 服事上帝（真理）" if is_zh else "Phaedrus → Minister → Serve God (Truth)"),
            ("执事 → 威胁削预算 → 牧师「没听见」" if is_zh else "Deacons → Threaten budget cuts → Minister ignores"),
            ("教授 → 面对压力 → 保持对真理忠诚" if is_zh else "Professor → Under pressure → Loyal to truth"),
        ]
        html = '<div class="confusion-table">\n'
        for r in rows:
            if is_zh:
                parts = r.split(" → ")
            else:
                parts = r.split(" → ")
            html += f'''      <div class="confusion-row">
        <div class="confusion-left">{parts[0]}</div>
        <div class="confusion-arrow">→</div>
        <div class="confusion-right">{parts[1] if len(parts)>1 else ""}</div>
      </div>
'''
        html += '    </div>'
        return html

    # Section 4 (indigo): typically insights/paradox
    elif sec_num == 4:
        left_title = "表面" if is_zh else "Surface"
        left_text = ("对理性狂热信仰" if is_zh else "Fanatically believes in reason")
        right_title = "深层" if is_zh else "Depth"
        right_text = ("对理性缺乏信心（互为因果）" if is_zh else "Lacks faith in reason (cause and effect)")
        return f'''    <div class="dual-grid">
      <div class="dual-card c">
        <div class="dual-icon">🔍</div>
        <div class="dual-text">
          <h4>{left_title}</h4>
          <p>{left_text}</p>
        </div>
      </div>
      <div class="dual-card d">
        <div class="dual-icon">🧠</div>
        <div class="dual-text">
          <h4>{right_title}</h4>
          <p>{right_text}</p>
        </div>
      </div>
    </div>'''

    # Section 5 (pink): typically meta/conclusion
    else:
        cards = [
            ("考古学家", "挖开尘封千年的坟墓——回忆片断与别人讲述" if is_zh else "Archaeologist", "Opening tombs sealed for millennia — fragments of memory and others' accounts"),
            ("《少数人的教会》", "纽约邮购的复制品——半抽象线条中的理性教会精神" if is_zh else '"Church of the Few"', "Mail-ordered reproduction from New York — the spirit of reason in semi-abstract lines"),
            ("这扇窗户", "发狂的地点——站在此处看麦迪逊山脉" if is_zh else "This Window", "Where he went mad — looking across at the Madison Range"),
        ]
        html = '<div class="data-row">\n'
        dc = ["d1", "d2", "d3"]
        for i, c in enumerate(cards[:3]):
            html += f'''      <div class="data-card {dc[i]}">
        <div class="data-big">{c[0]}</div>
        <div class="data-name">{c[1]}</div>
        <div class="data-sm">{c[2]}</div>
      </div>
'''
        html += '    </div>'
        return html


def validate_file(filepath):
    """Validate a generated HTML file."""
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    issues = []
    opens = html.count("<div")
    closes = html.count("</div>")
    if opens != closes:
        issues.append(f"DIV imbalance: {opens}/{closes}")

    # Check 10 mandatory layers
    checks = [
        ("catalog", 'class="back-catalog"'),
        ("lang-switch", 'class="lang-switch"'),
        ("H1", "<h1>"),
        ("subtitle", 'class="subtitle"'),
        ("divider", 'class="divider"'),
        ("chapter-overview", 'class="chapter-overview"'),
        ("KPI", 'class="kpi-row'),
        ("5 sections", '<div class="section section-'),
        ("takeaway", 'class="takeaway"'),
        ("footer", 'class="footer"'),
    ]
    for name, pattern in checks:
        if pattern not in html:
            issues.append(f"Missing: {name}")

    # Check section count
    sec_count = html.count('<div class="section section-')
    if sec_count != 5:
        issues.append(f"Section count: {sec_count} (expected 5)")

    # Check font
    if "FZXPYZS" not in html:
        issues.append("Missing FZXPYZS font")

    # Check background
    if "#f5f1eb" not in html:
        issues.append("Missing #f5f1eb background")

    # Check flex centering
    body_css = html[html.find("body {"):html.find("}", html.find("body {"))+50]
    if "display: flex" not in body_css:
        issues.append("Missing body display:flex")
    if "justify-content: center" not in body_css:
        issues.append("Missing body justify-content:center")

    return issues


# ─── MAIN ───
results = []
for ch_num in ["13", "14", "15", "16"]:
    data = chapters[ch_num]

    # Generate ZH
    zh_path = os.path.join(BOOKDIR, f"{SLUG}-ch{ch_num}-info-zh.html")
    zh_html = build_html("zh", ch_num, data)
    with open(zh_path, "w", encoding="utf-8") as f:
        f.write(zh_html)
    zh_issues = validate_file(zh_path)
    results.append((f"ch{ch_num}-ZH", len(zh_html), zh_issues))

    # Generate EN
    en_path = os.path.join(BOOKDIR, f"{SLUG}-ch{ch_num}-info-en.html")
    en_html = build_html("en", ch_num, data)
    with open(en_path, "w", encoding="utf-8") as f:
        f.write(en_html)
    en_issues = validate_file(en_path)
    results.append((f"ch{ch_num}-EN", len(en_html), en_issues))

# Print results
print("=" * 60)
print("GENERATION RESULTS")
print("=" * 60)
all_ok = True
for name, size, issues in results:
    status = "✅ OK" if not issues else "❌ FAIL"
    if issues:
        all_ok = False
    print(f"  {name}: {size:,} bytes → {status}")
    for iss in issues:
        print(f"    ⚠️  {iss}")

print("-" * 60)
if all_ok:
    print("ALL 8 FILES PASSED ✓")
else:
    print("SOME FILES HAVE ISSUES — CHECK ABOVE")
print("=" * 60)