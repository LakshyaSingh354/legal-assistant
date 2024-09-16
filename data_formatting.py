import google.generativeai as genai
from tqdm import tqdm
import os

genai.configure(api_key=os.environ['API_KEY'])
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_summary(file):
    prompt = f'''{file} \n please go through the above case in complete detail and provide me a contextual summary of the case, A summary of the relevant legal information.\nI want large data. give large contextual summary full detailed case by going through the whole txt file. give proper detailed info of what all happened in the case arguments by appealant, responsdent, judge decisions, etc etc,\nI want everything in detail. all the facts in the case, all relevant sections in the file, all legal principles in the file, each and every cotext in the file \n \n 
    Follow this template for all the summaries like a bible:\n 
    1. Case Title

	•	Case Name: [e.g., ABC Corp. vs. XYZ Ltd.]
	•	Court: [e.g., Supreme Court of India]
	•	Date of Judgment: [e.g., 23rd August 2024]
	•	Citation: [e.g., 2024 SCC 123]

2. Background and Context

	•	Brief Overview: A concise summary of the case background, including relevant events leading up to the legal dispute.
	•	Key Issues: A list of the main legal questions or issues presented in the case.

3. Legal Principles Involved

	•	Relevant Statutes and Provisions: List of statutory provisions, rules, and regulations relevant to the case.
	•	Precedents Cited: Key past judgments cited during the case.
	•	Legal Doctrines: Any specific legal doctrines or principles applied in the judgment.

4. Arguments Presented

	•	Plaintiff’s Argument: Summary of the arguments and claims made by the plaintiff.
	•	Defendant’s Argument: Summary of the arguments and defenses presented by the defendant.

5. Court’s Analysis and Reasoning

	•	Key Findings: Important observations and findings made by the court.
	•	Interpretation of Law: How the court interpreted the relevant legal provisions and precedents.
	•	Application of Law: How the court applied the law to the facts of the case.

6. Judgment

	•	Final Decision: The outcome of the case (e.g., in favor of the plaintiff/defendant).
	•	Relief Granted: Any relief or damages awarded, if applicable.
	•	Orders: Specific orders or directives issued by the court.

7. Implications

	•	Impact on Law: How the judgment impacts existing law or legal practice.
	•	Future Relevance: The potential influence of the case on future legal decisions or cases.
	•	Broader Context: Any broader implications, such as social, economic, or political impact.

8. Summary Points

	•	Key Takeaways: Bullet points summarizing the most critical aspects of the case, suitable for quick reference.

9. References

	•	Citations: Full citations of any statutes, cases, or legal texts referenced in the summary.
	•	Further Reading: Suggestions for further reading or related cases.'''
    response = model.generate_content(prompt)
    return response.text


def structured_data(file):
    prompt = f"""{file} \n
    Above is the case file. I want you to go through the same in detail and provide me the below reponse in json format. 
    Make sure to provide as much data as possible available in the file. Give me 10 queries with the following fields in a Json ARRAY with 10 different JSON objects (Make sure to follow this format).
    Query: A natural language query representing a typical legal research question.(Here the judge will eneter the present case for which the model will search in database)(The query can be the whole present case that judge wants to solve).
# 	•	Legal Principles: Key legal principles or precedents related to the query.
# 	•	Relevant Sections: Extracted and highlighted sections from the relevant documents.
# 	•	Context: Additional information about the legal context (e.g., jurisdiction, case type) that can be used to fine-tune the model's response.
# The Query should be an actual present case that a jusdge wants to solve. A one or 2 line description of the case over which the judge is currently presiding on. 
#  Make sure to create some imaginary case (not the same one provided above) for the queries"""
    
    response = model.generate_content(prompt)
    return response.text


files = os.listdir("data")
print(files)

for file in tqdm(files[:2], desc="Generating Summaries: "):
    text = open(f'data/{file}', 'r').read()
    summary = generate_summary(text)
    with open(f"case_summary{file}", "w", encoding="utf-8") as outfile:
        outfile.write(summary)


text = open(f'data/{file}','r', encoding="utf-8").read()


files = os.listdir("data")
print(files)
for i, file in enumerate(files):
    text = open(f'data/case15.txt','r', encoding="utf-8").read()
    query = structured_data(text)
    with open(f"data_json/query_jsoncase15", "w", encoding="utf-8") as outfile:
        outfile.write(query)
    print(f"Files completed {i}/400")
    print(f"Completed File: {file}")