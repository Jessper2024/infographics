#!/usr/bin/env python3
"""
Extract all chapter content from 明朝那些事儿.epub and save as JSON
for sub-agent processing.
"""
import zipfile, os, json, re
from bs4 import BeautifulSoup

epub_path = os.path.expanduser('~/Downloads/明朝那些事儿.epub')
out_dir = os.path.dirname(os.path.abspath(__file__))

# Emperor section mapping (from previous analysis)
sections_raw = [
    ("朱元璋", "ch001", range(4, 28)),     # ch4-27 (24 chapters)
    ("朱允炆", "ch025", range(29, 37)),    # ch29-36 (8 chapters)
    ("朱棣", "ch033", range(39, 49)),      # ch39-48 (10 chapters)
    ("朱高炽", "ch043", [50]),             # ch50 (1 chapter)
    ("朱瞻基", "ch044", [52]),             # ch52 (1 chapter)
    ("朱祁镇pt1", "ch045", [54, 55, 56, 57]), # ch54-57 (4 chapters)
    ("朱祁钰", "ch049", range(59, 65)),    # ch59-64 (6 chapters)
    ("朱祁镇pt2", "ch055", [67, 68, 69]),  # ch67-69 (3 chapters)
    ("朱见深", "ch058", [71, 72]),         # ch71-72 (2 chapters)
    ("朱祐樘", "ch060", [74]),             # ch74 (1 chapter)
    ("朱厚照", "ch061", range(76, 90)),    # ch76-89 (14 chapters)
    ("朱厚熜pt1", "ch075", range(92, 114)), # ch92-113 (22 chapters)
    ("朱厚熜pt2", "ch097", range(116, 120)), # ch116-119 (4 chapters)
    ("朱载垕", "ch101", range(121, 124)),  # ch121-123 (3 chapters)
    ("朱翊钧pt1", "ch104", range(125, 138)), # ch125-137 (13 chapters)
    ("朱翊钧pt2", "ch117", range(140, 149)), # ch140-148 (9 chapters)
    ("朱常洛", "ch126", [150]),            # ch150 (1 chapter)
    ("朱由校pt1", "ch127", range(152, 162)), # ch152-161 (10 chapters)
    ("朱由校pt2", "ch137", [164, 165]),    # ch164-165 (2 chapters)
    ("朱由检", "ch139", range(167, 186)),  # ch167-185 (19 chapters)
]

with zipfile.ZipFile(epub_path) as z:
    # Get font file
    font_data = None
    for name in z.namelist():
        if 'font' in name.lower() or name.endswith('.ttf') or name.endswith('.otf'):
            font_data = z.read(name)
            print(f"Found font: {name} ({len(font_data)} bytes)")
            break

    all_chapters = []
    global_idx = 0
    
    for emperor, prefix, ch_range in sections_raw:
        emperor_data = {
            "emperor": emperor,
            "prefix": prefix,
            "chapters": []
        }
        
        for epub_ch in ch_range:
            fname = f'OPS/chapter{epub_ch}.html'
            if fname not in z.namelist():
                print(f"  WARNING: {fname} not found, skipping")
                continue
            
            html = z.read(fname).decode('utf-8', errors='replace')
            soup = BeautifulSoup(html, 'html.parser')
            
            # Remove script/style
            for tag in soup(['script', 'style']):
                tag.decompose()
            
            # Get title
            h1s = soup.find_all(['h1', 'h2', 'h3'])
            titles = [h.get_text().strip() for h in h1s if h.get_text().strip() and len(h.get_text().strip()) > 1]
            title = titles[0] if titles else f'ch{epub_ch}'
            
            # Get body text
            text = soup.get_text(separator='\n')
            lines = [l.strip() for l in text.split('\n') if l.strip()]
            # Remove leading title duplicates
            while lines and lines[0] == title:
                lines.pop(0)
            body = '\n'.join(lines)
            
            global_idx += 1
            chapter = {
                "global_idx": global_idx,
                "info_num": f"ch{global_idx:03d}",
                "epub_ch": epub_ch,
                "title": title,
                "emperor": emperor,
                "body": body[:3000],  # First 3000 chars for context
                "body_full": body
            }
            emperor_data["chapters"].append(chapter)
        
        all_chapters.append(emperor_data)
        print(f"  {emperor}: {len(emperor_data['chapters'])} chapters (info ch{global_idx - len(emperor_data['chapters']) + 1:03d} - ch{global_idx:03d})")

# Save all data
data = {
    "book": "明朝那些事儿",
    "author": "当年明月",
    "total_sections": len(all_chapters),
    "total_chapters": global_idx,
    "font_file": "方正屏显雅宋简体.TTF",
    "sections": all_chapters
}

out_path = os.path.join(out_dir, '_ming_data.json')
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

print(f"\nSaved: {out_path}")
print(f"Total: {len(all_chapters)} emperor sections, {global_idx} chapters")