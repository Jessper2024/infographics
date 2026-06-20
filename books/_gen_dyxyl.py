#!/usr/bin/env python3
import os, json

BOOKDIR = os.path.expanduser("~/.openclaw/workspace/infographics/books")
SLUG = "第一性原理"
BOOK_ZH = "第一性原理"
BOOK_EN = "First Principles"
AUTHOR_ZH = "李善友"
AUTHOR_EN = "Li Shanyou"

# Load chapter data from JSON files
chapters = {}
for ch_num in range(1, 5):
    data_file = os.path.join(BOOKDIR, f"_dyxyl_data_ch{ch_num:03d}.json")
    with open(data_file, "r", encoding="utf-8") as f:
        chapters[ch_num] = json.load(f)

# ── Build component HTML ──
def build_section_html(s, idx):
    colors = ["01", "02", "03", "04", "05"]
    c = colors[idx % 5]
    tag = s["tag"]
    title_s = s["title"]
    desc = s["desc"]
    comp = s["component"]

    comp_html = ""
    if comp == "dual":
        yes = s["dual_yes"]
        no = s["dual_no"]
        comp_html = f"""        <div class="dual-grid">
          <div class="dual-card yes">
            <div class="dual-icon">✅</div>
            <div class="dual-text">
              <h4>{yes["h4"]}</h4>
              <p>{yes["p"]}</p>
            </div>
          </div>
          <div class="dual-card no">
            <div class="dual-icon">❌</div>
            <div class="dual-text">
              <h4>{no["h4"]}</h4>
              <p>{no["p"]}</p>
            </div>
          </div>
        </div>"""
    elif comp == "flow":
        steps = s["flow_steps"]
        pieces = []
        for j, step in enumerate(steps):
            cls = "end" if j == len(steps) - 1 else ""
            pieces.append(f'<div class="flow-step {cls}">{step}</div>')
            if j < len(steps) - 1:
                pieces.append('<div class="flow-arrow">→</div>')
        flow_html = "\n            ".join(pieces)
        comp_html = f'        <div class="flow-row">\n            {flow_html}\n          </div>'

    return f"""    <!-- Section {idx+1} / {c} -->
    <div class="section section-{c}">
      <div class="section-num num-{c}">{idx+1:02d}</div>
      <div class="section-body">
        <span class="tag tag-{c}">{tag}</span>
        <div class="section-title t-{c}">{title_s}</div>
        <div class="section-desc">{desc}</div>
{comp_html}
      </div>
    </div>"""

# ── Master CSS ──
MASTER_CSS = '''  @font-face {
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

  /* ── Lang switch ── */
  .lang-switch { text-align: right; margin-bottom: 16px; }
  .lang-btn {
    display: inline-block; padding: 6px 16px; border-radius: 8px;
    font-size: 13px; text-decoration: none; letter-spacing: 0.03em;
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
    background: #fef2f2; color: #dc2626; border: 1px solid #fecaca;
    transition: opacity 0.15s;
  }
  .lang-btn:hover { opacity: 0.75; }

  /* ── Back to catalog ── */
  .back-catalog {
    text-align: left; margin-bottom: 8px;
  }
  .back-catalog a {
    font-size: 13px; color: #4f46e5; text-decoration: none;
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
  }
  .back-catalog a:hover { text-decoration: underline; }

  /* ── Header ── */
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

  /* ── Overview splash ── */
  .splash {
    background: #ffffff; border: 1px solid #e8e0d5; border-radius: 14px;
    padding: 28px 32px; margin-bottom: 24px; color: #555;
    font-size: 15px; line-height: 2.0;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    border-left: 4px solid #4f46e5;
  }

  /* ── KPI row ── */
  .kpi-row {
    display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px;
    margin-bottom: 24px;
  }
  .kpi-card {
    background: #ffffff; border: 1px solid #e8e0d5; border-radius: 12px;
    padding: 16px 12px; text-align: center;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
  }
  .kpi-label {
    font-size: 11px; color: #888; margin-bottom: 6px;
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
    letter-spacing: 1px;
  }
  .kpi-value {
    font-size: 22px; color: #1a1a1a; font-weight: bold;
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
  }

  /* ── Section base ── */
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

  /* ── Dual comparison ── */
  .dual-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 10px; }
  .dual-card {
    border-radius: 12px; padding: 18px 20px;
    display: flex; gap: 12px; align-items: flex-start;
  }
  .dual-card.yes { background: #f0fdf4; border: 1px solid #bbf7d0; }
  .dual-card.no { background: #fef2f2; border: 1px solid #fecaca; }
  .dual-icon { font-size: 24px; flex-shrink: 0; line-height: 1; }
  .dual-text h4 { font-size: 14px; color: #1a1a1a; margin-bottom: 4px; font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif; }
  .dual-text p { font-size: 12px; color: #777; line-height: 1.6; }

  /* ── Flow diagram ── */
  .flow-row {
    display: flex; align-items: center; gap: 8px; flex-wrap: wrap;
    margin-top: 6px;
  }
  .flow-step {
    background: #fff7ed; border: 1px solid #fed7aa; border-radius: 10px;
    padding: 10px 12px; text-align: center; min-width: 80px; flex: 1;
    font-size: 13px; color: #9a3412; line-height: 1.5; font-weight: bold;
  }
  .flow-arrow { font-size: 20px; color: #ea580c; flex-shrink: 0; font-weight: bold; }
  .flow-step.end { background: #fef2f2; border-color: #fecaca; color: #991b1b; }

  /* ── Key Takeaway ── */
  .takeaway {
    background: #ffffff; border: 1px solid #e8e0d5; border-radius: 14px;
    padding: 24px 32px; margin-bottom: 18px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    border-left: 4px solid #dc2626;
  }
  .takeaway-label {
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
    font-size: 12px; color: #dc2626; letter-spacing: 2px; margin-bottom: 6px;
    font-weight: bold;
  }
  .takeaway-text {
    font-size: 16px; color: #1a1a1a; line-height: 1.9;
    font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif;
  }

  /* ── Footer ── */
  .footer {
    text-align: center; margin-top: 32px; padding-top: 20px;
    border-top: 1px solid #e8e0d5; color: #bbb; font-size: 13px; line-height: 1.8;
  }

  /* ── Responsive ── */
  @media (max-width: 640px) {
    .section { flex-direction: column; align-items: center; text-align: center; border-left: none; border-top: 4px solid transparent; padding-top: 20px; }
    .section-01 { border-top-color: #dc2626; }
    .section-02 { border-top-color: #ea580c; }
    .section-03 { border-top-color: #ca8a04; }
    .section-04 { border-top-color: #4f46e5; }
    .section-05 { border-top-color: #db2777; }
    .section-body { text-align: center; }
    .dual-grid { grid-template-columns: 1fr; }
    .flow-row { flex-direction: column; }
    .flow-arrow { transform: rotate(90deg); }
    .kpi-row { grid-template-columns: repeat(2, 1fr); }
    .data-row { grid-template-columns: 1fr; }
  }'''

