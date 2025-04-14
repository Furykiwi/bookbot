def word_count (book_text):
    """Counts words in a string provided"""
    return len(book_text.split())  

def count_char (book_text):
    """counts all the characters in the string provided and adds the valie to the character in a dictionary"""
    char_dict = {}
    for c in book_text.lower():
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
        
    return char_dict

def sort_on (dict):
    return dict["Number"]

def sort_list (char_dict):
    """Takes a dictionary and turns into report for readability"""
    report_list = []
    for k in char_dict:
        report_list.append({"Character":k, "Number":char_dict[k]})
    report_list.sort(reverse=True, key=sort_on)
    return report_list
