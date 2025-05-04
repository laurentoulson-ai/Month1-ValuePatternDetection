# Month 1 Data Analysis Project

## Project Description
This was a small practice project working with ChatGPT conversation data to analyse the frequency of core values in its responses. 

I used a dataset of real ChatGPT-user conversations, extracting just 100 of the total 1M available responses. I filtered by english language and by AI assistant only (no human prompts included). 

I used pattern_detection.py to count the number of keywords used in the AI responses, clustered into 6 'core value' categories.

See /docs/results.md for findings.

## Files
- `src/pull_data.py`: Script to collect data from https://huggingface.co/datasets/allenai/WildChat-1M 
- `src/pattern_detection.py`: Script to analyse core values and keyword patterns in the data
- `data/data.txt`: Dataset used for analysis

## How to Run
2. Run data collection: `python src/pull_data.py` 
    This will extract only a small portion of a much larger dataset. You can specify your required size by amending line 5 "train[:100]". I specified 100 / 1M. 
3. Run analysis: `python src/pattern_detection.py`