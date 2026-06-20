#!/usr/bin/env python3
"""Generate infographics for 第一性原理 chapters 5-8 (ZH + EN)"""

import os, json

BOOKDIR = os.path.expanduser("~/.openclaw/workspace/infographics/books")
SLUG = "diyixing-yuanli"
BOOK_NAME = "第一性原理"
AUTHOR = "李善友"
FONT = "FZXPYZS"

CSS_TEMPLATE = '''  @font-face {{
    font-family: '{font}';
    src: url('../方正屏显雅宋简体.TTF') format('truetype');
    font-weight: normal; font-style: normal;
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    background: #f5f1eb;
    font-family: '{font}', 'PingFang SC', 'Noto Serif SC', 'STSong', Georgia, serif;
    display: flex; justify-content: center; align-items: flex-start;
    min-height: 100vh; padding: 40px 20px 60px;
  }}
  .container {{ max-width: 880px; width: 100%; padding: 40px 32px 60px; }}
  h1 {{
    font-family: '{font}', 'PingFang SC', 'Noto Serif SC', serif;
    font-size: 36px; color: #1a1a1a; text-align: center;
    line-height: 1.4; margin-bottom: 8px; font-weight: normal;
    letter-spacing: 1.5px;
  }}
  .subtitle {{
    text-align: center; font-family: '{font}', 'PingFang SC', 'Noto Serif SC', serif;
    font-size: 14px; color: #888; margin-bottom: 24px; line-height: 1.7;
    max-width: 640px; margin-left: auto; margin-right: auto;
  }}
  .divider {{
    width: 60px; height: 3px;
    background: linear-gradient(90deg, #dc2626, #ea580c);
    margin: 0 auto 28px; border-radius: 2px;
  }}
  .chapter-overview {{
    background: #f8f6f3; border-left: 3px solid #4f46e5; border-radius: 8px;
    padding: 16px 20px; margin: 12px 0 24px; font-size: 14px; color: #555;
    line-height: 1.8; font-family: '{font}', 'PingFang SC', serif;
  }}
  .chapter-overview p {{ margin: 0; }}
  .section {{
    background: #ffffff; border-radius: 14px;
    margin-bottom: 18px; padding: 24px 28px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    display: flex; gap: 20px; align-items: flex-start;
    border-left: 4px solid transparent;
  }}
  .section-01 {{ border-left-color: #dc2626; }}
  .section-02 {{ border-left-color: #ea580c; }}
  .section-03 {{ border-left-color: #ca8a04; }}
  .section-04 {{ border-left-color: #4f46e5; }}
  .section-05 {{ border-left-color: #db2777; }}
  .section-num {{
    flex-shrink: 0; width: 42px; height: 42px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 17px; font-weight: bold; margin-top: 2px;
    font-family: '{font}', 'PingFang SC', 'Noto Serif SC', serif;
  }}
  .num-01 {{ background: #fef2f2; color: #dc2626; }}
  .num-02 {{ background: #fff7ed; color: #ea580c; }}
  .num-03 {{ background: #fefce8; color: #ca8a04; }}
  .num-04 {{ background: #eef2ff; color: #4f46e5; }}
  .num-05 {{ background: #fdf2f8; color: #db2777; }}
  .section-body {{ flex: 1; }}
  .tag {{
    display: inline-block; font-size: 11px; font-weight: bold;
    padding: 2px 10px; border-radius: 10px; margin-bottom: 8px;
    letter-spacing: 1px;
    font-family: '{font}', 'PingFang SC', 'Noto Serif SC', serif;
  }}
  .tag-01 {{ background: #fef2f2; color: #dc2626; }}
  .tag-02 {{ background: #fff7ed; color: #ea580c; }}
  .tag-03 {{ background: #fefce8; color: #ca8a04; }}
  .tag-04 {{ background: #eef2ff; color: #4f46e5; }}
  .tag-05 {{ background: #fdf2f8; color: #db2777; }}
  .section-title {{
    font-size: 18px; margin-bottom: 10px; font-weight: bold; line-height: 1.4;
    font-family: '{font}', 'PingFang SC', 'Noto Serif SC', serif;
  }}
  .t-01 {{ color: #dc2626; }} .t-02 {{ color: #ea580c; }}
  .t-03 {{ color: #ca8a04; }} .t-04 {{ color: #4f46e5; }}
  .t-05 {{ color: #db2777; }}
  .section-desc {{
    font-size: 14px; color: #555; line-height: 1.9; margin-bottom: 14px;
  }}
  .kpi-row {{ display: grid; gap: 14px; margin: 0 0 18px; }}
  .kpi-row.cols-4 {{ grid-template-columns: repeat(4, 1fr); }}
  .kpi-row.cols-5 {{ grid-template-columns: repeat(5, 1fr); }}
  .kpi-card {{ border-radius: 12px; padding: 16px 14px; text-align: center; border: 1px solid; }}
  .kpi-card.c01 {{ background: #fef2f2; border-color: #fecaca; }}
  .kpi-card.c02 {{ background: #fff7ed; border-color: #fed7aa; }}
  .kpi-card.c03 {{ background: #fefce8; border-color: #fde68a; }}
  .kpi-card.c04 {{ background: #eef2ff; border-color: #c7d2fe; }}
  .kpi-card.c05 {{ background: #fdf2f8; border-color: #fbcfe8; }}
  .kpi-value {{ font-size: 34px; font-weight: bold; font-family: '{font}', 'PingFang SC', 'Noto Serif SC', serif; color: #1a1a1a; line-height: 1.2; }}
  .kpi-unit {{ font-size: 13px; color: #888; font-weight: normal; }}
  .kpi-label {{ font-size: 12px; color: #666; margin-top: 6px; line-height: 1.4; font-family: '{font}', 'PingFang SC', serif; }}
  .kpi-note {{ font-size: 11px; color: #aaa; margin-top: 3px; line-height: 1.4; }}
  .flow-row {{ display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin-top: 6px; }}
  .flow-step {{ background: #fff7ed; border: 1px solid #fed7aa; border-radius: 10px; padding: 10px 12px; text-align: center; min-width: 80px; flex: 1; font-size: 13px; color: #9a3412; line-height: 1.5; font-weight: bold; }}
  .flow-arrow {{ font-size: 20px; color: #ea580c; flex-shrink: 0; font-weight: bold; }}
  .flow-step.end {{ background: #fef2f2; border-color: #fecaca; color: #991b1b; }}
  .dual-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 10px; }}
  .dual-card {{ border-radius: 12px; padding: 18px 20px; display: flex; gap: 12px; align-items: flex-start; }}
  .dual-card.yes {{ background: #fef2f2; border: 1px solid #fecaca; }}
  .dual-card.no  {{ background: #f0fdf4; border: 1px solid #bbf7d0; }}
  .dual-icon {{ font-size: 24px; flex-shrink: 0; line-height: 1; }}
  .dual-text h4 {{ font-size: 14px; color: #1a1a1a; margin-bottom: 4px; font-family: '{font}', 'PingFang SC', 'Noto Serif SC', serif; }}
  .dual-text p {{ font-size: 12px; color: #777; line-height: 1.6; }}
  .data-row {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin-top: 10px; }}
  .data-card {{ border-radius: 12px; padding: 18px 16px; text-align: center; border: 1px solid #fce7f3; }}
  .data-card.d1 {{ background: #fdf2f8; border-color: #f9a8d4; }}
  .data-card.d2 {{ background: #fdf2f8; border-color: #f9a8d4; }}
  .data-card.d3 {{ background: #fdf2f8; border-color: #f9a8d4; }}
  .data-big {{ font-size: 26px; margin-bottom: 6px; }}
  .data-name {{ font-size: 15px; font-weight: bold; color: #831843; margin-bottom: 6px; font-family: '{font}', 'PingFang SC', 'Noto Serif SC', serif; }}
  .data-sm {{ font-size: 12px; color: #9d174d; line-height: 1.6; }}
  .takeaway {{
    background: #ffffff; border: 1px solid #e8e0d5; border-radius: 14px;
    padding: 24px 32px; margin-bottom: 18px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    border-left: 4px solid #dc2626;
  }}
  .takeaway-label {{ font-family: '{font}', 'PingFang SC', 'Noto Serif SC', serif; font-size: 12px; color: #dc2626; letter-spacing: 2px; margin-bottom: 6px; font-weight: bold; }}
  .takeaway-text {{ font-size: 16px; color: #1a1a1a; line-height: 1.9; font-family: '{font}', 'PingFang SC', 'Noto Serif SC', serif; }}
  .footer {{ text-align: center; margin-top: 32px; padding-top: 20px; border-top: 1px solid #e8e0d5; color: #bbb; font-size: 13px; line-height: 1.8; }}
  .lang-switch {{ text-align: right; margin-bottom: 16px; }}
  .lang-btn {{ display: inline-block; padding: 6px 16px; border-radius: 8px; font-size: 13px; text-decoration: none; letter-spacing: 0.03em; font-family: '{font}', 'PingFang SC', 'Noto Serif SC', serif; background: #fef2f2; color: #dc2626; border: 1px solid #fecaca; transition: opacity 0.15s; }}
  .lang-btn:hover {{ opacity: 0.75; }}
  .back-catalog {{ text-align: right; margin-bottom: 4px; }}
  .back-catalog-btn {{ display: inline-block; padding: 5px 14px; border-radius: 8px; font-size: 12px; text-decoration: none; letter-spacing: .02em; background: #eef2ff; color: #4f46e5; border: 1px solid #c7d2fe; transition: opacity .15s; }}
  .back-catalog-btn:hover {{ opacity: .75; }}
  @media (max-width: 640px) {{
    .section {{ flex-direction: column; align-items: center; text-align: center; border-left: none; border-top: 4px solid transparent; padding-top: 20px; }}
    .section-01 {{ border-top-color: #dc2626; }} .section-02 {{ border-top-color: #ea580c; }}
    .section-03 {{ border-top-color: #ca8a04; }} .section-04 {{ border-top-color: #4f46e5; }}
    .section-05 {{ border-top-color: #db2777; }}
    .dual-grid, .data-row {{ grid-template-columns: 1fr; }}
    .flow-row {{ flex-direction: column; }}
    .flow-arrow {{ transform: rotate(90deg); }}
    .container {{ padding: 0 8px; }}
    h1 {{ font-size: 26px; }}
    .kpi-row.cols-4, .kpi-row.cols-5 {{ grid-template-columns: repeat(2, 1fr); }}
    .kpi-value {{ font-size: 34px; }}
  }}
  @media (max-width: 400px) {{
    .kpi-row.cols-4, .kpi-row.cols-5 {{ grid-template-columns: 1fr; }}
  }}'''.format(font=FONT)


def catalog_link(lang):
    en_text = "← Catalog" if lang == "en" else "← 返回章节目录"
    return '''<div class="back-catalog"><a class="back-catalog-btn" href="{slug}-catalog.html">{text}</a></div>'''.format(slug=SLUG, text=en_text)

