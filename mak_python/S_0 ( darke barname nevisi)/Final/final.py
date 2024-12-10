from docx import Document

filename = 'E:/WORK/MAKTABKHOONEH/mak_python/Final/text.docx'
    
    #-----Reading a docx file and converting it to a string-----#
def read_file(filename):
    doc = Document(filename)
    text = "\n".join(paragraph.text for paragraph in doc.paragraphs)
    return text
text = str(read_file(filename))
print('text is:')
print (text)

    #-----Creating a dictionary to replace English numbers with Persian numbers-----#    
fa_to_en_dict = {
    '۰': '0', '۱': '1', '۲': '2', '۳': '3', '۴': '4',
    '۵': '5', '۶': '6', '۷': '7', '۸': '8', '۹': '9'
}

    #-----Translate Persian numbers to English-----#
def fa_to_en(text):
    translated = "".join(fa_to_en_dict.get(char, char) for char in text)
    #print (translated) #-----for monitoring-----#
    return translated
    
    #-----Extracting numbers and putting them into a list-----#
def extract_numbers(text):
    translated = fa_to_en(text)
    numbers = []
    current_number = ''
    for char in translated:
        if char.isdigit() or char in '.٫':  #-----Handle both . and , as decimal points-----#
            if char in '.٫':
                current_number += '.'   #-----Standardize to dot-----#
            else:
                current_number += char
        elif current_number:    #-----If we hit a non-digit and have collected a number-----#
            try:
                numbers.append(float(current_number))
                current_number = ''
            except ValueError:
                current_number = ''
                
    if current_number:  #-----last number if text ends with a number-----#
        try:
            numbers.append(float(current_number))
        except ValueError:
            pass
            
    return numbers  #-----removed unnecessary return of translated-----#

numbers = extract_numbers(text)
print("Numbers found:", numbers)    #-----Output-----#
print("Sum of numbers:", sum(numbers))  # Output: Sum of all-----#