# NBA Writer 🏀

GitHubのIssuesから自動的にNBA記事を生成するシステムです。Claude AIを活用して、様々なスタイルでNBAに関する記事を自動生成します。

## 🌟 特徴

- **自動記事生成**: GitHubのIssueを作成するだけで、自動的に記事が生成されます
- **複数のスタイル対応**: ミルクボーイ風漫才、解説記事、ランキング形式など、様々なスタイルで記事を作成
- **Claude AI搭載**: Anthropic Claude APIを使用した高品質な記事生成
- **完全自動化**: GitHub Actionsによる自動コミット・プッシュ

## 🚀 使い方

### 1. 記事生成リクエストの作成

1. このリポジトリの **Issues** タブに移動
2. **New Issue** をクリック
3. **記事生成リクエスト** テンプレートを選択
4. フォームに必要事項を記入：
   - **トピック**: 記事のテーマ（例：ステフィン・カリーの3ポイント革命）
   - **記事のスタイル**: お好みのスタイルを選択
     - ミルクボーイ風漫才
     - 解説記事
     - ランキング形式
     - インタビュー形式
     - 統計分析
   - **詳細・要望**: 記事に含めたい内容や特別な要望
   - **タグ**: 記事に付けるタグ
   - **カテゴリー**: 記事のカテゴリー
5. **Submit new issue** をクリック

### 2. 自動生成を待つ

- Issueを作成すると、GitHub Actionsが自動的に起動します
- 数分後、記事が `articles/` ディレクトリに生成されます
- 生成が完了すると、Issueに通知コメントが追加されます
- Issueは自動的にクローズされます

### 3. 記事を確認

生成された記事は `articles/` ディレクトリで確認できます。

## ⚙️ セットアップ

このシステムを自分のリポジトリで使用する場合：

### 1. Anthropic API Keyの設定

1. [Anthropic Console](https://console.anthropic.com/) でAPI Keyを取得
2. GitHubリポジトリの **Settings** > **Secrets and variables** > **Actions** に移動
3. **New repository secret** をクリック
4. 以下のシークレットを追加：
   - Name: `ANTHROPIC_API_KEY`
   - Value: あなたのAnthropic API Key

### 2. リポジトリのパーミッション設定

1. リポジトリの **Settings** > **Actions** > **General** に移動
2. **Workflow permissions** セクションで以下を選択：
   - ✅ **Read and write permissions**
   - ✅ **Allow GitHub Actions to create and approve pull requests**
3. **Save** をクリック

## 📁 ディレクトリ構造

```
NBA_Writer/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── article_request.yml     # 記事生成リクエストのテンプレート
│   └── workflows/
│       └── generate-article.yml    # GitHub Actionsワークフロー
├── articles/                       # 生成された記事が保存されるディレクトリ
│   └── *.md                       # 記事ファイル
├── scripts/
│   └── generate_article.py        # 記事生成スクリプト
├── requirements.txt               # Python依存関係
└── README.md                      # このファイル
```

## 🛠️ 技術スタック

- **GitHub Actions**: ワークフロー自動化
- **Python 3.11**: 記事生成スクリプト
- **Anthropic Claude API**: AI記事生成
- **Markdown**: 記事フォーマット

## 📝 記事の例

既存の記事は `articles/` ディレクトリで確認できます：

- [NBA史上最も影響力のある選手Top10【ミルクボーイ風解説】](articles/nba-top-10-players-milkboy-style.md)

## 🎨 スタイルの説明

### ミルクボーイ風漫才
お笑いコンビ「ミルクボーイ」の漫才形式で、NBAの選手やトピックを楽しく解説します。

### 解説記事
従来の解説記事形式で、詳細な分析と情報を提供します。

### ランキング形式
Top 10などのランキング形式で選手や試合を紹介します。

### インタビュー形式
架空のインタビュー形式で選手の視点から物語を展開します。

### 統計分析
データと統計を中心に、客観的な分析を提供します。

## 🤝 貢献

問題や改善提案がある場合は、Issueを作成してください。

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 🔗 関連リンク

- [Anthropic Claude API Documentation](https://docs.anthropic.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

---

**楽しいNBA記事ライフを！** 🏀✨
