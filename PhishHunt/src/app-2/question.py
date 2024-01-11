def main():
    questions = [
        {
            "question": "Apa nilai md5 dari file lampiran?",
            "format": "abc....z"
        },
        { 
            "question": "Apa nama file didalam file lampiran?",
            "format": "File.ext (Sensitive Case)"
        },
        { 
            "question": "Apa nama asli file tersebut?",
            "format": "File.ext (Sensitive Case)"
        },
        { 
            "question": "Malware jenis apa file tersebut?",
            "format": "virus (Sensitive Case)"
        },
        { 
            "question": "Apa nama domain yang berkomunikasi dengan malware?",
            "format": "domain1.com,domain2.com"
        },
    ]

    answers = [
        "f667f7c0f470a550b6cfbce4236b3be4",
        "PO.pdf.exe",
        "ZySG.exe",
        "trojan",
        "api.ipify.org,api4.ipify.org",
    ]

    print("Please answer the provided questions:")

    correct_answers = 0

    for index, q in enumerate(questions, start=1):
        print(f"\nQ{index}:")
        print("Question: " + q["question"])
        print("Format: " + q["format"])
        user_answer = input("Answer: ")

        if user_answer.strip() == answers[index - 1].lower():
            correct_answers += 1
            print("Correct")
        else:
            print("Incorrect")
            return
    
    if correct_answers == len(questions):
        print("\nCongrats! Flag: CTFITB{p4rT_2_r34L_F0r&6_M4$T3r_Aku_Padamu_MAS_MBAK}")

if __name__ == "__main__":
    main()