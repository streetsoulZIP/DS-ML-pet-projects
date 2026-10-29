# ML / DS portfolio

Портфолио проектов Богдана Яковенко в области Data Science и Machine Learning: CV, геопространственный ML, NLP, retrieval, LLM/RAG, табличные данные и временные ряды.

## Выделенные работы

| Проект | Что сделано | Лучший зафиксированный результат |
| --- | --- | --- |
| [Мультиязычный поиск фильмов](projects/multilingual-movie-retrieval) | По запросу на одном из 10 языков ранжирует описания фильмов. Для этого подготовлены multilingual пары, сокращён BGE-M3 и выполнены distillation, fine-tuning и int8 inference. | Размер модели сокращён примерно на **63%**; test triplet loss **0.23**. |
| [Сегментация подводных сцен SUIM](projects/underwater-segmentation) | 8-классовая сегментация, class-aware crops, синхронные аугментации, combined loss; сравнение DeepLabV3+ и U-Net. | DeepLabV3+ + EfficientNet-B6: **mIoU 0.833**, Dice 0.8702 (локальная валидация). |
| [Синтетические данные для movie retrieval](projects/synthetic-movie-query-generation) | Mistral формирует структурированные описания, Qwen — поисковые запросы, затем добавляются реалистичные опечатки. | Около **70k запросов** и **6k описаний**. |
| `kaggle-biohub-cell-tracking` | Командный pipeline 3D cell tracking и восстановления lineage graph: 3D U-Net, temporal links, graph constraints и ILP. | **Серебряная медаль Kaggle**. |
| `kosmohackathon-ndvi-reconstruction` | Восстанавливает пропуски NDVI в спутниковых временных рядах Sentinel-2, Landsat и MODIS, учитывая смещения между сенсорами и сезонность. | hidden test RMSE **0.0536** против baseline 0.1024 (−47.6%). |

## Навигация

- [`projects/`](projects) — 14 самостоятельных работ.
- [`PORTFOLIO.md`](PORTFOLIO.md) — краткий обзор проектов и соревнований.
- [`EXPERIENCE_ARCHIVE.md`](EXPERIENCE_ARCHIVE.md) — подробные карточки задач, методов, вклада и результатов.
- [`portfolio/catalog.json`](portfolio/catalog.json) — структурированный каталог проектов и компетенций.

## Остальные локальные проекты

| Проект | Направление | Результат |
| --- | --- | --- |
| [Прогноз трудоустройства](projects/student-employment-prediction) | Tabular ML | ROC-AUC **0.92**, F1 **0.88**; 5 стратегий |
| [Классификация русскоязычных новостей](projects/russian-news-classification) | NLP | F1 **0.91** |
| [Прогноз спроса](projects/retail-demand-forecasting) | Time series | RMSE **0.0233**, R² **0.9995** |
| [Классификация спорта на фото](projects/sports-image-classification) | Computer Vision | F1 **0.8623** |
| [Регрессия энергоэффективности](projects/building-energy-efficiency-regression) | Tabular ML | MAE **0.25**, R² **0.9984** |
| [Рекомендации Spotify](projects/spotify-topic-recommendation) | Recommender systems | Recall@20 **0.31**; diversity **0.38** |
| [Вероятности шахматных ходов](projects/chess-move-probability-estimation) | Deep Learning | ROC-AUC **0.89** |
| [Тональность отзывов DNS](projects/dns-review-sentiment-analysis) | NLP, sentiment analysis | F1 **0.95**, ROC-AUC **0.97** |
| [Детекция фейковых новостей](projects/fake-news-detection) | NLP, text classification | accuracy **0.94** |
| [NER на резюме](projects/roberta-ner) | NLP, token classification | entity-level F1 **0.76** |
| [Классификация эмоций в речи](projects/speech-sentiment-classification) | Speech, emotion recognition | accuracy **0.66** |
