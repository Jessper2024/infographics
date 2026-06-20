#!/usr/bin/env python3
import os

BOOKDIR = os.path.expanduser("~/.openclaw/workspace/infographics/books")
SLUG = "chu-han-shuang-xiong"
BOOK_TITLE_ZH = "楚汉双雄"
BOOK_TITLE_EN = "The Chu-Han Contention: Heroes of Two Sides"
AUTHOR_ZH = "渤海小吏"
AUTHOR_EN = "Bohai Xiaoli"

# Chapter metadata
chapters = {
    1: {
        "title_zh": "揭竿大泽乡：秦为什么会「崩」",
        "title_en": "Uprising at Daze: Why the Qin Empire Collapsed",
        "subtitle_zh": "从郡县制到书同文，从驰道长城到大泽乡起义——解析中国第一个大一统帝国崩溃的深层逻辑",
        "subtitle_en": "From the prefecture-county system to standardized writing, from expressways to the Great Wall — decoding the collapse of China's first unified empire",
        "overview_zh": "公元前221年，秦始皇统一六国，开创中国历史上第一个大一统帝国。然而短短十余年后，陈胜、吴广在大泽乡的振臂一呼便让这个庞大的帝国土崩瓦解。本章深度剖析嬴政在统一后面临的千古难题：郡县还是分封？如何让六国人民认同「秦国人」这一身份？书同文、车同轨、统一度量衡这三大奠基工程背后隐藏着怎样的统治智慧？驰道与长城的修建如何透支了帝国国力？焚书坑儒的历史真相究竟如何？最终，两个戍卒屯长的一念之差，引爆了压死骆驼的最后一根稻草。",
        "overview_en": "In 221 BC, Qin Shi Huang unified the six warring states, creating China's first unified empire. Yet barely a decade later, a revolt at Daze Township by two conscripts brought the mighty empire crashing down. This chapter dissects the existential dilemmas facing the First Emperor after unification: a county system or feudal enfeoffment? How to forge a unified 'Qin' identity among six conquered peoples? What governing wisdom lies behind the three foundational projects — standardized writing, uniform axles, and unified measurements? How did the expressway system and Great Wall fatally overstretch imperial resources? What is the historical truth behind 'book burning and scholar burying'? Finally, the fateful decision of two garrison officers triggered the last straw that broke the empire's back.",
        "kpi": [
            {"label_zh": "统一六国用时", "value_zh": "10年", "label_en": "Time to Unify Six States", "value_en": "10 Years"},
            {"label_zh": "郡县制延续", "value_zh": "2000+年", "label_en": "County System Lasted", "value_en": "2000+ Years"},
            {"label_zh": "驰道总里程", "value_zh": "~6800km", "label_en": "Expressway Network", "value_en": "~6,800 km"},
            {"label_zh": "始皇帝功业", "value_zh": "万古一帝", "label_en": "Legacy Rank", "value_en": "Unprecedented"},
        ],
        "sections_zh": [
            {
                "tag": "制度抉择",
                "title": "郡县 vs 分封：秦始皇的千古难题",
                "desc": "丞相王琯建议分封诸子镇守远方，廷尉李斯力主郡县制集权中央。秦始皇顶着巨大压力选择了从未有人走过的道路——废分封、行郡县，将天下权力收归中央。这个决定为中国奠定了「天下一统」的政治基因，从此「分久必合」成为华夏大地不可撼动的信仰。",
                "component": "dual",
                "dual_yes": {"h4": "郡县制（采纳）", "p": "分钱不分权，税赋可重赏宗室功臣，全国无抗衡中央的力量。为后世两千年奠定大一统框架。"},
                "dual_no": {"h4": "分封制（否决）", "p": "周朝分封同姓子弟，几代人后血脉稀释、刀兵相向，周天子无力阻止。历史已证明此路不通。"},
            },
            {
                "tag": "三大奠基",
                "title": "书同文·车同轨·统一度量衡",
                "desc": "统一文字让跨越千里的政令畅通无阻，小篆成为官方规范文字；「车同轨」规定两轮一律六尺，使全国驰道网成为可能；统一度量衡则为官僚系统的考核与赋税奠定了技术基础。这三项工程看似技术细节，实则是庞大帝国运转的底层操作系统。",
                "component": "flow",
                "flow_steps": ["书同文：统一小篆", "车同轨：标准化道路", "统一度量衡", "官僚系统运转", "帝国机器成型"],
            },
            {
                "tag": "帝国负担",
                "title": "驰道与长城：大工程的两面性",
                "desc": "驰道系统连通全国，南征百越、北逐匈奴，看似无往不利。但每一项伟大工程背后都是天文数字的人力物力消耗。嬴政试图在有生之年完成所有伟业，却忽略了「把一辈子的饭用一辈子的时间去吃」这一朴素道理。帝国的消化能力，追不上始皇帝的雄心。",
                "component": "risk",
                "risk_items": [
                    {"label": "驰道建设", "fill": 85},
                    {"label": "长城修筑", "fill": 90},
                    {"label": "南征百越", "fill": 75},
                    {"label": "陵墓阿房宫", "fill": 95},
                ],
            },
            {
                "tag": "文化真相",
                "title": "焚书坑儒的真相",
                "desc": "秦始皇从未「焚书」，而是禁书——所有典籍藏于国家图书馆，供指定学者研究。真正焚书的是项羽。秦始皇埋的不是「儒」，而是欺骗他求仙的方士。司马迁为警醒后来者汉武帝，将「诸生皆诵法孔子」写入《史记》。历史的层累效应，让真相变得面目全非。",
                "component": "dual",
                "dual_yes": {"h4": "历史真相", "p": "禁书而非焚书，典籍藏于皇家图书馆。坑杀的是诈骗求仙的方士，而非儒生。统一的目的是思想整合。"},
                "dual_no": {"h4": "流行误解", "p": "烧毁全部典籍、活埋儒生。这一形象的塑造受到《史记》文学手法和后世话语建构的深刻影响。"},
            },
            {
                "tag": "崩溃引爆",
                "title": "大泽乡：压死骆驼的最后一根稻草",
                "desc": "两名戍卒屯长陈胜、吴广，因大雨误期面临杀头，一句「王侯将相，宁有种乎」点燃了燎原之火。但他们只是引爆点——真正的火药是六国旧贵族的复国渴望、广大百姓的疲惫不堪、以及秦制对「大有大的难处」的忽视。秦始皇留给了胡亥一个需要高超驾驭技术的庞大机器，而胡亥显然不是那个合格的驾驶员。",
                "component": "data",
                "data_items": [
                    {"big": "900", "name": "戍卒人数", "sm": "最初在大泽乡起义的人数"},
                    {"big": "2月", "name": "攻入函谷关", "sm": "从起义到周文大军打到咸阳郊外"},
                    {"big": "6国", "name": "同时复国", "sm": "起义后六国旧贵族纷纷响应复国"},
                ],
            },
        ],
        "sections_en": [
            {
                "tag": "Institutional Choice",
                "title": "Counties vs. Feudalism: The First Emperor's Dilemma",
                "desc": "Chancellor Wang Wan proposed enfeoffing imperial sons to govern distant territories, while Chief Justice Li Si championed the county system to centralize power. Qin Shi Huang, under immense pressure, chose a path no one had ever walked — abolishing feudalism and implementing counties, concentrating all power in the central government. This decision implanted the political DNA of 'unity under heaven' in China, making 'unity after division' an unshakeable belief across the land.",
                "component": "dual",
                "dual_yes": {"h4": "County System (Adopted)", "p": "Distribute wealth not power; reward clansmen through taxation without creating rival power centers. Established the framework for two millennia of unified rule."},
                "dual_no": {"h4": "Feudal Enfeoffment (Rejected)", "p": "The Zhou dynasty enfeoffed kinsmen, but after generations of bloodline dilution, they turned on each other. The Zhou king was powerless to stop it. History proved this path untenable."},
            },
            {
                "tag": "Three Cornerstones",
                "title": "Standardized Writing, Uniform Axles, Unified Measurements",
                "desc": "Standardizing writing enabled imperial decrees to travel unimpeded across thousands of miles, with Small Seal Script becoming the official form. 'Uniform axles' mandated all wheel spacing to be six chi, enabling a nationwide expressway network. Unifying measurements provided the technical foundation for bureaucratic assessment and taxation. These three projects, seemingly technical details, were in fact the operating system upon which the vast empire ran.",
                "component": "flow",
                "flow_steps": ["Standardize Writing", "Uniform Axles & Roads", "Unify Measurements", "Bureaucracy Functions", "Empire Machine Forms"],
            },
            {
                "tag": "Imperial Overstretch",
                "title": "Expressways and the Great Wall: The Dual Nature of Grand Projects",
                "desc": "The expressway network connected the realm; southern campaigns subdued the Hundred Yue; northern expeditions drove back the Xiongnu — all seemingly unstoppable. But behind every grand project lay astronomical human and material costs. Qin Shi Huang tried to accomplish all great deeds within a single lifetime, neglecting the simple truth of 'eat a lifetime's worth of meals over a lifetime.' The empire's digestive capacity could not keep pace with the First Emperor's ambition.",
                "component": "risk",
                "risk_items": [
                    {"label": "Expressway Construction", "fill": 85},
                    {"label": "Great Wall Construction", "fill": 90},
                    {"label": "Southern Campaigns", "fill": 75},
                    {"label": "Mausoleum & Epang Palace", "fill": 95},
                ],
            },
            {
                "tag": "Historical Truth",
                "title": "The Truth Behind 'Book Burning and Scholar Burying'",
                "desc": "Qin Shi Huang never 'burned books' — he banned them, storing all texts in the imperial library for designated scholars. The real book burner was Xiang Yu. The First Emperor buried not 'Confucian scholars' but alchemists who had deceived him about immortality elixirs. Sima Qian, aiming to warn the later Emperor Wu of Han, wrote 'all students recited and modeled themselves after Confucius' into the Records. The layering effect of history has rendered truth unrecognizable.",
                "component": "dual",
                "dual_yes": {"h4": "Historical Truth", "p": "Books were banned not burned, preserved in the imperial library. Those buried were fraudulent alchemists, not Confucian scholars. The goal was ideological unification."},
                "dual_no": {"h4": "Popular Misconception", "p": "All texts destroyed, Confucian scholars buried alive. This image was shaped by Sima Qian's literary technique and later discursive construction."},
            },
            {
                "tag": "The Collapse Trigger",
                "title": "Daze Township: The Last Straw That Broke the Empire",
                "desc": "Two conscript officers, Chen Sheng and Wu Guang, facing execution for rain-delayed arrival, ignited a wildfire with the cry: 'Are kings and nobles born to their station?' But they were merely the detonator — the real powder keg was the revanchist longing of old Six States aristocrats, the exhaustion of the common people, and the Qin system's neglect of the principle that 'greatness carries great burdens.' The First Emperor left his son Hu Hai a colossal machine requiring masterful piloting — and Hu Hai was clearly not a qualified pilot.",
                "component": "data",
                "data_items": [
                    {"big": "900", "name": "Initial Rebels", "sm": "The number who first rose up at Daze Township"},
                    {"big": "2 Mo.", "name": "To Hangu Pass", "sm": "From uprising to Zhou Wen's army reaching the outskirts of Xianyang"},
                    {"big": "6 States", "name": "Simultaneous Revolt", "sm": "Old Six States aristocrats rose up in response after the uprising"},
                ],
            },
        ],
        "takeaway_zh": "始皇帝搭建了一个需要极高驾驭能力的庞大机器，却未能建立与之匹配的传承机制。他的每一项「功在当代、利在千秋」的决策都没有做错，但错在没有给这套系统留出消化和沉淀的时间。大有大的难处，帝国的崩塌从来不是因为外敌，而是因为内部的系统性缺陷。",
        "takeaway_en": "The First Emperor built a colossal machine requiring extraordinary governing skill, yet failed to establish a matching succession mechanism. Every one of his groundbreaking decisions was correct — but he left no time for the system to digest and consolidate. Greatness carries great burdens, and empires collapse not from external enemies, but from internal systemic flaws.",
    },
    2: {
        "title_zh": "破釜沉舟：力拔山兮气盖世",
        "title_en": "Smashing the Cauldrons: The Rise of the Overlord",
        "subtitle_zh": "从陈胜吴广到项梁项羽，从章邯救火到巨鹿之战——秦末烽火中一代战神的横空出世",
        "subtitle_en": "From Chen Sheng and Wu Guang to Xiang Liang and Xiang Yu, from Zhang Han's counteroffensive to the Battle of Julu — the birth of a god of war amid the flames of Qin's collapse",
        "overview_zh": "公元前209年，陈胜在大泽乡揭竿而起，天下云集响应。秦帝国派出少府章邯率领骊山刑徒反扑，几乎将六国又灭了一遍。然而，楚国名将之后项梁和其侄子项羽的崛起彻底改变了战局。当章邯将赵王困于巨鹿、诸侯作壁上观之时，年仅二十五岁的项羽下令破釜沉舟，以五万楚军击溃四十万秦军主力，创造了中国战争史上最辉煌的以少胜多战例。一夜之间，天下易主。",
        "overview_en": "In 209 BC, Chen Sheng raised the banner of revolt at Daze, and the realm erupted in response. The Qin Empire dispatched Zhang Han with conscripted convicts to counterattack, nearly crushing the Six States all over again. But the emergence of Xiang Liang and his nephew Xiang Yu shifted the tide decisively. When Zhang Han besieged the King of Zhao at Julu while allied lords watched from the sidelines, the 25-year-old Xiang Yu ordered his troops to smash their cooking cauldrons and sink their boats — then crushed the 400,000-strong Qin main force with just 50,000 Chu soldiers, creating the most glorious upset in Chinese military history. Overnight, the realm changed hands.",
        "kpi": [
            {"label_zh": "项羽年龄", "value_zh": "25岁", "label_en": "Xiang Yu's Age", "value_en": "Age 25"},
            {"label_zh": "巨鹿之战", "value_zh": "5万 vs 40万", "label_en": "Battle of Julu", "value_en": "50K vs 400K"},
            {"label_zh": "起义扩散速度", "value_zh": "两个月", "label_en": "Revolt Spread", "value_en": "2 Months"},
            {"label_zh": "章邯军团", "value_zh": "骊山刑徒", "label_en": "Zhang Han's Army", "value_en": "Convict Conscripts"},
        ],
        "sections_zh": [
            {
                "tag": "星星之火",
                "title": "王侯将相，宁有种乎：中国第一次农民起义",
                "desc": "陈胜、吴广创造了多个「中国第一次」：第一次农民起义、第一次喊出革命口号、第一次用迷信凝聚人心、第一次打名人的旗号。他们以「大楚兴，陈胜王」的鱼腹藏书和篝火狐鸣来制造天命，用扶苏和项燕的名号来聚拢人心。然而，所有农民起义面临的根本问题——缺乏军事人才——最终注定了「张楚」的短暂命运。",
                "component": "flow",
                "flow_steps": ["陈胜吴广起义", "鱼腹藏书·篝火狐鸣", "攻入函谷关", "周文兵临咸阳", "章邯反扑"],
            },
            {
                "tag": "帝国救星",
                "title": "章邯救火：秦朝的回光返照",
                "desc": "面对周文大军兵临城下，少府章邯提议赦免骊山刑徒，迅速组建了一支临时军团。他以惊人速度击溃周文，守住函谷关，然后稳扎稳打——整军备战两个月，再出关扫荡。章邯展现出秦国将领体系的典型特征：重视后勤、稳打稳扎。他几乎以一己之力将秦朝从灭亡边缘拉了回来，但他终究不是那个能挽天倾的人。",
                "component": "risk",
                "risk_items": [
                    {"label": "函谷关防御", "fill": 95},
                    {"label": "击溃周文", "fill": 90},
                    {"label": "扫荡陈胜", "fill": 85},
                    {"label": "围点打援", "fill": 80},
                    {"label": "最终投降项羽", "fill": 20},
                ],
            },
            {
                "tag": "贵族崛起",
                "title": "项梁：从复仇到称霸",
                "desc": "项梁是抗秦名将项燕之子，凭借祖传威望和杀伐果断迅速成为反秦第一势力。他收拾了陈胜残部、击败秦嘉、拥立楚怀王，建立了一个以楚为核心的抗秦联盟。然而「成功者偏见」让他低估了章邯，最终在定陶之战中被章邯夜袭，兵败身亡。项梁之死，却为更可怕的人物腾出了舞台。",
                "component": "dual",
                "dual_yes": {"h4": "项梁的成功之道", "p": "祖传威望 + 杀伐果断 + 善用人才（范增、项羽）。建立楚系抗秦联盟，整合各方反秦势力。"},
                "dual_no": {"h4": "项梁的致命失误", "p": "成功者偏见——连胜后轻敌。低估章邯的夜战能力。在定陶被章邯突袭致死，大好局面毁于一旦。"},
            },
            {
                "tag": "世纪之战",
                "title": "巨鹿之战：破釜沉舟的真相",
                "desc": "章邯围困赵王于巨鹿，诸侯援军皆作壁上观。项羽斩宋义夺取军权后，下令全军「皆沉船，破釜甑，烧庐舍，持三日粮」。这不是匹夫之勇，而是精妙绝伦的兵法：三天口粮意味着必须速战速决；沉船破釜则断绝了一切退路。楚军以一当十，九战九捷，击溃秦军主力。这一战后，诸侯将领入见项羽时「无不膝行而前，莫敢仰视」。",
                "component": "data",
                "data_items": [
                    {"big": "5万", "name": "楚军兵力", "sm": "项羽率领的破釜沉舟之军"},
                    {"big": "40万", "name": "秦军主力", "sm": "章邯指挥的大秦帝国最后一支野战军"},
                    {"big": "9战", "name": "九战九捷", "sm": "楚军连续九次出击，无一次败绩"},
                ],
            },
            {
                "tag": "新王诞生",
                "title": "项羽称霸与章邯交枪",
                "desc": "巨鹿之战后，项羽成为实际上未被册封的「项王」。章邯在内外交困中投降项羽，二十万秦军降卒被坑杀于新安——这是项羽一生中最黑暗的一笔。项羽的军事天赋无可置疑，但他「对人不对事」的性格弱点已经悄然埋下：他恨秦人、恨章邯、恨一切不顺从者，这种情绪的驱动让他在未来的战略决策中屡犯大错。",
                "component": "flow",
                "flow_steps": ["巨鹿大捷", "诸侯膝行", "章邯投降", "坑杀20万秦卒", "项羽成为霸主"],
            },
        ],
        "sections_en": [
            {
                "tag": "Sparks Ignite",
                "title": "'Are Kings Born to Their Station?': China's First Peasant Revolt",
                "desc": "Chen Sheng and Wu Guang created many 'Chinese firsts': the first peasant uprising, the first revolutionary slogan, the first use of superstition to rally people, the first use of famous names as banners. With fish-belly scrolls reading 'Great Chu shall rise, Chen Sheng shall be king' and bonfire fox-calls, they manufactured a divine mandate, using the names of Fusu and Xiang Yan to gather support. Yet the fundamental problem of all peasant revolts — lack of military talent — ultimately doomed the short-lived 'Zhang Chu' state.",
                "component": "flow",
                "flow_steps": ["Chen Sheng & Wu Guang Revolt", "Fish Scrolls & Fox Calls", "Breaking Hangu Pass", "Zhou Wen at Xianyang", "Zhang Han Counterattacks"],
            },
            {
                "tag": "Imperial Savior",
                "title": "Zhang Han to the Rescue: Qin's Last Flash of Brilliance",
                "desc": "With Zhou Wen's army at the capital's gates, Chief Administrator Zhang Han proposed pardoning the convict laborers at Mount Li and rapidly assembled an improvised army. He crushed Zhou Wen with astonishing speed, held Hangu Pass, then methodically prepared — two months of reorganization before emerging to sweep the field. Zhang Han embodied the typical qualities of Qin's officer corps: logistical mastery and steady, grinding warfare. He single-handedly pulled Qin back from the brink of destruction, yet could not ultimately reverse the tide of heaven.",
                "component": "risk",
                "risk_items": [
                    {"label": "Hangu Pass Defense", "fill": 95},
                    {"label": "Crushing Zhou Wen", "fill": 90},
                    {"label": "Sweeping Chen Sheng", "fill": 85},
                    {"label": "Encirclement Tactics", "fill": 80},
                    {"label": "Final Surrender to Xiang Yu", "fill": 20},
                ],
            },
            {
                "tag": "The Aristocrat Rises",
                "title": "Xiang Liang: From Revenge to Dominance",
                "desc": "Xiang Liang, son of the famed anti-Qin general Xiang Yan, leveraged ancestral prestige and ruthless decisiveness to swiftly become the leading anti-Qin force. He absorbed Chen Sheng's remnants, defeated Qin Jia, enthroned a Chu puppet king, and built a Chu-centered anti-Qin coalition. However, 'survivor's bias' led him to underestimate Zhang Han — at Dingtao, Zhang Han ambushed him at night, killing him and shattering his momentum. Xiang Liang's death, however, cleared the stage for an even more terrifying figure.",
                "component": "dual",
                "dual_yes": {"h4": "Xiang Liang's Formula for Success", "p": "Ancestral prestige + decisive ruthlessness + brilliant talent management (Fan Zeng, Xiang Yu). Built a Chu-centered anti-Qin coalition integrating various forces."},
                "dual_no": {"h4": "Xiang Liang's Fatal Mistake", "p": "Survivor's bias — grew overconfident after successive victories. Underestimated Zhang Han's night-fighting capability. Ambushed and killed at Dingtao, wiping away his entire strategic position."},
            },
            {
                "tag": "The Decisive Battle",
                "title": "The Battle of Julu: The Truth Behind Smashing the Cauldrons",
                "desc": "Zhang Han besieged the King of Zhao at Julu while allied reinforcements watched idly from their ramparts. After beheading Song Yi and seizing command, Xiang Yu ordered his entire army to 'sink all boats, smash all cauldrons, burn all shelters, and carry only three days' rations.' This was not reckless courage but masterful military art: three days' rations meant a decisive quick battle; sunken boats and smashed cauldrons eliminated all possibility of retreat. The Chu army, each soldier fighting like ten, achieved nine consecutive victories and crushed the Qin main force. After this battle, allied generals entering Xiang Yu's tent 'all crawled forward on their knees, none daring to look up.'",
                "component": "data",
                "data_items": [
                    {"big": "50K", "name": "Chu Army", "sm": "Xiang Yu's cauldron-smashing force"},
                    {"big": "400K", "name": "Qin Main Force", "sm": "Zhang Han's last imperial field army"},
                    {"big": "9-0", "name": "Consecutive Victories", "sm": "Nine successive engagements, not one defeat"},
                ],
            },
            {
                "tag": "A New Overlord",
                "title": "The Rise of Xiang Yu and Zhang Han's Surrender",
                "desc": "After Julu, Xiang Yu became the de facto, uninvested 'King Xiang.' Zhang Han, trapped between external pressure and internal suspicion, surrendered to Xiang Yu — who then buried alive 200,000 Qin surrendered troops at Xin'an, the darkest stroke of Xiang Yu's life. His military genius was beyond doubt, but his fatal character flaw — judging people rather than situations — was already quietly planted. He hated Qin people, hated Zhang Han, hated all who did not submit, and this emotional drive would cause him to make repeated strategic blunders in the future.",
                "component": "flow",
                "flow_steps": ["Julu Triumph", "Allies Crawl in Submission", "Zhang Han Surrenders", "200K Qin Troops Buried Alive", "Xiang Yu Becomes Hegemon"],
            },
        ],
        "takeaway_zh": "项羽的破釜沉舟是军事史上最完美的孤注一掷——既断绝了自己的退路，也让敌人胆寒。然而，极致的战斗天才往往是最糟糕的战略家。巨鹿之战有多辉煌，项羽日后的败亡就有多必然。战神的光环让他迷信力量的绝对性，却忽略了政治和人心才是真正的战场。",
        "takeaway_en": "Xiang Yu's smashing of the cauldrons was the most perfect all-or-nothing gamble in military history — it cut off his own retreat while terrifying the enemy. Yet the most brilliant combat geniuses are often the worst strategists. As glorious as Julu was, Xiang Yu's later defeat was equally inevitable. The halo of the god of war made him worship absolute force, while overlooking that politics and human hearts are the real battlefield.",
    },
    3: {
        "title_zh": "先入关者为王上：刘邦的西行进军记",
        "title_en": "First to Enter the Pass Becomes King: Liu Bang's Western March",
        "subtitle_zh": "一个四十九岁亭长的逆袭之路——从沛县二流子到灭亡秦朝的第一功臣",
        "subtitle_en": "The comeback of a 49-year-old village officer — from small-town loafer to the first conqueror of the Qin capital",
        "overview_zh": "公元前209年九月，四十九岁的泗水亭长刘邦在沛县举起了反秦大旗。这个出身农家、好酒好色、满嘴脏话的「二流子」，如何一步步收拢萧何、樊哙、张良等不世之才？芒砀山斩白蛇的神话如何为他积累政治资本？西征灭秦途中，张良的加入如何让刘邦从游击流寇蜕变为战略统帅？最终，刘邦以约法三章的仁政赢得关中民心，二世胡亥的秦帝国在他面前轰然倒塌。",
        "overview_en": "In September 209 BC, the 49-year-old Sishui village officer Liu Bang raised the anti-Qin banner in Pei County. How did this farmer-born 'loafer' — fond of drink, women, and coarse language — gradually assemble unparalleled talents like Xiao He, Fan Kuai, and Zhang Liang? How did the myth of slaying a white serpent in Mount Mangdang build his political mystique? How did Zhang Liang's arrival during the western expedition transform Liu Bang from a guerrilla raider into a strategic commander? Finally, Liu Bang won the hearts of the Guanzhong people with a simple three-article legal code, and the Qin Empire of the Second Emperor came crashing down before him.",
        "kpi": [
            {"label_zh": "刘邦起兵年龄", "value_zh": "49岁", "label_en": "Age at Revolt", "value_en": "Age 49"},
            {"label_zh": "起步兵力", "value_zh": "数百人", "label_en": "Starting Troops", "value_en": "Hundreds"},
            {"label_zh": "约法三章", "value_zh": "杀人/伤人/盗", "label_en": "Three-Article Code", "value_en": "3 Articles"},
            {"label_zh": "秦二世在位", "value_zh": "3年", "label_en": "Qin Er Shi's Reign", "value_en": "3 Years"},
        ],
        "sections_zh": [
            {
                "tag": "草根出身",
                "title": "刘邦的家庭与早年：一个「二流子」的养成",
                "desc": "刘邦出身丰邑农户家庭，排行老三，故名刘季。他不喜读书、不爱干活，整日喝酒交友赊账，被亲爹骂作败家子。但酒馆女掌柜发现，「只要刘邦来喝酒，那天的生意就特别好」。三十五岁高龄考取泗水亭长后，刘邦与沛县基层官吏萧何、曹参、夏侯婴等人结下了深厚友谊——这批人日后全部成为大汉开国元勋。",
                "component": "data",
                "data_items": [
                    {"big": "35岁", "name": "考取亭长", "sm": "楚亡国后秦制推行，刘邦高龄应试"},
                    {"big": "49岁", "name": "起义之年", "sm": "同龄人已入土，他却掀开人生新篇章"},
                    {"big": "沛县班底", "name": "萧何·樊哙·夏侯婴", "sm": "上天为他配备了一套超豪华创业团队"},
                ],
            },
            {
                "tag": "造神运动",
                "title": "芒砀斩白蛇：神话如何塑造天命",
                "desc": "刘邦醉后斩白蛇，有老妇人哭诉「赤帝子斩白帝子」——这样的神异传说贯穿了刘邦的一生。吕公一见刘邦便断定「相貌不凡」，执意将女儿吕雉嫁给他。相面老者一再确认「君相贵不可言」。这些「天命所归」的叙事看似荒谬，却实实在在地为刘邦积累了巨大的政治号召力——在那个迷信盛行的年代，人们需要的不是一个凡人，而是一个「天选之子」。",
                "component": "flow",
                "flow_steps": ["龙种降生传说", "酒馆龙影显现", "吕公相面嫁女", "老翁预言天命", "斩白蛇·赤帝子"],
            },
            {
                "tag": "初识强敌",
                "title": "初识「大魔王」：刘邦与项羽的第一次交集",
                "desc": "刘邦在丰邑得而复失的惨痛教训中，第一次感受到了人性的背叛——雍齿的倒戈让他刻骨铭心。在项梁帐下，刘邦第一次见到了项羽，并与之并肩作战。这段时期的刘邦在项羽的光环下显得黯淡无光，但这恰恰是他积攒实力、学习战争的宝贵窗口期。他从未忘记雍齿，但也没有立刻报复——刘邦学会了隐忍。",
                "component": "dual",
                "dual_yes": {"h4": "刘邦的姿态", "p": "甘居人下、虚心学习。在项梁帐下低调发展，不与项羽争锋。雍齿背叛后不急于报复，等待时机。"},
                "dual_no": {"h4": "项羽的姿态", "p": "光芒万丈、锋芒毕露。巨鹿一战震惊天下，但也因此树敌无数。年轻人的锐气既是利刃也是负担。"},
            },
            {
                "tag": "西征灭秦",
                "title": "一路向西：刘邦的战略蜕变",
                "desc": "刘邦的西征起初并不顺利，在昌邑、开封等地屡攻不下。转机发生在张良归队之后——刘邦开始舍弃盲目游击，而是在张良的运筹下步步为营。当刘邦想要绕过宛城直奔武关时，张良喊停了他：「这个大城不能不打！」拿下宛城后以招降为主的策略，让刘邦从单纯的军事统帅蜕变为政治统帅。秦王子婴素车白马、系颈以组，在轵道旁向刘邦投降。",
                "component": "flow",
                "flow_steps": ["刘邦西征出发", "张良归队运筹", "攻宛城·招降策略", "破武关入关中", "子婴投降·秦亡"],
            },
            {
                "tag": "秦朝终局",
                "title": "二世而亡：一个帝国的迅速崩塌",
                "desc": "胡亥即位后秉承「他爹留下的人全都必须死」和「他爹上马的工程全都不能停」两条原则，大肆屠杀兄弟姐妹和老臣宿将，继续奴役天下。赵高指鹿为马、李斯被腰斩、章邯外困内疑——秦帝国的统治核心在短短三年内彻底瓦解。刘邦入关后约法三章「杀人者死，伤人及盗抵罪」，尽废秦苛法，关中百姓「唯恐沛公不为秦王」。",
                "component": "risk",
                "risk_items": [
                    {"label": "胡亥屠杀宗室", "fill": 100},
                    {"label": "赵高指鹿为马", "fill": 100},
                    {"label": "李斯被腰斩", "fill": 100},
                    {"label": "章邯被迫投降", "fill": 100},
                    {"label": "刘邦约法三章", "fill": 95},
                ],
            },
        ],
        "sections_en": [
            {
                "tag": "Grassroots Origins",
                "title": "Liu Bang's Family and Early Years: The Making of a 'Loafer'",
                "desc": "Liu Bang was born into a farming family in Fengyi, third in line, hence named Liu Ji ('Third Liu'). He disliked study and physical labor, passing his days drinking, socializing, and accruing tabs — earning his father's scorn as a wastrel. Yet the tavern's proprietress noticed that 'whenever Liu Bang comes to drink, business is exceptionally good.' After passing the Qin bureaucratic exam at the 'advanced' age of 35 to become Sishui Village Officer, Liu Bang forged deep friendships with Pei County's grassroots officials — Xiao He, Cao Shen, Xiahou Ying, and others who would all become founding ministers of the Great Han.",
                "component": "data",
                "data_items": [
                    {"big": "Age 35", "name": "Passed Bureaucratic Exam", "sm": "After Chu's fall, Qin system imposed; Liu took the exam at advanced age"},
                    {"big": "Age 49", "name": "Year of Revolt", "sm": "When peers were in their graves, he turned a new page of life"},
                    {"big": "Pei County Crew", "name": "Xiao He, Fan Kuai & More", "sm": "Heaven gifted him an all-star founding team"},
                ],
            },
            {
                "tag": "Manufacturing Destiny",
                "title": "Slaying the White Serpent: How Myth Forged a Mandate",
                "desc": "After beheading a white serpent while drunk, Liu Bang encountered an old woman weeping that 'the Red Emperor's son has slain the White Emperor's son' — such miraculous tales shadowed Liu Bang's entire life. Elder Lu, at first sight, pronounced Liu's physiognomy 'extraordinary' and insisted on marrying his daughter Lu Zhi to him. A fortune-telling elder repeatedly confirmed that 'your lordship's visage is too noble for words.' These 'divinely ordained' narratives, however absurd, accumulated enormous political capital for Liu Bang — in an age steeped in superstition, people needed not a mortal man, but a 'chosen one of heaven.'",
                "component": "flow",
                "flow_steps": ["Dragon-Birth Legend", "Tavern Dragon Shadow", "Lu Gong's Face-Reading Match", "Elder's Fate Prophecy", "White Serpent Beheading"],
            },
            {
                "tag": "Meeting the Adversary",
                "title": "First Encounter with the 'Demon King': Liu Bang Meets Xiang Yu",
                "desc": "In the bitter lesson of Fengyi — won and then lost — Liu Bang first tasted the sting of human betrayal, Yong Chi's defection searing into his memory. Under Xiang Liang's command, Liu Bang met Xiang Yu for the first time and even fought alongside him. During this period, Liu Bang appeared utterly eclipsed by Xiang Yu's brilliance — precisely the precious window he needed to accumulate strength and learn the art of war. He never forgot Yong Chi, yet he did not seek immediate revenge — Liu Bang had learned patience.",
                "component": "dual",
                "dual_yes": {"h4": "Liu Bang's Approach", "p": "Accepted a subordinate role, learning humbly. Developed quietly under Xiang Liang, avoiding direct competition with Xiang Yu. After Yong Chi's betrayal, waited patiently instead of rushing revenge."},
                "dual_no": {"h4": "Xiang Yu's Approach", "p": "Radiant brilliance, sharp-edged ambition. Julu shocked the realm, but also made countless enemies. A young man's élan is both a sword and a burden."},
            },
            {
                "tag": "The Western Expedition",
                "title": "Westward March: Liu Bang's Strategic Transformation",
                "desc": "Liu Bang's western expedition began poorly, failing repeatedly at Changyi, Kaifeng, and other strongholds. The turning point came when Zhang Liang rejoined — Liu Bang abandoned blind guerrilla raiding and, under Zhang Liang's strategic guidance, advanced methodically. When Liu Bang wanted to bypass Wan City and race for Wu Pass, Zhang Liang stopped him: 'This great city must be taken!' After capturing Wan through a surrender-first strategy, Liu Bang transformed from a mere military commander into a political leader. King Ziying of Qin, dressed in plain white, riding a white horse, with a cord tied around his neck, surrendered to Liu Bang by the Zhi Road.",
                "component": "flow",
                "flow_steps": ["Liu Bang Sets Out West", "Zhang Liang Returns & Plans", "Captures Wan by Surrender", "Breaks Wu Pass into Guanzhong", "Ziying Surrenders — Qin Falls"],
            },
            {
                "tag": "The End of Qin",
                "title": "Collapse in One Generation: The Rapid Demise of an Empire",
                "desc": "Upon ascending, Hu Hai followed two maxims: 'everyone his father left behind must die' and 'every project his father initiated must continue,' massacring siblings and veteran ministers while continuing to enslave the realm. Zhao Gao 'pointing at a deer and calling it a horse,' Li Si being cut in half at the waist, Zhang Han trapped between external enemies and internal suspicion — the Qin Empire's ruling core completely dissolved within three short years. After entering the pass, Liu Bang instituted a simple three-article law code: 'Murderers die, those who injure others or steal shall be punished accordingly,' abolishing all Qin's harsh laws. The people of Guanzhong 'feared only that the Governor of Pei might not become King of Qin.'",
                "component": "risk",
                "risk_items": [
                    {"label": "Hu Hai's Massacre of Royal Kin", "fill": 100},
                    {"label": "Zhao Gao Calls Deer a Horse", "fill": 100},
                    {"label": "Li Si Executed by Waist-Chop", "fill": 100},
                    {"label": "Zhang Han Forced to Surrender", "fill": 100},
                    {"label": "Liu Bang's Simple Law Code", "fill": 95},
                ],
            },
        ],
        "takeaway_zh": "刘邦的成功不是「天命所归」，而是一个不断升级的过程：从亭长到流寇，从流寇到军阀，从军阀到政治统帅。每一次升级的背后都有一个贵人在关键时刻拉他一把——张良、萧何、樊哙。刘邦最大的天赋不是军事才能，而是知人善任、从善如流。四十九岁起步，最终君临天下，这才是真正的「大器晚成」。",
        "takeaway_en": "Liu Bang's success was not 'divinely ordained' but a continuous process of upgrading: from village officer to roving bandit, from bandit to warlord, from warlord to political commander. Behind every upgrade was a benefactor who pulled him back on course at a critical moment — Zhang Liang, Xiao He, Fan Kuai. Liu Bang's greatest talent was not military prowess, but recognizing and employing talent, and accepting wise counsel. Starting at age 49 and ultimately ruling the realm — that is true 'late bloomer' greatness.",
    },
    4: {
        "title_zh": "鸿门宴：刘邦集团的内在升级",
        "title_en": "The Feast at Hong Gate: The Inner Transformation of Liu Bang's Camp",
        "subtitle_zh": "入关后的一个月如何改变了一个农民起义领袖——从贪恋享受到胸怀天下",
        "subtitle_en": "How one month after entering the pass transformed a peasant rebel leader — from craving pleasure to embracing a grand vision",
        "overview_zh": "公元前206年，刘邦率先进入咸阳。面对秦宫的珠宝美女，这个五十岁的农民一度沉溺其中，但樊哙和张良的当头棒喝让他做出了人生中最关键的决定——还军灞上。与此同时，萧何火速收缴了秦朝的户籍、地图、法令档案，为日后的楚汉争霸奠定了信息基础。随后，鸿门宴上刘邦在项羽的刀锋下用谦卑与运气死里逃生。这一章展现的不仅是生死一线的戏剧性，更是一个草根领袖在权力巅峰时刻的自我超越。",
        "overview_en": "In 206 BC, Liu Bang became the first rebel leader to enter the Qin capital Xianyang. Confronted with the palace's jewels and beauties, the fifty-year-old peasant momentarily wallowed in luxury — until Fan Kuai and Zhang Liang delivered a thunderous wake-up call that prompted the most critical decision of his life: withdrawing his army to Bashang. Meanwhile, Xiao He frantically seized the Qin dynasty's census registers, maps, and legal archives — laying the informational foundation for the coming Chu-Han war. Then came the Feast at Hong Gate, where Liu Bang narrowly escaped Xiang Yu's blade through humility and fortune. This chapter reveals not just a dramatic brush with death, but a grassroots leader's self-transcendence at the pinnacle of power.",
        "kpi": [
            {"label_zh": "刘邦入咸阳", "value_zh": "公元前206年", "label_en": "Entered Xianyang", "value_en": "206 BC"},
            {"label_zh": "萧何收图籍", "value_zh": "秦百年积累", "label_en": "Xiao He's Archive", "value_en": "100 Years of Qin"},
            {"label_zh": "鸿门宴随行", "value_zh": "5人+100骑", "label_en": "Hong Gate Escort", "value_en": "5 men + 100 riders"},
            {"label_zh": "项羽分封诸王", "value_zh": "18路诸侯", "label_en": "Xiang Yu's Enfeoffment", "value_en": "18 Vassal Kings"},
        ],
        "sections_zh": [
            {
                "tag": "自我克制",
                "title": "刘邦的人生升级：还军灞上的意义",
                "desc": "入咸阳后，刘邦一头扎进秦宫享受起来。樊哙当头棒喝：「沛公想取天下，还是想当富家翁？」刘邦置之不理。直到张良再次劝说：「良药苦口利于病，忠言逆耳利于行。」在痛苦的内心挣扎后，刘邦做出了几千年农民起义领袖中极其罕见的选择——放弃眼前的享受，还军灞上，告诉将士们「咱们还有大事要干」。这一刻，五十岁的农民完成了人生中最重要的阶层跨越。",
                "component": "dual",
                "dual_yes": {"h4": "刘邦的选择（非凡）", "p": "放弃咸阳美色财富，克制五十年形成的习气。将眼光放远到争天下。农民出身的阶层跨越——千古唯二（刘邦+朱元璋）。"},
                "dual_no": {"h4": "常人路径（普遍）", "p": "穷人乍富后贪图享受，被基因层面的「低级快乐」支配。如赤眉军、太平天国——缺乏眼界和克制力，终致败亡。"},
            },
            {
                "tag": "根基所在",
                "title": "萧何收图籍：奠定治国基础",
                "desc": "当所有人都在抢金银珠宝时，萧何火速赶往丞相府和御史府，将秦朝的户籍、地形、法令等档案全部登记造册带回。这一举动意味着秦帝国自商鞅变法以来一百多年真正值钱的工作——官僚系统的全部知识积累——被完整移交给了刘邦。知道哪里有粮、哪里有多少人、怎么征收赋税，比占领多少城池都要重要得多。",
                "component": "risk",
                "risk_items": [
                    {"label": "萧何的战略眼光", "fill": 100},
                    {"label": "户籍档案完整度", "fill": 100},
                    {"label": "法令图籍获取", "fill": 100},
                    {"label": "他人抢夺珠宝", "fill": 5},
                ],
            },
            {
                "tag": "生死时刻",
                "title": "鸿门宴：刘邦的至暗时刻",
                "desc": "刘邦封锁函谷关激怒了项羽，项羽扬言「旦日飨士卒，为击破沛公军」。危急关头，项伯连夜通风报信，张良策划应对策略。项庄舞剑，意在沛公——樊哙闯帐，「头发上指，目眦尽裂」。这场中国历史上最著名的饭局，刘邦靠着谦卑的姿态、张良的智慧和项伯的私心，在项羽的刀锋下侥幸生还。但这不是侥幸——刘邦放下了身段，而项羽放不下。",
                "component": "flow",
                "flow_steps": ["刘邦封锁函谷关", "项羽大怒·准备进攻", "项伯报信·张良策划", "鸿门宴·项庄舞剑", "刘邦险中逃生"],
            },
            {
                "tag": "心理博弈",
                "title": "项羽为何不杀刘邦？",
                "desc": "项羽在鸿门宴上放走了刘邦，千年来被无数人叹息。但细究之下，项羽不杀刘邦有其深层逻辑：第一，刘邦表现得足够卑微，「臣与将军戮力而攻秦」——主动将项羽放在主位；第二，杀刘邦缺乏正当性，两人同属楚怀王麾下，且刘邦有先入关中的功劳；第三，项羽此时的敌人名单上，刘邦排不到第一。项羽最大的问题是：他从未把刘邦视为真正的对手。",
                "component": "data",
                "data_items": [
                    {"big": "40万", "name": "项羽大军", "sm": "鸿门宴时项羽麾下的总兵力"},
                    {"big": "10万", "name": "刘邦兵力", "sm": "刘邦此时的军力，不构成战略威胁"},
                    {"big": "1次", "name": "错过机会", "sm": "唯一杀死刘邦的窗口，被项羽轻轻放过"},
                ],
            },
            {
                "tag": "新秩序",
                "title": "项羽分封：一个人的天下布局",
                "desc": "鸿门宴后，项羽进入咸阳，杀子婴、烧秦宫，然后以霸王身份分封十八路诸侯。他将刘邦分到偏远的巴蜀汉中，将关中一分为三分封给三位秦国降将（章邯、司马欣、董翳），将旧六国故地分给了各路功臣。然而这套分封体系一落地就漏洞百出：田荣未被封王即造反、陈馀因张耳之事怀恨、刘邦则凭借萧何收来的情报默默经营着还定三秦的蓝图。",
                "component": "flow",
                "flow_steps": ["项羽屠咸阳", "杀子婴焚秦宫", "分封18路诸侯", "刘邦被迁汉中", "天下暗流涌动"],
            },
        ],
        "sections_en": [
            {
                "tag": "Self-Mastery",
                "title": "Liu Bang's Life Upgrade: The Significance of Withdrawing to Bashang",
                "desc": "After entering Xianyang, Liu Bang plunged headlong into the Qin palace's pleasures. Fan Kuai delivered a thunderous rebuke: 'Do you want the realm, or do you want to retire as a rich old man?' Liu Bang ignored him — until Zhang Liang added: 'Bitter medicine cures illness; honest counsel, though unpleasant, benefits conduct.' After agonizing internal struggle, Liu Bang made a choice extraordinarily rare among peasant rebel leaders across millennia — renouncing immediate pleasures, withdrawing the army to Bashang, and telling his troops: 'We still have greater matters to attend to.' In that moment, a fifty-year-old peasant completed the most important class transcendence of his life.",
                "component": "dual",
                "dual_yes": {"h4": "Liu Bang's Choice (Extraordinary)", "p": "Renounced Xianyang's beauties and treasures, overcame fifty years of ingrained habits. Extended his vision to contesting the realm. A peasant-born class transcendence — only two in all of ancient Chinese history (Liu Bang + Zhu Yuanzhang)."},
                "dual_no": {"h4": "The Common Path (Typical)", "p": "The newly rich indulging in pleasure, dominated by biological 'base pleasures.' Examples: Red Eyebrows Army, Taiping Heavenly Kingdom — lacking vision and self-restraint, doomed to destruction."},
            },
            {
                "tag": "The Foundation",
                "title": "Xiao He Seizes the Archives: Laying the Bedrock of Governance",
                "desc": "While everyone else scrambled for gold and jewels, Xiao He rushed to the Chancellor's Office and the Imperial Secretary's Bureau, seizing and cataloging the Qin dynasty's census records, maps, laws, and decrees — bringing them all back to Liu Bang's camp. This single act meant that the Qin Empire's century-plus of real valuable work since Shang Yang's reforms — the entire accumulated knowledge of its bureaucratic system — was transferred intact to Liu Bang. Knowing where the grain was, how many people lived where, and how to levy taxes was far more important than seizing any number of walled cities.",
                "component": "risk",
                "risk_items": [
                    {"label": "Xiao He's Strategic Vision", "fill": 100},
                    {"label": "Census Archive Completeness", "fill": 100},
                    {"label": "Legal & Map Records Seized", "fill": 100},
                    {"label": "Others Grabbing Jewels", "fill": 5},
                ],
            },
            {
                "tag": "Moment of Death",
                "title": "The Feast at Hong Gate: Liu Bang's Darkest Hour",
                "desc": "Liu Bang sealing Hangu Pass enraged Xiang Yu, who threatened: 'At dawn we feast the troops and destroy the Governor of Pei's army!' At the critical moment, Xiang Bo leaked word overnight, and Zhang Liang devised the counter-plan. Xiang Zhuang danced with his sword, aiming at Liu Bang — then Fan Kuai stormed the tent, 'hair bristling, eyes blazing with fury.' At this most famous banquet in Chinese history, Liu Bang survived Xiang Yu's blade through humble posture, Zhang Liang's wisdom, and Xiang Bo's personal interests. But it wasn't just luck — Liu Bang was willing to lower himself, while Xiang Yu could not.",
                "component": "flow",
                "flow_steps": ["Liu Bang Seals Hangu Pass", "Xiang Yu Enraged & Prepares Attack", "Xiang Bo Leaks & Zhang Liang Plans", "Hong Gate Feast — Sword Dance", "Liu Bang Narrowly Escapes"],
            },
            {
                "tag": "Psychological Game",
                "title": "Why Didn't Xiang Yu Kill Liu Bang?",
                "desc": "Xiang Yu's decision to let Liu Bang go at Hong Gate has been lamented for millennia. But examined closely, there were deeper reasons: First, Liu Bang acted sufficiently humble — 'I, your servant, joined with you, General, to attack Qin' — actively placing Xiang Yu in the primary position. Second, killing Liu Bang lacked legitimacy — both served under King Huai of Chu, and Liu Bang had the merit of entering the pass first. Third, on Xiang Yu's enemy list at that moment, Liu Bang did not rank first. Xiang Yu's greatest problem: he never truly considered Liu Bang a real opponent.",
                "component": "data",
                "data_items": [
                    {"big": "400K", "name": "Xiang Yu's Forces", "sm": "Total troops under Xiang Yu at the time of the feast"},
                    {"big": "100K", "name": "Liu Bang's Forces", "sm": "Liu Bang's military strength at this point posed no strategic threat"},
                    {"big": "Once", "name": "Missed Opportunity", "sm": "The only window to kill Liu Bang — casually let slip by Xiang Yu"},
                ],
            },
            {
                "tag": "The New Order",
                "title": "Xiang Yu's Enfeoffment: One Man's Redesign of the Realm",
                "desc": "After the Hong Gate Feast, Xiang Yu entered Xianyang, killed Ziying, burned the Qin palaces, then, as Hegemon-King, enfeoffed eighteen vassal lords. He assigned Liu Bang to the remote region of Ba-Shu-Hanzhong, divided Guanzhong into three parts for three surrendered Qin generals (Zhang Han, Sima Xin, Dong Yi), and distributed the old Six States territories to various meritorious followers. Yet this enfeoffment system began leaking the moment it was implemented: Tian Rong, passed over for a kingship, immediately revolted; Chen Yu nursed a grudge over the Zhang Er affair; and Liu Bang, armed with the intelligence Xiao He had seized, quietly planned his campaign to reclaim the Three Qins.",
                "component": "flow",
                "flow_steps": ["Xiang Yu Sacks Xianyang", "Kills Ziying, Burns Qin Palace", "Enfeoffs 18 Vassal Kings", "Liu Bang Exiled to Hanzhong", "Undercurrents Surge Across the Realm"],
            },
        ],
        "takeaway_zh": "鸿门宴的真正主角不是刀光剑影，而是刘邦完成了人生中最关键的自我升级——从一个贪恋享受的农民领袖，蜕变为一个能将眼光放远到整个天下的政治家。与此同时，项羽在权力的巅峰沉醉，用个人的好恶而非制度来构建天下秩序。这两个人之间的差距，不是兵力、不是地理，而是格局——一个在上升，一个已到顶。",
        "takeaway_en": "The true protagonist of the Hong Gate Feast was not the flashing blades, but Liu Bang completing the most critical self-upgrade of his life — transforming from a pleasure-seeking peasant leader into a statesman who could extend his vision to the entire realm. Meanwhile, Xiang Yu got drunk on the pinnacle of power, constructing a world order based on personal likes and dislikes rather than institutions. The gap between these two men was not military strength or geography, but vision — one was still rising, the other had already peaked.",
    },
}

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
    elif comp == "risk":
        items = s["risk_items"]
        risk_parts = []
        for item in items:
            risk_parts.append(f"""<div class="risk-row">
            <div class="risk-label">{item["label"]}</div>
            <div class="risk-meter"><div class="risk-fill" style="width:{item["fill"]}%"></div></div>
            <div class="risk-val">{item["fill"]}%</div>
          </div>""")
        risk_html = "\n          ".join(risk_parts)
        comp_html = f'        <div class="risk-bars">\n          {risk_html}\n        </div>'
    elif comp == "data":
        items = s["data_items"]
        card_parts = []
        for item in items:
            card_parts.append(f"""<div class="data-card d1">
              <div class="data-big">{item["big"]}</div>
              <div class="data-name">{item["name"]}</div>
              <div class="data-sm">{item["sm"]}</div>
            </div>""")
        card_html = "\n            ".join(card_parts)
        comp_html = f'        <div class="data-row">\n            {card_html}\n          </div>'

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

  /* ── Risk bars ── */
  .risk-bars { margin-top: 10px; }
  .risk-row { display: flex; align-items: center; gap: 12px; margin-bottom: 10px; }
  .risk-label { font-size: 13px; color: #555; width: 130px; flex-shrink: 0; font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif; }
  .risk-meter { flex: 1; height: 10px; background: #eef2ff; border-radius: 5px; overflow: hidden; }
  .risk-fill { height: 100%; border-radius: 5px; background: #4f46e5; }
  .risk-val { font-size: 13px; font-weight: bold; color: #4f46e5; width: 50px; text-align: right; flex-shrink: 0; }

  /* ── Data cards ── */
  .data-row { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin-top: 10px; }
  .data-card {
    border-radius: 12px; padding: 20px 16px; text-align: center;
    border: 1px solid #fce7f3;
  }
  .data-card.d1 { background: #fdf2f8; border-color: #f9a8d4; }
  .data-card.d2 { background: #fdf2f8; border-color: #f9a8d4; }
  .data-card.d3 { background: #fdf2f8; border-color: #f9a8d4; }
  .data-big { font-size: 28px; margin-bottom: 6px; }
  .data-name { font-size: 15px; font-weight: bold; color: #831843; margin-bottom: 6px; font-family: 'FZXPYZS', 'PingFang SC', 'Noto Serif SC', serif; }
  .data-sm { font-size: 12px; color: #9d174d; line-height: 1.6; }

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
        book_title = BOOK_TITLE_ZH if is_zh else BOOK_TITLE_EN
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
            footer_line1 = f"渤海小吏 · 楚汉双雄 · 第{ch_label_zh}章 · 图书信息图"
            footer_line2 = "来源：楚汉双雄（渤海小吏 著，台海出版社，2020）"
        else:
            footer_line1 = f"Bohai Xiaoli · The Chu-Han Contention · Chapter {ch_label_en} · Book Infographic"
            footer_line2 = "Source: The Chu-Han Contention by Bohai Xiaoli (Taihai Press, 2020)"

        html = f'''<!DOCTYPE html>
<html lang="{L}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{book_title} · {ch_label}章「{title_s}」</title>
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
  <h1>{book_title} · {ch_label}章「{title_s}」</h1>

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
    <div class="takeaway-label">{'📌 核心启示' if is_zh else '📌 KEY TAKEAWAY'}</div>
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
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(html)

        size_kb = os.path.getsize(fpath) / 1024
        print(f"✅ Written: {fname} ({size_kb:.1f} KB)")

print(f"\n✅ All 8 files generated in {BOOKDIR}")