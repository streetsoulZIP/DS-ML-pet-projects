# Multilingual movie retrieval

## Задача

По запросу пользователя найти релевантное описание фильма на одном из 10 языков и обеспечить быстрый CPU inference. В проекте исследуется уменьшение BGE-M3 через pruning и distillation.

## Пайплайн

```text
Пары query–movie → NLLB-перевод → анализ слоёв → pruning
                                      ↓
Teacher embeddings → distillation → fine-tuning с triplet loss → int8 CPU inference
```

| Этап | Ноутбук |
| --- | --- |
| Перевод запросов | [01_translate-queries-nllb.ipynb](01_translate-queries-nllb.ipynb) |
| Анализ слоёв BGE-M3 | [02_analyze-bge-layers.ipynb](02_analyze-bge-layers.ipynb) |
| Pruning слоёв и словаря | [03_prune-bge-model-and-vocabulary.ipynb](03_prune-bge-model-and-vocabulary.ipynb) |
| Подготовка teacher embeddings | [04_prepare-teacher-embeddings.ipynb](04_prepare-teacher-embeddings.ipynb) |
| Distillation | [05_distill-retriever.ipynb](05_distill-retriever.ipynb) |
| Fine-tuning и оценка | [06_fine-tune-retriever.ipynb](06_fine-tune-retriever.ipynb) |

## Данные и методы

Исходная выборка — английские пары «запрос → описание фильма», переведённые NLLB и дополненные синтетическими запросами, шумом и негативными парами. Bi-encoder BGE-M3 используется для cosine-similarity retrieval. В эксперименте применены layer analysis, pruning словаря/слоёв, teacher–student distillation, triplet loss и int8-квантизация.

## Результат

- test triplet loss: **0.23**;
- сокращение размера модели примерно на **63%** (в исходной документации также описано сокращение примерно в три раза с учётом словаря);
- real-time inference на CPU.

Данные и артефакты fine-tuning: [Kaggle dataset](https://www.kaggle.com/datasets/kehhill/queries).



