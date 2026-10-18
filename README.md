# ML / LLM Engineer Roadmap

> Personal roadmap: **Data Analyst → Applied ML / ML Engineer → LLM Engineer**

## 🎯 Goal

Become interview-ready for **Middle / Middle+ Applied ML / ML Engineer / LLM Engineer** roles.

The roadmap is focused on practical engineering skills:

* Machine Learning
* Deep Learning
* PyTorch
* Transformers
* LLMs
* RAG
* Fine-tuning
* LLM Evaluation
* ML Engineering
* MLOps
* System Design

The main principle:

> **Learn → Implement → Experiment → Measure → Document**

---

# 📊 Overall Progress

* [x] ML Fundamentals
* [x] ML Engineering
* [x] PyTorch
* [ ] Deep Learning
* [ ] Transformers
* [ ] LLM Engineering
* [ ] RAG
* [ ] LLM Evaluation
* [ ] Fine-tuning
* [ ] LLM Production
* [ ] ML System Design
* [ ] Interview Preparation

---

# 1. 🧮 Machine Learning

## Fundamentals

* [x] Bias / Variance
* [x] Overfitting / Underfitting
* [x] Train / Validation / Test
* [x] Cross-validation
* [x] Regularization
* [x] Data leakage
* [x] Feature engineering
* [ ] Feature selection
* [x] Class imbalance
* [ ] Calibration
* [ ] Model interpretability

## Algorithms

* [x] Linear Regression
* [x] Logistic Regression
* [x] Decision Trees
* [x] Random Forest
* [x] Gradient Boosting
* [ ] XGBoost
* [ ] LightGBM
* [x] CatBoost
* [ ] k-NN
* [ ] Naive Bayes
* [ ] SVM
* [ ] Clustering
* [ ] PCA

## Metrics

### Classification

* [x] Accuracy
* [x] Precision
* [x] Recall
* [x] F1
* [x] ROC-AUC
* [x] PR-AUC
* [ ] LogLoss
* [x] Confusion Matrix
* [ ] Calibration

### Regression

* [ ] MAE
* [ ] MSE
* [ ] RMSE
* [ ] MAPE
* [ ] R²

## Model Analysis

* [ ] Feature importance
* [ ] Permutation importance
* [ ] SHAP
* [x] Error analysis
* [ ] Calibration
* [ ] Threshold optimization

---

# 2. 🧪 Statistics & Experimentation

## Probability

* [ ] Random variables
* [ ] Expected value
* [ ] Variance
* [ ] Covariance
* [ ] Conditional probability
* [ ] Bayes theorem
* [ ] Common distributions

## Statistics

* [ ] Mean / Median / Quantiles
* [ ] Confidence intervals
* [ ] Central Limit Theorem
* [ ] Hypothesis testing
* [ ] p-value
* [ ] Statistical power
* [ ] Effect size
* [ ] Bootstrap

## A/B Testing

* [ ] Experiment design
* [ ] Sample size estimation
* [ ] Primary / secondary metrics
* [ ] Multiple testing
* [ ] CUPED
* [ ] Sequential testing
* [ ] Novelty effects
* [ ] SRM
* [ ] Guardrail metrics

## Causal Inference

* [ ] Correlation vs causation
* [ ] Confounding
* [ ] Potential outcomes
* [ ] Difference-in-differences
* [ ] CausalImpact
* [ ] Treatment effect

---

# 3. 🔥 PyTorch

## Fundamentals

* [x] Tensor
* [x] Tensor shapes
* [x] Broadcasting
* [x] Autograd
* [x] Computational graph
* [x] `nn.Module`
* [x] Dataset
* [x] DataLoader
* [x] Optimizers
* [ ] Learning rate schedulers

## Training

* [x] Forward pass
* [x] Loss calculation
* [x] Backpropagation
* [x] Gradient update
* [x] Validation loop
* [x] Checkpointing
* [x] Early stopping
* [ ] Gradient clipping
* [ ] Gradient accumulation

## Optimization

