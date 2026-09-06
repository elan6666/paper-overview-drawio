# Illustrative conditional predictor

This is a synthetic method specification for testing the drawing workflow. It is not a trained implementation or an experimental result.

A cell encoder maps control expression to a latent vector. A graph encoder maps a prior graph to node embeddings. A perturbation ID selects its target embedding. That embedding is added to the cell embedding, then a decoder produces predicted expression. All edges and entities are defined in paper-contract.json. No training loss, teacher, EMA update, benchmark task or dataset size is specified.
