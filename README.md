# 分子生物学 Interactive Labs — FY2026

慶應義塾大学薬学部 分子生物学（FY2026）の学生向け復習 Web アプリ集。
各講義ごとに、探索型ミニツールと多肢選択クイズを1ページに統合した Interactive Lab を提供する。

**公開 URL**: https://kpdbcdt.github.io/molbio-lectures-FY2026/

## コンセプト

Canvas LMS (K-LMS) のビルトインクイズは便利だが単調。
このリポジトリでは各講義ごとに **完全クライアントサイドの静的 HTML アプリ** を用意し、
Canvas Page に `<iframe>` で埋め込むことで、学生が手を動かしながら学べる環境を作る。

- サーバー不要、追跡なし、個人情報非収集
- 進捗は各ブラウザの `localStorage` に保存
- GitHub Pages による HTTPS 配信（Keio 教学系からの iframe 埋め込みに安全）

## 収録内容 (Lec 01: セントラルドグマ入門)

| タブ | 機能 |
|------|------|
| 🌍 Genome Scale Explorer | 10 生物のゲノムサイズ・遺伝子数・コーディング率を対数/線形スケールで比較 |
| 📖 Codon Decoder | mRNA 配列を 6 reading frame で翻訳、最長 ORF をハイライト、セレノシステイン候補も表示 |
| 🎯 Central Dogma Assembler | DNA/RNA/Protein + 複製/転写/翻訳を drag-and-drop で正しい順に並べる |
| 💊 Drug-Target Matcher | 8 薬剤（AZT, Rifampicin, Gentamicin, Cisplatin, Acyclovir, 5-FU, Doxycycline, Efavirenz）をセントラルドグマ各段階にマッチング |
| ✅ Quiz (10 問) | 6 問の基本問題 + 4 問の <i>Genomes 5</i> Ch.1 章末問題を多肢選択化。クリックで即時フィードバック |

## ディレクトリ構成

```
molbio-lectures-FY2026/
├── index.html          ← ランディングページ
├── README.md
├── LICENSE
├── lec01/
│   └── index.html      ← Lec 01 Interactive Lab (単一ファイル)
└── lec02..08/          ← 今後追加予定
```

## Canvas (K-LMS) への埋め込み

Canvas Page の HTML エディタに以下を貼り付け:

```html
<iframe src="https://kpdbcdt.github.io/molbio-lectures-FY2026/lec01/"
        width="100%" height="900" frameborder="0" allow="fullscreen">
</iframe>
```

## 出典

問7-10 は Brown, T.A. (2023) *Genomes 5*, CRC Press, Chapter 1
"Genomes, transcriptomes, and proteomes" の章末 Short Answer Questions を
多肢選択形式に改変したもの。

## ライセンス

[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.ja) — 教材・コードともに同一ライセンス。

- ✅ 個人学習・教育目的での利用、改変、再配布自由
- ✅ 出典明記が必要
- ❌ 営利目的での利用不可
