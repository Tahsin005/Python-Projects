import random

print("🔤 WORD SCRAMBLER 🔤")

while True:
    word = input("\nEnter a word to scramble (or 'quit'):")
    if word.lower() == "quit":
        print("👋 Goodbye!")
        break

    letters = list(word)
    random.shuffle(letters)
    print(f"Scrambled: {"".join(letters)}")