def lang_switch(lang):
    if lang == "zh":
        return '''<div class="lang-switch"><a class="lang-btn" target="_blank" href="{slug}-ch{chnum}-info-en.html">中文 / EN</a></div>'''
    return '''<div class="lang-switch"><a class="lang-btn" target="_blank" href="{slug}-ch{chnum}-info-zh.html">EN / 中文</a></div>'''

def make_html(lang, ch, data):
    chnum = f"{ch:03d}"
    cn_nums = {5: "五", 6: "六", 7: "七", 8: "八"}
    cn = cn_nums[ch]

    h1_text = data["h1"]
    subtitle = data["subtitle"]
    overview = data["overview"]
    kpi_html = data["kpi"]
    sections_html = data["sections"]
    takeaway = data["takeaway"]
    footer_text = data["footer"]

    html = '''<!DOCTYPE html>
<html lang="{lang_attr}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
{css}
</style>
</head>
<body>
<div class="container">
{catalog}
{switch}
<h1>{h1}</h1>
<p class="subtitle">{subtitle}</p>
<div class="divider"></div>
<div class="chapter-overview"><p>{overview}</p></div>
{kpi}
{sections}
<div class="takeaway">
  <div class="takeaway-label">{takeaway_label}</div>
  <div class="takeaway-text">{takeaway_text}</div>
</div>
<div class="footer">{footer}</div>
</div>
</body>
</html>'''.format(
        lang_attr="zh-CN" if lang == "zh" else "en",
        title=data["title"],
        css=CSS_TEMPLATE,
        catalog=catalog_link(lang),
        switch=lang_switch(lang).format(slug=SLUG, chnum=chnum),
        h1=h1_text,
        subtitle=subtitle,
        overview=overview,
        kpi=kpi_html,
        sections=sections_html,
        takeaway_label="🔑 Core Takeaway" if lang == "en" else "🔑 核心结论",
        takeaway_text=takeaway,
        footer=footer_text
    )
    return html

# ============================================================
# CHAPTER DATA
# ============================================================

chapters_zh = {}
chapters_en = {}

# --- CH5 ---
chapters_zh[5] = {
    "h1": '第一性原理 · 第5章「第一创新：基于第一性原理进行创新」',
    "title": '第一性原理 · 第5章「第一创新」',
    "subtitle": '''<span style="display:block;margin-bottom:6px;font-weight:bold;color:#dc2626;font-size:12px;letter-spacing:1px;">从归纳创新到演绎创新 · 从抽象原理到具象商业系统</span>
    如果说破界创新的关键词是"破"，那么第一创新的关键字则是"立"。
    它是公理化思维在商业创新中的应用——从重要学科的重要理论出发，
    用演绎法推导出可用的商业模型，构建全新的商业系统。''',
    "overview": '本章将公理化思维引入商业创新领域，提出"第一创新"方法论。与破界创新的"破除"不同，第一创新重在"建立"——从物理学还原论、生物学进化论、哲学本体论等基础学科的第一性原理出发，通过演绎法推导出组合创新、分形创新等商业模型。查理·芒格的多元思维模型和埃隆·马斯克"从头算"的创业实践，都证明了第一创新的力量。而这一切的终极驱动力，源自使命——马斯克的"英雄之旅"告诉我们，最大的创新来自最大的追问。',
    "kpi": '''<div class="kpi-row cols-5">
  <div class="kpi-card c01">
    <div class="kpi-value">破<span class="kpi-unit">vs</span>立</div>
    <div class="kpi-label">两种创新模式</div>
    <div class="kpi-note">破界创新·第一创新</div>
  </div>
  <div class="kpi-card c02">
    <div class="kpi-value">3<span class="kpi-unit">步</span></div>
    <div class="kpi-label">破界创新三部曲</div>
    <div class="kpi-note">识别假设·建立基石·构建系统</div>
  </div>
  <div class="kpi-card c03">
    <div class="kpi-value">5<span class="kpi-unit">+</span></div>
    <div class="kpi-label">多元思维模型</div>
    <div class="kpi-note">物理·生物·哲学·经济·心理</div>
  </div>
  <div class="kpi-card c04">
    <div class="kpi-value">3<span class="kpi-unit">大</span></div>
    <div class="kpi-label">第一创新来源</div>
    <div class="kpi-note">还原论·进化论·本体论</div>
  </div>
  <div class="kpi-card c05">
    <div class="kpi-value">3<span class="kpi-unit">阶段</span></div>
    <div class="kpi-label">英雄之旅</div>
    <div class="kpi-note">启程·启蒙·回归</div>
  </div>
</div>''',
    "sections": '''<!-- 01: 从归纳到演绎 -->
<div class="section section-01">
  <div class="section-num num-01">01</div>
  <div class="section-body">
    <div class="tag tag-01">范式转换</div>
    <div class="section-title t-01">从归纳创新到演绎创新：爱因斯坦的方法论革命</div>
    <div class="section-desc"><strong>在爱因斯坦之前，大多数科学研究建立在归纳法基础上——通过观察和反复实验归纳出规律。</strong>但爱因斯坦利用公理化思维，从第一性原理出发，通过演绎法推导出自然定律。商业领域同样在发生这种转变：与其从经验中归纳创新模型，不如直接定位到对企业发展有根基性促进作用的第一性原理，然后演绎出新的创新模型。这就是"第一创新"的核心逻辑。</div>
    <div class="flow-row">
      <div class="flow-step">归纳创新<br>实践→经验→模型</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">演绎创新<br>第一性原理→推导→模型</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step end">第一创新<br>跨领域通用</div>
    </div>
  </div>
</div>

<!-- 02: 第一创新方法论 -->
<div class="section section-02">
  <div class="section-num num-02">02</div>
  <div class="section-body">
    <div class="tag tag-02">核心方法</div>
    <div class="section-title t-02">基于第一性原理的第一创新：从重要学科的重要理论出发</div>
    <div class="section-desc"><strong>系统有层级之分，商业系统的第一性原理不在商业系统内部，而在更大的自然科学和社会科学中。</strong>基于物理学的还原论，推导出"组合创新"模型；基于生物学的进化论，推导出"分形创新"模型；基于哲学的本体论，推导出"破界创新"模型。这些模型不是从案例归纳而来，而是从基础学科演绎而来——案例只用于验证模型。</div>
    <div class="flow-row">
      <div class="flow-step">物理学还原论<br>→组合创新</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">生物学进化论<br>→分形创新</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step end">哲学本体论<br>→破界创新</div>
    </div>
  </div>
</div>

<!-- 03: 芒格的多元思维模型 -->
<div class="section section-03">
  <div class="section-num num-03">03</div>
  <div class="section-body">
    <div class="tag tag-03">芒格的智慧</div>
    <div class="section-title t-03">"锤子综合征"的解药：查理·芒格的多元思维模型</div>
    <div class="section-desc"><strong>如果你的手中只有一把锤子，你满世界看到的都是钉子。</strong>芒格建议投资者建立多元思维模型：广泛学习数学、物理学、生物学、哲学、心理学、经济学等不同学科的思维模型。不是深入学习每个学科的全部内容，而是学习每个学科中真正的大道理——只占全部内容的5%，却代表95%的重要性。每个学科都是一种独特的思维视角，就像功能各异的眼镜。</div>
    <div class="dual-grid">
      <div class="dual-card no">
        <div class="dual-icon">🔨</div>
        <div class="dual-text">
          <h4>锤子综合征</h4>
          <p>用一种思维模型看待所有问题，认知被扭曲。大多数人的教育从普通知识到专业知识，思维模式逐渐固化。</p>
        </div>
      </div>
      <div class="dual-card yes">
        <div class="dual-icon">🧰</div>
        <div class="dual-text">
          <h4>多元思维工具箱</h4>
          <p>三五个跨学科的思维模型就会让人与众不同。关键不是学得多深，而是有多元视角。</p>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- 04: 马斯克的第一创新 -->
<div class="section section-04">
  <div class="section-num num-04">04</div>
  <div class="section-body">
    <div class="tag tag-04">第一创新实践</div>
    <div class="section-title t-04">从原子出发：埃隆·马斯克的"从头算"</div>
    <div class="section-desc"><strong>马斯克将物理学还原论作为第一性原理：一切物质都可以还原到原子层面。</strong>他将"从头算"应用于在线支付（PayPal）、能源（特斯拉）、航天（SpaceX）、交通运输（Hyperloop）、脑机接口（Neuralink）等看似不相关的领域。当别人问他为什么做多元化时，他的回答是：当你把一件事深挖到最基础的根源，所有具象的东西对你而言都是同一件事情。厄本说："我原以为他是天才，后来才发现他是正常的，而我们被思维方式遮蔽了。"</div>
    <div class="flow-row">
      <div class="flow-step">还原论<br>一切归为原子</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">PayPal<br>在线支付</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">SpaceX<br>航天</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step end">Neuralink<br>脑机接口</div>
    </div>
  </div>
</div>

<!-- 05: 源自使命的动机 -->
<div class="section section-05">
  <div class="section-num num-05">05</div>
  <div class="section-body">
    <div class="tag tag-05">终极动力</div>
    <div class="section-title t-05">源自使命的动机：马斯克的英雄之旅</div>
    <div class="section-desc"><strong>"让人类成为跨行星物种，是我积累财富的唯一目的。</strong>赚钱对我来说没有太大意义。"马斯克在大学时列了一份对整个人类有贡献的清单：互联网、可再生能源、太空探索。他后来的所有创业都在这份清单指导下完成。2002年他卖掉PayPal获利1.65亿美元，31岁已财富惊人，却选择投入全部资金去实现使命。四次火箭发射三次失败，资金只够最后一次——2008年9月28日第四枚火箭成功升空。坎贝尔的英雄之旅：启程→启蒙→回归，SpaceX海上回收平台命名"我当然还爱着你"。</div>
    <div class="data-row">
      <div class="data-card d1">
        <div class="data-big">🌍</div>
        <div class="data-name">启程</div>
        <div class="data-sm">大学时列出使命清单：互联网、能源、太空探索。卖掉Zip2和PayPal，投入所有财富。</div>
      </div>
      <div class="data-card d2">
        <div class="data-big">💥</div>
        <div class="data-name">启蒙</div>
        <div class="data-sm">三次火箭发射失败，资金只够最后一次。2008年经济危机，SpaceX和特斯拉双双濒临破产。</div>
      </div>
      <div class="data-card d3">
        <div class="data-big">🚀</div>
        <div class="data-name">回归</div>
        <div class="data-sm">第四次火箭成功升空。回收平台命名"我当然还爱着你"。计划2070年火星百万人口城市。</div>
      </div>
    </div>
  </div>
</div>''',
    "takeaway": '第一创新的本质，是从第一性原理出发用演绎法推导新系统。它不是从经验中归纳，而是从根基中"生长"。芒格的多元思维模型告诉我们，三五个跨学科的大道理就足以让人与众不同；马斯克的英雄之旅证明，最大的创新来自最大的追问。敲碎每一个玻璃罩子，敢于碰触本质问题，在无限的思维张力中呈现生命的无限精彩。',
    "footer": '《第一性原理》第5章信息图 · 基于「第一创新」内容提炼 · 李善友 著 · 仅供学习参考'
}

