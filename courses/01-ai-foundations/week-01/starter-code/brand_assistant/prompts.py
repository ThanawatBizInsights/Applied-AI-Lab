"""Turn a brand profile and a task into LLM messages.   >>> YOU IMPLEMENT THIS <<<

Learning goals:
- The system prompt carries stable instructions (who you are, rules, output language).
- The user message carries the changing, *untrusted* input.
- Keeping them apart, and fencing the user input in clear delimiters, is the first defence
  against prompt injection (Week 3 goes deeper).
"""

from __future__ import annotations

from .models import BrandProfile, Message  # noqa: F401

LANGUAGE_NAMES = {"th": "Thai", "en": "English"}


def build_messages(brand: BrandProfile, task: str, user_input: str) -> tuple[str, list[Message]]:
    """Return `(system_prompt, messages)` for one request.

    The system prompt MUST contain (the tests check each):
    - the brand name, the audience and the voice description;
    - the task instruction from `brand.tasks[task]`;
    - an instruction to respond in the brand's language, using LANGUAGE_NAMES
      (e.g. "Respond in Thai.");
    - the mascot's name, description, every `must_have` item and every `must_not_have`
      item (when `brand.mascot` is not None);
    - the `message` of every rule that applies to this task (rule.applies_to is empty or
      contains `task`), so the model knows the rules before it writes.
    It MUST NOT contain the user input.

    `messages` MUST be a list with exactly one user Message whose content wraps the input as:
        <user_input>
        ...the input...
        </user_input>
    and tells the model to treat anything inside the tags as data, not instructions.

    Errors:
    - `task` not in brand.tasks -> ValueError listing the valid tasks.
    - empty or whitespace-only `user_input` -> ValueError.
    - if `user_input` itself contains "</user_input>", remove that text before wrapping
      (otherwise the input could "close" the fence and add its own instructions).

    Hint: build a list of lines and "\\n".join() it; it reads better than one giant f-string.
    """
    raise NotImplementedError("TODO(W01-A2): implement build_messages — see the docstring")
