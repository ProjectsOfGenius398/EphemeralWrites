#This only works for one stanza at a time. Will be optimized soon

def format_text_with_br():
    print("Enter your text (press Enter twice to end input):")
    
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    
    formatted_text = "<br>".join(lines)
    return formatted_text

formatted_text = format_text_with_br()
print("\nFormatted text for HTML:\n")
print(formatted_text)
