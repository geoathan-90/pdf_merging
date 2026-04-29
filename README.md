
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
