##
## Concept    : Fine-Tuning — Data Validation & Job Submission
## What it does: Validates the format of training and validation JSONL datasets, uploads
##               them using the OpenAI Files API, and submits a fine-tuning job.
## What you'll learn:
##   - The required JSONL format for fine-tuning data: each line must be a JSON object
##     with a "messages" key containing a list of role/content pairs
##   - How to programmatically validate your dataset for common formatting errors before
##     submitting (missing keys, wrong roles, empty content, etc.)
##   - How to upload files with client.files.create(purpose="fine-tune")
##   - How to submit a fine-tuning job with client.fine_tuning.jobs.create()
##   - The job ID is saved to an env variable so file 8 can retrieve the trained model
## Prerequisite: training_set.jsonl and validation_set.jsonl must exist in this directory
## Run: python 7.submit_fine_tuning.py
##
import json
import os
import numpy as np
from collections import defaultdict
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def check_data_formatting(data_path):
    # load the data set
    with open(data_path, 'r', encoding='utf-8') as f:
        dataset = [json.loads(line) for line in f]

    # Initial dataset stats
    print(f"Num Examples in {data_path}: {len(dataset)}")
    print("First example:")
    for message in dataset[0]['messages']:
        print(message )

    # Format error checks
    format_errors = defaultdict(int)

    for ex in dataset:
        if not isinstance(ex, dict):
            format_errors['data_type'] += 1
            continue

        messages = ex.get('messages', None)

        if not messages or not isinstance(messages, list):
            format_errors['missing_messages_list'] += 1
            continue

        for message in messages:
            if not isinstance(message, dict):
                format_errors['message_not_dict'] += 1
                continue

            if 'role' not in message or 'content' not in message:
                format_errors['message_missing_key'] += 1
                continue

            if any(k not in ("role", "content", "name", "function_call") for k in message):
                format_errors['message_unrecognized_key'] += 1

            if message.get('role', None) not in ("system", "user", "assistant", "function"):
                format_errors['unrecognized_role'] += 1

            content = message.get('content', None)
            function_call = message.get("function_call", None)

            if (not content and not function_call) or not isinstance(content, str):
                format_errors["missing_content"] += 1

        if not any(message.get("role", None) == "assistant" for message in messages):
            format_errors["example_missing_assistant_message"] += 1

    if format_errors:
        print(f"Found Errors:")
        for k,v in format_errors.items():
                print(f"{k}: {v}")
    else:
        print("No formatting errors found. Dataset is ready for fine-tuning.")

# validate data
check_data_formatting("training_set.jsonl")
print("\n")
check_data_formatting("validation_set.jsonl")

client = OpenAI()

# This will make the files available for use with a fine-tuning job.
with open("training_set.jsonl", "rb") as f:
    training_response = client.files.create(file=f, purpose="fine-tune")

with open("validation_set.jsonl", "rb") as f:
    validation_response = client.files.create(file=f, purpose="fine-tune")

# submit our fine-tuning training job
response = client.fine_tuning.jobs.create(
    training_file=training_response.id,
    validation_file=validation_response.id,
    model="gpt-4.1-mini",
)

job_id = response.id

print(f"Fine-tuning job submitted. Job ID: {job_id}")

# save job_id as environment variable for later use
os.environ["FINE_TUNING_JOB_ID"] = job_id
