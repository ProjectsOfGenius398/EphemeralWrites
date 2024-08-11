import re
import random

# Word and definition list
words = [
    {"word": "Alliteration", "definition": "The repetition of consonant sounds at the beginning of words in a sentence or phrase."},
    {"word": "Assonance", "definition": "The repetition of vowel sounds within nearby words."},
    {"word": "Ballad", "definition": "A narrative poem that tells a story and is typically arranged in quatrains with a rhyme scheme."},
    {"word": "Blank Verse", "definition": "Unrhymed iambic pentameter, commonly used in English poetry."},
    {"word": "Caesura", "definition": "A pause or break within a line of poetry, often indicated by punctuation."},
    {"word": "Canto", "definition": "A division or section of a long poem."},
    {"word": "Chorus", "definition": "A repeated verse or line in a poem, similar to a refrain."},
    {"word": "Cinquain", "definition": "A five-line poem with a specific syllable or word count pattern."},
    {"word": "Couplet", "definition": "Two consecutive lines of poetry that rhyme."},
    {"word": "Dactyl", "definition": "A metrical foot consisting of one stressed syllable followed by two unstressed syllables."},
    {"word": "Dirge", "definition": "A mournful poem or song expressing grief, often for the dead."},
    {"word": "Dissonance", "definition": "A harsh or jarring combination of sounds in poetry."},
    {"word": "Elegy", "definition": "A poem of lamentation, usually for someone who has died."},
    {"word": "Enjambment", "definition": "The continuation of a sentence or phrase from one line of poetry to the next without a pause."},
    {"word": "Epigram", "definition": "A brief, witty, and often satirical poem."},
    {"word": "Epitaph", "definition": "A short poem or inscription in memory of someone who has died."},
    {"word": "Euphony", "definition": "Pleasant, harmonious sounds used in poetry."},
    {"word": "Foot", "definition": "The basic unit of measurement in a line of poetry, consisting of stressed and unstressed syllables."},
    {"word": "Free Verse", "definition": "Poetry that does not follow a regular rhyme or meter."},
    {"word": "Haiku", "definition": "A traditional Japanese three-line poem with a 5-7-5 syllable pattern."},
    {"word": "Hexameter", "definition": "A line of poetry consisting of six metrical feet."},
    {"word": "Hyperbole", "definition": "Exaggerated statements or claims not meant to be taken literally."},
    {"word": "Iamb", "definition": "A metrical foot consisting of one unstressed syllable followed by a stressed syllable."},
    {"word": "Imagery", "definition": "Descriptive language that appeals to the senses and creates mental images."},
    {"word": "Irony", "definition": "A figure of speech where the intended meaning is opposite to the literal meaning."},
    {"word": "Limerick", "definition": "A humorous five-line poem with an AABBA rhyme scheme."},
    {"word": "Lyric", "definition": "A short poem expressing personal thoughts and emotions."},
    {"word": "Metaphor", "definition": "A figure of speech that compares two unlike things without using 'like' or 'as.'"},
    {"word": "Meter", "definition": "The rhythmic structure of a line of poetry."},
    {"word": "Narrative", "definition": "A poem that tells a story with a plot and characters."},
    {"word": "Ode", "definition": "A formal, often ceremonious lyric poem that addresses and praises a person, place, or thing."},
    {"word": "Onomatopoeia", "definition": "Words that imitate the sounds they describe."},
    {"word": "Oxymoron", "definition": "A figure of speech that combines contradictory terms."},
    {"word": "Paradox", "definition": "A statement that seems contradictory but reveals a truth."},
    {"word": "Pastoral", "definition": "A poem that depicts rural life in an idealized manner."},
    {"word": "Personification", "definition": "Giving human characteristics to non-human things."},
    {"word": "Quatrain", "definition": "A stanza of four lines, often with a specific rhyme scheme."},
    {"word": "Refrain", "definition": "A repeated line or group of lines in a poem or song."},
    {"word": "Rhyme", "definition": "The repetition of similar sounds in two or more words."},
    {"word": "Rhyme Scheme", "definition": "The pattern of rhymes in a poem."},
    {"word": "Rhythm", "definition": "The pattern of stressed and unstressed syllables in a line of poetry."},
    {"word": "Sestet", "definition": "A six-line stanza or the final six lines of a sonnet."},
    {"word": "Simile", "definition": "A figure of speech comparing two things using 'like' or 'as.'"},
    {"word": "Sonnet", "definition": "A 14-line poem with a specific rhyme scheme and meter."},
    {"word": "Stanza", "definition": "A grouped set of lines within a poem, often sharing a common rhyme scheme."},
    {"word": "Symbolism", "definition": "The use of symbols to represent ideas or concepts."},
    {"word": "Synecdoche", "definition": "A figure of speech where a part represents the whole or vice versa."},
    {"word": "Tercet", "definition": "A three-line stanza or poem."},
    {"word": "Theme", "definition": "The central idea or message of a poem."},
    {"word": "Tone", "definition": "The attitude or mood conveyed by the poem."},
    {"word": "Verse", "definition": "A single line of poetry."},
    {"word": "Villanelle", "definition": "A 19-line poem with five tercets followed by a quatrain, using a specific rhyme scheme."},
    {"word": "Allegory", "definition": "A narrative that uses characters and events to symbolize broader themes or concepts."},
    {"word": "Antithesis", "definition": "A rhetorical device that contrasts opposing ideas within a balanced grammatical structure."},
    {"word": "Apostrophe", "definition": "A figure of speech in which the poet addresses an absent person, idea, or object."},
    {"word": "Archetype", "definition": "A universally recognized symbol or character that recurs across literature and art."},
    {"word": "Cacophony", "definition": "A mixture of harsh, discordant sounds used for poetic effect."},
    {"word": "Conceit", "definition": "An extended metaphor with a complex logic that governs a poetic passage or entire poem."},
    {"word": "Consonance", "definition": "The repetition of consonant sounds within or at the end of words in a sentence or phrase."},
    {"word": "Denotation", "definition": "The literal or primary meaning of a word."},
    {"word": "Diction", "definition": "The choice and use of words and phrases in poetry or writing."},
    {"word": "Epic", "definition": "A long narrative poem detailing the heroic deeds and adventures of legendary figures."},
    {"word": "Epiphany", "definition": "A moment of sudden revelation or insight experienced by a character or speaker."},
    {"word": "Epithet", "definition": "An adjective or phrase expressing a quality or attribute regarded as characteristic of a person or thing."},
    {"word": "Euphemism", "definition": "A mild or indirect word or expression substituted for one considered too harsh or blunt."},
    {"word": "Fable", "definition": "A short story or poem that typically features animals as characters and conveys a moral lesson."},
    {"word": "Figurative Language", "definition": "Language that uses figures of speech to convey meanings beyond the literal interpretation."},
    {"word": "Hyperbaton", "definition": "An inversion of the normal order of words for emphasis or poetic effect."},
    {"word": "Idiom", "definition": "A phrase or expression that has a figurative meaning different from its literal meaning."},
    {"word": "Litotes", "definition": "A figure of speech that employs understatement by using double negatives or a negation to express a positive statement."},
    {"word": "Malapropism", "definition": "The mistaken use of a word in place of a similar-sounding one, often with unintentionally amusing effect."},
    {"word": "Metonymy", "definition": "A figure of speech in which one word or phrase is substituted for another with which it is closely associated."},
    {"word": "Motif", "definition": "A recurring element, theme, or subject in a work of literature."},
    {"word": "Palindrome", "definition": "A word, phrase, or sequence of characters that reads the same backward as forward."},
    {"word": "Parody", "definition": "A humorous imitation of a particular style, genre, or work of literature."},
    {"word": "Pathetic Fallacy", "definition": "The attribution of human emotions or characteristics to inanimate objects or nature."},
    {"word": "Polyptoton", "definition": "A rhetorical device that involves the repetition of words derived from the same root."},
    {"word": "Portmanteau", "definition": "A word created by combining parts of two other words to form a new expression."},
    {"word": "Prose Poetry", "definition": "A form of poetry that combines elements of prose and poetry, often characterized by a lack of line breaks."},
    {"word": "Pun", "definition": "A play on words that exploits multiple meanings or similar sounds for humorous or rhetorical effect."},
    {"word": "Rhapsody", "definition": "An effusively enthusiastic or ecstatic expression of feeling in poetry or music."},
    {"word": "Satire", "definition": "A literary work that uses humor, irony, or ridicule to criticize or mock human vices or social institutions."},
    {"word": "Scansion", "definition": "The analysis of a poem's metrical pattern, including the identification of stressed and unstressed syllables."},
    {"word": "Soliloquy", "definition": "A speech delivered by a character alone on stage, revealing their inner thoughts and feelings."},
    {"word": "Spondee", "definition": "A metrical foot consisting of two stressed syllables."},
    {"word": "Sublime", "definition": "A quality of greatness or grandeur that inspires awe and wonder in poetry or art."},
    {"word": "Synesthesia", "definition": "A literary device that describes or associates one sense in terms of another, such as 'a loud color' or 'a sweet sound.'"},
    {"word": "Tautology", "definition": "The redundant repetition of an idea or statement using different words or phrases."},
    {"word": "Trochee", "definition": "A metrical foot consisting of a stressed syllable followed by an unstressed syllable."},
    {"word": "Vignette", "definition": "A short, descriptive piece of writing that captures a specific moment or scene in a poem."},
    {"word": "Zeugma", "definition": "A figure of speech in which a single word applies to two or more other words in different ways."}
]

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
    # Choose a random word and definition
    random_word = random.choice(words)

    # Update the HTML file with the new word and definition
    update_html_file('index.html', random_word['word'], random_word['definition'])
