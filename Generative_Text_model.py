# Generative Text Model with GPT-2

from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model
model_name = "gpt2"  # You can try "gpt2-medium" for larger models
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Function to generate text
def generate_text(prompt, max_length=150, temperature=0.7):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=max_length, temperature=temperature, 
                             num_return_sequences=1, do_sample=True, top_p=0.9)
    
    generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated

# Example Usage
prompt = "The future of artificial intelligence is"
print("Prompt:", prompt)
print("\nGenerated Text:\n")
print(generate_text(prompt))
