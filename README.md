# **chatGPT_prompt_engineering_for_developers_resources**

## Introduction

- In 2023, OpenAI engineer Isa Fulford and AI expert Andrew Ng launched a free one-hour online course on prompt engineering called DeepLearning.AI. The course can be accessed at: [https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)
  - The course provides several principles for writing effective prompts
  - It demonstrates how to use the OpenAI API to accomplish several tasks, including:
    - Summarizing: generating concise user reviews
    - Inferring: separating text sentiment / extracting topics
    - Transforming: translating text / correcting grammar
    - Expanding: automatically writing emails
  - The course includes videos, written explanations, and Jupyter Notebooks for real-time practice.
- Course Instructors
  - Andrew Ng's background:
    - Founder and CEO of Landing.AI
    - Founder of DeepLearning.AI
    - Founding lead of Google Brain
    - Former chief scientist at Baidu
    - Professor at Stanford University
    - Holds a PhD from UC Berkeley and a Bachelor's degree in CS, Statistics, and Economics from CMU
  - Isa Fulford's background:
    - Holds a Bachelor's and Master's degree in CS from Stanford
    - Worked as an engineer at AWS
    - Currently an engineer at OpenAI.

## Course Resources

- jupyternotebooks of each chapter
  - [assets/l2-guidelines.ipynb](./assets/2-Guidelines/l2-guidelines.ipynb)
  - [assets/3-Iterative/l3-iterative-prompt-development.ipynb](./assets/3-Iterative/l3-iterative-prompt-development.ipynb)
  - [assets/4-Summarizing/l4-summarizing.ipynb](assets/4-Summarizing/l4-summarizing.ipynb)
  - [assets/5-Inferring/l5-inferring.ipynb](assets/5-Inferring/l5-inferring.ipynb)
  - [assets/6-Transforming/l6-transforming.ipynb](assets/6-Transforming/l6-transforming.ipynb)
  - [assets/7-Expanding/l7-expanding.ipynb](assets/7-Expanding/l7-expanding.ipynb)
  - [assets/8-Chatbot/l8-chatbot.ipynb](assets/8-Chatbot/l8-chatbot.ipynb)
- traditional chinese notes: [https://sunset-polka-3bd.notion.site/Note-ChatGPT-Prompt-Engineering-for-Developers-beb31175898647c3b2e10d58fc065c3c](https://sunset-polka-3bd.notion.site/Note-ChatGPT-Prompt-Engineering-for-Developers-beb31175898647c3b2e10d58fc065c3c)

## Further Reading

- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)
  - The OpenAI Cookbook is an official resource that provides a variety of code examples on how to use their API. The content is quite rich and includes examples such as:
    - How to translate a Latex book using GPT
    - Using embeddings for question answering
    - Using embeddings for recommendation
    - How to handle rate limits
    - How to fine-tune GPT3
- Resources on prompt engineering
  - Prompt Engineering Guide: [https://www.promptingguide.ai/](https://www.promptingguide.ai/)
    - Provides a basic introduction to prompt engineering, including zero-shot, few-shot, chain of thought, and ReAct prompting.
  - [2023/03/15] OpenAI engineer Lilian Weng's blog about prompt engineering: [https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/)
    - Basic prompting
      - Instruction prompting
      - Chain of Thought
      - Automatic Prompt Design
      - Augmented Language Model
  - Learn Prompting: [https://learnprompting.org/](https://learnprompting.org/)
    - A tutorial book similar to the Prompt Engineering Guide
  - [2023/04/11] Chip Huyen's article on Building LLM applications for production: [https://huyenchip.com/2023/04/11/llm-engineering.html#backward_and_forward_compatibility](https://huyenchip.com/2023/04/11/llm-engineering.html#backward_and_forward_compatibility)
    - This article discusses some considerations for LLM when used in a production environment
      - Prompt version control
      - Cost and latency
      - LLM control flow design
      - Several product applications: AI assistants, chatbots, learning, search, and recommendation
    - Chip Huyen's background:
      - Originally from a humanities background, later moved into the CS field
      - AI engineer at Nvidia
      - AI engineer at Snorkel AI
      - Founder of [Claypot.AI](http://Claypot.AI)
