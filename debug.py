import json

# Load and check
with open('medical_chatbot.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Debug output
with open('debug.txt', 'w', encoding='utf-8') as f:
    f.write(f"Metadata keys: {list(nb.get('metadata', {}).keys())}\n")
    if 'widgets' in nb.get('metadata', {}):
        f.write(f"Widgets: {nb['metadata']['widgets']}\n")
        f.write(f"Has state: {'state' in nb['metadata']['widgets']}\n")
    else:
        f.write("No widgets key in metadata\n")
        
print("Debug file written")
