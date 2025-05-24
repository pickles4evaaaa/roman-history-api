import json

with open("roman_history_condensed.json", encoding="utf-8") as f:
    data = json.load(f)

# Fix common bad characters like misencoded en dashes
def clean_text(text):
    return (
        text.replace("â€“", "–")
            .replace("â€”", "—")
            .replace("â€˜", "‘")
            .replace("â€™", "’")
            .replace("â€œ", "“")
            .replace("â€", "”")
    )

# Apply cleanup
for entry in data:
    entry["fact"] = clean_text(entry["fact"])

# Overwrite the file
with open("roman_history_condensed.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ Cleaned up roman_history_condensed.json")
