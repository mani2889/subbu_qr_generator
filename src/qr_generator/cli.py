import argparse
from qr_generator.generator import generate_qr


def main():
    parser = argparse.ArgumentParser(
        description="Generate QR codes from text or URLs"
    )

    parser.add_argument("data", help="Text or URL to encode in QR code")
    parser.add_argument("-o", "--output", default="qrcode.png")
    parser.add_argument("--box-size", type=int, default=10)
    parser.add_argument("--border", type=int, default=4)

    args = parser.parse_args()

    output = generate_qr(
        data=args.data,
        output_file=args.output,
        box_size=args.box_size,
        border=args.border,
    )

    print(f"QR code generated: {output}")
