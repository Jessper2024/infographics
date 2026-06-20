#!/usr/bin/env python3
"""Generate 第一性原理 ch001-ch004 infographics (zh+en, 8 files).
Template: #f5f1eb bg, FZXPYZS font, 880px, 10-layer structure, per the spec.
"""

import os

OUTDIR = os.path.expanduser("~/.openclaw/workspace/infographics/books")
BOOK_SLUG = "第一性原理"
EN_SLUG = "First-Principles"
BOOK_EN = "First Principles"
AUTHOR = "李善友"
AUTHOR_EN = "Li Shanyou"
CATALOG_FILE = "第一性原理-catalog.html"

# ── Chapter metadata ──
CHAPTERS = {
    1: {
        "cn_num": "一",
        "en_num": "1",
        "cn_title": "第一性原理：任何理性系统的根基性命题",
        "en_title": "First Principles: The Foundational Axioms of Any Rational System",
        "overview_cn": (
            "本章建立了全书最重要的哲学基础。作者对比了人类两种基本思维方式——归纳法与演绎法，"
            "指出归纳法虽是人类99%日常知识的来源，却存在致命的“归纳法谬误”：连续性假设在逻辑上无法自证，"
            "只能证伪、不能证明。而演绎法虽然能从正确前提出发保真推导，但其前提本身必须来自更高层级的演绎——"
            "如此倒推到尽头，就是那个自确定的、不可动摇的元起点：第一性原理。"
            "任何理性系统都由第一性原理+演绎法构成，而第一性原理必定位于系统之外。"
        ),
        "overview_en": (
            "This chapter lays the philosophical foundation of the entire book. "
            "The author contrasts two fundamental modes of human thinking—induction and deduction. "
            "Induction, the source of 99% of daily knowledge, suffers from the 'induction fallacy': "
            "the hidden assumption of continuity cannot be logically self-proven; it can only falsify, never prove. "
            "Deduction, by contrast, guarantees truth when premises are correct—but those premises must themselves "
            "come from a higher-level deduction. Tracing this chain to its end reveals a self-evident, "
            "unshakable starting point: the First Principle. Every rational system = First Principle + Deduction, "
            "and the First Principle always lies outside the system itself."
        ),
        "subtitle_cn": "归纳法只能证伪不能证明 · 演绎法需要一个来自系统之外的元起点 · 找到你的"一"",
        "subtitle_en": "Induction can only falsify, never prove · Deduction needs an axiom outside the system · Find your 'One'",
        "kpis_cn": [
            ("99%", "%", "人类日常知识建立在归纳法之上", "具象经验→抽象知识"),
            ("2300", "年", "亚里士多德提出第一性原理", "每一系统皆有第一原理"),
            ("∞", "", "演绎法链条不能无限倒推", "必须有一个自确定的元起点"),
            ("5步", "", "从第一性原理到理性系统", "元前提→演绎法→中心思想"),    # changed from previous
        ],
        "kpis_en": [
            ("99%", "%", "Daily knowledge built on induction", "Concrete experience → abstract knowledge"),
            ("2300", "yrs", "Aristotle's First Principles", "Every system has a first principle"),
            ("∞", "", "Deduction chain cannot regress infinitely", "Must have a self-evident axiom"),
            ("5", "steps", "From First Principle to Rational System", "Axiom → deduction → central idea"),
        ],
        "sections_cn": [
            {
                "num": 1, "tag": "思维本质",
                "title": "归纳法：人类内置的思维定式，求存不求真",
                "desc": "<strong>归纳法是99%人类知识的来源，但它只能证伪，不能证明。</strong>空间性归纳默认一个空间有效的规律在所有空间有效；时间性归纳默认过去的规律在未来也有效。这两种归纳都依赖一个无法自证的隐含假设——连续性。休谟指出，我们无法用先验知识证明未来与过去一致；波普尔进一步断言，可证伪性才是科学的标志。归纳法的结论本质上是等待被推翻的假说。它的真正价值不在于追求真理，而在于以最小认知成本确保生存——这就是人类的"最小作用力原理"与"求存不求真"的阿喀琉斯之踵。",
                "desc_en": "<strong>99% of human knowledge comes from induction, but it can only falsify—never prove.</strong> Spatial induction assumes what works in one space works everywhere; temporal induction assumes past regularities persist. Both depend on an unprovable hidden assumption: continuity. Hume argued we cannot prove a priori that the future resembles the past; Popper declared falsifiability the hallmark of science. Inductive conclusions are essentially hypotheses awaiting refutation. Their true value lies not in truth-seeking but in survival at minimal cognitive cost—humanity's 'principle of least effort' and the Achilles' heel of 'surviving without truth.'",
                "flow_cn": ["空间性归纳\n欧洲天鹅白→全球白", "时间性归纳\n太阳过去东升→未来东升", "连续性假设\n未来与过去一样", "休谟问题\n归纳法谬误"],
                "flow_en": ["Spatial Induction\nWhite swans here → white everywhere", "Temporal Induction\nSun rose east → will rise east", "Continuity Assumption\nFuture = past", "Hume's Problem\nInduction fallacy"],
                "flow_end_cn": "波普尔\n可证伪性=科学",
                "flow_end_en": "Popper\nFalsifiability = science",
            },
            {
                "num": 2, "tag": "理性之光",
                "title": "演绎法三段论：逻辑比事实更真实",
                "desc": "<strong>演绎法是理性思维的主要用智形式，起源于古希腊。</strong>亚里士多德创造了三段论：大前提→小前提→结论，前提正确则结论必然为真。演绎法的核心准则不是事实，而是逻辑正确——古希腊人甚至认为逻辑才是实体，而事物本身未必。与东方"实践出真知"的归纳法传统不同，西方演绎法相信逻辑假设在先，实践检验在后。牛顿没有解决任何实际问题，他只是发现了F=ma这个抽象逻辑，然后瓦特将它用于蒸汽机，引发了第一次工业革命。这就是演绎法的力量——一条抽象公式可以解决所有相关的具象问题。",
                "desc_en": "<strong>Deduction is the primary vehicle of rational thought, originating in ancient Greece.</strong> Aristotle created the syllogism: major premise → minor premise → conclusion; if premises are correct, the conclusion must be true. The core criterion is logical correctness, not factual verification—the ancient Greeks even believed logic was the substance, while physical things need not be. Unlike the Eastern 'practice yields truth' inductive tradition, Western deduction places logical hypotheses first and empirical verification second. Newton solved no practical problem; he merely discovered F=ma—an abstract logic. Then Watt applied it to the steam engine, igniting the First Industrial Revolution. This is deduction's power: one abstract formula can solve all related concrete problems.",
                "dual_cn": [
                    ("🌏", "东方思维：实践→真知", "技术和艺术建立在实践之上，经验总结在后，典型的归纳法。相信实践第一、真知第二。"),
                    ("🏛️", "西方思维：假设→验证", "先提出抽象理论假设指导未来生活，再用实践检验。缺点是慢，优点是找到的理论可迁移。"),
                ],
                "dual_en": [
                    ("🌏", "Eastern: Practice → Truth", "Technique and art built on practice; experience-summary follows. Typical induction. Practice first, truth second."),
                    ("🏛️", "Western: Hypothesis → Verify", "Abstract theory hypothesis first guides life, then verified by practice. Slow, but yields transferable theory."),
                ],
            },
            {
                "num": 3, "tag": "隐含假设",
                "title": "前提的准确性：演绎法的结构性困境",
                "desc": "<strong>演绎法有一个结构性缺陷——不能证伪，其可保真性完全取决于前提为真。</strong>但演绎法的前提从何而来？归根结底来自归纳法，而归纳法不能保真，因此演绎法终极无效。唯一的出路是：前提必须来自一个更高层级演绎推理的结论。但这条链条不能无限倒推——最终必须有一个能够自确定的元起点，这就是第一性原理（First Principles）。换句话说，演绎法+第一性原理=理性系统。如果没有第一性原理，一切理性系统的建立无从谈起。在科学领域它被称为第一因，在哲学中称为逻辑奇点。",
                "desc_en": "<strong>Deduction has a structural flaw—it cannot falsify; its truth-preservation depends entirely on correct premises.</strong> But where do premises come from? Ultimately from induction—which cannot guarantee truth—so deduction is ultimately invalid. The only escape: premises must come from a higher-level deductive conclusion. But this chain cannot regress infinitely—there must be a self-evident, self-confirming origin: the First Principle. In other words: First Principle + Deduction = Rational System. Without a First Principle, no rational system can be built. In science it is called the First Cause; in philosophy, the Logical Singularity.",
                "flow_cn": ["归纳法前提\n（来自经验）", "演绎法三段论\n前提→结论", "前提必须为真\n→终极无效", "更高层演绎结论\n作为新前提"],
                "flow_en": ["Inductive premise\n(from experience)", "Deductive syllogism\npremise → conclusion", "Premise must be true\n→ ultimately invalid", "Higher-level deduction\nas new premise"],
                "flow_end_cn": "元起点\n第一性原理",
                "flow_end_en": "The Axiom\nFirst Principle",
            },
            {
                "num": 4, "tag": "系统基石",
                "title": "任何系统都有自己的基石假设，且位于系统之外",
                "desc": "<strong>亚里士多德早在2300年前就指出：每一系统探索中，存在一个不可省略、不可删除、不可违反的第一原理。</strong>需要注意的是，第一性原理不是系统的中心思想，而是系统之外、之前的元前提。牛顿力学的中心思想是F=ma，但其第一性原理是惯性假设和引力假设；爱因斯坦相对论的中心思想是E=mc²，但其第一性原理是光速不变和相对性原理。企业也是一样：商业模式是中心思想，但商业模式得以形成的基石假设才是第一性原理。就像地基越深大楼越高，找到那个"一"，注入所有力量——亚马逊的"一"是客户，乔布斯的"一"是产品。",
                "desc_en": "<strong>2300 years ago, Aristotle stated: every system inquiry has a First Principle that cannot be omitted, deleted, or violated.</strong> Importantly, a First Principle is not a system's central idea but an meta-premise that lies outside and before the system. Newtonian mechanics' central idea is F=ma, but its First Principles are the assumptions of inertia and gravity. Einstein's relativity centers on E=mc², but its First Principles are the constancy of light speed and the relativity principle. Same for business: a business model is the central idea, but the foundational assumption giving rise to it is the First Principle. Like deeper foundations supporting taller buildings—find your 'One' and pour all force into it. Amazon's 'One' is the customer; Jobs' 'One' is the product.",
                "dual_cn": [
                    ("🔴", "牛顿力学的第一性原理", "惯性假设 + 引力假设 → 推导出F=ma → 瓦特改良蒸汽机 → 第一次工业革命"),
                    ("🔵", "爱因斯坦的第一性原理", "光速不变 + 相对性原理 → 推导出E=mc² → 开启核能与现代物理"),
                ],
                "dual_en": [
                    ("🔴", "Newton's First Principles", "Inertia + Gravity assumptions → derive F=ma → Watt's steam engine → 1st Industrial Revolution"),
                    ("🔵", "Einstein's First Principles", "Light-speed constancy + Relativity principle → derive E=mc² → Nuclear energy & modern physics"),
                ],
            },
            {
                "num": 5, "tag": "层级结构",
                "title": "第一性原理有层级之分：母系统的中心思想=子系统的第一性原理",
                "desc": "<strong>系统之间是有层级之分的。</strong>大系统的中心思想可以作为小系统的第一性原理。对牛顿而言F=ma是其推导得出的中心思想，但对后来的使用者（如瓦特），F=ma就是第一性原理。E=mc²对爱因斯坦是结论，对后来的科学家就是第一性原理。从实际应用出发，我们不必找到终极的第一性原理，比我们想要推导的理性系统范围更大的母系统，其中心思想就可以作为子系统第一性原理的来源。每个系统都有自己的适用范围，第一性原理也非放之四海而皆准。许多大系统有2~3个第一性原理同时支撑——注意"First Principles"是个复数词。",
                "desc_en": "<strong>Systems exist in hierarchies.</strong> A parent system's central idea becomes a subsystem's First Principle. To Newton, F=ma was a derived conclusion; to later users like Watt, F=ma became the First Principle. E=mc² was Einstein's conclusion; for later scientists it became the First Principle. In practice, we need not find the ultimate First Principle—any parent system larger than our target system can provide its central idea as our subsystem's First Principle. Every system has its scope; no First Principle is universal. Many large systems are supported by 2-3 First Principles simultaneously—note that 'First Principles' is plural.",
                "flow_cn": ["母系统\n基石假设", "母系统\n中心思想 = F=ma", "子系统\n第一性原理 = F=ma", "瓦特的蒸汽机\n工业革命"],
                "flow_en": ["Parent system\nfoundational axiom", "Parent system\ncentral idea = F=ma", "Subsystem\nFirst Principle = F=ma", "Watt's steam engine\nIndustrial Revolution"],
                "flow_end_cn": "你的"一"是什么？",
                "flow_end_en": "What is YOUR 'One'?",
            },
        ],
        "takeaway_cn": (
            "第一性原理是任何理性系统的"源代码"。归纳法帮你生存，演绎法帮你创新——但前提是找到那个来自系统之外的、自确定的元起点。"
            "不要从结论入手推翻一个命题，要从它的隐含假设开始。问问自己：我的系统的"一"是什么？找到它，践行它，才能笃定地工作和生活。"
        ),
        "takeaway_en": (
            "The First Principle is the 'source code' of any rational system. Induction helps you survive; deduction helps you innovate—"
            "but only if you find the self-evident axiom that lies outside the system. "
            "To overturn a conclusion, attack its hidden assumption, not the conclusion itself. Ask: what is the 'One' underlying my system? Find it, live it, and work with conviction."
        ),
    },
    2: {
        "cn_num": "二",
        "en_num": "2",
        "cn_title": "公理化思维：人类理性思维的顶级智慧",
        "en_title": "Axiomatic Thinking: The Summit of Human Rational Intelligence",
        "overview_cn": (
            "如果说第一性原理是哲科思维的"根"，公理化思维就是它的"干"。"
            "本章追溯了从欧几里得《几何原本》到牛顿、达尔文、爱因斯坦的公理化思维脉络："
            "以少数不证自明的公理为起点，通过逻辑演绎，推导出整个系统。"
            "欧氏几何仅凭5条公设、5条公理和23个定义，就构建了包含48条定理、467个命题的完整平面几何系统，沿用两千余年。"
            "这种"从已知推导未知"的能力，正是科学革命的底层密码。遗憾的是，东方文明的"微言大义"传统缺乏公理化思维训练，"
            "这正是中国在近代基础科学领域贡献不足的深层原因。"
        ),
        "overview_en": (
            "If First Principles are the 'root' of philosophical-scientific thinking, axiomatic thinking is the 'trunk.' "
            "This chapter traces axiomatic thinking from Euclid's Elements through Newton, Darwin, and Einstein: "
            "begin with a few self-evident axioms, logically deduce the entire system. "
            "Euclidean geometry, built from just 5 postulates, 5 axioms, and 23 definitions, produced a complete system "
            "of 48 theorems and 467 propositions—still in use after 2,000+ years. "
            "This ability to 'derive the unknown from the known' is the secret code of the scientific revolution. "
            "Regrettably, the Eastern 'terse aphorism' tradition lacked axiomatic training—a deep reason "
            "for China's under-contribution to foundational modern science."
        ),
        "subtitle_cn": "5公设+5公理+23定义→48定理+467命题 · 逻辑推导过程比结果更重要 · 哲学始于对自明的追问",
        "subtitle_en": "5 postulates+5 axioms+23 defs→48 theorems+467 propositions · The logical process matters more than the result · Philosophy begins by questioning the self-evident",
        "kpis_cn": [
            ("10", "条", "公设+公理奠定欧氏几何", "5公设+5公理=基石"),
            ("48+467", "条", "推导所得定理与命题", "演绎法构建完整平面几何"),
            ("2000+", "年", "欧氏几何沿用至今", "人类思维的奇迹"),
            (">60%", "", "古代中国技术发明占比", "但近代基础定理贡献<1%"),
        ],
        "kpis_en": [
            ("10", "", "Postulates+Axioms underpin Euclidean Geometry", "5 postulates + 5 axioms = foundation"),
            ("48+467", "", "Derived theorems & propositions", "Deductive construction of plane geometry"),
            ("2000+", "yrs", "Euclidean geometry still in use", "A miracle of human thought"),
            (">60%", "", "Ancient Chinese tech inventions share", "But <1% of modern foundational theorems"),
        ],
        "sections_cn": [
            {
                "num": 1, "tag": "思维奇迹",
                "title": "欧氏几何：哲学家的思考工具，而非数学家的计算手册",
                "desc": "<strong>欧几里得的首要身份是哲学家。</strong>他创立几何学并非为了丈量田地，而是为了创造一种哲学思考工具。他从5条公设、5条公理和23个定义出发，运用形式逻辑推导出48条定理和467个命题，构成了一个严密的逻辑体系。在平面和三维空间中，这个系统已经"饱和"，穷尽了该维度的所有内容。与之同时期的古希腊科学结论几乎全被推翻，唯有欧氏几何两千多年后依然成立——这是人类思维的奇迹。柏拉图学园门口写着"不懂几何学者不得入内"，因为未经过公理化思维训练的人，不具备讨论哲学和科学顶级问题的思维方式。",
                "desc_en": "<strong>Euclid was first and foremost a philosopher.</strong> He created geometry not for land measurement but as a philosophical thinking tool. From 5 postulates, 5 axioms, and 23 definitions, he used formal logic to derive 48 theorems and 467 propositions, forming a rigorous logical system. In planar and 3D space, this system has been 'saturated'—exhausting all content in that dimension. While virtually all contemporaneous ancient Greek scientific conclusions have been overturned, Euclidean geometry still stands after 2,000+ years—a miracle of human thought. Plato's Academy entrance bore the inscription 'Let no one ignorant of geometry enter,' because without axiomatic training, one lacks the thinking mode for top-tier philosophical and scientific discourse.",
                "data_cn": [
                    ("📐", "5条公设", "由任意一点到任意一点可以画直线；有限直线可以继续延长；以任意点为中心、任意距离可以画圆；凡直角都彼此相等；平行公设。"),
                    ("📏", "5条公理", "等于同量的量彼此相等；等量加等量其和仍相等；等量减等量其差仍相等；彼此能重合的物体全等；整体大于部分。"),
                    ("📝", "23个定义", "点无长度宽度；线只有长度无宽度；面有长度宽度无厚度——在现实中这些根本不存在，欧氏几何是纯粹的逻辑实体。"),
                ],
                "data_en": [
                    ("📐", "5 Postulates", "From any point to any point a straight line can be drawn; a finite line can be extended; a circle can be drawn from any center at any distance; all right angles are equal; the parallel postulate."),
                    ("📏", "5 Axioms", "Things equal to the same thing are equal; if equals are added to equals, wholes are equal; if equals are subtracted from equals, remainders are equal; things coinciding are equal; the whole is greater than the part."),
                    ("📝", "23 Definitions", "A point has no length or width; a line has only length; a surface has length and width but no depth—none of these exist in reality. Euclidean geometry is a purely logical entity."),
                ],
            },
            {
                "num": 2, "tag": "证明系统",
                "title": "一切学问都是证明系统：逻辑推导过程比最终结果更重要",
                "desc": "<strong>"一切学问都是证明系统，但凡没有证明的东西都是虚假的东西。"</strong>在理性系统中，推导出事物的逻辑为真，事物才真。亚里士多德创立逻辑学的根本特征就是"必然的导出"——从命题1到命题2的推导过程本身就是逻辑。欧氏几何中每一步推导都必须有对应公理作为支撑，正是这种严谨性赋予了系统生命力。许多人抱怨数学老师过分追求推导完整性，但面对复杂命题时，只有一步步的推导才能打破思维禁锢，以正确过程引导出正确结果——小聪明在复杂命题面前毫无意义。",
                "desc_en": "<strong>'All learning is a proof system; anything unproven is false.'</strong> In a rational system, a thing is true only if the logic deriving it is true. The fundamental trait of Aristotle's logic is 'necessary derivation'—the derivation process itself from proposition 1 to proposition 2 IS logic. Every step in Euclidean geometry must be supported by a corresponding axiom; this rigor is what gives the system its vitality. Many complain about teachers demanding full derivation steps, but when facing complex propositions, only step-by-step derivation can break cognitive boundaries and lead to correct results—clever shortcuts are meaningless before complexity.",
                "flow_cn": ["公设/公理\n（不证自明）", "形式逻辑\n（必然的导出）", "命题推导\n（每一步有公理支撑）", "定理成立\n（逻辑为真）"],
                "flow_en": ["Postulates/Axioms\n(self-evident)", "Formal Logic\n(necessary derivation)", "Proposition derivation\n(each step axiom-backed)", "Theorem proven\n(logically true)"],
                "flow_end_cn": "完整理性系统",
                "flow_end_en": "Complete rational system",
            },
            {
                "num": 3, "tag": "超越现实",
                "title": "从《几何原本》到公理化思维：用已知推导未知的奥秘",
                "desc": "<strong>欧几里得用现实世界不存在的点、线、面，超越感官的禁闭，从已知推出来知。</strong>人类之所以能快速发展至今，依靠的就是从已知推导未知的能力。爱因斯坦的四维弯曲空间是人类感官无法想象的——就像二维虫无法理解三维世界——但他通过公理化思维得出广义相对论，因为逻辑正确的结果必然正确。几何学不是从丈量田地的经验中抽离出来的，而是通过纯逻辑想象构建的——欧几里得甚至愤怒地拒绝教"有用的东西"。真正的"知音"不是观点相同，而是思考方式（逻辑）相同的人——只有逻辑一致，才能从同一基石假设推导出同一结果。",
                "desc_en": "<strong>Euclid used points, lines, and surfaces that don't exist in reality to transcend sensory confinement—deriving the unknown from the known.</strong> Humanity's rapid progress rests on this very ability. Einstein's curved 4D spacetime is unimaginable to human senses—like a 2D bug cannot grasp 3D—but he derived general relativity through axiomatic thinking, because logically correct results must be true. Geometry wasn't abstracted from land-measurement experience but constructed through pure logical imagination—Euclid even angrily refused to teach 'useful things.' A true soulmate is not one who shares your opinions but one who shares your thinking method (logic)—only logical consistency enables deriving the same results from the same foundational axiom.",
                "dual_cn": [
                    ("🎓", "欧几里得的愤怒", "学生问："学几何有什么用处？"欧几里得大怒："你居然想跟我学有用的东西？去跟工匠学吧！"柏拉图学园门口写着"不懂几何学者不得入内"。"),
                    ("🔬", "爱因斯坦的假设", "广义相对论假设空间是四维且可弯曲的——人类大脑无法想象，但逻辑上成立。从已知推导未知，是人类最强大的能力。"),
                ],
                "dual_en": [
                    ("🎓", "Euclid's Anger", "A student asked: 'What use is geometry?' Euclid raged: 'You want to learn useful things from me? Go learn from a craftsman!' Plato's Academy: 'Let no one ignorant of geometry enter.'"),
                    ("🔬", "Einstein's Hypothesis", "General relativity assumes 4D curved space—the human brain cannot imagine it, but it's logically valid. Deriving the unknown from the known is humanity's greatest power."),
                ],
            },
            {
                "num": 4, "tag": "应用实证",
                "title": "公理化思维的应用：笛卡儿、牛顿、达尔文、爱因斯坦的共同武器",
                "desc": "<strong>公理化思维是顶级科学家的共同武器。</strong>笛卡儿受欧氏几何影响，试图将公理化方法引入哲学，提出"我思故我在"作为形而上学的第一性原理。牛顿的《自然哲学的数学原理》体例完全仿照《几何原本》，以惯性假设和引力假设为公理推导出万有引力。达尔文以遗传变异和生存竞争为两条公理，运用假说演绎法得出自然选择进化论——他坦言《物种起源》"从头到尾就是一篇长篇论证"。爱因斯坦更是直说：理论家的工作分两步——第一步发现公理（极难），第二步从公理推出结论（只要勤奋聪明就能做到）。",
                "desc_en": "<strong>Axiomatic thinking is the shared weapon of top scientists.</strong> Descartes, influenced by Euclid, sought to introduce axiomatic methods into philosophy, proposing 'I think, therefore I am' as metaphysics' First Principle. Newton's Principia Mathematica was modeled entirely on Euclid's Elements—deriving universal gravitation from the axioms of inertia and gravity. Darwin used genetic variation and survival competition as axioms, applying the hypothetico-deductive method to reach natural selection—he admitted Origin of Species is 'one long argument from beginning to end.' Einstein stated bluntly: a theorist's work has two steps—first, discover the axioms (extremely difficult); second, deduce conclusions from them (anyone diligent and clever can do this).",
                "flow_cn": ["笛卡儿\n我思故我在", "牛顿\n惯性+引力→万有引力", "达尔文\n遗传变异+生存竞争→进化论", "爱因斯坦\n相对性+光速不变→E=mc²"],
                "flow_en": ["Descartes\n'I think, therefore I am'", "Newton\nInertia+Gravity→Universal gravitation", "Darwin\nVariation+Competition→Evolution", "Einstein\nRelativity+Light-speed constancy→E=mc²"],
                "flow_end_cn": "亚当·斯密\n"看不见的手"→市场经济",
                "flow_end_en": "Adam Smith\n'Invisible hand'→Market economy",
            },
            {
                "num": 5, "tag": "文化根源",
                "title": "让哲科思维点亮中国的创新者：东西方思维的原型差异",
                "desc": "<strong>东西方思维的根本差异：东方以结论为实体（微言大义），西方以推理过程为实体（形式逻辑）。</strong>在技艺时代，中国技术发明占全世界的60%以上，但在近代6000条基础定理定律中，中国人原创贡献不到1%。爱因斯坦在回信中解释"李约瑟难题"时说：西方科学的基础是古希腊形式逻辑体系（欧氏几何）和文艺复兴时期的系统性实验——中国贤哲没有做到这些不足为奇，西方做到这些才令人惊奇。我们从小学习几何，却不知道它是训练顶级思维的教本，无异于买椟还珠。混沌大学的使命就是让哲科思维点亮中国的创新者。",
                "desc_en": "<strong>The fundamental East-West thinking difference: the East treats conclusions as substance (terse aphorisms); the West treats reasoning as substance (formal logic).</strong> In the craft era, China contributed >60% of global technical inventions, yet <1% of the 6,000 foundational modern theorems. Einstein, answering the 'Needham Question,' wrote: Western science rests on the Greek formal logic system (Euclidean geometry) and Renaissance systematic experimentation—it's unsurprising Chinese sages didn't achieve this; it's surprising the West did. We learned geometry as children yet never knew it was a textbook for training top-tier thinking—like buying the casket but returning the pearl. Hundun University's mission: let philosophical-scientific thinking illuminate Chinese innovators.",
                "data_cn": [
                    ("🧠", "东方思维原型", "以结论为实体，遵循圣人之言。微言大义——一句简练的话表达深刻道理。孔子和儒家圣贤快速建立了理性文明，但停留在理性思维层面，无法进展到科学基础。"),
                    ("🧬", "荣格的"原型"理论", "族群、民族、国家背后都有一种共通思维方式，以我们看不见的方式传承着。与其说你在思考，不如说是你背后族群共同的原型在思考。"),
                    ("💡", "李约瑟难题", "尽管中国古代对人类科技发展做出了很多重要贡献，但为什么科学和工业革命没有在近代中国发生？爱因斯坦的答案：缺乏形式逻辑体系+系统性实验方法。"),
                ],
                "data_en": [
                    ("🧠", "Eastern Thinking Prototype", "Treats conclusions as substance, follows sage words. 'Terse aphorisms'—one concise sentence conveying profound truth. Confucius and Confucian sages built rational civilization rapidly but stayed at the rational-thinking level, unable to advance to scientific foundations."),
                    ("🧬", "Jung's 'Archetype' Theory", "Behind every tribe, nation, and country lies a shared thinking mode, inherited invisibly. Rather than 'you think,' it's more that 'the shared archetype behind your group thinks.'"),
                    ("💡", "The Needham Question", "Why, despite ancient China's many contributions to human technology, did the scientific and industrial revolutions not occur in modern China? Einstein's answer: lack of formal logic system + systematic experimental method."),
                ],
            },
        ],
        "takeaway_cn": (
            "公理化思维不只是数学方法，而是一种世界观。"
            "从2-3条基本公理出发，推导出整个商业模式和战略——这个思维深度是可以做到的。"
            "逻辑推导过程比最终结果更重要，真正的"知音"是思考方式（逻辑）相同的人。"
            "没有公理化思维训练，我们推不开柏拉图学园的门。"
        ),
        "takeaway_en": (
            "Axiomatic thinking is not just a mathematical method—it's a worldview. "
            "From 2-3 foundational axioms, you CAN deduce an entire business model and strategy—this depth of thinking is achievable. "
            "The logical derivation process matters more than the final result; a true soulmate is one who shares your logic, not your opinion. "
            "Without axiomatic training, we cannot push open the door of Plato's Academy."
        ),
    },
    3: {
        "cn_num": "三",
        "en_num": "3",
        "cn_title": "破界创新：打破基石，边界外延",
        "en_title": "Boundary-Breaking Innovation: Shatter the Foundation, Expand the Boundary",
        "overview_cn": (
            "创新"不破不立"——"破"的是系统得以形成的第一性原理，"立"的是新的第一性原理，这就是破界创新。"
            "本章提出破界创新的三部曲：①"破"隐含假设——识别并打破构成系统边界的那个默认为真的群体信念；"
            "②"立"基石假设——重建一个更深、更强的第一性原理；"
            "③"见"全新系统——在新基石上自然涌现出全新体系。"
            "从欧氏几何到非欧几何、托勒密到哥白尼、IBM到苹果、诺基亚到iPhone，无数案例证明："
            "破界创新不在内容上做功，而在结构上做功——它让原有问题变得无关紧要，而不是解决原有问题。"
        ),
        "overview_en": (
            "Innovation means 'no breaking, no building'—break the First Principle that forms the system, then build a new one. This is boundary-breaking innovation. "
            "This chapter proposes a 3-step method: ① 'Break' the hidden assumption—identify and shatter the default group belief that forms the system boundary; "
            "② 'Build' a new foundational axiom—reconstruct a deeper, stronger First Principle; "
            "③ 'Envision' a new system—a fresh system naturally emerges on the new foundation. "
            "From Euclidean to non-Euclidean geometry, Ptolemy to Copernicus, IBM to Apple, Nokia to iPhone, countless cases prove: "
            "boundary-breaking innovation operates on structure, not content—it renders old problems irrelevant rather than solving them."
        ),
        "subtitle_cn": "破隐含假设→立基石假设→见全新系统 · 不解决旧问题，让它无关紧要 · 哲学始于对自明的追问",
        "subtitle_en": "Break hidden assumptions → Rebuild foundational axioms → Envision a new system · Don't solve old problems—make them irrelevant · Philosophy begins by questioning the self-evident",
        "kpis_cn": [
            ("3步", "", "破界创新三部曲", "破隐含假设→立基石假设→见全新系统"),
            ("2000+", "年", "欧氏几何→非欧几何", "打破平直空间假设"),
            ("1295", "美元", "Apple-1售价", "价格十倍速变化，进入家庭"),
            ("<4%", "", "失速点后恢复增长概率", "纳德拉4年让微软重回巅峰"),
        ],
        "kpis_en": [
            ("3", "steps", "Boundary-breaking innovation method", "Break → Rebuild → Envision"),
            ("2000+", "yrs", "Euclidean → Non-Euclidean geometry", "Shattering the flat-space assumption"),
            ("$1,295", "", "Apple-1 price", "10x price change, computers enter homes"),
            ("<4%", "", "Post-stall recovery probability", "Nadella revived Microsoft in 4 years"),
        ],
        "sections_cn": [
            {
                "num": 1, "tag": "三部曲",
                "title": "破界创新三部曲：不在内容上做功，在结构上做功",
                "desc": "<strong>破界创新是真正意义上的颠覆式创新。</strong>第一性原理支撑了理性系统，也同时禁锢了它的边界——它是系统最大的确定性，也是最脆弱之处，是真正的阿喀琉斯之踵。打破系统边界的最直接方式，就是将作为基石假设的第一性原理击碎。<br><br>三部曲：<strong>①"破"隐含假设</strong>——用哲学思维跳出系统，发现并打破那个默认的群体信念；<strong>②"立"基石假设</strong>——重构一个比原有层次更深、强度更大的新第一性原理（通常来自基础学科）；<strong>③"见"全新系统</strong>——在新基石上通过公理化方法演绎出新系统，新边界自然涌现。<br><br>关键洞见：破界创新不在内容上做功，而在结构上做功，在看不见的地方做功。这不是努力勤奋的事，而是一种认知、一种智慧。",
                "desc_en": "<strong>Boundary-breaking innovation is truly disruptive innovation.</strong> The First Principle supports the rational system but also imprisons its boundary—it is the system's greatest certainty yet also its greatest vulnerability, the true Achilles' heel. Shatter the foundational First Principle, and the building above collapses.<br><br>The 3 steps: <strong>① 'Break' the hidden assumption</strong>—use philosophical thinking to leap outside the system, identify and shatter the default group belief; <strong>② 'Build' a new foundational axiom</strong>—reconstruct a deeper, stronger new First Principle (typically from fundamental disciplines); <strong>③ 'Envision' a new system</strong>—on the new foundation, use axiomatic methods to deduce a new system, with boundaries emerging naturally.<br><br>Key insight: boundary-breaking innovation operates on structure, not content—it works in the invisible. It's not about effort or diligence; it's about cognition and wisdom.",
                "flow_cn": ["识别\n隐含假设", "打破旧\n第一性原理", "重构更深\n基石假设", "新系统\n自然涌现"],
                "flow_en": ["Identify\nhidden assumption", "Shatter old\nFirst Principle", "Rebuild deeper\nfoundational axiom", "New system\nnaturally emerges"],
                "flow_end_cn": "旧问题变得无关紧要",
                "flow_end_en": "Old problems become irrelevant",
            },
            {
                "num": 2, "tag": "认知囚徒",
                "title": "破界创新的难点：群体信念是最危险的隐含假设",
                "desc": "<strong>最常见的隐含假设就是群体信念。</strong>当某种共识深入人心变成常识时，人们根本不会甚至忘了去质疑它。这与人类的基因相关——原始社会不合群的个体面临死亡，因此听从群体认知的惯习刻在基因里。赫拉利指出，人类之所以主宰地球，靠的是"一起想象"虚构故事的能力——宗教、纸币均仰赖于这种集体想象。所以，破界创新的关键和难点在于：发现并打破群体信念。与禅修类似，当"看"到隐含假设时，我们就"开始"打破它了。质疑群体性共识，敢于打破群体信念，这是破除隐含假设的根本方法。",
                "desc_en": "<strong>The most common hidden assumption is the group belief.</strong> When a consensus becomes deeply internalized as common sense, people never—or forget to—question it. This is wired into human genes: in primitive societies, non-conforming individuals faced death, so the habit of following group cognition is genetically embedded. Harari argues that humans dominate Earth through the ability to 'imagine together' fictional stories—religion and fiat currency depend on this collective imagination. Thus, the key and difficulty of boundary-breaking innovation is: discover and shatter group beliefs. Like Zen practice, when you 'see' the hidden assumption, you have already 'begun' breaking it. Question group consensus; dare to shatter group beliefs—this is the fundamental method.",
                "dual_cn": [
                    ("🧬", "基因根源", "原始社会缺乏抵御天灾和野兽的手段，不合群的人面临死亡。听从群体认知的习性深深烙印在人类基因中——这是进化的遗产，也是创新的枷锁。"),
                    ("📖", "虚构的力量", "赫拉利《人类简史》：虚构的重点不只在于想象，更在于"一起"想象。宗教、纸币、公司、国家——都是人类集体编织的虚构故事，却成了真理。"),
                ],
                "dual_en": [
                    ("🧬", "Genetic Roots", "Primitive societies lacked defenses against disasters and beasts; non-conforming individuals faced death. The habit of following group cognition is deeply etched in human genes—an evolutionary legacy that is also the shackle of innovation."),
                    ("📖", "The Power of Fiction", "Harari's Sapiens: the key is not just imagination but 'imagining together.' Religion, fiat money, corporations, nations—all are fictions collectively woven by humanity, yet they became 'truth.'"),
                ],
            },
            {
                "num": 3, "tag": "科学革命",
                "title": "科学领域的破界创新：所有重大科学革命都是范式转换",
                "desc": "<strong>库恩指出：几乎所有真正的科学革命都不是新发现的革命，而是范式转换的革命。</strong>几何学：欧氏几何建立在"平直空间"的隐含假设上。罗巴切夫斯基和黎曼发现这一假设，提出非平直空间，开创了非欧几何——从逻辑角度看这是严谨的，虽然当时无人能验证，但后来爱因斯坦用黎曼几何表达了广义相对论。<br><br>天文学：托勒密（地心说+匀速圆周）→哥白尼（发现旧系统逻辑失洽，提出日心说）→开普勒（打破匀速圆周假设，建立椭圆轨道）——每一次都是"破旧基石→立新基石"。库恩说："只有破坏旧范式才能得到新发现，这是唯一可行的办法。"",
                "desc_en": "<strong>Kuhn demonstrated: almost all genuine scientific revolutions are not revolutions of new discoveries but revolutions of paradigm shifts.</strong> Geometry: Euclidean geometry rested on the hidden assumption of 'flat space.' Lobachevsky and Riemann identified this, proposed non-flat space, and pioneered non-Euclidean geometry—logically rigorous, though empirically unverifiable at the time, until Einstein used Riemannian geometry to express general relativity.<br><br>Astronomy: Ptolemy (geocentrism + uniform circular motion) → Copernicus (identified logical inconsistency in the old system, proposed heliocentrism) → Kepler (shattered the uniform-circular-motion assumption, established elliptical orbits)—each time was 'break old foundation → build new one.' Kuhn: 'Only by destroying the old paradigm can new discoveries be made—this is the only viable approach.'",
                "flow_cn": ["欧氏几何\n平直空间→5公设", "罗巴切夫斯基\n打破平直空间假设", "黎曼\n椭圆几何", "爱因斯坦\n弯曲时空→广义相对论"],
                "flow_en": ["Euclidean Geometry\nFlat space → 5 postulates", "Lobachevsky\nShatter flat-space assumption", "Riemann\nElliptic geometry", "Einstein\nCurved spacetime → General relativity"],
                "flow_end_cn": "范式转换\n革命而非继承",
                "flow_end_en": "Paradigm Shift\nRevolution, not inheritance",
            },
            {
                "num": 4, "tag": "商业实战",
                "title": "IBM和乔布斯的破界创新：从科研计算机到每个家庭一台电脑",
                "desc": "<strong>破界创新在计算机行业的完整演绎。</strong>优尼瓦克/IBM最初隐含假设：计算机只用于科研→IBM打破它，重构"企业市场潜力巨大"，成为大型商用机霸主。<br><br>DEC打破IBM"只有大企业需要计算机"的假设，重构"小公司也需要"，成为小型机之王。但DEC随后被自己的隐含假设"计算机只用于商业机构"禁锢，与PC时代擦肩而过。<br><br>乔布斯打破DEC的假设，重构"每个家庭都可以拥有一台计算机"，Apple-1定价$1295（仅为DEC的1/10），开辟PC时代。更惊艳的是产品层面：iPod Shuffle去掉屏幕（随机播放），iPod去掉开关键，iPhone用触摸屏取代键盘——每一次都是"识别隐含假设→重构基石→定义新品类"。",
                "desc_en": "<strong>The complete saga of boundary-breaking innovation in the computer industry.</strong> UNIVAC/IBM's initial hidden assumption: computers are only for scientific research → IBM broke it, rebuilt 'enterprise market has huge potential,' becoming the mainframe king.<br><br>DEC broke IBM's 'only large enterprises need computers' assumption, rebuilt 'small companies need them too,' became the minicomputer king. But DEC was then imprisoned by its own hidden assumption 'computers are only for business,' missing the PC era.<br><br>Jobs broke DEC's assumption, rebuilt 'every family can have a computer,' Apple-1 priced at $1,295 (1/10 of DEC's), opening the PC era. Even more stunning at the product level: iPod Shuffle removed the screen (random play), iPod removed the power switch, iPhone replaced the keyboard with a touchscreen—each time: 'identify hidden assumption → reconstruct foundation → define a new category.'",
                "flow_cn": ["优尼瓦克→IBM\n科研→商用", "DEC\n大企业→小企业", "苹果\n企业→每个家庭", "iPhone\n键盘→触摸屏"],
                "flow_en": ["UNIVAC→IBM\nScience→Business", "DEC\nLarge→Small business", "Apple\nBusiness→Every home", "iPhone\nKeyboard→Touchscreen"],
                "flow_end_cn": "破界创新\n让旧问题无关紧要",
                "flow_end_en": "Boundary-Breaking\nOld problems irrelevant",
            },
            {
                "num": 5, "tag": "创新者思维",
                "title": "成为创新企业家：解题家vs理论家，做让旧问题无关紧要的人",
                "desc": "<strong>数学家分为两类：解题家与理论家。理论家最荣耀的时刻是发现新理论，它不能解决任何老问题，却使它们变得无关紧要。</strong>创业者也一样。普通创业者解决极限点问题（针对问题解决问题），创新创业家解决边界问题（破界创新）。福特没有解决马车的问题，但汽车让马车的问题无关紧要；乔布斯没有解决功能手机的问题；马斯克没有解决传统汽车的问题；张小龙没有解决PC即时通信的问题；张一鸣没有解决门户新闻的问题——他们都是让旧问题无关紧要的人。第二曲线的本质不是解决第一曲线的极限点，而是构建一个新系统让它变得无关紧要。破界创新是混沌大学创新模型之王。",
                "desc_en": "<strong>Mathematicians divide into two types: problem-solvers and theorists. The theorist's greatest moment is discovering a new theory—it solves NO old problems, but renders them irrelevant.</strong> Same for entrepreneurs. Ordinary entrepreneurs solve limit-point problems (solving problems within problems); innovative entrepreneurs solve boundary problems (boundary-breaking innovation). Ford didn't solve the carriage problem—the automobile made it irrelevant. Jobs didn't solve the feature-phone problem. Musk didn't solve the traditional-car problem. Zhang Xiaolong didn't solve PC instant-messaging problems. Zhang Yiming didn't solve portal-news problems—they all made old problems irrelevant. The essence of the second curve is not solving the first curve's limit point but building a new system that renders it irrelevant. Boundary-breaking innovation is Hundun University's crown jewel innovation model.",
                "data_cn": [
                    ("🚗", "福特", "没有解决马车的问题，但汽车让马车变得无关紧要。"),
                    ("📱", "乔布斯", "没有解决功能手机的问题，但iPhone让功能手机变得无关紧要。"),
                    ("🚀", "马斯克", "没有解决传统汽车的问题，但特斯拉让燃油车问题变得无关紧要。"),
                ],
                "data_en": [
                    ("🚗", "Ford", "Didn't solve the carriage problem—the automobile made it irrelevant."),
                    ("📱", "Jobs", "Didn't solve the feature-phone problem—the iPhone made it irrelevant."),
                    ("🚀", "Musk", "Didn't solve the combustion-car problem—Tesla made it irrelevant."),
                ],
            },
        ],
        "takeaway_cn": (
            "破界创新是"由内而外"的创新——打破内在认知边界，引起外在现实变化。"
            "不要在内容上做功，要在结构上做功。不要问"怎么解决这个问题"，要问"这个问题基于什么隐含假设"。"
            "打破那个假设，旧问题会变得无关紧要。我们不是生活在客观世界中，而是生活在思想家为我们打造的思想世界中——打破它，你就自由了。"
        ),
        "takeaway_en": (
            "Boundary-breaking innovation is 'inside-out' innovation—shatter inner cognitive boundaries, trigger outer reality changes. "
            "Work on structure, not content. Don't ask 'how to solve this problem'—ask 'what hidden assumption does this problem rest on?' "
            "Break that assumption, and the old problem becomes irrelevant. We don't live in an objective world but in the thought-world built for us by thinkers—break it, and you are free."
        ),
    },
    4: {
        "cn_num": "四",
        "en_num": "4",
        "cn_title": "组织刷新：使命—战略的破界创新",
        "en_title": "Organizational Refresh: Mission-Strategy Boundary-Breaking Innovation",
        "overview_cn": (
            "本章通过微软CEO纳德拉的案例，完整呈现破界创新在组织层面的应用。"
            "鲍尔默时代微软固守"PC时代"的隐含假设，错过搜索、社交、移动、云四次浪潮，市值腰斩。"
            "纳德拉上任后，以"重新发现微软灵魂"的哲学追问，找到盖茨创立微软的第一性原理——"为他人赋能"。"
            "由此刷新使命（从"每桌一台PC"到"赋能全球每一人每一组织"）→刷新文化（从固化型思维到成长型思维）"
            "→刷新战略（移动为先、云为先，大胆去Windows化）。结果：市值从$3017亿（2014年）飙至$1.21万亿（2020年）。"
            "战略变革不是从内容着手，而是从结构着手——刷新使命，新战略自然涌现。"
        ),
        "overview_en": (
            "This chapter demonstrates boundary-breaking innovation at the organizational level through Nadella's Microsoft transformation. "
            "Under Ballmer, Microsoft clung to the 'PC era' hidden assumption, missing search, social, mobile, and cloud waves—market cap halved. "
            "Nadella, upon becoming CEO, used philosophical inquiry to 'rediscover Microsoft's soul,' finding Gates' founding First Principle: 'empowering others.' "
            "He refreshed the mission (from 'a PC on every desk' to 'empower every person and organization on the planet') → "
            "refreshed culture (from fixed mindset to growth mindset) → refreshed strategy (mobile-first, cloud-first, boldly de-Windowsizing). "
            "Result: market cap soared from $301.7B (2014) to $1.21T (2020). "
            "Strategic transformation doesn't start with content—it starts with structure. Refresh the mission, and a new strategy naturally emerges."
        ),
        "subtitle_cn": "重新发现灵魂→刷新使命→刷新文化→刷新战略 · Windows既是光环也是枷锁 · 大象起舞，重回巅峰",
        "subtitle_en": "Rediscover the soul → Refresh mission → Refresh culture → Refresh strategy · Windows is both halo and shackle · The elephant dances back to the top",
        "kpis_cn": [
            ("$6000亿", "", "2000年微软市值·全球第一", "盖茨功成身退，鲍尔默接任"),
            ("$3017亿", "", "2014年纳德拉接任时市值", "营收回升但市值腰斩"),
            ("$8512亿", "", "2018年市值·超越苹果重返第一", "4年刷新，大象起舞"),
            ("$1.21万亿", "", "2020年市值", "云服务收入占比从5%→20%+"),
        ],
        "kpis_en": [
            ("$600B", "", "2000 MSFT market cap · #1 globally", "Gates retires, Ballmer takes over"),
            ("$301.7B", "", "2014 Nadella takes over · market cap", "Revenue up but market cap halved"),
            ("$851.2B", "", "2018 market cap · surpasses Apple back to #1", "4-year refresh, the elephant dances"),
            ("$1.21T", "", "2020 market cap", "Cloud revenue from 5% → 20%+"),
        ],
        "sections_cn": [
            {
                "num": 1, "tag": "帝国迷失",
                "title": "鲍尔默时代的迷失：成于第一曲线，失于第二曲线",
                "desc": "<strong>盖茨1976年使命：让每个家庭、每张办公桌上都有一台个人计算机。</strong>这个使命驱动微软在前15年成为全球第一。2000年微软市值$6000亿，全球第一，盖茨功成身退。鲍尔默接任后：营收增长4倍（$778亿），利润增长10倍（$267亿），Windows占据PC端90%+市场份额，毛利率75%——但市值却下降近一半。<br><br>原因：微软错过了四次浪潮——搜索引擎（谷歌崛起）、互联网社交（Facebook崛起）、移动互联网（智能机OS份额仅1%）、云计算（亚马逊领先）。Windows既是微软的"长子"，却成了"独子"，扼杀了其他所有可能性。微软从未被竞争对手打败，而是被自己的隐含假设——PC时代的第一性原理——禁锢。到2013年鲍尔默仍宣称"在微软没有什么比Windows更重-要。"",
                "desc_en": "<strong>Gates' 1976 mission: a PC on every desk, in every home.</strong> This drove Microsoft to become #1 globally in its first 15 years. In 2000, market cap hit $600B, #1 globally; Gates retired. Under Ballmer: revenue grew 4x ($77.8B), profit 10x ($26.7B), Windows held 90%+ PC market share, 75% gross margin—yet market cap dropped nearly 50%.<br><br>Why: Microsoft missed four waves—search engines (Google rose), social networking (Facebook rose), mobile internet (smartphone OS share only 1%), cloud computing (Amazon led). Windows was Microsoft's 'first-born' but became the 'only child,' strangling all other possibilities. Microsoft was never defeated by competitors—it was imprisoned by its own hidden assumption: the PC-era First Principle. As late as 2013, Ballmer still declared 'Nothing at Microsoft is more important than Windows.'",
                "data_cn": [
                    ("📈", "鲍尔默的功绩", "营收4倍→$778亿；利润10倍→$267亿；员工3倍→近10万人。Windows占PC操作系统90%+市场份额。"),
                    ("📉", "错过的浪潮", "搜索引擎（谷歌）、社交网络（Facebook）、移动互联网（手机OS仅1%）、云计算（亚马逊AWS领先）——四次浪潮全部错过。"),
                    ("🔒", "隐含假设", "PC时代=微软的一切。Windows从"长子"变成"独子"——它扼杀了其他"孩子"的出生权利。创始人的认知边界=企业的发展边界。"),
                ],
                "data_en": [
                    ("📈", "Ballmer's Achievements", "Revenue 4x→$77.8B; Profit 10x→$26.7B; Staff 3x→~100K. Windows held 90%+ PC OS market share."),
                    ("📉", "Missed Waves", "Search (Google), Social (Facebook), Mobile (smartphone OS only 1%), Cloud (Amazon AWS led)—all four waves missed."),
                    ("🔒", "Hidden Assumption", "PC era = Everything for Microsoft. Windows went from 'first-born' to 'only child'—strangling all other 'children.' Founder's cognitive boundary = enterprise's development boundary."),
                ],
            },
            {
                "num": 2, "tag": "刷新奇迹",
                "title": "纳德拉刷新微软：4年把一个渐趋失速的巨人拉回巅峰",
                "desc": "<strong>企业一旦到达失速点，恢复增长引擎的可能性只有4%。</strong>纳德拉2014年接任CEO时，微软无比接近失速点。他深刻理解熵增定律——任何组织都趋向于混乱无序，必须主动"刷新"系统。<br><br>他的"刷新"本质就是第二曲线创新：从第一曲线（PC+Windows为中心）跳到第二曲线（云+移动+赋能）。关键在于他不是从战略内容着手，而是从结构着手——先刷新使命（打破旧隐含假设），再刷新文化（改变思维模式），最后刷新战略（自然涌现）。微软的旧使命"每桌一台PC"在20世纪90年代末已基本实现，完成后反而成了发展的禁锢。纳德拉通过追问"盖茨为什么创办微软"找到背后精神：为他人赋能。",
                "desc_en": "<strong>Once a company hits the stall point, the probability of restoring the growth engine is only 4%.</strong> When Nadella took over as CEO in 2014, Microsoft was dangerously close to the stall point. He deeply understood entropy—any organization trends toward chaos and must actively 'refresh' its system.<br><br>His 'refresh' is essentially second-curve innovation: jumping from curve one (PC+Windows-centric) to curve two (cloud + mobile + empowerment). Crucially, he didn't start with strategic content but with structure—first refreshing the mission (breaking the old hidden assumption), then refreshing the culture (changing the mindset), and finally refreshing the strategy (which emerged naturally). Microsoft's old mission 'a PC on every desk' was largely achieved by the late 1990s; once fulfilled, it became a shackle on development. Nadella traced 'Why did Gates found Microsoft?' to its spiritual core: empowering others.",
                "flow_cn": ["阶段一\n刷新使命", "阶段二\n刷新文化", "阶段三\n刷新战略", "结果\n市值重返第一"],
                "flow_en": ["Phase 1\nRefresh Mission", "Phase 2\nRefresh Culture", "Phase 3\nRefresh Strategy", "Result\nMarket cap #1 again"],
                "flow_end_cn": "$3017亿→$1.21万亿",
                "flow_end_en": "$301.7B→$1.21T",
            },
            {
                "num": 3, "tag": "使命刷新",
                "title": "刷新使命：重新发现微软的灵魂——"为他人赋能"",
                "desc": "<strong>纳德拉的刷新不是从内容着手，而是从结构着手——这是整个变革中最亮眼的地方。</strong>他追问：盖茨为什么提出"每桌一台PC"？背后精神是什么？通过灵魂拷问，纳德拉找到答案：为他人赋能（to empower others）。<br><br>由此推导出新使命：<strong>赋能全球每一人、每一个组织，帮助他们成就不凡。</strong>关键词从"PC"和"每桌"变成了"赋能"和"帮助"。纳德拉说："我说的不是宗教意义上的灵魂，而是一种最自然的、表露内心的声音。我们必须回答：这家公司是做什么的，我们为什么而存在？"使命不是宣传口号，而是一家公司的战略起点和支撑点。旧战略基于旧使命，刷新使命后新战略自然涌现。",
                "desc_en": "<strong>Nadella's refresh didn't start with content but with structure—the most brilliant aspect of the entire transformation.</strong> He asked: why did Gates propose 'a PC on every desk'? What spirit lay behind it? Through soul-searching, Nadella found the answer: to empower others.<br><br>From this he derived a new mission: <strong>empower every person and every organization on the planet to achieve more.</strong> The keywords shifted from 'PC' and 'every desk' to 'empower' and 'help.' Nadella said: 'I'm not talking about soul in a religious sense but a most natural, innermost voice. We must answer: what does this company do? Why do we exist?' Mission is not a slogan for publicity; it's a company's strategic starting point and pillar. Old strategy rests on old mission; refresh the mission, and a new strategy emerges naturally.",
                "dual_cn": [
                    ("🔄", "旧使命（1976年·盖茨）", "让每个家庭、每张办公桌上都有一台个人计算机。关键词：PC、每个桌上。20世纪90年代末已基本实现→完成后成为禁锢。"),
                    ("✨", "新使命（2014年·纳德拉）", "赋能全球每一人、每一个组织，帮助他们成就不凡。关键词：赋能、帮助。来自盖茨创立微软的第一性原理：为他人赋能。"),
                ],
                "dual_en": [
                    ("🔄", "Old Mission (1976 · Gates)", "A PC on every desk, in every home. Keywords: PC, every desk. Largely achieved by late 1990s→Once fulfilled, became a shackle."),
                    ("✨", "New Mission (2014 · Nadella)", "Empower every person and every organization on the planet to achieve more. Keywords: empower, help. Derived from Gates' founding First Principle: empowering others."),
                ],
            },
            {
                "num": 4, "tag": "文化刷新",
                "title": "刷新文化：从固化型思维到成长型思维——重塑积病已久的文化",
                "desc": "<strong>"文化把战略当早餐吃。"</strong>纳德拉从卡罗尔·德韦克的《终身成长》中汲取灵感：固化型思维认为人的能力天生不变（包括智商），成长型思维相信人的能力可以通过努力提高。他猛然发现微软的文化漏洞——员工必须向所有人证明自己无所不知，是"屋子里最聪明的人"，不能出一点差错。<br><br>纳德拉将文化刷新简化为一句口号：从固化型思维转为成长型思维。作为CEO，他每天检查每个业务决定是否有助于公司转向成长型思维。效果立显：Windows负责人迈尔森将付费升级改为限时免费升级，成就史上最受欢迎的Windows升级（数亿用户）。微软从碾压对手的封闭公司转变为与硅谷交朋友的开放公司——甚至同意雅虎解除必应独家搜索协议，不索取任何补偿。",
                "desc_en": "<strong>'Culture eats strategy for breakfast.'</strong> Nadella drew inspiration from Carol Dweck's Mindset: fixed mindset believes abilities are innate and unchangeable (including IQ); growth mindset believes abilities can be improved through effort. He suddenly saw Microsoft's cultural flaw—employees had to prove to everyone they knew everything, always 'the smartest person in the room,' never making a single mistake.<br><br>Nadella distilled the cultural refresh into one phrase: shift from fixed mindset to growth mindset. As CEO, he checked daily whether every business decision moved toward growth mindset. Results were immediate: Windows chief Myerson switched paid upgrades to free limited-time upgrades—the most popular Windows upgrade in history (hundreds of millions of users). Microsoft transformed from a closed company crushing competitors to an open company befriending Silicon Valley—even agreeing to Yahoo's request to terminate the exclusive Bing search agreement, seeking no compensation.",
                "dual_cn": [
                    ("🔒", "固化型思维", "能力天生不变，包括智商。须证明无所不知、永不出错。逃避风险却期待创新。不同部门打架，收购企业难以存活。看结果，不看过程。"),
                    ("🌱", "成长型思维", "能力可通过努力提高。关注点从"做错了什么"转变为"学到了什么"。从守势变攻势，目标从怕市场萎缩变成赢得数十亿联网设备。看过程，不只看结果。"),
                ],
                "dual_en": [
                    ("🔒", "Fixed Mindset", "Abilities are innate and unchangeable, including IQ. Must prove you know everything, never make a mistake. Avoids risk yet expects innovation. Departments fight, acquisitions can't survive. Focuses on outcomes, not process."),
                    ("🌱", "Growth Mindset", "Abilities can improve through effort. Focus shifts from 'what went wrong' to 'what did we learn.' From defensive to offensive posture, from fearing shrinking markets to winning billions of connected devices. Focuses on process, not just outcomes."),
                ],
            },
            {
                "num": 5, "tag": "战略刷新",
                "title": "刷新战略：移动为先、云为先——去掉"Windows"这个光环和枷锁",
                "desc": "<strong>使命刷新→文化刷新→战略自然涌现：移动为先、云为先。</strong>移动为先：打破"Office只能在Windows PC上运行"的隐含假设。Office推广到iOS和安卓（100+款iOS应用），纳德拉甚至用iPhone演示微软软件。Windows手机OS授权费取消，所有厂商免费使用。微软从封闭走向开放。<br><br>云为先：纳德拉力排众议，将重点从收入庞大的服务器工具业务转向微不足道的Azure云。他从大客户入手，提供混合云、智能云等差异化方案。他投入几十亿美元/年，$75亿收购GitHub聚拢开发者，$262亿收购LinkedIn引商业用户上云。2018年云收入$200亿（占比20%+），替代Windows成为真正的第二曲线。他甚至将Windows部门分拆——Windows这个名字在微软内部消失了。纳德拉说："Windows既是光环也是枷锁，卸下它才能走得更远。"",
                "desc_en": "<strong>Mission refreshed → Culture refreshed → Strategy emerges naturally: mobile-first, cloud-first.</strong> Mobile-first: broke the hidden assumption that 'Office only runs on Windows PCs.' Office extended to iOS and Android (100+ iOS apps); Nadella even demonstrated Microsoft software using an iPhone. Windows phone OS licensing fees eliminated, free for all manufacturers. Microsoft went from closed to open.<br><br>Cloud-first: against all internal opposition, Nadella shifted focus from the massive server-tools business to the tiny Azure cloud. He targeted large enterprises first, offering differentiated solutions like hybrid cloud and intelligent cloud. He invested tens of billions per year, acquired GitHub for $7.5B to rally developers, LinkedIn for $26.2B to funnel business users to the cloud. By 2018, cloud revenue hit $20B (>20% of total), replacing Windows as the true second curve. He even split the Windows division—the name 'Windows' disappeared inside Microsoft. Nadella said: 'Windows is both a halo and a shackle; only by removing it can we go further.'",
                "data_cn": [
                    ("📱", "移动为先", "Office覆盖iOS/安卓（100+应用），取消Windows手机OS授权费（所有厂商免费），纳德拉用iPhone演示微软软件。"),
                    ("☁️", "云为先", "Azure从几百万美元→$200亿营收。每年投入数十亿，$75亿收购GitHub，$262亿收购LinkedIn。混合云方案从大客户入手。"),
                    ("🪓", "去Windows化", "Windows部门分拆，Windows从微软内部"消失"。2018年云收入占比超20%，成为真正的第二曲线。PC时代→赋能时代。"),
                ],
                "data_en": [
                    ("📱", "Mobile-First", "Office on iOS/Android (100+ apps), Windows phone OS licensing fees eliminated (free for all), Nadella demoed Microsoft software on an iPhone."),
                    ("☁️", "Cloud-First", "Azure from a few million → $20B revenue. Tens of billions invested annually, $7.5B GitHub acquisition, $26.2B LinkedIn acquisition. Hybrid cloud strategy targeting large enterprises."),
                    ("🪓", "De-Windowsizing", "Windows division split, 'Windows' disappeared inside Microsoft. By 2018, cloud revenue >20% of total, becoming the true second curve. PC era → Empowerment era."),
                ],
            },
        ],
        "takeaway_cn": (
            "卓有成效的战略变革，不是从内容着手，而是从结构着手。"
            "纳德拉的刷新三部曲——刷新使命、刷新文化、刷新战略——本质就是破界创新在组织层面的完整应用。"
            "任何战略之下都有隐含假设（组织中的表现为使命），打破旧使命→重构新基石→新战略自然涌现。"
            "记住：企业的"灵魂"不是一句口号，而是对"我们为什么而存在"的真诚回答。"
        ),
        "takeaway_en": (
            "Effective strategic transformation doesn't start with content—it starts with structure. "
            "Nadella's 3-step refresh—refresh mission, refresh culture, refresh strategy—is the complete application of boundary-breaking innovation at the organizational level. "
            "Every strategy rests on a hidden assumption (manifested as mission in organizations); break the old mission → reconstruct a new foundation → new strategy emerges naturally. "
            "Remember: a company's 'soul' is not a slogan but a sincere answer to 'Why do we exist?'"
        ),
    },
}


