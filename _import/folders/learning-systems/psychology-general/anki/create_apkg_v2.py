#!/usr/bin/env python3
"""
使用 Anki 官方 API 建立 .apkg
"""
import sys
import os
import tempfile
import shutil
import zipfile
from pathlib import Path
from anki.collection import Collection

def parse_cards(txt_file):
    """解析 .txt 格式的卡片

    兼容舊格式：若遇到以「中文重點：」開頭的行，視為上一張卡的補充，附加到 Back。
    """
    cards = []
    last_idx = None

    with open(txt_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            parts = line.split('\t')
            if len(parts) < 2:
                continue

            front = parts[0].strip()

            if front.startswith('中文重點：'):
                if last_idx is None:
                    continue
                prev_front, prev_back = cards[last_idx]
                cards[last_idx] = (prev_front, f"{prev_back}\n\n{front}")
                continue

            back = parts[1].strip()
            cards.append((front, back))
            last_idx = len(cards) - 1

    return cards

def create_apkg_v2(txt_file, output_file, deck_name="Psychology::General"):
    """使用官方 API 建立 .apkg"""
    # 建立臨時 Anki profile
    temp_dir = tempfile.mkdtemp()
    profile_dir = os.path.join(temp_dir, "User 1")
    os.makedirs(profile_dir, exist_ok=True)
    
    # 建立 collection.media 目錄
    media_dir = os.path.join(profile_dir, "collection.media")
    os.makedirs(media_dir, exist_ok=True)
    
    col_path = os.path.join(profile_dir, "collection.anki21")
    
    try:
        # 建立 collection
        col = Collection(col_path)
        
        # 建立牌組
        deck_id = col.decks.id(deck_name)
        
        # 取得基本模型
        model = col.models.by_name("Basic")
        if not model:
            # 如果沒有 Basic 模型，建立一個
            mm = col.models
            model = mm.new("Basic")
            mm.add_field(model, mm.new_field("Front"))
            mm.add_field(model, mm.new_field("Back"))
            
            tmpl = mm.new_template("Card 1")
            tmpl['qfmt'] = "{{Front}}"
            tmpl['afmt'] = "{{FrontSide}}\n\n<hr id=answer>\n\n{{Back}}"
            mm.add_template(model, tmpl)
            mm.add(model)
        
        # 解析並加入卡片
        cards = parse_cards(txt_file)
        added = 0
        
        for front, back in cards:
            note = col.new_note(model)
            note.fields[0] = front
            note.fields[1] = back
            col.add_note(note, deck_id)
            added += 1
        
        print(f"✓ Added {added} cards to deck: {deck_name}")
        
        # 關閉 collection
        col.close()
        
        # 手動打包成 .apkg（就是個 zip 檔案）
        print(f"✓ Packaging into {output_file}...")
        with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zf:
            # 加入 collection.anki21
            zf.write(col_path, "collection.anki21")
            # 加入空的 media 檔案
            zf.writestr("media", "{}")
        
        print(f"✓ Created: {output_file}")
        print(f"  Size: {os.path.getsize(output_file)} bytes")
        
        return True
        
    finally:
        # 清理臨時目錄
        shutil.rmtree(temp_dir, ignore_errors=True)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: create_apkg_v2.py <input.txt> [output.apkg]")
        sys.exit(1)
    
    txt_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else txt_file.replace('.txt', '.apkg')
    
    create_apkg_v2(txt_file, output_file)
