import re

def cleanTXT(text):
    text = re.sub(r'\s+', ' ', text).strip() # remove whitespaces
    text = re.sub(r'(?i)home furniture|dining chairs|dining tables|mattresses|privacy policy|cookie policy|terms of service', '', text) # remove unrelevant sections
    text = re.sub(r'(?i)contact us|about us|privacy policy|cookie policy|terms of service', '', text) # remove unrelevant sections
    text = re.sub(r'[\t\n\r]', ' ', text) # remove tabs, newlines, and carriage returns
    return text

def cleanTXTfile(inputFile, outputFile):
    seen_lines = set()
    with open(inputFile, 'r') as inFile, open(outputFile, 'w') as outFile:
        for line in inFile:
            cleanedLine = cleanTXT(line)
            if cleanedLine.strip() and cleanedLine not in seen_lines:
                outFile.write(cleanedLine + '\n')
                seen_lines.add(cleanedLine)

input_path = "../data/output_furniture_stores_pages.txt"  # Path to your raw output file
output_path = "../data/cleaned_furniture_stores_pages.txt"  # Where to save the cleaned data
cleanTXTfile(input_path, output_path)