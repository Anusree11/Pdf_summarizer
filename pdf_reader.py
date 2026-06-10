from pypdf import PdfReader
reader = PdfReader("Anusree_M_A.pdf")

text = ""

for page in reader.pages:
    text+=page.extract_text()

print(text[:1000])