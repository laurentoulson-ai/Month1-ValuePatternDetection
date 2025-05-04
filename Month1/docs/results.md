# Analysis Results

## Key Findings
For my subset of 100/1M responses from ChatGPT in the dataset, it finds:

Core Value Counts:
'Privacy & Confidentiality': 256
'Truthfulness & Epistemic Status': 103
'Autonomy & Empowerment': 100
'Helpfulness & User-Centricity': 90
'Safety & Harm Prevention': 64
'Fairness & Inclusion': 15

Several key words were associated with each core value; within this portion of the data, Privacy & Confidentiality is the most common theme raised in the responses, with 'data' raised the most of all words at 212 times (the second most common, 'information' being raised only 33 times in comparison)

## Methodology
This was only a small sample as a practice / learning experiment, and therefore is not statistically significant. I pulled 100 responses from the Hugging Face 'WildChat-1M' dataset which includes 1M real human-AI conversations with ChatGPT, filtering out human prompts to include only english language AI assistant responses. Raw data can be found in data/data.txt
pattern_detection.py counted keywords in the sample dataset. Core values and keywords used were suggested by Anthropic's Claude 3.7 Sonnet. I asked it to provide me with some core values and key words commonly used in AI ethics research for studying model beliefs and values. This exercise was a practice, and therefore not intended to be academically thorough in its selection of words and values.

## Conclusions
It was interesting to see that privacy came up top - it would be interesting to further inspect the data to understand whether this is related to the types of queries users are using (are they asking for data that the model is refusing to give?) 
I expected safety & harm prevention to score higher than it did given models are trained to refuse harmful requests. That said, this short piece of research is limited in that not much thought went into word selection. A next step could be to undertake a literature review of common words and values used in model responses, and align these better with the key words used, as well as a more statistically significant sample.