#Replace all empty lines with Ω symbol
print("Replace all empty lines with the Ω symbol")
def format_text_with_br():
    print("Enter your text (press Enter twice to end input):")
    
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    
    formatted_text = ""
    for line in lines:
        if "Ω" in line:
            line = line.replace("Ω", "<br><br>")
        formatted_text += line + "<br>"
    
    return formatted_text.strip("<br>")

formatted_text = format_text_with_br()
print("\nFormatted text for HTML:\n")
print(formatted_text)
