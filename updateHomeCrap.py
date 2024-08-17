import re
import sys

def update_html_file(file_path, word, definition):
    """Update the HTML file with a new word and definition."""
    try:
        # Read the current contents of the HTML file
        with open(file_path, 'r') as file:
            content = file.read()

        # Define the regex patterns to find the current word and definition
        word_pattern = r'(<h2 id="word" class="underWord" style="font-weight:500;">)(.*?)(</h2>)'
        definition_pattern = r'(<p id="wordDef" class="underWord">)(.*?)(</p>)'

        # Replace the old word and definition with the new ones
        updated_content = re.sub(word_pattern, r'\1' + word + r'\3', content)
        updated_content = re.sub(definition_pattern, r'\1' + definition + r'\3', updated_content)

        # Write the updated contents back to the file
        with open(file_path, 'w') as file:
            file.write(updated_content)

        print("HTML file updated successfully with new word and definition.")
    except Exception as e:
        print(f"Error updating HTML file: {e}")

if __name__ == '__main__':
    # Ensure the correct number of command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python updateHomeCrap.py <word> <definition>")
        sys.exit(1)

    # Get the word and definition from command-line arguments
    word = sys.argv[1]
    definition = sys.argv[2]

    # Update the HTML file with the provided word and definition
    update_html_file('index.html', word, definition)
