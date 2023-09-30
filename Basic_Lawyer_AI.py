import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
import re

# Sample compliance rules
compliance_rules = {
    "No offensive language": r"\b(?:offensive|inappropriate)\b",
    "No spam": r"\b(?:spam|unsolicited)\b",
}

def text_analyzer(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Sentiment analysis
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)
    
    # Check for compliance violations
    violations = []
    for rule_name, rule_pattern in compliance_rules.items():
        if re.search(rule_pattern, text, re.IGNORECASE):
            violations.append(rule_name)
    
    return {
        "tokens": tokens,
        "sentiment_score": sentiment_score,
        "compliance_violations": violations
    }

def main():
    user_input = input("Enter your transaction text: ")
    analysis_result = text_analyzer(user_input)
    
    if analysis_result["compliance_violations"]:
        print("Compliance violations detected:")
        for violation in analysis_result["compliance_violations"]:
            print("- " + violation)
        print("Please review your transaction for compliance.")
    else:
        print("Transaction is compliant.")
    
    # You can add more checks, identity verification, and user guidance logic here.

if __name__ == "__main__":
    main()
