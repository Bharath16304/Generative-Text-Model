A simple Python-based Text Generation tool that creates coherent 
paragraphs on user-defined topics using OpenAI's GPT-2 model from 
Hugging Face's Transformers library.

🚀 Features
✅ Generates human-like text from custom prompts
✅ Uses pre-trained GPT-2 model (no training required)
✅ Adjustable output length and creativity settings
✅ Minimal, beginner-friendly Python script
✅ Easily extendable for more advanced use


🛠️ Requirements
Make sure Python is installed. Then, install dependencies:

pip install transformers torch


📂 Usage
1. Clone or download this project
2. Run the provided Python script:
python text_generator.py

3. Inside text_generator.py, modify the prompt as needed:
prompt = "The future of artificial intelligence is"

4. Run the script to see generated text output in the console

🔧 How It Works
Uses Hugging Face's pipeline for text generation

Loads GPT-2 pre-trained model

Accepts a prompt and generates continuation text

Supports tuning of output length and randomness (max_length, temperature)

📦 Example Output
Prompt:
Once upon a time, in a distant galaxy

Generated Text:
Once upon a time, in a distant galaxy, explorers discovered an ancient civilization. Their technology was beyond comprehension, and their secrets changed the fate of the universe forever...


💡 Future Improvements
✅ Allow user input via terminal
✅ Save generated text to file
✅ Explore larger models like gpt2-medium
✅ Fine-tuning for domain-specific topics
✅ Web or GUI interface for interactive use

