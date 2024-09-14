import re

def load_sample_text(filename):
    with open(filename, 'r') as file:
        return file.read()
    
#Regex function to filter needed elements
# 1. Extracting Email Addresses
def extract_Emails(Emails):
    Emails_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    return re.findall(Emails_pattern, Emails)

# 2. Extracting URLs
def extract_urls(text):
    url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
    return re.findall(url_pattern, text)

# 3. Extracting Phone Numbers (various formats)
def extract_phone_numbers(text):
    phone_pattern = r'(\(?\d{3}\)?[\s.-]?)?\d{3}[\s.-]?\d{4}'
    return re.findall(phone_pattern, text)

# 4. Extracting Credit Card Numbers
def extract_credit_cards(text):
    credit_card_pattern = r'(\d{4}[-\s]?){3}\d{4}'
    return re.findall(credit_card_pattern, text)

# 5. Extracting HTML Tags
def extract_html_tags(text):
    html_tag_pattern = r'</?[a-zA-Z][a-zA-Z0-9\-]*(\s+[a-zA-Z\-]+(\s*=\s*(".*?"|\'.*?\'|[^\s>]+))?)*\s*/?>'
    return re.findall(html_tag_pattern, text)


# Main function to load the text and run the extractions
def main():
    # Load the sample text from the file
    sample_text = load_sample_text('sample_text.txt')

    # Extract and print different types of data

    print()
    print("Extracted Emails:", extract_Emails(sample_text))
    print()
    print("Extracted URLs:", extract_urls(sample_text))
    print()
    print("Extracted Phone Numbers:", extract_phone_numbers(sample_text))
    print()
    print("Extracted Credit Card Numbers:", extract_credit_cards(sample_text))
    print()
    print("Extracted HTML Tags:", extract_html_tags(sample_text))
  

if __name__ == '__main__':
    main()
