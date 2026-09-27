# ML / LLM Engineer Roadmap

> Период: **25 сентября — 31 декабря 2026**
> Цель: выйти на уверенный **Middle / Middle+ уровень** в ML / LLM Engineering.
> Ориентир по нагрузке: **15–20 часов в неделю**.
> Принцип: **30% теория / 70% практика**.

---

## Как работать с roadmap

Каждую неделю:

1. Изучить необходимую теорию.
2. Реализовать ключевые концепции самостоятельно.
3. Применить их в проекте.
4. Зафиксировать результаты в Git.
5. Подготовить короткое объяснение того, что было изучено.
6. Если тема требует — добавить тесты, benchmark или эксперимент.

Roadmap определяет **порядок работы**, а `README.md` содержит чекбоксы навыков.

---

# Week 0 — Setup

### 25–27 сентября

### Repository

* [ ] Создать структуру репозитория.
* [ ] Создать `README.md`.
* [ ] Создать `ROADMAP.md`.
* [ ] Создать `PROGRESS.md`.
* [ ] Создать директории для проектов.
* [ ] Настроить `.gitignore`.
* [ ] Настроить `pyproject.toml`.
* [ ] Настроить Ruff.
* [ ] Настроить pytest.
* [ ] Настроить pre-commit.
* [ ] Создать базовый CI pipeline.

### Environment

* [ ] Настроить Python environment.
* [ ] Зафиксировать зависимости.
* [ ] Проверить локальный запуск тестов.
* [ ] Проверить linting.
* [ ] Сделать первый commit.

### Результат

Рабочий репозиторий, в котором можно развивать все последующие проекты.

---

# Week 1 — ML Fundamentals

### 28 сентября – 4 октября

## Теория

* [ ] Bias / Variance.
* [ ] Overfitting / Underfitting.
* [ ] Train / validation / test.
* [ ] Cross-validation.
* [ ] Data leakage.
* [ ] Feature engineering.
* [ ] Regularization.
* [ ] Hyperparameter optimization.

## Algorithms

* [ ] Linear Regression.
* [ ] Logistic Regression.
* [ ] Decision Tree.
* [ ] Random Forest.
* [ ] Gradient Boosting.
* [ ] CatBoost / LightGBM.

## Metrics

* [ ] Accuracy.
* [ ] Precision.
* [ ] Recall.
* [ ] F1.
* [ ] ROC-AUC.
* [ ] PR-AUC.
* [ ] MAE.
* [ ] MSE.
* [ ] RMSE.

## Практика

* [ ] Создать baseline ML pipeline.
* [ ] Сделать preprocessing.
* [ ] Обучить несколько моделей.
* [ ] Провести cross-validation.
* [ ] Сравнить модели.
* [ ] Провести error analysis.

### Результат недели

Первый воспроизводимый ML experiment с baseline и сравнением моделей.

---

# Week 2 — ML Engineering

### 5–11 октября

## Experiment Management

* [ ] MLflow.
* [ ] Tracking parameters.
* [ ] Tracking metrics.
* [ ] Tracking artifacts.
* [ ] Model registry.
* [ ] Reproducibility.

## API

* [ ] FastAPI.
* [ ] Pydantic.
* [ ] `/predict`.
* [ ] `/health`.
* [ ] Validation ошибок.

## Docker

* [ ] Dockerfile.
* [ ] Docker image.
* [ ] Environment variables.
* [ ] Local deployment.

## Практика

* [ ] Обернуть ML-модель в API.
* [ ] Добавить MLflow.
* [ ] Собрать Docker image.
* [ ] Запустить сервис локально.
* [ ] Добавить тесты API.

### Результат недели

ML-модель доступна как воспроизводимый сервис.

---

# Week 3 — PyTorch

### 12–18 октября

## Fundamentals

* [ ] Tensor.
* [ ] Shape.
* [ ] Broadcasting.
* [ ] Autograd.
* [ ] Dataset.
* [ ] DataLoader.
* [ ] Module.
* [ ] Optimizer.
* [ ] Loss.

## Training

* [ ] Forward pass.
* [ ] Backpropagation.
* [ ] Training loop.
* [ ] Validation loop.
* [ ] Checkpointing.
* [ ] Early stopping.

## Практика

* [ ] Реализовать neural network.
* [ ] Написать training loop самостоятельно.
* [ ] Добавить validation.
* [ ] Сохранять checkpoints.
* [ ] Построить графики train/validation loss.

### Результат недели

Понимание полного цикла обучения нейронной сети без reliance на high-level abstractions.

---

# Week 4 — Transformers

### 19–25 октября

## Теория

* [ ] Embeddings.
* [ ] Positional encoding.
* [ ] Query / Key / Value.
* [ ] Self-attention.
* [ ] Multi-head attention.
* [ ] Residual connections.
* [ ] LayerNorm.
* [ ] Feed-forward network.
* [ ] Transformer block.

## Практика

