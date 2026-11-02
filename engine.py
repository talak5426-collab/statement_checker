# cambridge_app-cambridge personal statement checker
import re
import streamlit as st


print("welcome to personal statement checker! ")

# Ask user for information
name = input("what's your name?")
major = input("what major/program are you applying for?")
grade = input("what's your grade?")

print("\n--- statement Analysis ---")
print(f"student:{name}")
print(f"major: {major}")
print(f"grade:{grade}")

# simple validation check
if len(major) > 3:
    print("major is clear")
else:
    print("major too short- please be more specific")

#strength
skills = input("Mention one strong skill you have:")
print(f"Great! skill {skills} is very important for your application")

# final Message
print("Next step: paste your statement to Analyze it")
text = input("\npaste your statement hear: ")
print("word count:", len(text.split()))
print("\n your first statement is done!")
GENERIC =["since i was young","i have always been passionate",
     "from a young age","ever since i was a child"] 


found = [p for p in GENERIC if p in text.lower()]
if found:
    print("GENERIC phrases to replace:")
    for p in found:
        print("-",p)
else:
    print("No generic phrases found.")

CLAIMS = ["i am hard-working","i am passionate","i am a leader",
          "i am creative","i am dedicated"]

print("\n-- Unsupported clamis check ---")
claims_found = [c for c in CLAIMS if c in text.lower()]
if claims_found:
    print("These claims need an example for a number:")
    for c in claims_found:
        print("-",c)

    else:
        print("No unsopported claims found.")

def count_words(text):
    return len(text.split())

def find_phrases(text, phrases):
    return[p for p in phrases if p in text.lower()]

def score (text):
    POINTS = 100
    POINTS -= 10*len(find_phrases(text, GENERIC))
    POINTS -= 10* len(find_phrases(text, CLAIMS))
    return max (POINTS, 0)

def show_results(title, found, OK_message):
    print(f"\n--- {title}---")
    if found:
     for p in found:
            print("-",p)
     else:
            print(OK_message)

#----------RUN the new checks----------
print("\nWord count:", count_words(text))
show_results("GENERIC phrases to replace", find_phrases(text, GENERIC),
             "No Generic phrases found.")
show_results("claims that need an example or a number", find_phrases(text, CLAIMS),
             "No unsupported claims found.") 
print(f"\nYOUR score: {score(text)}/100")




def general_checks(text):
    sentences = [s.strip()for s in re.split(r"[.!?]", text)if s.strip()]
    words = text.lower().split()

    print("\n--- General checkes ---")
    print("sentences:", len(sentences))

    avg = len(words) / max(len(sentences), 1)
    print(f"Average sentence length:{avg:.1f}words")
    if avg > 25:
        print("sentence are long, try shorter onse.")

    if not any(ch.isdigit() for ch in text):
        print("No numbers found, add facts like dates or results.")

    starts_with_i =sum (1 for s in sentences if s.lower().startswith("i "))
    if starts_with_i > len(sentences) / 2:
        print("Too many sentences start with 'I', vary your openings.")
    
    for w in set(words):
        if len(w) > 4 and words.count(w) >= 4:
            print(f"word repeated a lot: '{w}'")



#cell 4 - same engine, just as a website 


st.title("personal statement checker")
text = st.text_area("paste here:")


if st.button("check"):
    st.write(count_words(text))
    st.write(score(text))