import re

def load_sample_text(filename):
    with open(filename, 'r') as file:
        return file.read()
    
#Regex function to filter needed elements
# 1. Extracting Email Addresses
def extract_Emails(Emails):
    Emails_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    return re.findall(Emails_pattern, Emails)




# Main function to load the text and run the extractions
def main():
    # Load the sample text from the file
    sample_text = load_sample_text('sample_text.txt')

    # Extract and print different types of data

    print()
    print("Extracted Emails:", extract_Emails(sample_text))
    print()
 
  

if __name__ == '__main__':
    main()
