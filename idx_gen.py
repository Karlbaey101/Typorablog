import os
import json

os.chdir(r"E:/Repository/Typorablog/blog")

BLOG_DIR = os.getcwd()
OUTPUT_JSON = "blog_index.json"

def build_blog_index():
    entries = []
    for filename in sorted(os.listdir(BLOG_DIR)):
        if filename.endswith(".html"):
            title = filename[:-5]  # 去掉 ".html"
            entries.append({
                "title": title,
                "url": f"/blog/{filename}"
            })
    return entries

def save_json(data, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    index = build_blog_index()
    save_json(index, OUTPUT_JSON)
    print(f"✅ 生成 {len(index)} 项，已保存为 {OUTPUT_JSON}")
