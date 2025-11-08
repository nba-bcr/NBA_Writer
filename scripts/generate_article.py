#!/usr/bin/env python3
"""
NBA記事生成スクリプト

GitHub Issueから情報を抽出して、Claude APIを使ってNBA記事を生成します。
"""

import os
import sys
import json
import re
from datetime import datetime
from anthropic import Anthropic

def parse_issue_body(issue_body):
    """
    Issueのボディから情報を抽出
    """
    data = {
        'topic': '',
        'style': 'ミルクボーイ風漫才',
        'details': '',
        'tags': 'NBA, バスケットボール',
        'category': 'NBA分析'
    }

    # トピックの抽出
    topic_match = re.search(r'### トピック\s*\n\s*(.+)', issue_body)
    if topic_match:
        data['topic'] = topic_match.group(1).strip()

    # スタイルの抽出
    style_match = re.search(r'### 記事のスタイル\s*\n\s*(.+)', issue_body)
    if style_match:
        data['style'] = style_match.group(1).strip()

    # 詳細の抽出
    details_match = re.search(r'### 詳細・要望\s*\n\s*(.+?)(?=\n###|\Z)', issue_body, re.DOTALL)
    if details_match:
        data['details'] = details_match.group(1).strip()

    # タグの抽出
    tags_match = re.search(r'### タグ\s*\n\s*(.+)', issue_body)
    if tags_match:
        data['tags'] = tags_match.group(1).strip()

    # カテゴリーの抽出
    category_match = re.search(r'### カテゴリー\s*\n\s*(.+)', issue_body)
    if category_match:
        data['category'] = category_match.group(1).strip()

    return data


def generate_article_with_claude(topic, style, details, category):
    """
    Claude APIを使って記事を生成
    """
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY環境変数が設定されていません")

    client = Anthropic(api_key=api_key)

    # プロンプトの構築
    prompt = f"""あなたはNBAに詳しいプロのライターです。以下の条件で記事を書いてください。

トピック: {topic}
スタイル: {style}
カテゴリー: {category}
"""

    if details:
        prompt += f"\n追加の要望:\n{details}\n"

    prompt += """
記事の要件:
- 日本語で書いてください
- 読者が楽しめる内容にしてください
- 正確な情報を含めてください
- 適切な見出しと構成を使ってください
- Markdown形式で出力してください（タイトル、日付、著者、タグなどのメタデータは含めないで、本文のみ）

それでは記事本文を書いてください:
"""

    # Claude APIで記事生成
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text


def create_filename(topic):
    """
    トピックからファイル名を生成
    """
    # 日本語を英語に変換（簡易版）
    # 実際にはより洗練された変換が必要かもしれません
    filename = topic.lower()
    filename = re.sub(r'[^\w\s-]', '', filename)
    filename = re.sub(r'[-\s]+', '-', filename)
    filename = filename[:50]  # ファイル名を短くする

    # 日付を追加
    date_str = datetime.now().strftime('%Y%m%d')
    filename = f"{date_str}-{filename}.md"

    return filename


def save_article(content, topic, tags, category):
    """
    記事をMarkdownファイルとして保存
    """
    # ファイル名の生成
    filename = create_filename(topic)
    filepath = os.path.join('articles', filename)

    # メタデータの作成
    metadata = f"""---
title: "{topic}"
date: {datetime.now().strftime('%Y-%m-%d')}
author: NBA Writer
tags: [{tags}]
category: {category}
description: "{topic}についてのNBA記事"
---

"""

    # ファイルに書き込み
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(metadata)
        f.write(content)

    return filepath


def main():
    """
    メイン処理
    """
    # GitHub Actionsから渡される環境変数を取得
    issue_body = os.getenv('ISSUE_BODY', '')
    issue_title = os.getenv('ISSUE_TITLE', '')

    if not issue_body:
        print("Error: ISSUE_BODY環境変数が設定されていません")
        sys.exit(1)

    print(f"記事生成開始: {issue_title}")
    print("=" * 60)

    # Issueから情報を抽出
    data = parse_issue_body(issue_body)

    print(f"トピック: {data['topic']}")
    print(f"スタイル: {data['style']}")
    print(f"カテゴリー: {data['category']}")
    print("-" * 60)

    # 記事を生成
    print("Claude APIで記事を生成中...")
    article_content = generate_article_with_claude(
        data['topic'],
        data['style'],
        data['details'],
        data['category']
    )

    # 記事を保存
    filepath = save_article(
        article_content,
        data['topic'],
        data['tags'],
        data['category']
    )

    print(f"記事を保存しました: {filepath}")
    print("=" * 60)
    print("完了！")

    # GitHub Actionsの出力として設定
    if os.getenv('GITHUB_OUTPUT'):
        with open(os.getenv('GITHUB_OUTPUT'), 'a') as f:
            f.write(f"article_path={filepath}\n")
            f.write(f"article_title={data['topic']}\n")


if __name__ == '__main__':
    main()
