# 批次更新 CH3 簡報檔案
import os
import re

SLIDES_DIR = r"D:\自己架設AI_零基礎到大師\CH3_打造RAG知識庫問答平台\簡報"

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 更新年份
    content = content.replace('2025', '2026')

    # 更新 FB 連結
    content = content.replace('https://www.facebook.com/?locale=zh_TW', 'https://www.facebook.com/iddmail')
    content = content.replace('href="https://www.facebook.com/"', 'href="https://www.facebook.com/iddmail"')

    # 在 Part 檔案加入課程總覽按鈕
    filename = os.path.basename(filepath)
    if filename.startswith('Part') and 'index.html' not in content:
        if '課程總覽' not in content:
            # 在 nav-buttons 中加入課程總覽按鈕
            pattern = r'(<div class="nav-buttons">)'
            if re.search(pattern, content):
                content = re.sub(pattern, r'\1\n            <a href="index.html" class="nav-btn">📚 課程總覽</a>', content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print("更新 CH3 簡報...")
    for filename in os.listdir(SLIDES_DIR):
        if filename.endswith('.html'):
            filepath = os.path.join(SLIDES_DIR, filename)
            if update_file(filepath):
                print(f"  [O] {filename}")
            else:
                print(f"  [-] {filename}")
    print("完成!")

if __name__ == '__main__':
    main()
