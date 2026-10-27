# ML / DS portfolio

Портфолио проектов Богдана Яковенко в области Data Science и Machine Learning: CV, геопространственный ML, NLP, retrieval, LLM/RAG, табличные данные и временные ряды. Здесь хранится только код и материалы, которые допустимо публиковать; командные и закрытые решения описаны с корректным статусом и ссылками на свидетельства.

## Выделенные работы

| Проект | Что сделано | Лучший зафиксированный результат |
| --- | --- | --- |
| [Мультиязычный поиск фильмов](projects/multilingual-movie-retrieval) | BGE-M3 retriever на 10 языках: NLLB-перевод, layer analysis, pruning словаря/слоёв, distillation, fine-tuning и int8 inference. | Размер модели сокращён примерно на **63%**; test triplet loss **0.23**. |
| [Сегментация подводных сцен SUIM](projects/underwater-segmentation) | 8-классовая сегментация, class-aware crops, синхронные аугментации, combined loss; сравнение DeepLabV3+ и U-Net. | DeepLabV3+ + EfficientNet-B6: **mIoU 0.833**, Dice 0.8702 (локальная валидация). |
| [Синтетические данные для movie retrieval](projects/synthetic-movie-query-generation) | Mistral формирует структурированные описания, Qwen — поисковые запросы, затем добавляются реалистичные опечатки. | Около **70k запросов** и **6k описаний**. |
| `kaggle-biohub-cell-tracking` | Командный pipeline 3D cell tracking и восстановления lineage graph: 3D U-Net, temporal links, graph constraints и ILP. | **Серебряная медаль Kaggle**. Код не копируется из внешнего решения. |
| `kosmohackathon-ndvi-reconstruction` | Sensor-aware восстановление пропусков NDVI для Sentinel-2, Landsat и MODIS. | hidden test RMSE **0.0536** против baseline 0.1024 (−47.6%). |

## Навигация

- [`projects/`](projects) — 14 локальных самостоятельных работ; каждая папка названа по задаче, а не по технологии.
- [`PORTFOLIO.md`](PORTFOLIO.md) — краткий обзор проектов и соревнований.
- [`EXPERIENCE_ARCHIVE.md`](EXPERIENCE_ARCHIVE.md) — публичная, отредактированная версия банка опыта: задачи, методы, вклад и статус результатов.
- [`portfolio/catalog.json`](portfolio/catalog.json) — основной машиночитаемый каталог для будущей генерации резюме.
- [`SOURCES.md`](SOURCES.md) — происхождение импортированных материалов.

## Остальные локальные проекты

| Проект | Направление | Результат |
| --- | --- | --- |
| [Прогноз трудоустройства](projects/student-employment-prediction) | Tabular ML | пять выявленных стратегий |
| [Классификация русскоязычных новостей](projects/russian-news-classification) | NLP | F1 **0.91** |
| [Прогноз спроса](projects/retail-demand-forecasting) | Time series | RMSE **0.0233**, R² **0.9995** |
| [Классификация спорта на фото](projects/sports-image-classification) | Computer Vision | F1 **0.8623** |
| [Регрессия энергоэффективности](projects/building-energy-efficiency-regression) | Tabular ML | MAE **0.25**, R² **0.9984** |
| [Рекомендации Spotify](projects/spotify-topic-recommendation) | Recommender systems | результат не зафиксирован |
| [Вероятности шахматных ходов](projects/chess-move-probability-estimation) | Deep Learning | сохранены необходимые веса `Hybrid.pt` |
| [Четыре NLP-эксперимента](projects) | sentiment, NER, fake news, speech | результаты не подтверждены |

## Надёжность результатов

Значение всегда сопровождается характером проверки: локальная валидация, hidden/public/private leaderboard или официальное достижение. Сохранённые outputs ноутбуков удалены и не используются как доказательство. Записи с `unknown` в каталоге не содержат придуманных метрик.

## Для сопровождения

Добавьте новый проект в `projects/<kebab-case-name>/`, создайте устойчивый `id` в `portfolio/catalog.json`, сошлитесь на него в обзоре и выполните:

```powershell
python tools/validate_portfolio.py
```
