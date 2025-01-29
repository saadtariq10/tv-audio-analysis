# import spacy
# # Load spaCy's pre-trained model for NER
# NER = spacy.load("en_core_web_sm")

# def extract_company_name_from_text(text):
#     """
#     Extracts company names (ORG entities) from the transcribed text using spaCy NER.
#     """
#     doc = NER(text)  # Run NER on the transcribed text
#     companies = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
#     return companies






import spacy
# Load spaCy's pre-trained model for NER from the models folder
nlp = spacy.load("models/en_core_web_sm/en_core_web_sm-3.8.0")

def extract_company_name_from_text(text):
    """
    Extracts company names (ORG entities) from the transcribed text using spaCy NER.
    """
    doc = nlp(text)  # Run NER on the transcribed text
    companies = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
    return companies

