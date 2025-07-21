"""
This is the demonstration that If we have a large document and we only want to see the summarized version of the document into 10 different template sections.
"""


# Define your 10-section template
TEMPLATE_SECTIONS = {
    1: "Introduction",
    2: "Background Context",
    3: "Local Challenges",
    4: "Social Perception",
    5: "Information Gaps",
    6: "Regulatory Case Study",
    7: "Economic Impact",
    8: "Behavioral Economics",
    9: "Institutional Efforts",
    10: "Innovation & Trends"
}

# Manually assign keywords or phrases that map to sections
SECTION_KEYWORDS = {
    1: ["study", "overview", "introduction"],
    2: ["history", "background", "context"],
    3: ["challenge", "barrier", "difficulty", "traditional belief"],
    4: ["perception", "belief", "social", "distrust"],
    5: ["information", "awareness", "education", "gap"],
    6: ["policy", "regulation", "csr", "legal"],
    7: ["economic", "finance", "profit", "market"],
    8: ["behavior", "motivation", "decision", "psychology"],
    9: ["institution", "government", "ngo", "initiative"],
    10: ["trend", "innovation", "new", "future"]
}

def map_sentence_to_section(sentence):
    sentence_lower = sentence.lower()
    for section_id, keywords in SECTION_KEYWORDS.items():
        if any(keyword in sentence_lower for keyword in keywords):
            return section_id
    return None  # If no keywords match

def project_highlights_to_template(clustered_sentences):
    projected = {section_id: [] for section_id in TEMPLATE_SECTIONS}
    for cluster_id, sentences in clustered_sentences.items():
        for sentence in sentences:
            section_id = map_sentence_to_section(sentence)
            if section_id:
                projected[section_id].append(sentence)
    return projected

# Example input: sentences from each cluster
clustered_sentences = {
    0: ["A Study of Nigerian Youths' Understanding, Perception of HIV/AIDS Phenomenon and Sex Attitudes: The Link between Acceptance of Reality and Marketing Motives of Multinational Pharmaceutical Companies. The HIV/AIDS Pandemic is one of the most serious and urgent public health challenges facing the government people and civil society in Nigeria today."],
    1: ["HIV/AIDS Pandemic is one of the most serious..."],
    2: ["Youth sexual behaviour info is inadequate..."],
    3: ["Behavioral economics can help reduce pollution..."],
    4: ["Gamification as innovation in management..."]
}

# Run projection
projected_sections = project_highlights_to_template(clustered_sentences)

# Output mapped sections
for sec_id, content in projected_sections.items():
    print(f"\nSection {sec_id}: {TEMPLATE_SECTIONS[sec_id]}")
    for sent in content:
        print(f"  - {sent}")