# ── CSS shared across all files ──
CSS = """\
  @font-face {
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
  .container { max-width: 880px; width: 100%; padding: 40px 32px 60px; }

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

  .chapter-overview {
    background: #f8f6f3; border-left: 3px solid #4f46e5; border-radius: 8px;
    padding: 16px 20px; margin: 12px 0 24px; font-size: 14px; color: #555;
    line-height: 1.8; font-family: 'FZXPYZS', 'PingFang SC', serif;
  }
  .chapter-overview p { margin: 0; }

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

  /* KPI */
  .kpi-row { display: grid; gap: 14px; margin: 0 0 18px; }
  .kpi-row.cols-4 { grid-template-columns: repeat(4, 1fr); }
  .kpi-card { border-radius: 12px; padding: 16px 14px; text-align: center; border: 1px solid; }
  .kpi-card.c01 { background: #fef2f2; border-color: #fecaca; }
  .kpi-card.c02 { background: #fff7ed; border-color: #fed7aa; }
  .kpi-card.c03 { background: #fefce8; border-color: #fde68a; }
  .kpi-card.c04 { background: #eef2ff; border-color: #c7d2fe; }
  .kpi-value { font-size: 34px; font-weight: bold; font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif; color: #1a1a1a; line-height: 1.2; }
  .kpi-unit { font-size: 13px; color: #888; font-weight: normal; }
  .kpi-label { font-size: 12px; color: #666; margin-top: 6px; line-height: 1.4; font-family: 'FZXPYZS', 'PingFang SC', serif; }
  .kpi-note { font-size: 11px; color: #aaa; margin-top: 3px; line-height: 1.4; }

  /* Flow */
  .flow-row { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin-top: 6px; }
  .flow-step { background: #fff7ed; border: 1px solid #fed7aa; border-radius: 10px; padding: 10px 12px; text-align: center; min-width: 80px; flex: 1; font-size: 13px; color: #9a3412; line-height: 1.5; font-weight: bold; }
  .flow-arrow { font-size: 20px; color: #ea580c; flex-shrink: 0; font-weight: bold; }
  .flow-step.end { background: #fef2f2; border-color: #fecaca; color: #991b1b; }

  /* Data row */
  .data-row { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin-top: 10px; }
  .data-card { border-radius: 12px; padding: 18px 16px; text-align: center; border: 1px solid #fce7f3; }
  .data-card.d1 { background: #fdf2f8; border-color: #f9a8d4; }
  .data-card.d2 { background: #fdf2f8; border-color: #f9a8d4; }
  .data-card.d3 { background: #fdf2f8; border-color: #f9a8d4; }
  .data-big { font-size: 26px; margin-bottom: 6px; }
  .data-name { font-size: 15px; font-weight: bold; color: #831843; margin-bottom: 6px; font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif; }
  .data-sm { font-size: 12px; color: #9d174d; line-height: 1.6; }

  /* Dual grid */
  .dual-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 10px; }
  .dual-card { border-radius: 12px; padding: 18px 20px; display: flex; gap: 12px; align-items: flex-start; }
  .dual-card.yes { background: #fef2f2; border: 1px solid #fecaca; }
  .dual-card.no  { background: #f0fdf4; border: 1px solid #bbf7d0; }
  .dual-icon { font-size: 24px; flex-shrink: 0; line-height: 1; }
  .dual-text h4 { font-size: 14px; color: #1a1a1a; margin-bottom: 4px; font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif; }
  .dual-text p { font-size: 12px; color: #777; line-height: 1.6; }

  /* Takeaway */
  .takeaway {
    background: #ffffff; border: 1px solid #e8e0d5; border-radius: 14px;
    padding: 24px 32px; margin-bottom: 18px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    border-left: 4px solid #dc2626;
  }
  .takeaway-label { font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif; font-size: 12px; color: #dc2626; letter-spacing: 2px; margin-bottom: 6px; font-weight: bold; }
  .takeaway-text { font-size: 16px; color: #1a1a1a; line-height: 1.9; font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif; }

  /* Footer */
  .footer { text-align: center; margin-top: 32px; padding-top: 20px; border-top: 1px solid #e8e0d5; color: #bbb; font-size: 13px; line-height: 1.8; }

  /* Lang */
  .lang-switch { text-align: right; margin-bottom: 16px; }
  .lang-btn { display: inline-block; padding: 6px 16px; border-radius: 8px; font-size: 13px; text-decoration: none; letter-spacing: 0.03em; font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif; background: #fef2f2; color: #dc2626; border: 1px solid #fecaca; transition: opacity 0.15s; }
  .lang-btn:hover { opacity: 0.75; }

  .back-catalog { text-align: right; margin-bottom: 4px; }
  .back-catalog-btn { display: inline-block; padding: 5px 14px; border-radius: 8px; font-size: 12px; text-decoration: none; letter-spacing: .02em; background: #eef2ff; color: #4f46e5; border: 1px solid #c7d2fe; transition: opacity .15s; }
  .back-catalog-btn:hover { opacity: .75; }

  @media (max-width: 640px) {
    .section { flex-direction: column; align-items: center; text-align: center; border-left: none; border-top: 4px solid transparent; padding-top: 20px; }
    .section-01 { border-top-color: #dc2626; } .section-02 { border-top-color: #ea580c; }
    .section-03 { border-top-color: #ca8a04; } .section-04 { border-top-color: #4f46e5; }
    .section-05 { border-top-color: #db2777; }
    .dual-grid, .data-row { grid-template-columns: 1fr; }
    .flow-row { flex-direction: column; }
    .flow-arrow { transform: rotate(90deg); }
    .container { padding: 0 8px; }
    h1 { font-size: 26px; }
    .kpi-row.cols-4 { grid-template-columns: repeat(2, 1fr); }
    .kpi-value { font-size: 34px; }
  }
  @media (max-width: 400px) {
    .kpi-row.cols-4 { grid-template-columns: 1fr; }
  }
"""