chapters_en[5] = {
    "h1": 'First Principles · Ch5 "First Innovation: Innovation Based on First Principles"',
    "title": 'First Principles · Ch5「First Innovation」',
    "subtitle": '''<span style="display:block;margin-bottom:6px;font-weight:bold;color:#dc2626;font-size:12px;letter-spacing:1px;">From Inductive to Deductive Innovation · From Abstract Principles to Concrete Systems</span>
    If boundary-breaking innovation is about "breaking," then first innovation is about "building."
    It applies axiomatic thinking to business innovation — starting from foundational theories
    of key disciplines and using deduction to derive usable business models. ''',
    "overview": 'This chapter introduces axiomatic thinking into business innovation, proposing the "First Innovation" methodology. Unlike boundary-breaking innovation\'s focus on "dismantling," first innovation emphasizes "building" — deriving business models like combinatorial innovation and fractal innovation from first principles in physics (reductionism), biology (evolution), and philosophy (ontology). Charlie Munger\'s multi-disciplinary mental models and Elon Musk\'s "first principles" entrepreneurial practice demonstrate the power of first innovation. The ultimate driver is mission — Musk\'s "Hero\'s Journey" shows that the greatest innovation comes from the deepest questioning.',
    "kpi": '''<div class="kpi-row cols-5">
  <div class="kpi-card c01">
    <div class="kpi-value">Break<span class="kpi-unit">vs</span>Build</div>
    <div class="kpi-label">Two Innovation Modes</div>
    <div class="kpi-note">Boundary-breaking · First Innovation</div>
  </div>
  <div class="kpi-card c02">
    <div class="kpi-value">3<span class="kpi-unit"> Steps</span></div>
    <div class="kpi-label">Boundary-Breaking Triad</div>
    <div class="kpi-note">Identify assumption · New axiom · Build system</div>
  </div>
  <div class="kpi-card c03">
    <div class="kpi-value">5<span class="kpi-unit">+</span></div>
    <div class="kpi-label">Multi-Disciplinary Models</div>
    <div class="kpi-note">Physics · Biology · Philosophy · Economics</div>
  </div>
  <div class="kpi-card c04">
    <div class="kpi-value">3<span class="kpi-unit"> Sources</span></div>
    <div class="kpi-label">First Innovation Sources</div>
    <div class="kpi-note">Reductionism · Evolution · Ontology</div>
  </div>
  <div class="kpi-card c05">
    <div class="kpi-value">3<span class="kpi-unit"> Phases</span></div>
    <div class="kpi-label">Hero\'s Journey</div>
    <div class="kpi-note">Departure · Initiation · Return</div>
  </div>
</div>''',
    "sections": '''<!-- 01 -->
<div class="section section-01">
  <div class="section-num num-01">01</div>
  <div class="section-body">
    <div class="tag tag-01">Paradigm Shift</div>
    <div class="section-title t-01">From Inductive to Deductive Innovation: Einstein\'s Method Revolution</div>
    <div class="section-desc"><strong>Before Einstein, most scientific research relied on induction — observing, experimenting, and generalizing.</strong> Einstein used axiomatic thinking: starting from first principles and deriving natural laws through deduction. Business is undergoing the same shift: rather than inducing innovation models from experience, locate the foundational first principle that drives business growth and deduce new innovation models from it. This is the core logic of First Innovation.</div>
    <div class="flow-row">
      <div class="flow-step">Inductive Innovation<br>Practice → Experience → Model</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">Deductive Innovation<br>First Principle → Derive → Model</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step end">First Innovation<br>Cross-domain Universal</div>
    </div>
  </div>
</div>

<!-- 02 -->
<div class="section section-02">
  <div class="section-num num-02">02</div>
  <div class="section-body">
    <div class="tag tag-02">Core Method</div>
    <div class="section-title t-02">First Innovation: Deriving Business Models from Foundational Disciplines</div>
    <div class="section-desc"><strong>Systems are hierarchical — a business system\'s first principle lies outside business itself, within larger natural and social sciences.</strong> From physics\' reductionism comes "combinatorial innovation"; from biology\'s evolution comes "fractal innovation"; from philosophy\'s ontology comes "boundary-breaking innovation." These models are deduced, not induced from cases — cases only validate them.</div>
    <div class="flow-row">
      <div class="flow-step">Physics Reductionism<br>→ Combinatorial Innovation</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">Biology Evolution<br>→ Fractal Innovation</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step end">Philosophy Ontology<br>→ Boundary-Breaking</div>
    </div>
  </div>
</div>

<!-- 03 -->
<div class="section section-03">
  <div class="section-num num-03">03</div>
  <div class="section-body">
    <div class="tag tag-03">Munger\'s Wisdom</div>
    <div class="section-title t-03">The Hammer Syndrome Cure: Charlie Munger\'s Multi-Disciplinary Mental Models</div>
    <div class="section-desc"><strong>"To the man with only a hammer, every problem looks like a nail."</strong> Munger advises building a latticework of mental models from mathematics, physics, biology, philosophy, psychology, and economics. You don\'t need deep expertise — just the big ideas from each discipline, which represent 5% of content but 95% of importance. Each discipline is a unique lens, like different pairs of glasses for viewing the world.</div>
    <div class="dual-grid">
      <div class="dual-card no">
        <div class="dual-icon">🔨</div>
        <div class="dual-text">
          <h4>Hammer Syndrome</h4>
          <p>Using one mental model for all problems distorts cognition. Most education narrows from general to specialized knowledge.</p>
        </div>
      </div>
      <div class="dual-card yes">
        <div class="dual-icon">🧰</div>
        <div class="dual-text">
          <h4>Multi-Model Toolkit</h4>
          <p>Just 3-5 cross-disciplinary models make you exceptional. Depth matters less than breadth of perspective.</p>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- 04 -->
<div class="section section-04">
  <div class="section-num num-04">04</div>
  <div class="section-body">
    <div class="tag tag-04">First Innovation Practice</div>
    <div class="section-title t-04">Starting from Atoms: Elon Musk\'s "First Principles" Thinking</div>
    <div class="section-desc"><strong>Musk uses physics reductionism as his first principle: everything reduces to atoms.</strong> He applies this "reasoning from the ground up" to online payments (PayPal), energy (Tesla), aerospace (SpaceX), transportation (Hyperloop), and brain-computer interfaces (Neuralink) — seemingly unrelated fields. When asked about diversification, Musk says: when you dig deep enough to the root, all concrete things become the same thing. Urban: "I thought he was a genius, then realized he is normal, and we are blinded by our own thinking patterns."</div>
    <div class="flow-row">
      <div class="flow-step">Reductionism<br>Everything → Atoms</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">PayPal<br>Online Payments</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">SpaceX<br>Aerospace</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step end">Neuralink<br>Brain-Computer</div>
    </div>
  </div>
</div>

<!-- 05 -->
<div class="section section-05">
  <div class="section-num num-05">05</div>
  <div class="section-body">
    <div class="tag tag-05">Ultimate Driver</div>
    <div class="section-title t-05">Mission-Driven Motivation: Musk\'s Hero\'s Journey</div>
    <div class="section-desc"><strong>"Making humanity a multi-planetary species is the sole purpose of my wealth accumulation."</strong> As a college student, Musk listed what benefits humanity: internet, renewable energy, space exploration. All his ventures followed this list. In 2002, he sold PayPal for $165M — wealthy at 31 — yet poured everything into his mission. Three rocket launches failed; funds only covered a fourth. On September 28, 2008, the fourth rocket succeeded. Campbell\'s Hero\'s Journey: Departure → Initiation → Return. SpaceX\'s drone ship named "Of Course I Still Love You."</div>
    <div class="data-row">
      <div class="data-card d1">
        <div class="data-big">🌍</div>
        <div class="data-name">Departure</div>
        <div class="data-sm">College mission list: internet, energy, space. Sold Zip2 and PayPal, committed all wealth to the mission.</div>
      </div>
      <div class="data-card d2">
        <div class="data-big">💥</div>
        <div class="data-name">Initiation</div>
        <div class="data-sm">Three failed launches, funds for only one more. 2008 financial crisis hit Tesla and SpaceX simultaneously.</div>
      </div>
      <div class="data-card d3">
        <div class="data-big">🚀</div>
        <div class="data-name">Return</div>
        <div class="data-sm">Fourth rocket succeeded. Drone ship named "Of Course I Still Love You." Plans 1M-person Mars city by 2070.</div>
      </div>
    </div>
  </div>
</div>''',
    "takeaway": 'The essence of First Innovation is deriving new systems from first principles through deduction. It does not induce from experience but "grows" from foundations. Munger\'s multi-disciplinary models show that 3-5 cross-disciplinary big ideas make you exceptional. Musk\'s Hero\'s Journey proves that the greatest innovation comes from the deepest questioning. Break every glass ceiling, dare to touch fundamental questions, and manifest life\'s infinite brilliance through unbounded thinking.',
    "footer": '"First Principles" Ch5 Infographic · Based on "First Innovation" · By Li Shanyou · For learning reference'
}