* [ ] Реализовать Self-Attention.
* [ ] Реализовать Multi-Head Attention.
* [ ] Реализовать Transformer Block.
* [ ] Написать минимальный Transformer.
* [ ] Проверить shapes каждого tensor.

### Результат недели

Умение объяснить Transformer на уровне tensor operations и написать его базовые компоненты самостоятельно.

---

# Week 5 — Mini GPT

### 26 октября – 1 ноября

## Language Modeling

* [ ] Tokenization.
* [ ] Vocabulary.
* [ ] Input / target shifting.
* [ ] Causal mask.
* [ ] Next-token prediction.
* [ ] Cross-entropy loss.
* [ ] Temperature.
* [ ] Top-k.
* [ ] Top-p.

## Inference

* [ ] Greedy decoding.
* [ ] Sampling.
* [ ] KV cache.
* [ ] Context window.

## Практика

* [ ] Реализовать tokenizer pipeline.
* [ ] Создать небольшой dataset.
* [ ] Обучить mini GPT.
* [ ] Реализовать generation.
* [ ] Реализовать sampling.
* [ ] Добавить KV cache.

### Результат недели

Минимальная language model, которую можно обучить и использовать для генерации текста.

---

# Week 6 — Hugging Face & LLM Inference

### 2–8 ноября

## Hugging Face

* [ ] Transformers.
* [ ] Tokenizers.
* [ ] Model loading.
* [ ] Generation API.
* [ ] Datasets.

## Inference

* [ ] Local inference.
* [ ] Batch inference.
* [ ] Quantization.
* [ ] GPU memory.
* [ ] CPU vs GPU.
* [ ] Tokens/sec.
* [ ] Latency.

## Практика

* [ ] Запустить локальную LLM.
* [ ] Сделать inference script.
* [ ] Добавить batch inference.
* [ ] Замерить latency.
* [ ] Замерить throughput.
* [ ] Сравнить разные settings.

### Результат недели

Умение самостоятельно запускать и измерять LLM inference.

---

# Week 7 — RAG Fundamentals

### 9–15 ноября

## Architecture

* [ ] Document ingestion.
* [ ] Parsing.
* [ ] Chunking.
* [ ] Embeddings.
* [ ] Vector database.
* [ ] Retrieval.
* [ ] Context construction.
* [ ] Generation.

## Project 02

**Enterprise Knowledge Assistant**

* [ ] Определить domain.
* [ ] Собрать документы.
* [ ] Реализовать ingestion.
* [ ] Реализовать chunking.
* [ ] Построить embeddings.
* [ ] Создать vector index.
* [ ] Реализовать retrieval.
* [ ] Подключить LLM.
* [ ] Вернуть citations.

### Результат недели

Работающий end-to-end RAG prototype.

---

# Week 8 — Advanced RAG

### 16–22 ноября

## Retrieval

* [ ] Dense retrieval.
* [ ] BM25.
* [ ] Hybrid search.
* [ ] Metadata filtering.
* [ ] Reranking.

## Query Transformation

* [ ] Query rewriting.
* [ ] Query expansion.
* [ ] Multi-query retrieval.
* [ ] HyDE.

## Chunking

* [ ] Fixed-size.
* [ ] Sentence-based.
* [ ] Semantic chunking.
* [ ] Overlap.
* [ ] Metadata-aware chunks.

## Практика

* [ ] Реализовать BM25.
* [ ] Реализовать dense retrieval.
* [ ] Сравнить retrieval approaches.
* [ ] Добавить hybrid search.
* [ ] Добавить reranker.
* [ ] Провести chunking experiments.

### Результат недели

RAG pipeline с несколькими retrieval strategies.

---

# Week 9 — LLM Evaluation

### 23–29 ноября

## Dataset

* [ ] Создать evaluation dataset.
* [ ] Подготовить queries.
* [ ] Подготовить ground truth.
* [ ] Определить expected citations.

## Retrieval Metrics

* [ ] Recall@K.
* [ ] Precision@K.
* [ ] MRR.
* [ ] Hit Rate.

## Generation Metrics

* [ ] Answer relevance.
* [ ] Faithfulness.
* [ ] Citation correctness.
* [ ] Context relevance.

## Engineering Metrics

* [ ] Latency.
* [ ] Token usage.
* [ ] Cost.
* [ ] Throughput.

## Практика

* [ ] Сделать evaluation pipeline.
* [ ] Сохранение результатов.
* [ ] Автоматический benchmark.
* [ ] Error analysis.

### Результат недели

Измеримая система оценки качества RAG.

---

# Week 10 — RAG Experiments

### 30 ноября – 6 декабря

## Benchmark

Сравнить:

* [ ] Naive RAG.
* [ ] Better chunking.
* [ ] Dense retrieval.
* [ ] BM25.
* [ ] Hybrid retrieval.
* [ ] Reranking.
* [ ] Query rewriting.

## Analysis

* [ ] Сравнить Recall@K.
* [ ] Сравнить MRR.
* [ ] Сравнить answer quality.
* [ ] Сравнить citation correctness.
* [ ] Сравнить latency.
* [ ] Сравнить token usage.
* [ ] Провести error analysis.