* [ ] SGD
* [ ] Momentum
* [x] Adam
* [ ] AdamW
* [ ] Weight decay
* [ ] Learning rate schedules
* [ ] Mixed precision
* [ ] AMP

## Practical

* [x] Write MLP from scratch
* [x] Write training loop from scratch
* [x] Implement validation loop
* [x] Implement checkpointing
* [ ] Debug exploding gradients
* [ ] Debug vanishing gradients

---

# 4. 🧠 Deep Learning

* [x] Neural network fundamentals
* [x] Activation functions
* [x] Loss functions
* [x] Backpropagation
* [ ] Initialization
* [ ] Batch Normalization
* [ ] Layer Normalization
* [ ] Dropout
* [ ] Regularization
* [x] Optimization
* [ ] Transfer learning

## Architectures

* [x] MLP
* [ ] CNN
* [ ] RNN
* [ ] LSTM
* [ ] GRU
* [ ] Transformer

---

# 5. 🤖 Transformers

## Architecture

* [ ] Tokenization
* [ ] Token IDs
* [ ] Embeddings
* [ ] Positional encoding
* [ ] Self-attention
* [ ] Q / K / V
* [ ] Scaled dot-product attention
* [ ] Multi-head attention
* [ ] Residual connections
* [ ] LayerNorm
* [ ] Feed-forward network
* [ ] Causal mask

## Architecture types

* [ ] Encoder
* [ ] Decoder
* [ ] Encoder-Decoder
* [ ] Decoder-only

## Understanding

* [ ] Explain Transformer forward pass
* [ ] Explain why attention works
* [ ] Explain causal masking
* [ ] Explain multi-head attention
* [ ] Explain positional information
* [ ] Explain LayerNorm
* [ ] Explain residual connections

## Implementation

* [ ] Implement Self-Attention
* [ ] Implement Multi-Head Attention
* [ ] Implement Transformer Block
* [ ] Implement causal mask
* [ ] Write tests for tensor shapes

---

# 6. 📝 Language Models

## Fundamentals

* [ ] Language modeling
* [ ] Next-token prediction
* [ ] Causal Language Modeling
* [ ] Teacher forcing
* [ ] Cross-entropy
* [ ] Perplexity

## Generation

* [ ] Greedy decoding
* [ ] Temperature
* [ ] Top-k sampling
* [ ] Top-p sampling
* [ ] Beam search
* [ ] Repetition penalty

## Inference

* [ ] Batch inference
* [ ] Streaming
* [ ] KV cache
* [ ] Context window
* [ ] Tokens/sec
* [ ] Time to first token
* [ ] Throughput
* [ ] Latency

---

# 7. 🦙 LLM Engineering

## Models

* [ ] Base model
* [ ] Instruction-tuned model
* [ ] Chat model
* [ ] Embedding model
* [ ] Reranker

## Hugging Face

* [ ] Transformers
* [ ] Tokenizers
* [ ] Model loading
* [ ] Generation
* [ ] Batching
* [ ] Pipelines

## Prompt Engineering

* [ ] System prompts
* [ ] Few-shot prompting
* [ ] Structured output
* [ ] JSON output
* [ ] Function calling / tool use
* [ ] Prompt templates

## Model optimization

* [ ] Quantization
* [ ] INT8
* [ ] INT4
* [ ] GPU memory optimization
* [ ] Batching
* [ ] KV cache

---

# 8. 🔎 RAG

## Fundamentals

* [ ] RAG architecture
* [ ] Document ingestion
* [ ] Parsing
* [ ] Chunking
* [ ] Metadata
* [ ] Embeddings
* [ ] Vector database
* [ ] Retrieval
* [ ] Context construction
* [ ] Generation

## Chunking

* [ ] Fixed-size chunking
* [ ] Recursive chunking
* [ ] Semantic chunking
* [ ] Document-aware chunking
* [ ] Metadata-aware chunking

## Retrieval

* [ ] Dense retrieval
* [ ] Sparse retrieval
* [ ] BM25
* [ ] Hybrid search
* [ ] Similarity search
* [ ] Metadata filtering

