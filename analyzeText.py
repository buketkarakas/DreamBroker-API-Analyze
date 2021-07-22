
def analyze_text_length(txt):
    """ Analyze the text length with and without space and return it in an object"""
    length_with_spaces = len(txt)
    temp_txt = txt.replace(" ","")
    #print("Removed white spaces",temp_txt) #DEBUG
    length_without_spaces = len(temp_txt)

    return {
        "withSpaces": length_with_spaces,
        "withoutSpaces": length_without_spaces
        }

def count_words(txt):
    """Count the words in a text and return it"""
    total_word_num = len(txt.split())
    #print("Total word number:", total_word_num) #DEBUG
    return total_word_num

def count_characters(txt):
    english_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    adjusted_txt = txt.lower()
    result = []

    for letter in english_alphabet:
        if letter in adjusted_txt:
            num_of_occurence = adjusted_txt.count(letter)
            result.append({letter: num_of_occurence})
    
    #print("Result array for chars:", result) #DEBUG

    return result


def lambda_handler(event, context):
    text = event.get("text")
    if text == None:
        return{
            "message" : "Something wrong with the request data!" 
        }
    
    text_length = analyze_text_length(text)
    word_count = count_words(text)
    character_count = count_characters(text)

    return {
        "textLength":text_length,
        "wordCount": word_count,
        "characterCount": character_count
    }

print(count_characters("Hello my friend!!!!!!"))