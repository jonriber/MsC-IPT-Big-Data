import os
import json
import pdfplumber
import uuid

def get_publication_date(metadata):
    date = metadata.get('CreationDate', '')
    return date

def generate_unique_id():
    return str(uuid.uuid4())

def extract_info_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        

        print("stating to extract info from pdf")
        info = {}
        info['id'] = generate_unique_id()
        info['authors'] = pdf.metadata.get('Author', '')
        info['title'] = pdf.metadata.get('Title', '')
        info['abstract'] = ''
        info['publication_date'] = get_publication_date(pdf.metadata)
        for page in pdf.pages:
            text = page.extract_text()
            if 'abstract' in text.lower():
                # Assuming abstract starts with the word "Abstract"
                abstract_index = text.lower().find('abstract')
                abstract = text[abstract_index:]
                info['abstract'] += abstract
        return info

if __name__ == '__main__':

    pdf_folder = 'PROJECTS/PROJ1/pdf_source'
    output_data = []

    for file_name in os.listdir(pdf_folder):
        if file_name.endswith('.pdf'):
            print("pdf file found", file_name)
            pdf_path = os.path.join(pdf_folder, file_name)
            info = extract_info_from_pdf(pdf_path)
            output_data.append(info)
    print("output_data:",output_data)        
    output_file = 'extracted_info.json'
    with open(output_file, 'w') as json_file:
        json.dump(output_data, json_file, indent=4)
        
    print(f"Extracted information saved to {output_file}")