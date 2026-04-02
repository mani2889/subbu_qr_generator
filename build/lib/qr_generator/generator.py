from pathlib import Path
import qrcode


def generate_qr(
    data: str,
    output_file: str | Path = "qrcode.png",
    version: int | None = None,
    box_size: int = 10,
    border: int = 4,
) -> Path:
    output_path = Path(output_file)

    qr = qrcode.QRCode(
        version=version,
        box_size=box_size,
        border=border,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)

    return output_path
