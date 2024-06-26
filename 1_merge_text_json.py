import os
import json

# def merge_json_files(folder_path, output_file):
#     # Initialize an empty list to hold all the json data
#     all_data = []

#     # List all files in the given folder
#     for filename in os.listdir(folder_path):
#         if filename.endswith('.json'):
#             file_path = os.path.join(folder_path, filename)
            
#             # Open and read each json file
#             with open(file_path, 'r', encoding='utf-8') as file:
#                 data = json.load(file)
#                 all_data.append(data)
    
#     # Write the merged data to the output file
#     with open(output_file, 'w', encoding='utf-8') as output_file:
#         json.dump(all_data, output_file, ensure_ascii=False, indent=4)

# # Usage
# folder_path = '/data1/fabulator/GRAPH_STUDY/Relation_Intent_Story_Generation/intent_DB_text'
# output_file = '/data1/fabulator/GRAPH_STUDY/Relation_Intent_Story_Generation/intent_DB_text/merged_text_DB.json'
# merge_json_files(folder_path, output_file)

###################################################################

import os
import json

# Specify the directory containing the JSON files
directory = '/data1/fabulator/GRAPH_STUDY/Relation_Intent_Story_Generation/intent_DB_text'  # Replace with the path to your directory

# Initialize an empty list to hold all data
all_data = []

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        # Open and read the JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # Add the data to the list
            all_data.extend(data)

# Save the merged data to a new JSON file
with open('/data1/fabulator/GRAPH_STUDY/Relation_Intent_Story_Generation/intent_DB_text/merged_DB_text.json', 'w', encoding='utf-8') as file_merged:
    json.dump(all_data, file_merged, ensure_ascii=False, indent=4)

print("Merged JSON has been saved to 'merged.json'")
