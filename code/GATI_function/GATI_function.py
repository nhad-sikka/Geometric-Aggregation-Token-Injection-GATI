import torch

def apply_gati(tokens: list, tokenizer, model):
    """
    Generates norm-scaled subword embeddings (GATI) for out-of-vocabulary tokens.
    """
    # Use universal HF method to extract the embedding matrix
    embedding_matrix = model.get_input_embeddings().weight
    
    gati_outputs = []
    
    # Iterate through each new token
    for custom_token in tokens:
        # Shatter the token to get component IDs (e.g., "'a" -> ["'", "a"])
        subword_ids = tokenizer(custom_token, add_special_tokens=False)["input_ids"]
        
        # Retrieve vectors for the shattered components
        subword_tensor_ids = torch.tensor(subword_ids, device=model.device)
        subword_vectors = embedding_matrix[subword_tensor_ids]
        
        # Norm-Scaled Mean Aggregation
        # A. Calculate the raw mean vector
        mean_vector = torch.mean(subword_vectors, dim=0)
        
        # B. Calculate the target magnitude (average norm of the shattered pieces)
        original_norms = torch.norm(subword_vectors, dim=1)
        target_norm = torch.mean(original_norms)
        
        # C. Scale the mean vector to restore its geometric magnitude
        aggregated_vector = (mean_vector / torch.norm(mean_vector)) * target_norm
        
        # Vocabulary Generation Output
        gati_outputs.append({
            "token_string": custom_token,
            "shattered_pieces": tokenizer.convert_ids_to_tokens(subword_ids),
            "vector_embedding": aggregated_vector.detach() # Detach to prevent gradient tracking
        })
        
    return gati_outputs
