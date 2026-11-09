    # personal statement checker
import re
import streamlet as st 
programming_languages =[]
code_keywords = []
model = None

st.title("welcome to personal statement checker! ")

# Ask User fore information
name = st.text_input("What's your name" )
major = st.text_input("What major/program are you applying for?")
grade = st.text_input("What's your grade? ")

st.write("\n--- statement Analysis ---")
st.write(f"student:{name}")
st.write(f"major: {major}")
st.write(f"grade:{grade}")

    # simple validation check
if len(major) > 3:
        st.write("major is clear")
else:
        st.write("major too short- please be more specific")

    #strength
skills = st.text_input("Mention one strong skill you have:")
st.write(f"Great! skill {skills} is very important for your application")

    # final Message
st.write("Next step: paste your statement to Analyze it")
text = st.text_input("\npaste your statement here: ")
st.write("word count:", len(text.split()))
st.write("\n your first statement is done!")
GENERIC =["since i was young","i have always been passionate",
    "from a young age","ever since i was a child"] 


found = [p for p in GENERIC if p in text.lower()]
if found:
        st.write("GENERIC phrases to replace:")
        for p in found:
            st.write("-",p)
else:
        st.write("No generic phrases found.")

CLAIMS = ["i am hard-working","i am passionate","i am a leader",
            "i am creative","i am dedicated"]

st.write("\n-- Unsupported clamis check ---")
claims_found = [c for c in CLAIMS if c in text.lower()]
if claims_found:
    st.write("These claims need an example for a number:")
    for c in claims_found:
        st.write("-",c)

    else:
        st.write("No unsopported claims found.")

    def count_words(text):
        return len(text.split())

    def find_phrases(text, phrases):
        return [p for p in phrases if p in text.lower()]

    def score (text):
        POINTS = 100
        POINTS -= 10*len(find_phrases(text, GENERIC))
        POINTS -= 10* len(find_phrases(text, CLAIMS))
        return max (POINTS, 0)

    def show_results(title, found, OK_message):
        st.write(f"\n--- {title}---")
        if found:
            for p in found:
                st.write("-",p)
        else:
                st.write(OK_message)

    #----------RUN the new checks----------
    st.write("\nWord count:", count_words(text))
    show_results("GENERIC phrases to replace", find_phrases(text, GENERIC),
                "No Generic phrases found.")
    show_results("claims that need an example or a number", find_phrases(text, CLAIMS),
                "No unsupported claims found.") 
    st.write(f"\nYOUR score: {score(text)}/100")




    def general_checks(text):
        sentences = [s.strip()for s in re.split(r"[.!?]", text)if s.strip()]
        words = text.lower().split()

        st.write("\n--- General checkes ---")
        st.write("sentences:", len(sentences))

        avg = len(words) / max(len(sentences), 1)
        st.write(f"Average sentence length:{avg:.1f}words")
        if avg > 25:
            st.write("sentence are long, try shorter once.")

        if not any(ch.isdigit() for ch in text):
            st.write("No numbers found, add facts like dates or results.")

        starts_with_i =sum (1 for s in sentences if s.lower().startswith("i "))
        if starts_with_i > len(sentences) / 2:
            st.write("Too many sentences start with 'I', vary your openings.")
        
        for w in set(words):
            if len(w) > 4 and words.count(w) >= 4:
                st.write(f"word repeated a lot: '{w}'")



    #cell 4 - same engine, just as a website 


    st.title("personal statement checker")
    text = st.text_area("paste here:")


    if st.button("check"):
        st.write(count_words(text))
        st.write(score(text))
        
    # ==========================================================================
    # personal statement checker - version 2.0 (AI-Enhanced Edition)
    # built by TALIA KAMAL. warning: there is a license on my projects.
    # ==========================================================================

    def ai_personal_statement_checker(text):
        st.write("--- starting AI analysis(version 2.0) ---")

    # --------------------------------------------------------------------------
    # Feature 1: AI code block & full syntxs Analyzir
    # --------------------------------------------------------------------------
    programming_languages = ["python","c++","javascript","java"]
    code_keywords = ["def", "import", "while", "for", "st.write", "return", "if"]


    # AI logic to identify technical programming infrastructure in text 
    detected_languages = [lang for lang in programming_languages if lang in text.lower()] 
    detected_keywords = [kw for kw in code_keywords if kw in text.lower()] 

    if detected_keywords or detected_languages:
        # Build a detailed text analysis report for code infrastructure
        analysis_report = "--- CODE INFRASTRUCTURE ANALYSIS---\n"
        if detected_languages:
            analysis_report += "Detected Programming Languages: "+",".join(detected_languages)+"\n"
            
        if detected_keywords:
            analysis_report += "Detected syntax/keywords:",".join(detected_keywords)"

            analysis_report += "status: The text refrences opertional development environments."
            
    else:
          "No specific programming languages or development syntax keywords detected."

    if detected_keywords or detected_languages:
    

    #2. if Gemini is not connected, use your exact local report as a backup 
    analysis_report = "--- CODE INFRASTRUCTURE ANALYSIS ---\n"
    if detected_languages:
        analysis_report += "Detcted programming LANGUAGES:" + ",""join(detected_languages)"

    if detected_keywords:
 # --- LOCAL FALLBACK REPORT (Your exact comprehensive layout) ---  m
         analysis_report = "--- CODE INFRASTRUCTURE ANALYSIS ---\n" 
if detected_languages: 
    analysis_report += f"Detected Programming Languages: {', '.join(detected_languages)}\n"

if detected_keywords:
    analysis_report += f"Detected Syntax/Keywords: {', '.join(detected_keywords)}\n"
    analysis_report += "Status: The text references operational development environments." 
else:
        "No specific programming languages or development syntax keywords detected."

if __name__ == "__main__": 
    st.write("Welcome to Personal Statement Checker v2.0!")


# Run your text evaluation functions 
GENERIC = ["since i was young", "i have always been passionate",
 "from a young age", "ever since i was a child"]
CLAIMS = ["i am hard-working", "i am passionate", 
"i am a leader", "i am creative", "i am dedicated"] 

 # Streamlit Interface configuration
st.title("Personal Statement Checker - Version 2.0")
text_st_text_input = st.text_area("Paste your statement here:") 

if st.button("Check Statement"):
    st.write(f"Word count: {count_words(st.text_input)}")
    st.write (f"Score evaluation:")