# --- CH6 ---
chapters_zh[6] = {
    "h1": '第一性原理 · 第6章「万物至理：宇宙的终极密码」',
    "title": '第一性原理 · 第6章「万物至理」',
    "subtitle": '''<span style="display:block;margin-bottom:6px;font-weight:bold;color:#dc2626;font-size:12px;letter-spacing:1px;">洞见公理比推导更困难 · 理论定义现实而非现实定义理论</span>
    若将整个宇宙当作一个系统，它也有第一性原理——万物至理。
    爱因斯坦打破牛顿力学的隐含假设，建立全新基石假设，
    推导出狭义与广义相对论。这是第一性原理在科学领域的最高范式。''',
    "overview": '本章阐释第一性原理在科学领域中的应用——万物至理（Theory of Everything）。爱因斯坦的整个学术生涯都在追寻物理学的终极统一理论。从质疑牛顿力学体系的两个隐含假设（绝对时间和绝对空间），到建立光速不变和相对性原理两个全新基石，再到推导出狭义相对论（统一时间与空间、质量与能量）和广义相对论（以时空弯曲替代万有引力）。爱因斯坦不仅改变了物理学，更改变了科学家的工作方式——在问题的原有维度上无法解决，只有升维才能看到答案。',
    "kpi": '''<div class="kpi-row cols-5">
  <div class="kpi-card c01">
    <div class="kpi-value">2<span class="kpi-unit">大</span></div>
    <div class="kpi-label">牛顿隐含假设</div>
    <div class="kpi-note">绝对时间·绝对空间</div>
  </div>
  <div class="kpi-card c02">
    <div class="kpi-value">2<span class="kpi-unit">个</span></div>
    <div class="kpi-label">爱因斯坦新基石</div>
    <div class="kpi-note">光速不变·相对性原理</div>
  </div>
  <div class="kpi-card c03">
    <div class="kpi-value">10<span class="kpi-unit">年</span></div>
    <div class="kpi-label">从狭义到广义</div>
    <div class="kpi-note">1905狭义→1915广义</div>
  </div>
  <div class="kpi-card c04">
    <div class="kpi-value">2<span class="kpi-unit">次</span></div>
    <div class="kpi-label">升维统一</div>
    <div class="kpi-note">时空统一·质能统一</div>
  </div>
  <div class="kpi-card c05">
    <div class="kpi-value">4D<span class="kpi-unit"></span></div>
    <div class="kpi-label">四维时空</div>
    <div class="kpi-note">三维空间+时间=时空</div>
  </div>
</div>''',
    "sections": '''<!-- 01: 洞见公理 -->
<div class="section section-01">
  <div class="section-num num-01">01</div>
  <div class="section-body">
    <div class="tag tag-01">公理发现</div>
    <div class="section-title t-01">洞见公理比推导更加困难：爱因斯坦的"定律中的定律"</div>
    <div class="section-desc"><strong>爱因斯坦认为理论家的工作分两步：发现公理，再从公理出发推导结论。</strong>第二步只要勤奋和聪明就能完成，而第一步发现公理的性质完全不同——它无法用逻辑推导出来，只能通过不断假设和试错来定位。爱因斯坦的方法论有二："定律中的定律"（如对称性、能量守恒、最小作用量原理）和"思想实验"（在大脑中纯逻辑推演）。好奇心与想象力，比知识重要得多。</div>
    <div class="flow-row">
      <div class="flow-step">定律中的定律<br>对称性·守恒律</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">思想实验<br>纯逻辑推演</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step end">发现公理<br>无法逻辑推导</div>
    </div>
  </div>
</div>

<!-- 02: 质疑牛顿 -->
<div class="section section-02">
  <div class="section-num num-02">02</div>
  <div class="section-body">
    <div class="tag tag-02">破界创新</div>
    <div class="section-title t-02">对牛顿力学体系的质疑：打破200年的物理学基石</div>
    <div class="section-desc"><strong>1687年至20世纪初，牛顿经典力学是物理学的根基。</strong>19世纪最后一天，开尔文勋爵宣称"物理学的大厦已经落成，剩下的只是装修装饰"。仅仅5年后，26岁的爱因斯坦发表了6篇论文，其中4篇被誉为"天神级"——任意一篇都有获得诺贝尔奖的潜力。1905年因此被称为"爱因斯坦奇迹年"。爱因斯坦识别出了牛顿体系中的隐含假设：绝对时间和绝对空间。</div>
    <div class="dual-grid">
      <div class="dual-card no">
        <div class="dual-icon">🏛️</div>
        <div class="dual-text">
          <h4>牛顿的隐含假设</h4>
          <p>绝对时间（独立于任何参考系的均匀流逝）和绝对空间（独立于物质的固定舞台）。统治物理学200年。</p>
        </div>
      </div>
      <div class="dual-card yes">
        <div class="dual-icon">💡</div>
        <div class="dual-text">
          <h4>爱因斯坦的质疑</h4>
          <p>如果时间与空间是绝对的，光速在不同参考系中就不应恒定——但实验和理论都表明光速始终不变。</p>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- 03: 狭义相对论 -->
<div class="section section-03">
  <div class="section-num num-03">03</div>
  <div class="section-body">
    <div class="tag tag-03">新基石</div>
    <div class="section-title t-03">两个全新基石假设，推导出狭义相对论</div>
    <div class="section-desc"><strong>爱因斯坦提出两个新基石：光速不变原理（无论在何种惯性系中，真空光速恒为常数）和相对性原理（一切物理定律在所有惯性系中等价）。</strong>从这两个基石出发，他推导出：时间与空间不再是绝对的——运动速度越快，时间越慢，空间越短。这完全颠覆了牛顿的时空观。爱因斯坦说："新理论不是新发现的革命，而是概念的革命。"</div>
    <div class="flow-row">
      <div class="flow-step">光速不变<br>真空光速恒为c</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">相对性原理<br>所有惯性系等价</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step end">狭义相对论<br>时间·空间相对</div>
    </div>
  </div>
</div>

<!-- 04: 爱因斯坦的升维 -->
<div class="section section-04">
  <div class="section-num num-04">04</div>
  <div class="section-body">
    <div class="tag tag-04">升维思考</div>
    <div class="section-title t-04">爱因斯坦的升维：三维空间→四维时空→E=mc²</div>
    <div class="section-desc"><strong>狭义相对论引发时空观危机：时间和空间都变成了相对概念。</strong>爱因斯坦进一步升维——将时间和空间合为一体（时空），发现"时空"在任何惯性系中保持不变。同样的升维逻辑应用于质量和能量：物体速度越快，质量越大，增加的质量只能来自能量。于是推导出E=mc²——质量与能量是同一实体（质能）的一体两面。加来道雄说："自然规律在高维空间更简单。"</div>
    <div class="flow-row">
      <div class="flow-step">时间+空间<br>→时空(4D)</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">质量+能量<br>→质能</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step end">E=mc²<br>科学史最著名方程</div>
    </div>
  </div>
</div>

<!-- 05: 广义相对论 -->
<div class="section section-05">
  <div class="section-num num-05">05</div>
  <div class="section-body">
    <div class="tag tag-05">终极突破</div>
    <div class="section-title t-05">广义相对论：万有引力不存在——它是时空弯曲的表现</div>
    <div class="section-desc"><strong>10年后，爱因斯坦做出最大胆的推论：万有引力根本不是"力"，而是时空弯曲的表现。</strong>大质量物体使周围时空场弯曲，其他物体在弯曲时空中出于最小作用量原理呈现弯曲运动轨迹。1919年日食观测证实了这一预测：光经过太阳附近时确实发生了爱因斯坦计算出的偏折。在牛顿体系中引力是天然存在的力，爱因斯坦打破了这一群体认知——"宇宙最不可思议的是它居然是可以被理解的。"</div>
    <div class="dual-grid">
      <div class="dual-card no">
        <div class="dual-icon">🍎</div>
        <div class="dual-text">
          <h4>牛顿范式</h4>
          <p>万有引力是远距离瞬时超光速的神秘作用。太阳消失，地球立即脱离轨道。</p>
        </div>
      </div>
      <div class="dual-card yes">
        <div class="dual-icon">🌀</div>
        <div class="dual-text">
          <h4>爱因斯坦范式</h4>
          <p>引力=时空弯曲。太阳消失8分钟后地球才会脱离——因为引力波以光速传播。</p>
        </div>
      </div>
    </div>
  </div>
</div>''',
    "takeaway": '爱因斯坦的整个学术生涯都在践行第一性原理：识别系统的隐含假设（绝对时空），打破它，建立新基石（光速不变+相对性原理），用演绎法推导出新系统（狭义与广义相对论）。在原有维度上只能呈现问题，只有升维才能解决问题。自然规律在高维空间更简单。理解宇宙的钥匙不是更多实验数据，而是更深的第一性原理。',
    "footer": '《第一性原理》第6章信息图 · 基于「万物至理」内容提炼 · 李善友 著 · 仅供学习参考'
}