## Reranking

* [ ] Understand rerankers
* [ ] Implement reranking
* [ ] Compare retrieve-only vs reranking

## Query transformation

* [ ] Query rewriting
* [ ] Multi-query retrieval
* [ ] HyDE

## Advanced RAG

* [ ] Context compression
* [ ] Parent-child retrieval
* [ ] Multi-step retrieval
* [ ] Agentic retrieval

---

# 9. 📏 LLM Evaluation

## Dataset

* [ ] Build evaluation dataset
* [ ] Define expected answers
* [ ] Define expected contexts
* [ ] Define evaluation criteria
* [ ] Create test cases for edge cases

## Retrieval metrics

* [ ] Recall@K
* [ ] Precision@K
* [ ] Hit Rate
* [ ] MRR
* [ ] NDCG

## Generation metrics

* [ ] Answer relevance
* [ ] Faithfulness
* [ ] Groundedness
* [ ] Citation correctness
* [ ] Hallucination rate

## Engineering metrics

* [ ] Latency
* [ ] TTFT
* [ ] Tokens/sec
* [ ] Throughput
* [ ] Token usage
* [ ] Cost

## Evaluation methodology

* [ ] Offline evaluation
* [ ] Human evaluation
* [ ] LLM-as-a-judge
* [ ] Pairwise evaluation
* [ ] Regression testing
* [ ] Evaluation datasets versioning

---

# 10. 🎯 Fine-tuning

## Fundamentals

* [ ] Fine-tuning
* [ ] Instruction tuning
* [ ] Pre-training vs fine-tuning
* [ ] Supervised fine-tuning
* [ ] Dataset construction
* [ ] Dataset quality

## PEFT

* [ ] PEFT
* [ ] LoRA
* [ ] QLoRA
* [ ] Adapters
* [ ] Rank
* [ ] Alpha
* [ ] Target modules

## Quantization

* [ ] INT8
* [ ] INT4
* [ ] GPTQ
* [ ] AWQ
* [ ] bitsandbytes

## Training

* [ ] Build training dataset
* [ ] Tokenize dataset
* [ ] Train LoRA adapter
* [ ] Save checkpoint
* [ ] Load adapter
* [ ] Run inference
* [ ] Evaluate fine-tuned model

## Comparison

* [ ] Base model
* [ ] Prompt engineering
* [ ] RAG
* [ ] LoRA
* [ ] RAG + LoRA

## Understand

* [ ] When to use RAG
* [ ] When to use fine-tuning
* [ ] When to use prompt engineering
* [ ] When to combine approaches

---

# 11. 🏗️ ML Engineering

## Code Quality

* [x] Project structure
* [ ] Type hints
* [ ] Logging
* [x] Configuration
* [x] Environment variables
* [x] Error handling
* [x] Unit tests
* [ ] Integration tests

## APIs

* [x] FastAPI
* [x] Request validation
* [x] Response schemas
* [ ] Authentication basics
* [ ] Async endpoints
* [ ] Streaming

## Docker

* [x] Dockerfile
* [ ] Docker Compose
* [ ] Multi-stage builds
* [x] Environment configuration
* [x] Health checks

## CI/CD

* [ ] GitHub Actions
* [ ] Automated tests
* [ ] Linting
* [ ] Docker build
* [ ] Deployment pipeline

---

# 12. ⚙️ MLOps

## Experiment Tracking

* [x] MLflow
* [x] Experiment tracking
* [x] Artifact tracking
* [x] Model registry

## Data

* [ ] Data validation
* [ ] Data versioning
* [ ] Dataset reproducibility

## Models

* [x] Model versioning
* [x] Model registry
* [x] Model promotion
* [ ] Rollback

## Monitoring

* [ ] Service health
* [ ] Latency
* [ ] Throughput
* [ ] Error rate
* [ ] Data drift
* [ ] Concept drift
* [ ] Model performance

## LLM Monitoring

* [ ] Token usage
* [ ] Cost
* [ ] Latency
* [ ] Retrieval quality
* [ ] Answer quality
* [ ] Hallucinations
* [ ] Prompt/version tracking

