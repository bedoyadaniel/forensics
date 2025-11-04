import os
import deepl
from pathlib import Path

DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")
if not DEEPL_API_KEY:
    raise ValueError("Missing DEEPL_API_KEY environment variable.")

translator = deepl.Translator(DEEPL_API_KEY)

TARGET_LANGUAGES = ["EN", "ES", "PT-BR"]  # ISO codes: FR = French, ES = Spanish, DE = German

def translate_markdown_file(file_path: str, target_lang: str):
    """Translate a Markdown file using DeepL API."""
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    print(f"🔁 Translating {file_path} → {target_lang}")
    result = translator.translate_text(
        text,
        target_lang=target_lang,
        tag_handling="xml",  # Helps preserve Markdown-like formatting
        outline_detection=False,
        non_splitting_tags=["code", "pre"],
    )

    new_filename = f"{Path(file_path).stem}.{target_lang.lower()}.md"
    new_path = Path(file_path).with_name(new_filename)

    with open(new_path, "w", encoding="utf-8") as f:
        f.write(result.text)

    print(f"✅ Saved translation to {new_path}")
    return new_path


def main():
    md_files = [f for f in Path(".").rglob("*.md") if not f.name.endswith((".fr.md", ".es.md", ".de.md"))]

    for md_file in md_files:
        for lang in TARGET_LANGUAGES:
            translate_markdown_file(md_file, lang)


if __name__ == "__main__":
    main()