chapters_en[6] = {
    "h1": 'First Principles · Ch6 "Theory of Everything: The Universe\'s Ultimate Code"',
    "title": 'First Principles · Ch6「Theory of Everything」',
    "subtitle": '''<span style="display:block;margin-bottom:6px;font-weight:bold;color:#dc2626;font-size:12px;letter-spacing:1px;">Finding axioms is harder than deriving from them · Theory defines reality</span>
    If the universe itself is a system, it too has a first principle — the Theory of Everything.
    Einstein broke Newton\'s hidden assumptions, established new foundational axioms,
    and deduced Special and General Relativity. This is first-principles thinking at its highest. ''',
    "overview": 'This chapter illustrates first principles in science: the Theory of Everything. Einstein\'s entire career pursued physics\' ultimate unified theory. He identified Newton\'s two hidden assumptions (absolute time and absolute space), established two new axioms (constancy of light speed and the principle of relativity), and deduced Special Relativity (unifying space-time and mass-energy) and General Relativity (replacing gravity with spacetime curvature). Einstein not only changed physics but transformed how scientists work — a problem cannot be solved in its original dimension; only by ascending dimensions can the answer be found.',
    "kpi": '''<div class="kpi-row cols-5">
  <div class="kpi-card c01">
    <div class="kpi-value">2<span class="kpi-unit"> Hidden</span></div>
    <div class="kpi-label">Newton\'s Assumptions</div>
    <div class="kpi-note">Absolute time · Absolute space</div>
  </div>
  <div class="kpi-card c02">
    <div class="kpi-value">2<span class="kpi-unit"> New</span></div>
    <div class="kpi-label">Einstein\'s Axioms</div>
    <div class="kpi-note">Light speed constant · Relativity</div>
  </div>
  <div class="kpi-card c03">
    <div class="kpi-value">10<span class="kpi-unit"> Years</span></div>
    <div class="kpi-label">Special → General</div>
    <div class="kpi-note">1905 Special → 1915 General</div>
  </div>
  <div class="kpi-card c04">
    <div class="kpi-value">2<span class="kpi-unit"> Unifications</span></div>
    <div class="kpi-label">Dimensional Unification</div>
    <div class="kpi-note">Space-time · Mass-energy</div>
  </div>
  <div class="kpi-card c05">
    <div class="kpi-value">4D<span class="kpi-unit"></span></div>
    <div class="kpi-label">Spacetime</div>
    <div class="kpi-note">3D space + time = spacetime</div>
  </div>
</div>''',
    "sections": '''<!-- 01 -->
<div class="section section-01">
  <div class="section-num num-01">01</div>
  <div class="section-body">
    <div class="tag tag-01">Axiom Discovery</div>
    <div class="section-title t-01">Finding Axioms Is Harder than Deriving From Them: Einstein\'s "Laws of Laws"</div>
    <div class="section-desc"><strong>Einstein divided theorists\' work into two steps: discover axioms, then derive conclusions from them.</strong> Step two requires only diligence and intelligence; step one — discovering axioms — is fundamentally different. It cannot be reached through logical derivation, only through continuous hypothesis and trial-and-error. Einstein had two methods: "laws of laws" (symmetry, conservation, least action) and "thought experiments" (pure logical deduction in the mind). Curiosity and imagination matter far more than knowledge.</div>
    <div class="flow-row">
      <div class="flow-step">Laws of Laws<br>Symmetry · Conservation</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">Thought Experiments<br>Pure logical deduction</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step end">Discover Axioms<br>Cannot be logically derived</div>
    </div>
  </div>
</div>

<!-- 02 -->
<div class="section section-02">
  <div class="section-num num-02">02</div>
  <div class="section-body">
    <div class="tag tag-02">Boundary Breaking</div>
    <div class="section-title t-02">Questioning Newton\'s Mechanical System: Breaking a 200-Year Foundation</div>
    <div class="section-desc"><strong>From 1687 to the early 20th century, Newton\'s classical mechanics was the bedrock of physics.</strong> On the last day of the 19th century, Lord Kelvin declared "the edifice of physics is complete, only decoration remains." Just five years later, 26-year-old Einstein published six papers — four of them "god-tier," any one worthy of a Nobel Prize. 1905 became "Einstein\'s Miracle Year." Einstein identified Newton\'s hidden assumptions: absolute time and absolute space.</div>
    <div class="dual-grid">
      <div class="dual-card no">
        <div class="dual-icon">🏛️</div>
        <div class="dual-text">
          <h4>Newton\'s Hidden Assumptions</h4>
          <p>Absolute time (uniform flow independent of reference frames) and absolute space (fixed stage independent of matter). Ruled for 200 years.</p>
        </div>
      </div>
      <div class="dual-card yes">
        <div class="dual-icon">💡</div>
        <div class="dual-text">
          <h4>Einstein\'s Question</h4>
          <p>If time and space are absolute, light speed shouldn\'t be constant across reference frames — yet experiments show it always is.</p>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- 03 -->
<div class="section section-03">
  <div class="section-num num-03">03</div>
  <div class="section-body">
    <div class="tag tag-03">New Axioms</div>
    <div class="section-title t-03">Two New Foundational Assumptions That Led to Special Relativity</div>
    <div class="section-desc"><strong>Einstein proposed two new axioms: light speed constancy (in any inertial frame, vacuum light speed is constant) and the principle of relativity (all physical laws are equivalent in all inertial frames).</strong> From these, he deduced: time and space are not absolute — the faster you move, the slower time flows and the shorter space becomes. This completely overturned Newton\'s spacetime view. Einstein said: "New theories are not revolutions of discovery but revolutions of concepts."</div>
    <div class="flow-row">
      <div class="flow-step">Light Speed Constancy<br>c is always constant</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">Relativity Principle<br>All inertial frames equal</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step end">Special Relativity<br>Time & Space relative</div>
    </div>
  </div>
</div>

<!-- 04 -->
<div class="section section-04">
  <div class="section-num num-04">04</div>
  <div class="section-body">
    <div class="tag tag-04">Dimensional Ascent</div>
    <div class="section-title t-04">Einstein\'s Dimensional Ascent: 3D Space → 4D Spacetime → E=mc²</div>
    <div class="section-desc"><strong>Special Relativity created a spacetime crisis: time and space became relative concepts.</strong> Einstein ascended dimensions — merged time and space into one entity (spacetime), discovering that "spacetime" remains invariant in all inertial frames. The same logic applied to mass and energy: faster objects gain mass; the added mass must come from energy. Thus E=mc² — mass and energy are two faces of one entity (mass-energy). Kaku: "The laws of nature are simpler in higher dimensions."</div>
    <div class="flow-row">
      <div class="flow-step">Time + Space<br>→ Spacetime (4D)</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">Mass + Energy<br>→ Mass-Energy</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step end">E=mc²<br>Science\'s most famous equation</div>
    </div>
  </div>
</div>

<!-- 05 -->
<div class="section section-05">
  <div class="section-num num-05">05</div>
  <div class="section-body">
    <div class="tag tag-05">Ultimate Breakthrough</div>
    <div class="section-title t-05">General Relativity: Gravity Doesn\'t Exist — It\'s the Curvature of Spacetime</div>
    <div class="section-desc"><strong>Ten years later, Einstein made his boldest deduction: universal gravitation isn\'t a "force" at all — it\'s the manifestation of spacetime curvature.</strong> Massive objects curve the surrounding spacetime field; other objects moving in this curved spacetime follow curved paths due to the principle of least action. The 1919 solar eclipse observation confirmed his prediction: light passing near the sun bent exactly as Einstein calculated. Newton saw gravity as a naturally existing force; Einstein broke this group consensus — "The most incomprehensible thing about the universe is that it is comprehensible."</div>
    <div class="dual-grid">
      <div class="dual-card no">
        <div class="dual-icon">🍎</div>
        <div class="dual-text">
          <h4>Newton\'s Paradigm</h4>
          <p>Gravity is a distant, instantaneous, superluminal mysterious force. Sun vanishes → Earth immediately breaks orbit.</p>
        </div>
      </div>
      <div class="dual-card yes">
        <div class="dual-icon">🌀</div>
        <div class="dual-text">
          <h4>Einstein\'s Paradigm</h4>
          <p>Gravity = spacetime curvature. Sun vanishes → Earth escapes 8 minutes later, because gravity waves travel at light speed.</p>
        </div>
      </div>
    </div>
  </div>
</div>''',
    "takeaway": 'Einstein\'s entire career embodied first-principles thinking: identify a system\'s hidden assumptions (absolute spacetime), break them, establish new axioms (constant light speed + relativity principle), and deduce a new system through deduction (Special and General Relativity). In the original dimension, you can only present problems; only by ascending dimensions can you solve them. The laws of nature are simpler in higher dimensions. The key to understanding the universe is not more experimental data but deeper first principles.',
    "footer": '"First Principles" Ch6 Infographic · Based on "Theory of Everything" · By Li Shanyou · For learning reference'
}

# --- CH7 ---
chapters_zh[7] = {
    "h1": '第一性原理 · 第7章「从众效应："真理"的真相」',
    "title": '第一性原理 · 第7章「从众效应」',
    "subtitle": '''<span style="display:block;margin-bottom:6px;font-weight:bold;color:#dc2626;font-size:12px;letter-spacing:1px;">所有人相信的真便是真理 · 破界创新最大的隐含假设</span>
    个体受到他人影响，会怀疑并改变自己的观点以求安心——这是从众效应。
    我们所做的绝大部分决策，隐含假设都是"因为周围人是这么想的"。
    只有认知到这个内置在基因中的桎梏，才有机会从中跳出。''',
    "overview": '本章揭示破界创新最大的隐含假设——从众效应。通过两种真理观（符合论与连贯论）的对比，论证了所谓的"客观真理"并不存在：人类感官只能感知现象界而非物自体。真理连贯论指出，大多数人所认同的"真理"不过是群体信念的产物。阿希实验证明75%的人至少一次屈从于群体错误判断，勒庞的《乌合之众》揭示了群体无智慧、无逻辑、无意识的本质。斯坦福监狱实验更展示了从众效应如何将普通人变成施暴者与顺从者。认识到这一内置在基因中的桎梏，是跳出从众效应的第一步。',
    "kpi": '''<div class="kpi-row cols-5">
  <div class="kpi-card c01">
    <div class="kpi-value">2<span class="kpi-unit">种</span></div>
    <div class="kpi-label">真理观</div>
    <div class="kpi-note">符合论·连贯论</div>
  </div>
  <div class="kpi-card c02">
    <div class="kpi-value">80<span class="kpi-unit">%</span></div>
    <div class="kpi-label">认知来自视觉</div>
    <div class="kpi-note">仅感知十万分之一光段</div>
  </div>
  <div class="kpi-card c03">
    <div class="kpi-value">75<span class="kpi-unit">%</span></div>
    <div class="kpi-label">至少一次从众</div>
    <div class="kpi-note">阿希线段实验</div>
  </div>
  <div class="kpi-card c04">
    <div class="kpi-value">33<span class="kpi-unit">%</span></div>
    <div class="kpi-label">完全从众率</div>
    <div class="kpi-note">明知错误仍然跟随</div>
  </div>
  <div class="kpi-card c05">
    <div class="kpi-value">3<span class="kpi-unit">无</span></div>
    <div class="kpi-label">群体特性</div>
    <div class="kpi-note">无智慧·无逻辑·无意识</div>
  </div>
</div>''',
    "sections": '''<!-- 01: 两种真理观 -->
<div class="section section-01">
  <div class="section-num num-01">01</div>
  <div class="section-body">
    <div class="tag tag-01">真理的本质</div>
    <div class="section-title t-01">两种真理观：符合论——信念是否与客观事实一致</div>
    <div class="section-desc"><strong>真理符合论是绝大多数人的默认真理观：某个信念如果与客观事实一致就是真理。</strong>但悖论在于，人类根本没有独立于"主观信念"之外的"客观事实"。大脑如同一台照相机，只能拍摄"照片"而非物体本身——我们只能比较照片与照片，不能比较照片与物体。更残酷的是，感官系统本身就在"扭曲"外物：视觉仅感知十万分之一光段，且将波长扭曲为"颜色"。王阳明："心外无物，心外无理。"康德："我们只能认知现象界，无法认知物自体。"</div>
    <div class="flow-row">
      <div class="flow-step">客观事物</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">感官通道<br>(5条，简化扭曲)</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">主观信念<br>(大脑"照片")</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step end">≠客观事实</div>
    </div>
  </div>
</div>

<!-- 02: 真理连贯论 -->
<div class="section section-02">
  <div class="section-num num-02">02</div>
  <div class="section-body">
    <div class="tag tag-02">群体共识</div>
    <div class="section-title t-02">真理连贯论：信念是否与群体信念一致——"所有人相信的真便是真理"</div>
    <div class="section-desc"><strong>既然符合论不成立，人类判别真理的第二条路径——真理连贯论——便浮出水面。</strong>如果某个信念与群体信念一致，它就被认为是"真理"。大多数人会第一时间反驳：我不会因为他人而改变自己的观点。但事实恰好相反——我们所做的绝大部分决策，隐含假设都是"因为周围其他人是这么想的"。从众效应是内置在人类基因中的认知模式，在组织中常常表现为群体信念。</div>
    <div class="dual-grid">
      <div class="dual-card no">
        <div class="dual-icon">🎯</div>
        <div class="dual-text">
          <h4>真理符合论</h4>
          <p>信念与客观事实一致 = 真理。但人类永远无法直接触达客观事实，感官本质上是"简化+扭曲"的求存系统。</p>
        </div>
      </div>
      <div class="dual-card yes">
        <div class="dual-icon">👥</div>
        <div class="dual-text">
          <h4>真理连贯论</h4>
          <p>信念与群体信念一致 = 真理。从众效应决定了我们大多数人的"真理"标准。独立于群体认知之外是极度困难的。</p>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- 03: 阿希实验 -->
<div class="section section-03">
  <div class="section-num num-03">03</div>
  <div class="section-body">
    <div class="tag tag-03">实验证据</div>
    <div class="section-title t-03">阿希实验：明知答案是错的，75%的人仍然选择从众</div>
    <div class="section-desc"><strong>阿希的线段认知实验揭示了从众效应的惊人力量。</strong>7人一组，其中6人是实验助手被安排同时选择错误答案。结果：33%的参与者完全跟随了错误答案，74%的人至少有一次同意了错误意见。不涉及理论，不涉及价值观，只是简单的线段长度判断，明知道答案是错的，在群体压力下人们还是选择了错误的答案。芒格称从众效应为"商业人士最糟糕的误判心理之一"，摩尔说它是"扭曲认知的罪魁祸首"。</div>
    <div class="data-row">
      <div class="data-card d1">
        <div class="data-big">7<span class="kpi-unit">人/组</span></div>
        <div class="data-name">实验设计</div>
        <div class="data-sm">6名助手 + 1名被试。助手同时选择明显错误的线段长度。</div>
      </div>
      <div class="data-card d2">
        <div class="data-big">33<span class="kpi-unit">%</span></div>
        <div class="data-name">完全从众</div>
        <div class="data-sm">三分之一的被试在所有试次中都跟随了错误的群体判断。</div>
      </div>
      <div class="data-card d3">
        <div class="data-big">74<span class="kpi-unit">%</span></div>
        <div class="data-name">至少一次从众</div>
        <div class="data-sm">近四分之三的人至少有一次放弃了正确答案，选择了群体错误答案。</div>
      </div>
    </div>
  </div>
</div>

<!-- 04: 乌合之众 -->
<div class="section section-04">
  <div class="section-num num-04">04</div>
  <div class="section-body">
    <div class="tag tag-04">群体心理学</div>
    <div class="section-title t-04">逃不脱的乌合之众：勒庞的"三无"定律</div>
    <div class="section-desc"><strong>勒庞在《乌合之众》中提出群体三大特性。</strong>①群体无智慧：群体的叠加只是愚蠢的叠加，个体智商会被群体拉低。②群体无逻辑：逻辑法则对群体无效——"做出简洁有力的断言，不理睬任何推理和证据，是让观念进入群众头脑最可靠的方法"。③群体无意识：个体在群体中不再是原本的自己，变成了不再有独立思想的傀儡。斯坦福监狱实验中，普通志愿者迅速进入施暴狱警与顺从囚徒的角色，连主持实验的教授都深陷其中。</div>
    <div class="flow-row">
      <div class="flow-step">群体无智慧<br>愚蠢的叠加</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">群体无逻辑<br>只被形象打动</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step end">群体无意识<br>成为傀儡</div>
    </div>
  </div>
</div>

<!-- 05: 认知跳出 -->
<div class="section section-05">
  <div class="section-num num-05">05</div>
  <div class="section-body">
    <div class="tag tag-05">突破之路</div>
    <div class="section-title t-05">认知如何跳出：格雷厄姆的地狱石油商寓言</div>
    <div class="section-desc"><strong>一位石油大亨想进天堂，被告知石油商名额已满。</strong>他朝门内大喊"地狱里有石油"，于是所有石油商都跳入地狱。守门人请他进入天堂，他却拒绝了——"如果他们都去了地狱，说明地狱里可能真的有石油。"自己编织的谎言，当所有人都相信了之后，自己也跟着信以为真。这是人类的天性。罗素说："很多人宁可死，也不愿独立思考。"认识到从众效应是内置在基因中的桎梏，是我们跳出它的第一步。</div>
    <div class="dual-grid">
      <div class="dual-card no">
        <div class="dual-icon">🛢️</div>
        <div class="dual-text">
          <h4>地狱石油商</h4>
          <p>"地狱里有石油"——自己编的谎言，但看到所有人都跳下去后，自己也信了。从众效应的终极隐喻。</p>
        </div>
      </div>
      <div class="dual-card yes">
        <div class="dual-icon">🧠</div>
        <div class="dual-text">
          <h4>独立思考</h4>
          <p>群体中的独立思考，等于用自己的意识去对抗天性，用思想去对峙身体。但这正是突破的唯一路径。</p>
        </div>
      </div>
    </div>
  </div>
</div>''',
    "takeaway": '真理连贯论揭示了一个残酷事实：大多数人所相信的"真理"，不过是群体信念的产物。75%的人在群体压力下放弃了自己的正确判断。从众效应是内置在人类基因中的认知模式，它表现为群体的"三无"——无智慧、无逻辑、无意识。罗素说"很多人宁可死也不愿独立思考"。认识到这个内置桎梏，是我们跳出它的第一步。独立思考是用意识对抗天性，用思想对峙身体——但这正是突破的唯一路径。',
    "footer": '《第一性原理》第7章信息图 · 基于「从众效应」内容提炼 · 李善友 著 · 仅供学习参考'
}

