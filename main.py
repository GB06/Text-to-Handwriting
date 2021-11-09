import pywhatkit

text = input("Enter your text: ")

pywhatkit.text_to_handwriting(text, "handwriting.png", [0,179,255])