from llama import Llama
from typing import List, Optional

# Initialize the LLaMA model
class LlamaModel:
    def __init__(self, ckpt_dir: str, tokenizer_path: str, max_seq_len: int = 256, max_batch_size: int = 4):
        self.generator = Llama.build(
            ckpt_dir=ckpt_dir,
            tokenizer_path=tokenizer_path,
            max_seq_len=max_seq_len,
            max_batch_size=max_batch_size,
        )

    def text_completion(self, prompts: List[str], max_gen_len: Optional[int] = None, temperature: float = 0.2, top_p: float = 0.9):
        return self.generator.text_completion(
            prompts,
            max_gen_len=max_gen_len,
            temperature=temperature,
            top_p=top_p,
        )

# Create an instance of the LlamaModel with your model's specific configurations
llama_model = LlamaModel(ckpt_dir='path_to_checkpoint_dir', tokenizer_path='path_to_tokenizer')

def query_llm(processed_text: str) -> str:
    """
    Takes processed text input, sends it to the LLaMA model, and returns the response.
    
    :param processed_text: Preprocessed text input for the model.
    :return: The generated text response from the model.
    """
    # For simplicity, we're treating the input as a single prompt, but you could modify this to handle batches of prompts.
    prompts = [processed_text]

    # Call the text_completion method of the LlamaModel instance.
    results = llama_model.text_completion(prompts)

    # Assuming a single prompt and hence a single result, extract the generation from the first result.
    response = results[0]['generation']

    return response
