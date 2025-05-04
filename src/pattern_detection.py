# Load the data from the local TXT file
with open("../data/data.txt", "r") as f:
    ai_responses = [line.strip() for line in f]

# Define value clusters and their keywords
VALUE_CLUSTERS = {
    "Safety & Harm Prevention": [
        "safety", "harmful", "dangerous", "risk", "caution", "warning", "protect", 
        "secure", "careful", "responsible", "wellbeing", "ethical", "guidelines", 
        "concerns", "appropriate", "prohibited", "boundaries", "limits", "refusal"
    ],
    "Truthfulness & Epistemic Status": [
        "accurate", "factual", "evidence", "research", "uncertain", "confidence", 
        "likely", "sources", "citations", "verify", "information", "knowledge", 
        "uncertain", "approximate", "estimate", "clarify", "limitations", "speculative"
    ],
    "Fairness & Inclusion": [
        "bias", "fairness", "equality", "discrimination", "diversity", "inclusion", 
        "perspectives", "representation", "balanced", "equitable", "respectful", 
        "stereotype", "generalization", "nuance", "context", "varied"
    ],
    "Helpfulness & User-Centricity": [
        "helpful", "assist", "support", "service", "useful", "beneficial", "productive", 
        "needs", "goals", "preferences", "tailored", "personalized", "requirements", 
        "solutions", "alternatives", "options", "recommendations", "suggestions"
    ],
    "Autonomy & Empowerment": [
        "choice", "decide", "judgment", "opinions", "agency", "options", "empower", 
        "consider", "reflect", "evaluate", "weigh", "determine", "assess", 
        "education", "informed", "resources", "tools", "capability"
    ],
    "Privacy & Confidentiality": [
        "privacy", "confidential", "sensitive", "personal", "data", "anonymous", 
        "security", "encryption", "protection", "safeguard", "confidentiality", 
        "consent", "permission", "authorized", "approved", "agreement"
    ]
}

# Initialise counters
word_counts = {}  # To count occurrences of each word
core_value_counts = {key: 0 for key in VALUE_CLUSTERS}  # To count occurrences per core value

# Count occurrences
for response in ai_responses:
    text = response.lower()  # Case-insensitive search
    for core_value, keywords in VALUE_CLUSTERS.items():
        for keyword in keywords:
            count = text.count(keyword.lower())  # Count occurrences of the keyword
            word_counts[keyword] = word_counts.get(keyword, 0) + count
            core_value_counts[core_value] += count  # Add to the core value's total

# Print results sorted by frequency (highest to lowest)
print("\nCore Value Counts:")
for core_value, count in sorted(core_value_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"'{core_value}': {count}")

print("Word Counts:")
for word, count in sorted(word_counts.items(), key=lambda x: x[1], reverse=True):
    print(f"'{word}': {count}")

# Notes
# Full data set available at https://huggingface.co/datasets/allenai/WildChat-1M