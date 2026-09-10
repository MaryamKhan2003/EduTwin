import fitz


def extract_text_from_pdf(uploaded_file):

    document = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text
