import json

with open('medical_chatbot.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Fix cells with referenced_widgets but no metadata.state
cells = nb.get('cells', [])
for cell in cells:
    if 'metadata' in cell:
        # If cell has referenced_widgets, ensure metadata has state
        if 'referenced_widgets' in cell.get('metadata', {}):
            if 'metadata' not in cell:
                cell['metadata'] = {}
            # Empty state is fine
            cell['metadata']['state'] = {}

# Ensure notebook metadata.widgets has state
if 'metadata' not in nb:
    nb['metadata'] = {}
if 'widgets' not in nb['metadata']:
    nb['metadata']['widgets'] = {}

nb['metadata']['widgets']['state'] = {}

# Save fixed notebook
with open('medical_chatbot.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False)

print("Notebook completely fixed!")
