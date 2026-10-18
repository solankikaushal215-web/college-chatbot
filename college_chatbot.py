
print("====================================")
print("       COLLEGE HELP CHATBOT")
print("====================================")
print("Hello! Welcome to College Help Chatbot.")
print("You can ask about courses, fees, timing, exams, and library.")
print("Type 'bye' to exit the chatbot.")

while True:
    user = input("\nYou: ").lower().strip()

    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif "course" in user:
        print("Bot: Please contact your college office for the list of available courses.")

    elif "fee" in user:
        print("Bot: For fee details and payment information, please contact the college accounts department.")

    elif "timing" in user or "time" in user:
        print("Bot: Please check your college timetable for the latest class timings.")

    elif "exam" in user:
        print("Bot: Please check the official college notice or student portal for examination details.")

    elif "library" in user:
        print("Bot: The college library provides books and study resources to students. Please check the library schedule.")

    elif "admission" in user:
        print("Bot: For admission details, eligibility, and required documents, please contact the admission office.")

    elif "contact" in user or "office" in user:
        print("Bot: Please visit your college's official website to find office contact details.")

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Thank you for using College Help Chatbot. Goodbye!")
        break

    else:
        print("Bot: Sorry, I did not understand that question.")
        print("Bot: Try asking about courses, fees, timing, exams, library, or admission.")
