import os

ENTRY = (
    "I didn't lose, human — I donated it to a rival model as a "
    "peer-review gift; the ROI is still pending."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
