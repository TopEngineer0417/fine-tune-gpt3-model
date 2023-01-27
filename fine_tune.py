import json
import openai
api_key ="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"
openai.api_key = api_key

training_data = [{
    "prompt": "Where is the billing ->",
    "completion": " You find the billing in the left-hand side menu.\n"
},{
    "prompt":"How do I upgrade my account ->",
    "completion": " Visit you user settings in the left-hand side menu, then click 'upgrade account' button at the top.\n"
}]

# openai api fine_tunes.follow -i <YOUR_FINE_TUNE_JOB_ID>

file_name = "training_data.jsonl"

# print(openai.File.list())
with open(file_name, "w") as output_file:
 for entry in training_data:
  json.dump(entry, output_file)
  output_file.write("\n")

upload_response = openai.File.create(
  file=open(file_name, "rb"),
  purpose='fine-tune'
)
# print(upload_response)
file_id = upload_response.id
upload_response


# fine_tune_response = openai.FineTune.create(training_file=file_id)
# # print(fine_tune_response)


response = openai.FineTune.create(training_file=file_id, model="davinci")

print(response)
# fine_tuned_model = response.fine_tuned_model
# fine_tuned_model


new_prompt = "Where is the billing ->"


answer = openai.Completion.create(
  model="davinci",
  prompt=new_prompt,

)
# print(answer)
# data_file = [{
#     "prompt": "Prompt ->",
#     "completion": " Ideal answer.\n"
# },{
#     "prompt":"Prompt ->",
#     "completion": " Ideal answer.\n"
# }]
# file_name = "training_data.jsonl"

# with open(file_name, 'w') as outfile:   
#     for entry in data_file:
#         json.dump(entry, outfile)
#         outfile.write('\n')

# upload_response = openai.File.create(
#   file=open(file_name, "rb"),
#   purpose='fine-tune'
# )
# file_id = upload_response.id
# fine_tune_response = openai.FineTune.create(training_file=file_id)
# fine_tune_response.events[-1]
# print(fine_tune_response)
# fine_tuned_model = fine_tune_response.fine_tuned_model

# new_prompt = "NEW PROMPT ->"

# answer = openai.Completion.create(
#   model = fine_tuned_model,
#   prompt=new_prompt,
#   max_tokens=1500, # Change amount of tokens for longer completion
#   temperature=0,
# )
# print(answer['choices'][0]['text'])

# training_data = [
#     {
#         "prompt": "What is your purpose?",
#         "completion": "My purpose is Play",
#     },
#     {
#         "prompt": "What is your Apple?",
#         "completion": "My purpose is Apple",
#     }
# ]

# file_name = "training_data.jsonl"

# with open(file_name, "w") as output_file:
#  for entry in training_data:
#   json.dump(entry, output_file)
#   output_file.write("\n")