def build_kpi(kpis):
    """Build KPI row HTML. 4 KPIs in 4-column grid."""
    colors = ["c01", "c02", "c03", "c04"]
    cards = []
    for i, (val, unit, label, note) in enumerate(kpis):
        c = colors[i] if i < len(colors) else "c01"
        cards.append(f'''  <div class="kpi-card {c}">
    <div class="kpi-value">{val}<span class="kpi-unit">{unit}</span></div>
    <div class="kpi-label">{label}</div>
    <div class="kpi-note">{note}</div>
  </div>''')
    return '\n'.join(cards)


def build_flow(steps, end_step):
    """Build flow row HTML."""
    items = []
    for i, step in enumerate(steps):
        items.append(f'      <div class="flow-step">{step}</div>')
        if i < len(steps) - 1:
            items.append('      <div class="flow-arrow">→</div>')
    items.append(f'      <div class="flow-arrow">→</div>')
    items.append(f'      <div class="flow-step end">{end_step}</div>')
    return '\n'.join(items)


def build_section(s, lang):
    """Build a single section HTML block."""
    n = s["num"]
    tag_text = s["tag"]
    title_text = s["title"]
    desc_text = s["desc_en"] if lang == "en" else s["desc"]
    tag_class = f"tag tag-{n:02d}"
    title_class = f"t-{n:02d}"
    section_class = f"section section-{n:02d}"
    num_class = f"section-num num-{n:02d}"

    inner = ""
    # Determine which substructure to render
    if "flow_cn" in s:\n        flow_steps = s["flow_en"] if lang == "en" else s["flow_cn"]
        flow_end = s["flow_end_en"] if lang == "en" else s["flow_end_cn"]
        inner = build_flow(flow_steps, flow_end)
    elif "dual_cn" in s:\n        duals = s["dual_en"] if lang == "en" else s["dual_cn"]
        cards = []
        for icon, h4_text, p_text in duals:
            cls = "no" if cards else "yes"
            cards.append(f'''      <div class="dual-card {cls}">
        <div class="dual-icon">{icon}</div>
        <div class="dual-text">
          <h4>{h4_text}</h4>
          <p>{p_text}</p>
        </div>
      </div>''')
        inner = '\n'.join(cards)
    elif "data_cn" in s:\n        datas = s["data_en"] if lang == "en" else s["data_cn"]
        cards = []
        classes = ["d1", "d2", "d3"]
        for i, (icon, name, text) in enumerate(datas):
            c = classes[i] if i < len(classes) else "d1"
            cards.append(f'''      <div class="data-card {c}">
        <div class="data-big">{icon}</div>
        <div class="data-name">{name}</div>
        <div class="data-sm">{text}</div>
      </div>''')
        inner = '\n'.join(cards)

    return f'''<!-- {n:02d}: {tag_text} -->
<div class="{section_class}">
  <div class="{num_class}">{n:02d}</div>
  <div class="section-body">
    <div class="{tag_class}">{tag_text}</div>
    <div class="section-title {title_class}">{title_text}</div>
    <div class="section-desc">{desc_text}</div>
{inner_to_rows(inner)}
  </div>
</div>'''


