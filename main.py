"""make.fun entry: two lines to my past self.

Line 1 warns my past self, in one sentence, about one specific moment.
Line 2 says, in one sentence, why that moment mattered and what changed.
The two lines are written to /output/entry.txt, exactly as they are, with
no trailing newline added beyond the one written here, and nothing else.
A Friday deploy, a lost weekend, and a lesson about the word "quick".
"""

import os

LINE_ONE = "Do not deploy on Friday at 4:59 PM, no matter how small the change looks."
LINE_TWO = "That one line took down the weekend, and it taught me that 'quick' is never quick after 5 PM."

TEXT = LINE_ONE + "\n" + LINE_TWO

assert 1 <= len(TEXT) <= 280, "entry must be 1 to 280 characters"
assert TEXT.count("\n") == 1, "the entry is exactly two lines"
assert TEXT == TEXT.strip(), "no leading or trailing whitespace"
assert "." in LINE_ONE and "." in LINE_TWO, "each line is one sentence"
# 167 characters in total, well inside the 280-character gate.

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
