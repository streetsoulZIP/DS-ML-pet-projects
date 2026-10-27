# Synthetic movie query generation

## Задача

Подготовить query–description пары для обучения мультиязычного movie retriever без копирования пользовательских запросов с сайтов. Отдельно моделируются описание фильма, естественный поисковый запрос и типичные опечатки.

## Последовательность

```text
Краткое содержание → Mistral: структурированное описание
                     → Qwen: разнообразные поисковые запросы
                     → программа внесения опечаток → training pairs
```

| Материал | Назначение |
| --- | --- |
| [01_generate-film-descriptions-mistral.ipynb](01_generate-film-descriptions-mistral.ipynb) | извлечение жанра, сюжета, настроения и других аспектов из синопсиса |
| [02_generate-search-queries-qwen.ipynb](02_generate-search-queries-qwen.ipynb) | генерация запросов по неполному набору аспектов описания |
| [03_add-typos-to-queries.ipynb](03_add-typos-to-queries.ipynb) | добавление ошибок и неточностей в запросы |
| [queries_and_desc.parquet](queries_and_desc.parquet) | подготовленный публичный датасет |

Также сохранен [legacy experiment](00_legacy-film-description-experiment.ipynb) из исходного репозитория; он не заменяет основной пайплайн.

## Результат

Подготовлено около **70 000** натуральных поисковых запросов и **6 000** структурированных описаний фильмов. Это объём сформированных данных, а не метрика качества модели.

