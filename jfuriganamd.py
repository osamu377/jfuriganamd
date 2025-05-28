import sys
from janome.tokenizer import Tokenizer
import jaconv
import re

def add_ruby_to_kanji(text):
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(text)
    
    result = []
    for token in tokens:
        surface = token.surface
        reading = token.reading
        # ルビを付ける条件: 漢字が含まれ、読みが'*'でない場合
        if re.search(r'[一-龯]', surface) and reading != '*':
            hiragana = jaconv.kata2hira(reading)
            # print(f"{surface}:{reading}:{hiragana}")  # デバッグ用の出力
            result.append(f'<ruby>{surface}<rt>{hiragana}</rt></ruby>')
        else:
            result.append(surface)
    
    return ''.join(result)

# コマンドライン引数から入力ファイル名を取得
if len(sys.argv) < 2:
    print("使い方: python add_ruby.py 入力ファイル名")
    sys.exit(1)

input_file = sys.argv[1]
output_file = input_file.replace('.md', 'フリガナ.md')

# Markdownファイルの読み込み
with open(input_file, 'r', encoding='utf-8') as file:
    content = file.read()

# ルビを付ける
annotated_content = add_ruby_to_kanji(content)

# 新しいMarkdownファイルとして保存
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(annotated_content)

print(f"ルビ付きのMarkdownファイルを作成しました: {output_file}")