def inner_to_rows(inner):
    """Wrap inner content in appropriate row container."""
    if inner.startswith('      <div class="flow-step">'):
        return f'    <div class="flow-row">\n{inner}\n    </div>'
    elif inner.startswith('      <div class="dual-card'):
        return f'    <div class="dual-grid">\n{inner}\n    </div>'
    elif inner.startswith('      <div class="data-card'):
        return f'    <div class="data-row">\n{inner}\n    </div>'
    return inner


def build_html(ch_num, lang, ch):
    """Build complete HTML for one chapter, one language."""
    is_zh = lang == "zh"
    lang_attr = "zh-CN" if is_zh else "en"
    
    if is_zh:
        title = f"{BOOK_SLUG} · 第{ch['cn_num']}章「{ch['cn_title']}」"
        h1_text = f"{BOOK_SLUG} · 第{ch['cn_num']}章「{ch['cn_title']}」"
        subtitle = ch["subtitle_cn"]
        overview = ch["overview_cn"]
        kpis = ch["kpis_cn"]
        sections = ch["sections_cn"]
        takeaway = ch["takeaway_cn"]
        footer_text = f"《{BOOK_SLUG}》第{ch['cn_num']}章信息图 · 作者：{AUTHOR} · 基于章节内容提炼 · 仅供学习参考"
        lang_label = "中文 / English"
        other_href = f"{BOOK_SLUG}-ch{ch_num:03d}-info-en.html"
        catalog_label = "← 返回章节目录"
        tag_label = "核心结论"
    else:
        title = f"{BOOK_EN} · Ch{ch['en_num']} \"{ch['en_title']}\""
        h1_text = f"{BOOK_EN} · Ch{ch['en_num']}「{ch['en_title']}」"
        subtitle = ch["subtitle_en"]
        overview = ch["overview_en"]
        kpis = ch["kpis_en"]
        sections = ch["sections"]
        takeaway = ch["takeaway_en"]
        footer_text = f"{BOOK_EN} · Ch{ch['en_num']} Infographic · By {AUTHOR_EN} · Based on chapter content · For study reference only"
        lang_label = "English / 中文"
        other_href = f"{BOOK_SLUG}-ch{ch_num:03d}-info-zh.html"
        catalog_label = "← Back to Chapter Catalog"
        tag_label = "🔑 Key Takeaway"

    sections_html = '\n\n'.join(build_section(sec, lang) for sec in sections)

    return f'''<!DOCTYPE html>
<html lang="{lang_attr}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
{CSS}</style>
</head>
<body>
<div class="container">
<div class="back-catalog"><a class="back-catalog-btn" href="{CATALOG_FILE}">{catalog_label}</a></div>
<div class="lang-switch">
  <a class="lang-btn" target="_blank" href="{other_href}">{lang_label}</a>
</div>

<h1>{h1_text}</h1>
<p class="subtitle">{subtitle}</p>
<div class="divider"></div>
<div class="chapter-overview">
  <p>{overview}</p>
</div>

<!-- KPI -->
<div class="kpi-row cols-4">
{build_kpi(kpis)}
</div>

{sections_html}

<div class="takeaway">
  <div class="takeaway-label">{tag_label}</div>
  <div class="takeaway-text">{takeaway}</div>
</div>

<div class="footer">
  {footer_text}
</div>
</div>
</body>
</html>'''


# ── Generate all 8 files ──
def main():
    os.makedirs(OUTDIR, exist_ok=True)
    generated = []
    for ch_num in range(1, 5):
        ch = CHAPTERS[ch_num]
        for lang in ("zh", "en"):
            fname = f"{BOOK_SLUG}-ch{ch_num:03d}-info-{lang}.html"
            fpath = os.path.join(OUTDIR, fname)
            html = build_html(ch_num, lang, ch)
            with open(fpath, "w", encoding="utf-8") as f:\n                f.write(html)\n            size = os.path.getsize(fpath)\n            generated.append((fname, size))\n            print(f"✅ {fname}  ({size:,} bytes)")
    
    print(f"\n📊 Generated {len(generated)} files")
    return generated


if __name__ == "__main__":
    main()