# ── Generate all 8 files ──
for lang in ["zh", "en"]:
    for ch_num in range(1, 5):
        ch = chapters[ch_num]
        is_zh = (lang == "zh")
        L = "zh-CN" if is_zh else "en"

        title_s = ch["title_zh"] if is_zh else ch["title_en"]
        subtitle_s = ch["subtitle_zh"] if is_zh else ch["subtitle_en"]
        overview_s = ch["overview_zh"] if is_zh else ch["overview_en"]
        takeaway_s = ch["takeaway_zh"] if is_zh else ch["takeaway_en"]
        book_title = BOOK_ZH if is_zh else BOOK_EN
        sections = ch["sections_zh"] if is_zh else ch["sections_en"]

        # KPI
        kpis = ch["kpi"]
        kpi_parts = []
        for k in kpis:
            label = k["label_zh"] if is_zh else k["label_en"]
            val = k["value_zh"] if is_zh else k["value_en"]
            kpi_parts.append(f"""      <div class="kpi-card">
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{val}</div>
      </div>""")
        kpi_html = "\n".join(kpi_parts)

        # Sections
        section_parts = [build_section_html(s, i) for i, s in enumerate(sections)]
        sections_html = "\n".join(section_parts)

        # Language switch link
        other_lang = "en" if is_zh else "zh"
        other_label = "EN" if is_zh else "中文"
        other_file = f"{SLUG}-ch{ch_num:03d}-info-{other_lang}.html"

        # Catalog link
        nav_catalog = f"{SLUG}-catalog.html"

        # Chapter number labels
        ch_label_zh = ["一", "二", "三", "四"][ch_num-1]
        ch_label_en = ["One", "Two", "Three", "Four"][ch_num-1]
        ch_label = f"第{ch_label_zh}" if is_zh else f"Chapter {ch_label_en}"

        # Footer
        if is_zh:
            footer_line1 = f"李善友 · 第一性原理 · 第{ch_label_zh}章 · 图书信息图"
            footer_line2 = "来源：第一性原理（李善友 著，人民邮电出版社，2021）"
        else:
            footer_line1 = f"Li Shanyou · First Principles · Chapter {ch_label_en} · Book Infographic"
            footer_line2 = "Source: First Principles by Li Shanyou (Posts & Telecom Press, 2021)"

        html = f'''<!DOCTYPE html>
<html lang="{L}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{book_title} · {ch_label}「{title_s}」</title>
<style>
{MASTER_CSS}
</style>
</head>
<body>
<div class="container">

  <!-- Language Switch -->
  <div class="lang-switch">
    <a class="lang-btn" href="{other_file}">{other_label}</a>
  </div>

  <!-- Back to Catalog -->
  <div class="back-catalog">
    <a href="{nav_catalog}">← 返回章节目录</a>
  </div>

  <!-- Chapter Title -->
  <h1>{book_title} · {ch_label}「{title_s}」</h1>

  <!-- Subtitle -->
  <div class="subtitle">{subtitle_s}</div>

  <!-- Divider -->
  <div class="divider"></div>

  <!-- Overview -->
  <div class="splash">
    <p>{overview_s}</p>
  </div>

  <!-- KPI Row -->
  <div class="kpi-row">
{kpi_html}
  </div>

  <!-- Content Sections -->
{sections_html}

  <!-- Key Takeaway -->
  <div class="takeaway">
    <div class="takeaway-label">{"📌 核心启示" if is_zh else "📌 KEY TAKEAWAY"}</div>
    <div class="takeaway-text">{takeaway_s}</div>
  </div>

  <!-- Footer -->
  <div class="footer">
{footer_line1}<br>
{footer_line2}
  </div>

</div>
</body>
</html>'''

        fname = f"{SLUG}-ch{ch_num:03d}-info-{lang}.html"
        fpath = os.path.join(BOOKDIR, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)

        size_kb = os.path.getsize(fpath) / 1024
        print(f"✅ Written: {fname} ({size_kb:.1f} KB)")

print(f"\n✅ All 8 files generated in {BOOKDIR}")