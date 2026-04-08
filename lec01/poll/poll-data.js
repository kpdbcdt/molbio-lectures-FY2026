// Poll questions for Lec01 — extracted from Speaker Notes
// Each question has: id, slide, stem, options (4), correct (index), reveal text

export const POLLS = {
  q1: {
    id: 'q1',
    slide: 'S09',
    stem: 'ヒトの全 DNA を一直線に伸ばすと、どのくらいの長さになる？',
    options: ['2 mm', '2 cm', '2 m', '2 km'],
    correct: 2,
    reveal: '答え: C) 約 2 m。3.2×10⁹ bp × 0.34 nm/bp ≈ 1.09 m（一倍体）、二倍体で 2.2 m。直径 10 μm の核に折りたたまれている。',
  },
  q2: {
    id: 'q2',
    slide: 'S11',
    stem: 'ヒト細胞 1 個の DNA 情報量をデジタルデータに換算すると、約何ギガバイト？',
    options: ['0.015 GB', '0.15 GB', '1.5 GB', '15 GB'],
    correct: 2,
    reveal: '答え: C) 約 1.5 GB。1 塩基 = 2 bit、6.4×10⁹ bp × 2 bit ≈ 1.5 GB。HD 映画 1 本分。',
  },
  q3: {
    id: 'q3',
    slide: 'S18',
    stem: 'ヒトの遺伝子の数は約何個？',
    options: ['2,000', '20,000', '100,000', '200,000'],
    correct: 1,
    reveal: '答え: B) 約 20,000。HGP 以前は ~10 万個と予想されていたが、線虫とほぼ同数だった。複雑さは「使い方」（選択的スプライシング、PTM、調節）で生まれる。',
  },
  q4: {
    id: 'q4',
    slide: 'S38',
    stem: '1 秒に 1 塩基ずつヒトゲノムを読むと、全部読むのに何年かかる？',
    options: ['1 年', '10 年', '100 年', '1000 年'],
    correct: 2,
    reveal: '答え: C) 約 100 年。3.2×10⁹ ÷ 3.15×10⁷ 秒/年 ≈ 101.6 年。一生かけても読めないが、現代の NGS は 2 日で完了。',
  },
};
