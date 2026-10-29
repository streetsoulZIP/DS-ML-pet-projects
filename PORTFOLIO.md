# Обзор портфолио

## Профиль

Data Scientist / ML Engineer с практикой в tabular ML, Computer Vision, NLP, LLM/RAG, retrieval и геопространственных данных. Основной источник для автоматизации — [`portfolio/catalog.json`](portfolio/catalog.json); расширенные карточки — [`EXPERIENCE_ARCHIVE.md`](EXPERIENCE_ARCHIVE.md).

## Проекты с локальным кодом

| ID | Работа | Лучший результат и характер |
| --- | --- | --- |
| `semantic-retrieval-films` | [Multilingual Movie Retrieval](projects/multilingual-movie-retrieval) | test triplet loss 0.23; размер модели −63% |
| `underwater-semantic-segmentation` | [SUIM Underwater Segmentation](projects/underwater-segmentation) | local validation mIoU 0.833, Dice 0.8702 |
| `llm-film-data-generation` | [Synthetic Movie Query Generation](projects/synthetic-movie-query-generation) | 70k запросов и 6k описаний |
| `russian-news-classification` | Russian News Classification | F1 0.91 |
| `demand-forecasting` | Retail Demand Forecasting | RMSE 0.0233, R² 0.9995 |
| `sports-image-classification` | Sports Image Classification | F1 0.8623 |
| `building-energy-regression` | Building Energy Regression | MAE 0.25, R² 0.9984 |
| `student-employment-tabular` | Student Employment Prediction | ROC-AUC 0.92, F1 0.88; 5 стратегий трудоустройства |
| `spotify-topic-recommender` | Spotify Topic Recommendations | Recall@20 0.31; intra-list diversity 0.38 |
| `chess-move-probabilities` | Chess Move Probability Estimation | held-out ROC-AUC 0.89 |
| `dns-review-sentiment` | Тональность отзывов DNS | F1 0.95; ROC-AUC 0.97 |
| `fake-news-detection` | Детекция фейковых новостей WELFake | accuracy 0.94; baseline 0.90 |
| `roberta-ner` | NER на резюме | entity-level F1 0.76 (seqeval) |
| `speech-sentiment` | Эмоции в аудио CREMA-D | accuracy 0.66; random baseline 0.167 |

Полный список локальных работ — в [`projects/`](projects). В проекте шахматного задания сохранены веса `Hybrid.pt`.

## Соревнования и командные работы

| ID | Задача и работа | Результат |
| --- | --- | --- |
| `kaggle-biohub-cell-tracking` | 3D-трекинг клеток и восстановление делений по микроскопическим кадрам. | **Kaggle Silver Medal** |
| `kosmohackathon-fires` | Детекция очагов и сегментация последствий пожаров по спутниковым данным. | team private Score **0.8307** |
| `kosmohackathon-ndvi-reconstruction` | Восстановление пропусков NDVI в данных Sentinel-2, Landsat и MODIS. | hidden test RMSE **0.0536** |
| `kosmohackathon-hydrowatch` | Сегментация воды и новых зон затопления по паре спутниковых сцен. | public Score **0.8943**; transfer Score 0.4646 |
| `ozon-ecup-product-matching` | Поиск дубликатов товарных карточек по тексту, атрибутам, изображениям и OCR. | local Human validation macro PR-AUC **0.769580845** |
| `ozon-ecup-ltv-forecasting` | Прогноз будущего GMV клиента по истории покупок и событий. | ~1.67 RMSE в log1p(GMV) |
| `data-fest-2026-track-2` | 41-target классификация клиентов по ~2k признакам. | local Macro ROC-AUC ~**0.83** |
| `ai-finance-rag-assistant` | RAG-ответы на финансовые и правовые вопросы по корпусу документов. | выход в финал |
| `llm-product-attribute-labeling` | LLM извлекает и проверяет атрибуты из описаний товарных карточек. | agreement 85.2%; JSON valid rate 98.1% |
| `neftehack-process-forecasting` | Прогноз качества продукта по телеметрии и лабораторным измерениям. | held-out normalized RMSE 0.061; MAPE 7.1%; R² 0.902 |

Для каждого результата указан тип проверки: public/private leaderboard, hidden test, локальная валидация или официальный итог.
