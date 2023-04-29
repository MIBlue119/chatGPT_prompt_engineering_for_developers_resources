from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import concurrent

from .utils import (
    breakup_text_into_chunks,
    parse_text_response,
    get_model_selection,
    generate_openai_completion,
)


# Define the prompt
def get_prompt(chunk):
    prompt = f"""
#Instructions:
You are a professional translator, equips professional domain knowhow about computer science and literature writing skills.
Please help me to translate the text under #Input delimited by Triple backticks ```<text>``` to lang:zh-Hant
Follow these rules:
1. Do not add explanations on what the commands do 
2. Do not return the original text and the rules
3. Keep the meaning the same, but make them more literal

#Input:
```{chunk}```
"""
    return {"messages": [{"role": "user", "content": prompt}]}


def translate_chunk(chunk, index, text_engine):
    chunk_prompt = get_prompt(chunk)
    api_settings = {
        **get_model_selection(text_engine),
        **chunk_prompt,
        "n": 1,
        "temperature": 1,
    }
    response = generate_openai_completion(
        text_engine=text_engine, api_settings=api_settings
    )
    translated_chunk = parse_text_response(response, text_engine=text_engine)
    # If the the translated chunk contains ``` replace them with empty string
    translated_chunk = translated_chunk.replace("```", "")
    # Add a new line if the translated chunk contains a "。" we replace it with "。\n"
    translated_chunk = translated_chunk.replace("。", "。\n")
    return (index, translated_chunk)


def translate(text):
    """Translate the text with OpenAI API"""
    max_tokens = 1024
    overlap_length = 0
    text_engine = "gpt-3.5-turbo"
    # Breakup the text into chunks to avoid context length error
    chunks = breakup_text_into_chunks(
        text=text, max_tokens=max_tokens, overlap_size=overlap_length
    )
    # Translate the chunks
    translated_chunks = []
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [
            executor.submit(translate_chunk, chunk, i, text_engine)
            for i, chunk in enumerate(chunks)
        ]
        for future in tqdm(
            concurrent.futures.as_completed(futures), total=len(futures)
        ):
            index, translated_chunk = future.result()
            translated_chunks.append((index, translated_chunk))
    # Sort the translated chunks by their original index
    sorted_translated_chunks = sorted(translated_chunks, key=lambda x: x[0])
    # Combine the translated chunks into a single string
    total_translated_chunks = "".join([chunk[1] for chunk in sorted_translated_chunks])
    return total_translated_chunks


def main():
    import openai
    import os
    from pathlib import Path
    from loguru import logger

    openai.api_key = "set_with_your_key"
    current_script_path_dir = Path(os.path.realpath(__file__)).parent
    transcripts_dir = current_script_path_dir / "../assets"
    # Iterate all subdirectories to find transcripts named with `original.txt`
    for transcript_dir in transcripts_dir.iterdir():
        if transcript_dir.is_dir():
            original_text_path = transcript_dir / "original.txt"
            if original_text_path.exists():
                # Read the original text
                with open(original_text_path, "r") as f:
                    original_text = f.read()
                # Translate the original text
                logger.info(f"Start to translate the text with OpenAI API: {original_text_path}")
                translated_text = translate(original_text)
                # Write the translated text
                translated_text_path = transcript_dir / "translated_zh_tw.txt"
                with open(translated_text_path, "w") as f:
                    f.write(translated_text)
                logger.info(f"Export the translated to: {translated_text_path}")

if __name__ =="__main__":
    main()