from pathlib import Path
from pypdf import PdfReader, PdfWriter


def merge_pdfs_alternating(
    pdf1_path="1.pdf",
    pdf2_path="2.pdf",
    output_path="merged.pdf",
):
    """
    Merge two PDFs with the same number of pages in the following order:

        page 1 of PDF 1
        page N of PDF 2
        page 2 of PDF 1
        page N-1 of PDF 2
        ...
        page N of PDF 1
        page 1 of PDF 2

    Parameters
    ----------
    pdf1_path : str
        Path to the first input PDF.

    pdf2_path : str
        Path to the second input PDF.

    output_path : str
        Path to the output merged PDF.
    """

    pdf1_path = Path(pdf1_path)
    pdf2_path = Path(pdf2_path)
    output_path = Path(output_path)

    if not pdf1_path.exists():
        raise FileNotFoundError(f"Could not find {pdf1_path}")

    if not pdf2_path.exists():
        raise FileNotFoundError(f"Could not find {pdf2_path}")

    reader1 = PdfReader(str(pdf1_path))
    reader2 = PdfReader(str(pdf2_path))

    n1 = len(reader1.pages)
    n2 = len(reader2.pages)

    if n1 != n2:
        raise ValueError(
            f"The PDFs must have the same number of pages. "
            f"{pdf1_path} has {n1} pages, while {pdf2_path} has {n2} pages."
        )

    writer = PdfWriter()

    n = n1

    for i in range(n):
        # Add page i from PDF 1: 0, 1, 2, ..., N-1
        writer.add_page(reader1.pages[i])

        # Add page N-1-i from PDF 2: N-1, N-2, ..., 0
        writer.add_page(reader2.pages[n - 1 - i])

    with open(output_path, "wb") as output_file:
        writer.write(output_file)

    print(f"Created merged PDF: {output_path}")
    print(f"Total pages: {2 * n}")


if __name__ == "__main__":
    merge_pdfs_alternating()