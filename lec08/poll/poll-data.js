// Poll questions for Lec08 — 組換え DNA とゲノム編集
// q1-q3: いきなり質問

export const POLLS = {
  q1: {
    id: 'q1',
    slide: 'S04',
    stem: '制限酵素 EcoRI の「Eco」の部分は何を表している？',
    options: [
      'A) 発見者の名前 (Edward Cohen)',
      'B) 切断するDNA配列 (Eco-site)',
      'C) 酵素が見つかった細菌 (Escherichia coli)',
      'D) 酵素の分子量 (Eco kDa)',
    ],
    correct: 2,
    reveal: '答え: C) Escherichia coli。EcoRI = Escherichia coli, strain R, 最初(I)に発見された制限酵素。BamHI なら Bacillus amyloliquefaciens H 株の I 番目、HindIII なら Haemophilus influenzae d 株の III 番目。名前だけで「どの細菌の免疫系を借りてきた酵素か」が読める。全世界で 4,000 種類以上の制限酵素が同定されており、細菌の防御機構が人類の遺伝子工学のツール箱になっている。',
  },
  q2: {
    id: 'q2',
    slide: 'S14',
    stem: 'PCR を 30 サイクル回すと、理論上 DNA は何倍に増幅される？',
    options: [
      'A) 約 30 倍',
      'B) 約 900 倍 (30\u00B2)',
      'C) 約 100 万倍 (10\u2076)',
      'D) 約 10 億倍 (10\u2079)',
    ],
    correct: 3,
    reveal: '答え: D) 約 10 億倍。1 サイクルで 2 倍 → n サイクル後は 2\u207F 倍。2\u00B3\u2070 ≈ 1.07 × 10\u2079。たった 1 分子の DNA から 30 サイクル (≈ 2 時間) で 10 億コピー。これが PCR 検査 (COVID-19 RT-qPCR など) が 1 個のウイルス RNA からでも検出できる理由。Kary Mullis が 1983 年に着想、1993 年ノーベル化学賞。「指数関数的増幅」が分子生物学の臨床応用を根底から変えた。',
  },
  q3: {
    id: 'q3',
    slide: 'S28',
    stem: 'CRISPR-Cas9 で遺伝子をノックアウトするとき、主に利用される DNA 修復経路はどれ？',
    options: [
      'A) 塩基除去修復 (BER)',
      'B) ヌクレオチド除去修復 (NER)',
      'C) 非相同末端結合 (NHEJ)',
      'D) 相同組換え修復 (HDR)',
    ],
    correct: 2,
    reveal: '答え: C) NHEJ。Cas9 が作る二本鎖切断 (DSB) は細胞自身の修復機構で直される。NHEJ は鋳型を使わず末端をつなぐためエラーが入りやすく、indel → フレームシフト → 早期終止コドン → タンパク質が作れない → 遺伝子機能喪失。この「エラーの多さ」を逆手にとるのがノックアウト。HDR は鋳型 DNA を正確にコピーするので「ノックイン・点変異修正」に使う (S/G2 期限定で効率低)。Lec04 修復 + Lec08 応用の融合問題。',
  },
};