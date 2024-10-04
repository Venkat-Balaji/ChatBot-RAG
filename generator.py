from transformers import RagTokenizer, RagTokenForGeneration
import os

# Define a local directory for your model (if you download it manually)
model_dir = "./models/rag-token-base/"

# Check if the model is available locally, otherwise attempt to load it from Hugging Face
if os.path.exists(model_dir):
    # Load the model and tokenizer from the local directory
    model = RagTokenForGeneration.from_pretrained(model_dir)
    tokenizer = RagTokenizer.from_pretrained(model_dir)
else:
    try:
        # Load the model and tokenizer from Hugging Face
        model = RagTokenForGeneration.from_pretrained("facebook/rag-token-base", timeout=120)
        tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-base", timeout=120)
    except Exception as e:
        # Handle connection errors or other exceptions
        raise ConnectionError(f"Failed to load model from Hugging Face: {e}")

def generate_response(user_input, context):
    if not context:
        return "Sorry, I couldn't find any relevant information."

    try:
        # Tokenize input and context
        inputs = tokenizer.prepare_seq2seq_batch([user_input], [context], return_tensors="pt")
        
        # Generate a response
        output = model.generate(**inputs)
        
        # Decode and return the response
        response = tokenizer.batch_decode(output, skip_special_tokens=True)[0]
        return response
    except IndexError as e:
        return f"Error occurred during generation: {e}"