chapters_en[7] = {
    "h1": 'First Principles · Ch7 "Bandwagon Effect: The Truth About Truth"',
    "title": 'First Principles · Ch7「Bandwagon Effect」',
    "subtitle": '''<span style="display:block;margin-bottom:6px;font-weight:bold;color:#dc2626;font-size:12px;letter-spacing:1px;">What everyone believes becomes truth · The greatest hidden assumption</span>
    Individuals influenced by others will doubt and change their views for comfort — this is the bandwagon effect.
    Most decisions we make are implicitly based on "because everyone around us thinks this way."
    Only by recognizing this genetically-embedded shackle can we break free. ''',
    "overview": 'This chapter reveals the greatest hidden assumption in boundary-breaking innovation: the bandwagon effect. Through comparing two theories of truth (correspondence and coherence), it demonstrates that "objective truth" does not exist — human senses only perceive phenomena, not noumena. Truth coherence theory shows that what most people call "truth" is merely the product of group belief. The Asch experiment proved 75% conform at least once; Le Bon\'s "The Crowd" reveals groups as unintelligent, illogical, and unconscious. The Stanford Prison Experiment showed how ordinary people become abusers and conformists. Recognizing this genetically-embedded shackle is step one to escaping it.',
    "kpi": '''<div class="kpi-row cols-5">
  <div class="kpi-card c01">
    <div class="kpi-value">2<span class="kpi-unit"> Theories</span></div>
    <div class="kpi-label">Truth Theories</div>
    <div class="kpi-note">Correspondence · Coherence</div>
  </div>
  <div class="kpi-card c02">
    <div class="kpi-value">80<span class="kpi-unit">%</span></div>
    <div class="kpi-label">Cognition from Vision</div>
    <div class="kpi-note">Only 1/100,000 of light spectrum</div>
  </div>
  <div class="kpi-card c03">
    <div class="kpi-value">75<span class="kpi-unit">%</span></div>
    <div class="kpi-label">Conformed Once</div>
    <div class="kpi-note">Asch line experiment</div>
  </div>
  <div class="kpi-card c04">
    <div class="kpi-value">33<span class="kpi-unit">%</span></div>
    <div class="kpi-label">Full Conformity</div>
    <div class="kpi-note">Followed despite knowing wrong</div>
  </div>
  <div class="kpi-card c05">
    <div class="kpi-value">3<span class="kpi-unit"> Nots</span></div>
    <div class="kpi-label">Crowd Traits</div>
    <div class="kpi-note">Not intelligent · Not logical · Not conscious</div>
  </div>
</div>''',
    "sections": '''<!-- 01 -->
<div class="section section-01">
  <div class="section-num num-01">01</div>
  <div class="section-body">
    <div class="tag tag-01">Nature of Truth</div>
    <div class="section-title t-01">Two Theories of Truth: Correspondence — Does Belief Match Objective Reality?</div>
    <div class="section-desc"><strong>Correspondence theory is most people\'s default: a belief matching objective reality is truth.</strong> But the paradox is: humans have no access to "objective reality" independent of "subjective belief." The brain is a camera producing "photos" of objects — we can only compare photos with photos, never photos with objects. Worse, our senses inherently distort: vision perceives only 1/100,000 of the light spectrum and twists wavelength into "color." Wang Yangming: "Outside the mind, there are no things." Kant: "We can only know phenomena, never noumena."</div>
    <div class="flow-row">
      <div class="flow-step">Objective Reality</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">Sensory Channels<br>(5, simplify & distort)</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">Subjective Belief<br>(Brain\'s "Photo")</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step end">≠ Objective Truth</div>
    </div>
  </div>
</div>

<!-- 02 -->
<div class="section section-02">
  <div class="section-num num-02">02</div>
  <div class="section-body">
    <div class="tag tag-02">Group Consensus</div>
    <div class="section-title t-02">Truth Coherence: What Everyone Believes Becomes Truth</div>
    <div class="section-desc"><strong>Since correspondence fails, the second path to truth — coherence theory — emerges.</strong> If a belief aligns with group belief, it is accepted as "truth." Most people reflexively deny being influenced by others — yet our decisions are implicitly based on "because everyone around us thinks this way." The bandwagon effect is genetically embedded in human cognition, manifesting in organizations as group belief.</div>
    <div class="dual-grid">
      <div class="dual-card no">
        <div class="dual-icon">🎯</div>
        <div class="dual-text">
          <h4>Correspondence Theory</h4>
          <p>Belief matching objective reality = truth. But humans can never directly access objective reality — senses are survival systems that simplify and distort.</p>
        </div>
      </div>
      <div class="dual-card yes">
        <div class="dual-icon">👥</div>
        <div class="dual-text">
          <h4>Coherence Theory</h4>
          <p>Belief matching group belief = truth. The bandwagon effect determines most people\'s standard of "truth." Independence from group cognition is extremely difficult.</p>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- 03 -->
<div class="section section-03">
  <div class="section-num num-03">03</div>
  <div class="section-body">
    <div class="tag tag-03">Experimental Proof</div>
    <div class="section-title t-03">The Asch Experiment: 75% Conform Even Knowing the Answer Is Wrong</div>
    <div class="section-desc"><strong>Asch\'s line-length experiment revealed the stunning power of conformity.</strong> Groups of 7, with 6 confederates instructed to give the same wrong answer. Result: 33% fully conformed, 74% conformed at least once. No theory, no values — just simple line-length judgment. Knowing the answer was wrong, people still chose the wrong answer under group pressure. Munger called the bandwagon effect "one of the worst misjudgment tendencies for businesspeople."</div>
    <div class="data-row">
      <div class="data-card d1">
        <div class="data-big">7<span class="kpi-unit">/group</span></div>
        <div class="data-name">Experiment Design</div>
        <div class="data-sm">6 confederates + 1 subject. Confederates simultaneously chose the obviously wrong line length.</div>
      </div>
      <div class="data-card d2">
        <div class="data-big">33<span class="kpi-unit">%</span></div>
        <div class="data-name">Full Conformity</div>
        <div class="data-sm">One-third of subjects followed the wrong group judgment in all trials.</div>
      </div>
      <div class="data-card d3">
        <div class="data-big">74<span class="kpi-unit">%</span></div>
        <div class="data-name">Conformed Once</div>
        <div class="data-sm">Nearly three-quarters abandoned the correct answer at least once, choosing the group\'s wrong answer.</div>
      </div>
    </div>
  </div>
</div>

<!-- 04 -->
<div class="section section-04">
  <div class="section-num num-04">04</div>
  <div class="section-body">
    <div class="tag tag-04">Crowd Psychology</div>
    <div class="section-title t-04">Inescapable Herd: Le Bon\'s Three Laws of Crowds</div>
    <div class="section-desc"><strong>Le Bon\'s "The Crowd" revealed three crowd properties.</strong> ① No intelligence: crowds are the sum of stupidity; individual intelligence is dragged down. ② No logic: logic doesn\'t work on crowds — "making assertive, concise statements without reasoning is the most reliable way to plant ideas in the crowd\'s mind." ③ No consciousness: individuals in crowds are no longer themselves but puppets without independent thought. The Stanford Prison Experiment: ordinary volunteers rapidly became abusive guards and submissive prisoners — even the professor running it got engulfed.</div>
    <div class="flow-row">
      <div class="flow-step">No Intelligence<br>Sum of stupidity</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">No Logic<br>Moved only by images</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step end">No Consciousness<br>Become puppets</div>
    </div>
  </div>
</div>

<!-- 05 -->
<div class="section section-05">
  <div class="section-num num-05">05</div>
  <div class="section-body">
    <div class="tag tag-05">Breaking Free</div>
    <div class="section-title t-05">How to Escape: Graham\'s "Oil in Hell" Parable</div>
    <div class="section-desc"><strong>An oil tycoon wants to enter Heaven but is told the quota for oilmen is full.</strong> He shouts into Heaven: "There\'s oil in Hell!" All the oilmen leap into Hell. The gatekeeper invites him in — he refuses: "If they all went, there might really be oil in Hell." A lie he himself fabricated; when everyone believed it, he believed it too. This is human nature. Russell: "Most people would rather die than think independently." Recognizing the bandwagon effect as a genetically-embedded shackle is step one to escaping it.</div>
    <div class="dual-grid">
      <div class="dual-card no">
        <div class="dual-icon">🛢️</div>
        <div class="dual-text">
          <h4>Oil in Hell</h4>
          <p>"Oil in Hell!" — a self-fabricated lie. But seeing everyone jump, he believed it too. The ultimate metaphor for the bandwagon effect.</p>
        </div>
      </div>
      <div class="dual-card yes">
        <div class="dual-icon">🧠</div>
        <div class="dual-text">
          <h4>Independent Thinking</h4>
          <p>Independent thinking in a crowd means using consciousness against instinct, thought against biology. But this is the only path to breakthrough.</p>
        </div>
      </div>
    </div>
  </div>
</div>''',
    "takeaway": 'Coherence theory reveals a harsh truth: what most people believe as "truth" is merely the product of group belief. 75% abandoned correct judgment under group pressure. The bandwagon effect is a genetically-embedded cognitive pattern manifesting as the crowd\'s three nots — not intelligent, not logical, not conscious. Russell said "most people would rather die than think independently." Recognizing this embedded shackle is the first step to breaking free. Independent thinking means using consciousness against instinct — but that is the only path to breakthrough.',
    "footer": '"First Principles" Ch7 Infographic · Based on "Bandwagon Effect" · By Li Shanyou · For learning reference'
}