## Documentation

* [ ] Сформулировать hypotheses.
* [ ] Зафиксировать experiment setup.
* [ ] Сохранить результаты.
* [ ] Сделать выводы.

### Результат недели

Benchmark RAG-системы с объяснением того, какие изменения повлияли на какие метрики.

---

# Week 11 — Fine-tuning

### 7–13 декабря

## Fundamentals

* [ ] Pretraining vs fine-tuning.
* [ ] Instruction tuning.
* [ ] SFT.
* [ ] LoRA.
* [ ] QLoRA.
* [ ] PEFT.
* [ ] Quantization.

## Dataset

* [ ] Сбор данных.
* [ ] Cleaning.
* [ ] Deduplication.
* [ ] Instruction format.
* [ ] Train / validation split.

## Практика

* [ ] Выбрать небольшую open-source LLM.
* [ ] Подготовить dataset.
* [ ] Провести baseline inference.
* [ ] Настроить LoRA.
* [ ] Провести fine-tuning.
* [ ] Сохранить adapter.
* [ ] Запустить inference.

### Результат недели

Работающий LoRA/QLoRA fine-tuning pipeline.

---

# Week 12 — RAG vs Fine-tuning

### 14–20 декабря

## Сравнение

Сравнить:

* [ ] Base model.
* [ ] Prompt engineering.
* [ ] RAG.
* [ ] LoRA.
* [ ] RAG + LoRA.

## Evaluation

* [ ] Accuracy / task quality.
* [ ] Faithfulness.
* [ ] Citation correctness.
* [ ] Latency.
* [ ] Memory.
* [ ] Token usage.
* [ ] Inference cost.

## Практика

* [ ] Создать единый evaluation dataset.
* [ ] Прогнать все approaches.
* [ ] Сохранить результаты.
* [ ] Провести error analysis.
* [ ] Написать technical report.

### Результат недели

Понимание того, когда использовать prompting, RAG и fine-tuning.

---

# Week 13 — Production & System Design

### 21–27 декабря

## ML System Design

* [ ] Problem formulation.
* [ ] Data pipeline.
* [ ] Feature store concept.
* [ ] Training pipeline.
* [ ] Model serving.
* [ ] Batch inference.
* [ ] Online inference.
* [ ] Monitoring.
* [ ] Retraining.
* [ ] Scaling.
* [ ] Failure handling.

## LLM System Design

* [ ] LLM gateway.
* [ ] Prompt management.
* [ ] RAG architecture.
* [ ] Vector database.
* [ ] Caching.
* [ ] Rate limiting.
* [ ] Fallbacks.
* [ ] Evaluation.
* [ ] Cost control.
* [ ] Observability.

## Практика

* [ ] Нарисовать ML system design.
* [ ] Нарисовать RAG system design.
* [ ] Провести design review самостоятельно.
* [ ] Описать bottlenecks.
* [ ] Описать failure modes.
* [ ] Описать scaling strategy.

### Результат недели

Умение спроектировать production ML/LLM system и аргументировать архитектурные решения.

---

# Week 14 — Interview Sprint

### 28–31 декабря

## ML

* [ ] Повторить ML fundamentals.
* [ ] Повторить metrics.
* [ ] Повторить algorithms.
* [ ] Повторить feature engineering.
* [ ] Повторить model evaluation.

## Statistics

* [ ] Probability.
* [ ] Hypothesis testing.
* [ ] Confidence intervals.
* [ ] A/B testing.
* [ ] Causal inference.

## Deep Learning

* [ ] Backpropagation.
* [ ] Optimization.
* [ ] Regularization.
* [ ] CNN.
* [ ] Transformer.
* [ ] Attention.

## LLM

* [ ] Transformer architecture.
* [ ] Generation.
* [ ] RAG.
* [ ] Evaluation.
* [ ] Fine-tuning.
* [ ] LoRA / QLoRA.
* [ ] Quantization.
* [ ] Inference optimization.

## Python

* [ ] Data structures.
* [ ] Algorithms.
* [ ] Complexity.
* [ ] OOP.
* [ ] Iterators / generators.
* [ ] Decorators.
* [ ] Async basics.

## SQL

* [ ] JOIN.
* [ ] Window functions.
* [ ] CTE.
* [ ] Aggregations.
* [ ] Query optimization.
* [ ] Complex analytical queries.

## Mock Interviews

* [ ] ML mock interview.
* [ ] Python mock interview.
* [ ] SQL mock interview.
* [ ] ML System Design mock interview.
* [ ] LLM interview.

### Финальный результат

К концу декабря должны быть готовы:

* [ ] Production ML project.
* [ ] Enterprise RAG project.
* [ ] LLM fine-tuning project.
* [ ] GitHub repository.
* [ ] Technical documentation.
* [ ] Benchmarks.
* [ ] System design diagrams.
* [ ] Interview preparation.
* [ ] Updated CV.
* [ ] Updated LinkedIn / profile.
