from pypdf import PdfReader
from summarizer import summarize

reader = PdfReader("Anusree_M_A.pdf")

text = ""

for page in reader.pages:
    text += page.extract_text()

result = summarize(text)

print(result)