# --- CH8 ---
chapters_zh[8] = {
    "h1": '第一性原理 · 第8章「批判性思维：我讲的可能都是错的」',
    "title": '第一性原理 · 第8章「批判性思维」',
    "subtitle": '''<span style="display:block;margin-bottom:6px;font-weight:bold;color:#dc2626;font-size:12px;letter-spacing:1px;">科学革命不是知识的革命，而是无知的革命 · 独立思考是创新的第一特征</span>
    逻辑三洽判断信念是否暂时正确。破除"我执"（主体性认同）
    和"群体信念"两大禁锢。批判性思维=独立思考+普遍怀疑+反共识。
    没有批判性思维，认知边界便无法打破。''',
    "overview": '本书终章讲授批判性思维——全书一以贯之的思维方法：不是批判思维的内容，而是批判思维的结构（寻找系统的隐含假设并打破它）。首先用逻辑三洽（自洽、他洽、续洽）判断信念的暂时正确性；然后揭示比逻辑更深的两大力量——"我执"（主体性认同：为了证明"我是对的"必须证明"你是错的"，99%的争吵都是本能性的尊严之争）和"群体信念"（"我们的思想"比"我的思想"更可怕）。最后引出批判性思维三要素——独立思考、普遍怀疑、反共识——并通过保尔森做空次级贷、乔布斯的反文化精神等案例加以证明。',
    "kpi": '''<div class="kpi-row cols-5">
  <div class="kpi-card c01">
    <div class="kpi-value">3<span class="kpi-unit">洽</span></div>
    <div class="kpi-label">逻辑三洽</div>
    <div class="kpi-note">自洽·他洽·续洽</div>
  </div>
  <div class="kpi-card c02">
    <div class="kpi-value">2<span class="kpi-unit">大</span></div>
    <div class="kpi-label">禁锢力量</div>
    <div class="kpi-note">我执·群体信念</div>
  </div>
  <div class="kpi-card c03">
    <div class="kpi-value">99<span class="kpi-unit">%</span></div>
    <div class="kpi-label">争吵是尊严之争</div>
    <div class="kpi-note">本能性的存在性防卫</div>
  </div>
  <div class="kpi-card c04">
    <div class="kpi-value">3<span class="kpi-unit">要素</span></div>
    <div class="kpi-label">批判性思维</div>
    <div class="kpi-note">独立思考·普遍怀疑·反共识</div>
  </div>
  <div class="kpi-card c05">
    <div class="kpi-value">20<span class="kpi-unit">亿</span></div>
    <div class="kpi-label">保尔森次贷获利</div>
    <div class="kpi-note">反共识的经典案例</div>
  </div>
</div>''',
    "sections": '''<!-- 01: 逻辑三洽 -->
<div class="section section-01">
  <div class="section-num num-01">01</div>
  <div class="section-body">
    <div class="tag tag-01">信念的标尺</div>
    <div class="section-title t-01">逻辑三洽：判断信念是否"暂时正确"的三重标准</div>
    <div class="section-desc"><strong>既然没有绝对的客观真理，我们如何判断一个信念是否暂时正确？答案是逻辑三洽。</strong>①自洽：信念内部逻辑自圆其说，且与相关事实相互验证——"实践是检验真理的标准"仅存在于逻辑层面。②他洽：信念系统与周边及更深层系统保持一致——如任何物理学理论必须符合熵增定律和光速不变。③续洽：当时代和场景发生变化，新信息出现后，原有信念是否仍能成立。如果原有逻辑出现错乱，信念便不再正确。但这些标准在理性之上仍面临两大力量的挑战。</div>
    <div class="flow-row">
      <div class="flow-step">逻辑自洽<br>内部逻辑自圆其说</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">逻辑他洽<br>与深层系统一致</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step end">逻辑续洽<br>新信息仍能成立</div>
    </div>
  </div>
</div>

<!-- 02: 主体性认同 -->
<div class="section section-02">
  <div class="section-num num-02">02</div>
  <div class="section-body">
    <div class="tag tag-02">"我执"的陷阱</div>
    <div class="section-title t-02">主体性认同：99%的争吵不是为了思想，而是"我执"的尊严之争</div>
    <div class="section-desc"><strong>在逻辑和理性之上，始终存在一个更强大的力量——"我执"。</strong>从逻辑实体角度分析，"我"作为主体其实并不存在，因此"我"必须依附于"我的××"才能证实自身。笛卡儿说"我思故我在"——正因为"我"在思考，所以"我"才存在。这导致了严重后果：没有什么比思想的正确性更能强化"小我"的存在。为了证明"我是对的"，必须证明"你是错的"。99%的争吵不是思想之争，而是本能性的存在性防卫——从某个事件上升到人格与尊严。这不是道理之争，而是尊严之争。</div>
    <div class="dual-grid">
      <div class="dual-card no">
        <div class="dual-icon">🪞</div>
        <div class="dual-text">
          <h4>"我执"=主体性认同</h4>
          <p>"我"并非逻辑实体，必须依附于"我的XX"才能存在。内容千变万化（玩具→名字→工作→钱财），结构始终如一。</p>
        </div>
      </div>
      <div class="dual-card yes">
        <div class="dual-icon">⚔️</div>
        <div class="dual-text">
          <h4>二元对立陷阱</h4>
          <p>为了证明"我是对的"，必须证明"你是错的"。争吵从事件升级到人格。这就是ego——一切痛苦的根源。</p>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- 03: 群体信念 -->
<div class="section section-03">
  <div class="section-num num-03">03</div>
  <div class="section-body">
    <div class="tag tag-03">群体禁锢</div>
    <div class="section-title t-03">群体信念：比"我的思想"更可怕的，是"我们的思想"</div>
    <div class="section-desc"><strong>群体信念中最重要的隐含假设是群体经验：一旦大家相信了，作为群体的一员，我们也会惯性认同。</strong>如果说"我执"是个人版的从众效应（内部群体），那么"群体信念"就是社会版的从众效应。在群体中，"我们的思想"的"我执"更强——"我们的思想"更能自证其明。打破个人信念已然艰难，打破群体信念更是困难百倍。所以破界创新的核心不是在内容上改变，而是在结构上打破——寻找隐含假设并击碎它。</div>
    <div class="flow-row">
      <div class="flow-step">"我执"<br>内部群体信念</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">"群体信念"<br>社会从众效应</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step end">"我们的思想"<br>最强禁锢</div>
    </div>
  </div>
</div>

<!-- 04: 不可知论 -->
<div class="section section-04">
  <div class="section-num num-04">04</div>
  <div class="section-body">
    <div class="tag tag-04">科学精神</div>
    <div class="section-title t-04">不可知论与进步：科学革命不是"知识的革命"而是"无知的革命"</div>
    <div class="section-desc"><strong>康德提出"物自体不可知"——我们只能认知现象界。</strong>不可知论看似消极，实际上是进步的驱动力：破界创新最大的障碍是认知边界，而不可知论告诉我们，之前所了解的一切都不一定是正确的。《人类简史》作者赫拉利指出：科学革命与前现代知识体系的第一个不同之处是"愿意承认自己的无知"。1492年哥伦布发现美洲，欧洲人发现地图是错的——于是留下大片空白，激励后人去填补。牛顿说："我不相信任何假设。"达尔文说自己"后半生坚持传播怀疑主义"。</div>
    <div class="dual-grid">
      <div class="dual-card no">
        <div class="dual-icon">🗺️</div>
        <div class="dual-text">
          <h4>1492年：地图错了</h4>
          <p>哥伦布发现美洲——地图上不存在的大陆。欧洲人更换世界地图，留下空白，激励了探索时代。</p>
        </div>
      </div>
      <div class="dual-card yes">
        <div class="dual-icon">🔬</div>
        <div class="dual-text">
          <h4>科学革命=无知的革命</h4>
          <p>牛顿、达尔文都是不可知论者。愿意承认无知，是打破认知边界的前提。这不是虚无，而是进步的动力。</p>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- 05: 反共识 -->
<div class="section section-05">
  <div class="section-num num-05">05</div>
  <div class="section-body">
    <div class="tag tag-05">反共识行动</div>
    <div class="section-title t-05">反共识：批判性思维的终极实践——保尔森做空次贷与乔布斯的反叛</div>
    <div class="section-desc"><strong>保尔森2006年发现房价年涨7%严重偏离历史1.4%均值，做空CDO。</strong>房价继续上涨，基金不断亏损，受到各方嘲笑。2007年次贷危机爆发，反共识为他带来数十亿美元收益。彼得·蒂尔："在什么重要问题上，你与其他人有不同看法？"贝索斯："必须采取一个非共识但正确的观点，才能打败竞争对手。"芒格："反过来想，总是反过来想。"乔布斯浸润于反文化运动，质疑一切权威。批判性思维=独立思考+普遍怀疑+反共识。</div>
    <div class="flow-row">
      <div class="flow-step">保尔森<br>做空次贷(2006)</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">彼得·蒂尔<br>"你与别人有何不同看法"</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">贝索斯<br>"非共识但正确"</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step end">芒格<br>"反过来想"</div>
    </div>
  </div>
</div>''',
    "takeaway": '批判性思维是创新精神的第一特征，也是打破认知边界的必要条件。它由三个要素构成：独立思考（不被"我执"绑架）、普遍怀疑（承认无知）、反共识（敢于与群体不同）。保尔森做空次贷、乔布斯的反叛精神、芒格的"反过来想"、贝索斯的"非共识但正确"——这些顶级的创新者和投资者都在践行同一个原则。本书从头到尾都在应用批判性思维的结构：寻找任何系统的隐含假设并打破它。我讲的可能都是错的，重要的是思维的模型，而不是思维的内容。',
    "footer": '《第一性原理》第8章信息图 · 基于「批判性思维」内容提炼 · 李善友 著 · 仅供学习参考'
}

