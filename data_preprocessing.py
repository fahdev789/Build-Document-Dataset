import os
import json
import pandas as pd
import pdfminer.high_level
import docx
import fitz  # PyMuPDF

DATA_DIR = "parsed_docs/"

def extract_text_from_pdf(pdf_path):
    return pdfminer.high_level.extract_text(pdf_path)

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_txt(txt_path):
    with open(txt_path, "r", encoding="utf-8") as file:
        return file.read()

def write_parsed_docs(parsed_docs, jsonl_path):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(jsonl_path, "w", encoding="utf-8") as file:
        for doc in parsed_docs:
            file.write(json.dumps(doc) + "\n")

def load_and_parse_documents(doc_paths):
    parsed_docs = []
    for doc_id, doc_path in enumerate(doc_paths, start=1):
        file_ext = os.path.splitext(doc_path)[1].lower()
        if file_ext == ".pdf":
            text = extract_text_from_pdf(doc_path)
        elif file_ext == ".docx":
            text = extract_text_from_docx(doc_path)
        elif file_ext == ".txt":
            text = extract_text_from_txt(doc_path)
        else:
            continue
        parsed_docs.append({"doc_id": doc_id, "text": text})
    return parsed_docs

