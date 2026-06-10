from ollama import chat

def summarize(text):

    prompt = f"""

    Read the following document.

    Explain:
    1. What type of documetn is this
    2. Main topic 
    3. key points
    4. Short summary

    Document:

    {text[:1000]}
    
    """

    response = chat(
        model = "llama3.2",
        messages=[
            {"role": "user",
             "content": prompt}
        ])
    
    return response["message"]["content"]