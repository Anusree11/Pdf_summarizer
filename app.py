from flask import Flask, render_template, request
from pypdf import PdfReader
from ollama import chat
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

@app.route("/", methods=["GET", "POST"])
def home():

    summary = ""

    if request.method == "POST":

        pdf = request.files["pdf"]

        filepath = os.path.join(
            UPLOAD_FOLDER,
            pdf.filename
        )

        print("Filename:", pdf.filename)
        print("Filepath:", filepath)

        pdf.save(filepath)

        reader = PdfReader(filepath)

        text = ""

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

        response = chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    Summarize this document.

                    Tell:
                    - What it is about
                    - Main points
                    - Key conclusions

                    {text[:10000]}
                    """
                }
            ]
        )

        summary = response["message"]["content"]

    return render_template(
        "index.html",
        summary=summary
    )

if __name__ == "__main__":
    app.run(debug=True)