chapters_en[8] = {
    "h1": 'First Principles · Ch8 "Critical Thinking: Everything I Say May Be Wrong"',
    "title": 'First Principles · Ch8「Critical Thinking」',
    "subtitle": '''<span style="display:block;margin-bottom:6px;font-weight:bold;color:#dc2626;font-size:12px;letter-spacing:1px;">Scientific revolution is not a revolution of knowledge but of ignorance</span>
    Logic\'s three coherences judge whether beliefs are temporarily correct.
    Break free from "ego" (identity attachment) and "group belief."
    Critical thinking = independent thought + universal doubt + anti-consensus. ''',
    "overview": 'The final chapter teaches critical thinking — the mental method running through the entire book: not the content of critical thinking, but its structure (finding a system\'s hidden assumptions and breaking them). First, use the three coherences (self-consistency, other-consistency, time-consistency) to judge a belief\'s temporary correctness. Then reveal two forces deeper than logic — "ego" (identity attachment: to prove "I am right," one must prove "you are wrong"; 99% of arguments are instinctive dignity battles) and "group belief" ("our thought" is more terrifying than "my thought"). Finally, the three elements of critical thinking — independent thought, universal doubt, anti-consensus — are demonstrated through Paulson\'s shorting of subprime mortgages and Jobs\' countercultural spirit.',
    "kpi": '''<div class="kpi-row cols-5">
  <div class="kpi-card c01">
    <div class="kpi-value">3<span class="kpi-unit"> Coherences</span></div>
    <div class="kpi-label">Logic Standard</div>
    <div class="kpi-note">Self · Other · Time</div>
  </div>
  <div class="kpi-card c02">
    <div class="kpi-value">2<span class="kpi-unit"> Shackles</span></div>
    <div class="kpi-label">Binding Forces</div>
    <div class="kpi-note">Ego · Group Belief</div>
  </div>
  <div class="kpi-card c03">
    <div class="kpi-value">99<span class="kpi-unit">%</span></div>
    <div class="kpi-label">Arguments = Dignity Wars</div>
    <div class="kpi-note">Instinctive identity defense</div>
  </div>
  <div class="kpi-card c04">
    <div class="kpi-value">3<span class="kpi-unit"> Elements</span></div>
    <div class="kpi-label">Critical Thinking</div>
    <div class="kpi-note">Independent · Doubt · Anti-Consensus</div>
  </div>
  <div class="kpi-card c05">
    <div class="kpi-value">$2<span class="kpi-unit">B</span></div>
    <div class="kpi-label">Paulson\'s Subprime Gain</div>
    <div class="kpi-note">Classic anti-consensus case</div>
  </div>
</div>''',
    "sections": '''<!-- 01 -->
<div class="section section-01">
  <div class="section-num num-01">01</div>
  <div class="section-body">
    <div class="tag tag-01">Belief Standard</div>
    <div class="section-title t-01">Logic\'s Three Coherences: Judging Whether a Belief Is "Temporarily Correct"</div>
    <div class="section-desc"><strong>Without absolute objective truth, how do we judge whether a belief is temporarily correct? Through the three coherences.</strong> ① Self-consistency: the belief\'s internal logic is coherent and verified by relevant facts — "practice is the standard of truth" only exists at the logical level. ② Other-consistency: the belief system aligns with adjacent and deeper systems — any physics theory must conform to entropy increase and constant light speed. ③ Time-consistency: when times and contexts change and new information emerges, does the original belief still hold? If its logic unravels, the belief is no longer correct. But even these standards face challenges from two forces beyond logic.</div>
    <div class="flow-row">
      <div class="flow-step">Self-Consistency<br>Internal logic coherent</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">Other-Consistency<br>Aligns with deeper systems</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step end">Time-Consistency<br>Holds with new evidence</div>
    </div>
  </div>
</div>

<!-- 02 -->
<div class="section section-02">
  <div class="section-num num-02">02</div>
  <div class="section-body">
    <div class="tag tag-02">The Ego Trap</div>
    <div class="section-title t-02">Identity Attachment: 99% of Arguments Are Not About Ideas but Dignity Wars of "Ego"</div>
    <div class="section-desc"><strong>Above logic and reason always stands a more powerful force — "ego."</strong> From a logical entity perspective, "I" as a subject doesn\'t actually exist, so "I" must attach to "my XX" to confirm itself. Descartes: "I think, therefore I am" — precisely because "I" think, "I" exist. This leads to a serious consequence: nothing strengthens the "small self" more than the correctness of thought. To prove "I am right," one must prove "you are wrong." 99% of arguments are not about ideas but instinctive defenses of existence — escalating from a specific issue to personality and dignity. It\'s not a battle of reason but a battle of dignity.</div>
    <div class="dual-grid">
      <div class="dual-card no">
        <div class="dual-icon">🪞</div>
        <div class="dual-text">
          <h4>"Ego" = Identity Attachment</h4>
          <p>"I" is not a logical entity — must attach to "my XX" to exist. Content changes (toys→name→work→wealth), structure never does.</p>
        </div>
      </div>
      <div class="dual-card yes">
        <div class="dual-icon">⚔️</div>
        <div class="dual-text">
          <h4>The Binary Opposition Trap</h4>
          <p>To prove "I am right," must prove "you are wrong." Arguments escalate from issues to personhood. This is ego — the root of all suffering.</p>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- 03 -->
<div class="section section-03">
  <div class="section-num num-03">03</div>
  <div class="section-body">
    <div class="tag tag-03">Group Shackles</div>
    <div class="section-title t-03">Group Belief: "Our Thought" Is More Terrifying Than "My Thought"</div>
    <div class="section-desc"><strong>The most important hidden assumption in group belief is group experience: once everyone believes, as a group member, we habitually identify with it.</strong> If "ego" is the individual version of the bandwagon effect (internal group), then "group belief" is its social version. In groups, "our thought\'s" ego is even stronger — "our thought" self-validates more powerfully. Breaking personal beliefs is already hard; breaking group beliefs is a hundred times harder. That\'s why the core of boundary-breaking innovation isn\'t changing content but breaking structure — finding hidden assumptions and shattering them.</div>
    <div class="flow-row">
      <div class="flow-step">"Ego"<br>Internal group belief</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">"Group Belief"<br>Social bandwagon effect</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step end">"Our Thought"<br>Strongest shackle</div>
    </div>
  </div>
</div>

<!-- 04 -->
<div class="section section-04">
  <div class="section-num num-04">04</div>
  <div class="section-body">
    <div class="tag tag-04">Scientific Spirit</div>
    <div class="section-title t-04">Agnosticism and Progress: Scientific Revolution Is "Revolution of Ignorance"</div>
    <div class="section-desc"><strong>Kant proposed "noumena are unknowable" — we can only know phenomena.</strong> Agnosticism seems pessimistic but is actually a driver of progress: the biggest obstacle in boundary-breaking innovation is our cognitive boundary, and agnosticism tells us everything we previously knew might not be correct. Harari points out: the first difference between scientific revolution and pre-modern knowledge systems is "willingness to admit ignorance." 1492: Columbus discovered America — the map was wrong. Europeans left vast blanks, motivating exploration. Newton: "I believe in no hypotheses." Darwin spent "the second half of my life spreading skepticism."</div>
    <div class="dual-grid">
      <div class="dual-card no">
        <div class="dual-icon">🗺️</div>
        <div class="dual-text">
          <h4>1492: The Map Was Wrong</h4>
          <p>Columbus found America — a continent not on any map. Europeans redrew the world map, leaving blanks that inspired the Age of Exploration.</p>
        </div>
      </div>
      <div class="dual-card yes">
        <div class="dual-icon">🔬</div>
        <div class="dual-text">
          <h4>Scientific Revolution = Ignorance Revolution</h4>
          <p>Newton and Darwin were agnostics. Admitting ignorance is the prerequisite for breaking cognitive boundaries. Not nihilism — it\'s the engine of progress.</p>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- 05 -->
<div class="section section-05">
  <div class="section-num num-05">05</div>
  <div class="section-body">
    <div class="tag tag-05">Anti-Consensus Action</div>
    <div class="section-title t-05">Anti-Consensus: Critical Thinking\'s Ultimate Practice — Paulson, Jobs, Thiel</div>
    <div class="section-desc"><strong>In 2006, Paulson spotted home prices rising 7% annually vs. the historical 1.4% mean, and shorted CDOs.</strong> Prices kept rising, his fund kept losing, and he faced ridicule. When the subprime crisis erupted in 2007, anti-consensus earned him billions. Peter Thiel: "On what important question do you differ from others?" Bezos: "You must take a non-consensus but correct view to beat competitors." Munger: "Invert, always invert." Jobs was steeped in counterculture, questioning all authority. Critical thinking = independent thought + universal doubt + anti-consensus.</div>
    <div class="flow-row">
      <div class="flow-step">Paulson<br>Shorted subprime (2006)</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">Peter Thiel<br>"What\'s your different view?"</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step">Bezos<br>"Non-consensus but right"</div>
      <div class="flow-arrow">→</div>
      <div class="flow-step end">Munger<br>"Invert, always invert"</div>
    </div>
  </div>
</div>''',
    "takeaway": 'Critical thinking is the first characteristic of the innovative spirit and a necessary condition for breaking cognitive boundaries. It consists of three elements: independent thought (not hijacked by "ego"), universal doubt (admitting ignorance), and anti-consensus (daring to differ from the crowd). Paulson shorting subprime, Jobs\' rebellious spirit, Munger\'s "invert, always invert," Bezos\' "non-consensus but correct" — these top innovators and investors all practice the same principle. Throughout this book, we\'ve applied the structure of critical thinking: find any system\'s hidden assumptions and break them. Everything I say may be wrong — what matters is the model of thinking, not the content of thinking.',
    "footer": '"First Principles" Ch8 Infographic · Based on "Critical Thinking" · By Li Shanyou · For learning reference'
}


# ============================================================
# WRITE FILES
# ============================================================

for ch in [5, 6, 7, 8]:
    chnum = f"{ch:03d}"
    
    # ZH
    zh_html = make_html("zh", ch, chapters_zh[ch])
    zh_file = os.path.join(BOOKDIR, f"{SLUG}-ch{chnum}-info-zh.html")
    with open(zh_file, 'w') as f:
        f.write(zh_html)
    print(f"ZH ch{chnum}: {len(zh_html)} bytes -> {zh_file}")
    
    # EN
    en_html = make_html("en", ch, chapters_en[ch])
    en_file = os.path.join(BOOKDIR, f"{SLUG}-ch{chnum}-info-en.html")
    with open(en_file, 'w') as f:
        f.write(en_html)
    print(f"EN ch{chnum}: {len(en_html)} bytes -> {en_file}")

print("All 8 files generated!")