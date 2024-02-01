# # from googletrans import Translator

# # def translate_to_spanish(input_language, input_text):
# #     try:
# #         translator = Translator()
# #         translated_text = translator.translate(input_text, src=input_language, dest='es')
# #         return translated_text.text
# #     except Exception as e:
# #         print("An error occurred. Please try again.")

# # input_language = 'en'
# # input_text = "Hello, how are you?"

# # print(translate_to_spanish(input_language, input_text))

# #  Source: assistant
# # Destination: user

# #  Yes, you can do that for some languages with Python libraries that support Machine Learning and NLP.
# # Libraries like NLTK (Natural Language Toolkit), polyglot and TextBlob offer some functionally like this.
# # Here's a example of how you can use these libraries to do so.
# # If desirable, any of these libraries could be called or used through your 'translate_to_spanish' function:

# # # ```python
# # import nltk
# # nltk.download('punkt')
# # nltk.download('averaged_perceptron_tagger')
# # nltk.download('words')

# # from nltk.stem import WordNetLemmatizer
# # from nltk.corpus import wordnet

# # lemmatizer = WordNetLemmatizer()

# # def translate_to_spanish(text):
# #     tokens = nltk.word_tokenize(text)
# #     translated_words = [' '.join(translate(w)) for w in tokens]
# #     translated_sentence = ' '.join(transl


# #  Source: assistant
# # Destination: user

# #  Ah, that's a great idea! Using the translate_to_spanish function we created earlier, we can create a new function called `translate_list_of_texts` that accepts a list of texts and two desired languages and returns two lists with the translated texts. This function will handle both English to Spanish and English to Portuguese translations. Here is an implementation:

# # ```python
# from googletrans import Translator

# def translate_to_spanish(input_language, input_text):
#     try:
#         translator = Translator()
#         translated_text = translator.translate(input_text, src=input_language, dest='es')
#         return translated_text.text
#     except Exception as e:
#         print("An error occurred. Please try again.")

# def translate_to_portuguese(input_language, input_text):
#     try:
#         translator = Translator()
#         translated_text = translator.translate(input_text, src=input_language, dest='pt')
#         return translated_text.text
#     except Exception as e:
#         print("An error occurred. Please try again.")

# def translate_list_of_texts(text_list, lang1, lang2):
#     spanish_translations = []
#     portuguese_translations = []
#     for text in text_list:
#         spanish_translations.append(translate_to_spanish(lang1, text))
#         portuguese_translations.append(translate_to_portuguese(lang1, text))
#     return (spanish_translations, portuguese_translations)

# # Test:
# text_list = ["Hello", "Good morning", "How are you?"]
# print(translate_list_of_texts(text_list, 'en', 'es'))
# # ```

# # Please note that googletrans has some usage limits per day. If you want to translate a long list of texts, consider increasing the time interval between each translation request, or consider switching to a paid translation service.

# # Let's go through this function:

# # * We created two new helper functions: `translate_to_spanish` and `translate_to_portuguese`.
# # * `translate_list_of_texts` takes a list of texts and two target languages, and returns two lists containing the translated texts. It will iterate through the list of texts and use `translate_to_spanish` and `translate_to_portuguese` to compute the translations.
# # * The output of the function is a tuple: (`spanish_translations`, `portuguese_translations`).

# # You can use this function for the same purpose that you mentioned earlier: Having a list of English texts, use this function to get two lists of their translations, one in Spanish and another in Portuguese. For example, if you have a mobile app, you can programmatically make API calls to these functions every time you need to update your UI with the new translations. For brevity, I'm not showing here how to call it in the context of a mobile app. 😊

#  Source: assistant
# Destination: user

#  Sure! Let's create a function that takes a list of English messages as input and returns two lists, one containing the Spanish translations and the other containing the Portuguese translations.

# ```python
from googletrans import Translator

def translate_messages(messages):
    translator = Translator()

    # Spanish translations
    spanish = [translator.translate(msg, src='en', dest='es').text for msg in messages]
    print("Spanish translations:")
    print(spanish)

    # Portuguese translations
    portuguese = [translator.translate(msg, src='en', dest='pt').text for msg in messages]
    print("Portuguese translations:")
    print(portuguese)

    return spanish, portuguese

# Test the function
messages = ["Hello, how are you?", "What is your name?", "I'm John."]
translate_messages(messages)
# ```

# This function uses list comprehension to apply the translation to each message in the input list. It then prints the translated messages in Spanish and Portuguese and returns two lists containing the translated messages.

# Note: The translation quality may be inconsistent and depends on Google Translate's service, which may have limitations, especially for longer texts. If you need more accurate translations, considering using a professional translation service or hiring a professional translator.
