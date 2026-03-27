import json
import sys

with open('medical_chatbot.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Ensure metadata exists
if 'metadata' not in nb:
    nb['metadata'] = {}

# Remove widgets completely if it exists to avoid issues
# Then we'll create proper structure
if 'widgets' in nb['metadata']:
    # Check what's in there
    print(f"Current widgets: {nb['metadata']['widgets']}")
    # Remove it
    del nb['metadata']['widgets']

# Add proper widgets structure with state
nb['metadata']['widgets'] = {}
nb['metadata']['widgets']['state'] = {}

# Also fix any cell metadata that references widgets
for cell in nb.get('cells', []):
    if 'metadata' in cell and 'referenced_widgets' in cell['metadata']:
        # Remove referenced_widgets from cells
        del cell['metadata']['referenced_widgets']

# Save with proper formatting
with open('medical_chatbot.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook fixed completely!")
print("metadata.widgets.state is now properly set")
