"""Generate QR code PNGs for Lec04 poll questions.

Each QR encodes the student URL with ?q=N parameter.
Output: qr_q1.png ... qr_q3.png in the same directory.
Also generates qr_with_label_qN.png with question text below the QR.
"""
import os
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image, ImageDraw, ImageFont

BASE_URL = "https://kpdbcdt.github.io/molbio-lectures-FY2026/lec04/poll/student.html"
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

QUESTIONS = {
    1: ("S04", "ヒトゲノム複製のエラー率"),
    2: ("S09", "大腸菌の全ゲノム複製時間"),
    3: ("S21", "あなたの DNA に蓄積した変異"),
}


def find_font(size):
    candidates = [
        "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for c in candidates:
        if os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                pass
    return ImageFont.load_default()


def make_qr(url):
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_H,
        box_size=14,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    return qr.make_image(fill_color="#1a2633", back_color="white").convert("RGB")


def make_labeled(qnum, slide, question_text, qr_img):
    W, H = 900, 1100
    canvas = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(canvas)

    draw.rectangle([(0, 0), (W, 130)], fill="#2b6cb0")
    f_lec = find_font(22)
    f_title = find_font(38)
    f_q = find_font(30)
    f_url = find_font(18)
    f_inst = find_font(24)

    draw.text((40, 30), "分子生物学 LEC 04 · Slide " + slide, font=f_lec, fill="white")
    draw.text((40, 65), f"いきなり質問 #{qnum}", font=f_title, fill="white")

    draw.text((40, 160), question_text, font=f_q, fill="#1a2633")

    draw.text((40, 220), "スマホのカメラで QR を読み取って回答して下さい", font=f_inst, fill="#5a6978")

    qr_resized = qr_img.resize((640, 640))
    qr_x = (W - 640) // 2
    qr_y = 280
    canvas.paste(qr_resized, (qr_x, qr_y))

    url = f"{BASE_URL}?q={qnum}"
    draw.text((40, 970), "URL:", font=f_lec, fill="#5a6978")
    draw.text((100, 968), url, font=f_url, fill="#5a6978")

    draw.text((40, 1030), "FY2026 · 慶應義塾大学薬学部", font=f_lec, fill="#94a3b8")
    draw.text((40, 1060), "匿名投票・個人情報収集なし", font=f_lec, fill="#94a3b8")

    return canvas


def make_lab_qr_slide():
    """Generate a QR code slide pointing to the main Lec04 Interactive Lab."""
    url = "https://kpdbcdt.github.io/molbio-lectures-FY2026/lec04/"
    qr_img = make_qr(url)
    W, H = 1200, 1200
    canvas = Image.new("RGB", (W, H), "white")
    draw = ImageDraw.Draw(canvas)

    draw.rectangle([(0, 0), (W, 160)], fill="#2e8b57")
    f_lec = find_font(26)
    f_title = find_font(48)
    f_sub = find_font(34)
    f_url = find_font(20)
    f_inst = find_font(28)

    draw.text((50, 35), "分子生物学 LEC 04 — 講義後の復習", font=f_lec, fill="white")
    draw.text((50, 80), "Interactive Lab", font=f_title, fill="white")

    draw.text((50, 200), "3 つのミニツール + 12 問の復習クイズ", font=f_sub, fill="#1a2633")
    draw.text((50, 260), "  Chromatin Compaction Calculator", font=f_inst, fill="#5a6978")
    draw.text((50, 305), "  Genome Composition Explorer", font=f_inst, fill="#5a6978")
    draw.text((50, 350), "  Gene Architecture Visualizer + 国試クイズ", font=f_inst, fill="#5a6978")

    qr_resized = qr_img.resize((720, 720))
    qr_x = (W - 720) // 2
    qr_y = 410
    canvas.paste(qr_resized, (qr_x, qr_y))

    draw.text((50, 1140), f"URL:  {url}", font=f_url, fill="#5a6978")

    out = os.path.join(OUT_DIR, "qr_lec04_lab_slide.png")
    canvas.save(out)
    print(f"Lab landing: {url}")
    print(f"  → {out}")


def main():
    for qnum, (slide, qtext) in QUESTIONS.items():
        url = f"{BASE_URL}?q={qnum}"
        qr_img = make_qr(url)
        plain_path = os.path.join(OUT_DIR, f"qr_q{qnum}.png")
        qr_img.save(plain_path)
        labeled = make_labeled(qnum, slide, qtext, qr_img)
        labeled_path = os.path.join(OUT_DIR, f"qr_q{qnum}_slide.png")
        labeled.save(labeled_path)
        print(f"Q{qnum}: {url}")
        print(f"  → {plain_path}")
        print(f"  → {labeled_path}")
    make_lab_qr_slide()


if __name__ == "__main__":
    main()
