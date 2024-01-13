def main():
    questions = [
        {
            "question": "Apa email pengirim?",
            "format": "someone@mail.x"
        },
        { 
            "question": "Apa email penerima?",
            "format": "someone@mail.x"
        },
        { 
            "question": "Alamat IP pengirim?",
            "format": "x.x.x.x"
        },
        { 
            "question": "Berasal dari negara mana IP pengirim?",
            "format": "nama_negara (bahasa indonesia)"
        },
        { 
            "question": "Apa nama file lampiran pada email?",
            "format": "FILE.ext"
        },
    ]

    answers = [
        "alvawensz@hlsholding.com.cn",
        "admin@starlucktech.com",
        "185.225.74.18",
        "belanda",
        "BANK DETAILS.pdf.zip",
    ]

    print("Please answer the provided questions:")

    correct_answers = 0

    for index, q in enumerate(questions, start=1):
        print(f"\nQ{index}:")
        print("Question: " + q["question"])
        print("Format: " + q["format"])
        user_answer = input("Answer: ")

        if user_answer.strip().lower() == answers[index - 1].lower():
            correct_answers += 1
            print("Correct")
        else:
            print("Incorrect")
            return
    
    if correct_answers == len(questions):
        print("\nCongrats! Flag: CTFITB24{r34L_F0r&6_M4$T3r_P4rT1}")

if __name__ == "__main__":
    main()