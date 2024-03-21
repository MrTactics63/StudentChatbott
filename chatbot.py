import random


def answer_for_questions(question):
    questions = {
        "jak się masz?": ["Dobrze, dziękuję!", "Mam się całkiem nieźle, a Ty?", "Fantastycznie!"],
        "jak masz na imię?": ["Mam na imię MaronoBot.", "Jestem znany jako MaronoBot."],
        "co robisz?": ["Odpowiadam na Twoje pytania.", "Pracuję jako MaronoBot."],
    }

    # Odpowiedz na pytanie, jeśli znamy odpowiedź
    if question.lower() in questions:
        return random.choice(questions[question.lower()])
    else:
        return "Przepraszam, nie rozumiem pytania."

# Funkcja główna obsługująca rozmowę
def main():
    print("Witaj! Jestem prostym MaronoBotem. Jak mogę Ci pomóc?")
    while True:
        question = input("Ty: ")
        if question.lower() == 'do widzenia':
            print("MaronBot: Do widzenia! Miłego dnia!")
            break
        answer = answer_for_questions(question)
        print("MaronBot:", answer)

# Uruchomienie chatbota
if __name__ == "__main__":
    main()