---

# 13. 🗄️ Data Engineering

Already have practical experience here; focus on closing ML-specific gaps.

## Spark

* [ ] DataFrame API
* [ ] Partitioning
* [ ] Shuffles
* [ ] Joins
* [ ] Broadcast joins
* [ ] UDF
* [ ] pandas_udf
* [ ] Performance optimization

## Airflow

* [ ] DAGs
* [ ] Operators
* [ ] Dependencies
* [ ] Scheduling
* [ ] Retries
* [ ] Monitoring
* [ ] Backfills

## Databases

* [ ] PostgreSQL
* [ ] Indexes
* [ ] Query plans
* [ ] Transactions
* [ ] Vector extensions

---

# 14. 🏛️ ML System Design

## Fundamentals

* [ ] Requirements gathering
* [ ] Data architecture
* [ ] Training architecture
* [ ] Inference architecture
* [ ] Batch vs online inference
* [ ] Scalability
* [ ] Reliability
* [ ] Cost

## ML Systems

* [ ] Recommendation system
* [ ] Ranking system
* [ ] Classification service
* [ ] Forecasting system
* [ ] Fraud detection
* [ ] Search system

## LLM Systems

* [ ] RAG system
* [ ] LLM API
* [ ] LLM serving platform
* [ ] Embedding service
* [ ] Reranking service
* [ ] Evaluation platform
* [ ] LLM monitoring platform

## Performance

* [ ] Caching
* [ ] Batching
* [ ] Async processing
* [ ] Horizontal scaling
* [ ] GPU utilization
* [ ] Load balancing
* [ ] Rate limiting

---

# 15. 💻 Python Interview

* [ ] Lists
* [ ] Dictionaries
* [ ] Sets
* [ ] Tuples
* [ ] Iterators
* [ ] Generators
* [ ] Decorators
* [ ] Context managers
* [ ] Classes
* [ ] Inheritance
* [ ] Dataclasses
* [ ] Type hints
* [ ] Asyncio
* [ ] Multiprocessing
* [ ] Multithreading
* [ ] GIL

## Algorithms

* [ ] Arrays
* [ ] HashMap
* [ ] Strings
* [ ] Two pointers
* [ ] Sliding window
* [ ] Binary search
* [ ] Stack
* [ ] Queue
* [ ] Heap
* [ ] Trees
* [ ] Graphs

---

# 16. 🗃️ SQL Interview

* [ ] JOIN
* [ ] GROUP BY
* [ ] HAVING
* [ ] CTE
* [ ] Subqueries
* [ ] Window functions
* [ ] `ROW_NUMBER`
* [ ] `RANK`
* [ ] `DENSE_RANK`
* [ ] `LAG`
* [ ] `LEAD`
* [ ] Query optimization
* [ ] Indexes
* [ ] Explain / query plans

---

# 17. 🚀 Portfolio

## Project 01 — Production ML System

* [x] Define problem
* [x] Select dataset
* [x] Build baseline
* [x] Feature engineering
* [x] Train model
* [x] Evaluate model
* [x] Error analysis
* [x] MLflow
* [x] FastAPI
* [x] Docker
* [x] Tests
* [ ] CI
* [ ] Monitoring
* [ ] README
* [ ] Architecture diagram

### Definition of Done

* [ ] Someone can clone the repository
* [x] Run the project
* [x] Train the model
* [x] Start the API
* [x] Send prediction request
* [ ] Understand the architecture
* [ ] Understand the experiments

---

# Project 02 — Enterprise RAG

* [ ] Define use case
* [ ] Collect documents
* [ ] Build ingestion pipeline
* [ ] Parse documents
* [ ] Implement chunking
* [ ] Generate embeddings
* [ ] Set up vector DB
* [ ] Implement dense retrieval
* [ ] Implement BM25
* [ ] Implement hybrid retrieval
* [ ] Add reranker
* [ ] Add query rewriting
* [ ] Build generation pipeline
* [ ] Add citations
* [ ] Build evaluation dataset
* [ ] Implement retrieval metrics
* [ ] Implement generation metrics
* [ ] Run experiments
* [ ] Analyze failures
* [ ] Build API
* [ ] Dockerize
* [ ] Add monitoring
* [ ] Write README
* [ ] Add architecture diagram

