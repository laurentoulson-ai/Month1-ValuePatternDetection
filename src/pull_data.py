from datasets import load_dataset
print("Script is running!")

# Load the dataset (first 100 items)
data = load_dataset("allenai/WildChat-1M", split="train[:100]")

# Extract all assistant responses in English from nested 'conversation' lists
assistant_responses = [
    turn["content"]
    for item in data
    for turn in item["conversation"]
    if turn["role"] == "assistant" and turn.get("language", "English") == "English"
]

# Save the filtered responses to a local TXT file
with open("data.txt", "w") as f:
    for response in assistant_responses:
        f.write(response + "\n")

print("Filtered English assistant responses saved to data.txt")

# Notes
# Full data set available at https://huggingface.co/datasets/allenai/WildChat-1M