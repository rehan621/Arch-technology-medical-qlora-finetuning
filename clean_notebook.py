import json

with open('medical_chatbot.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Remove entire widgets metadata - Colab notebooks don't need it
if 'widgets' in nb.get('metadata', {}):
    del nb['metadata']['widgets']

# Clean up cells - remove widget references
for cell in nb.get('cells', []):
    if 'metadata' in cell:
        keys_to_remove = []
        for key in cell['metadata']:
            if 'widget' in key.lower():
                keys_to_remove.append(key)
        for key in keys_to_remove:
            del cell['metadata'][key]

# Save
with open('medical_chatbot.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

# Success message - write to file
with open('fix_result.txt', 'w') as f:
    f.write('FIXED\n')