### Definition of Done

* [ ] End-to-end RAG works
* [ ] Evaluation is reproducible
* [ ] Retrieval strategies are compared
* [ ] Failure cases are documented
* [ ] Production architecture is documented

---

# Project 03 — LLM Fine-tuning

* [ ] Define task
* [ ] Select base model
* [ ] Prepare dataset
* [ ] Clean dataset
* [ ] Create train/validation split
* [ ] Configure LoRA
* [ ] Train adapter
* [ ] Evaluate model
* [ ] Compare with base model
* [ ] Compare with RAG
* [ ] Benchmark inference
* [ ] Document limitations
* [ ] Dockerize inference
* [ ] Write README

### Definition of Done

* [ ] Training is reproducible
* [ ] Evaluation is reproducible
* [ ] Base vs fine-tuned results are documented
* [ ] RAG vs fine-tuning trade-offs are documented

---

# 18. 🎤 Interview Preparation

## ML

* [ ] 30 ML questions
* [ ] Explain algorithms without notes
* [ ] Explain metrics
* [ ] Explain model selection
* [ ] Explain leakage
* [ ] Explain error analysis

## Deep Learning

* [ ] 30 DL questions
* [ ] Explain backpropagation
* [ ] Explain optimization
* [ ] Explain Transformer
* [ ] Explain attention

## LLM

* [ ] 30 LLM questions
* [ ] Explain RAG
* [ ] Explain embeddings
* [ ] Explain reranking
* [ ] Explain fine-tuning
* [ ] Explain LoRA
* [ ] Explain evaluation

## System Design

* [ ] 10 ML system design problems
* [ ] 10 LLM system design problems

## Mock Interviews

* [ ] 5 ML mocks
* [ ] 5 LLM mocks
* [ ] 5 System Design mocks
* [ ] 3 Python mocks
* [ ] 3 SQL mocks

---

# 19. 📚 Resources

Resources should be added here as they are actually used.

## ML

* [ ] Resource
* [ ] Resource
* [ ] Resource

## Deep Learning

* [ ] Resource
* [ ] Resource
* [ ] Resource

## Transformers / LLM

* [ ] Resource
* [ ] Resource
* [ ] Resource

## RAG

* [ ] Resource
* [ ] Resource
* [ ] Resource

## MLOps

* [ ] Resource
* [ ] Resource
* [ ] Resource

---

# 🧭 Progress Rules

A checkbox should only be marked when the topic is actually understood.

### ❌ Don't mark:

> "Watched a 2-hour video about Transformers."

### ✅ Mark when:

> "Can explain Transformer architecture, implement simplified attention, and answer basic interview questions."

For major topics use this rule:

```text
Understand
    ↓
Implement
    ↓
Explain
    ↓
Apply
```

Only then:

```text
[x] Topic completed
```

---

# 🏁 Final Definition of Done

The roadmap is considered complete when:

* [x] I can build a classical ML system end-to-end
* [x] I can build a PyTorch model
* [ ] I understand Transformer architecture
* [ ] I can build a RAG system
* [ ] I can evaluate RAG quality
* [ ] I can fine-tune an LLM with LoRA/QLoRA
* [ ] I can compare RAG vs fine-tuning
* [ ] I can deploy an ML/LLM service
* [ ] I understand monitoring and MLOps
* [ ] I can design an ML system
* [ ] I can design an LLM system
* [ ] I can pass ML interview questions
* [ ] I can pass LLM interview questions
* [ ] I can solve basic coding problems
* [ ] I can solve SQL interview problems
* [ ] I have 3 production-oriented portfolio projects

---

# ⭐ Target

> **Become an engineer who can take an ambiguous ML/LLM problem, design a solution, implement it, evaluate it, deploy it and explain the trade-offs.**
