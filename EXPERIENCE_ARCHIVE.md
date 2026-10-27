# Профессиональный архив опыта

Публичная версия банка опыта. Контакты, биографические сведения и неподтверждённые персональные данные исключены. Поля и статусы для автоматической обработки — в [`portfolio/catalog.json`](portfolio/catalog.json).

## CV и геопространственный ML

### Kaggle Biohub: Cell Tracking During Development

Командное решение для 3D cell tracking и реконструкции lineage graph: 3D U-Net/DeepCenter для priors, TemporalUNet3D для межкадровых связей, candidate graph, lineage constraints и ILP. Вклад: интеграция detection/tracking-компонентов, настройка inference и графовых эвристик, проверка целостности lineage и сборка submission pipeline. **Официальный результат: серебряная медаль Kaggle.**

### SUIM Underwater Semantic Segmentation

Локальный код: [`projects/underwater-segmentation`](projects/underwater-segmentation). Выполнены class-aware crops, балансировка, синхронные image-mask аугментации и combined Focal+Dice+IoU loss; сравнены DeepLabV3+ и U-Net. Лучший вариант DeepLabV3+ + EfficientNet-B6 достиг **mIoU 0.833, Dice 0.8702, PA 0.8663, mPA 0.8401** на локальной валидации.

### КосмоХакатон: Fires

Задача объединяет детекцию активного горения по VIIRS и сегментацию контура/степени повреждения по Sentinel-1/2, GIS и DEM. Применялись rule baseline, LightGBM, U-Net/Siamese U-Net, hard-crop mining и пространственная валидация. Вклад в команде: данные и EDA, baselines, моделирование, ансамблирование и интеграция inference через Docker/сервис. **Лучший командный private Score 0.8307**; median-excess AF показал локальный OOF F1 0.9272.

### КосмоХакатон: NDVI reconstruction

Восстановление пропусков NDVI в наблюдениях Sentinel-2, Landsat и MODIS с учётом sensor bias. Созданы признаки соседних измерений, сезона, климата, сенсора и погоды, использован spatial holdout и LightGBM. На актуальном hidden test: **RMSE 0.0536** против 0.1024 у neighbor-mean baseline (−47.6%).

### КосмоХакатон: HydroWatch

Change detection базовой/пиковой воды и новых зон наводнения по SAR/оптическим парам сцен. Сравнены Siamese ResNet18 и scene-specific boosting; применена event-level validation. Tuned boosting достиг **public Score 0.8943**, однако отдельная проверка переносимости дала 0.4646 — это ограничение явно зафиксировано, а не скрыто.

## NLP, retrieval и LLM

### Multilingual Movie Retrieval

Локальный код: [`projects/multilingual-movie-retrieval`](projects/multilingual-movie-retrieval). BGE-M3 bi-encoder для поиска фильмов на 10 языках: NLLB, pruning, distillation, triplet fine-tuning и int8 inference. **Test triplet loss 0.23**, уменьшение размера модели около 63%.

### Synthetic Movie Query Generation

Локальный код: [`projects/synthetic-movie-query-generation`](projects/synthetic-movie-query-generation). Mistral формирует структурированные описания, Qwen генерирует запросы, а последующая обработка добавляет опечатки. Получено около **70k запросов** и **6k описаний**.

### AI Finance Challenge: RAG-ассистент

Индивидуальный RAG pipeline: разбиение документов на чанки до 400 токенов, `text-embedding-3-small`, FAISS, Qwen3-Reranker-4B, генерация Mistral Small/Gemma 3, answer grading и regeneration. **Результат: выход в финал.** Код не публикуется в этом репозитории.

### LLM-разметка товарных пар

Extractor–Critic–Judge для атрибутов товарных карточек: Gemma/Qwen через llama.cpp и GGUF, строгая JSON schema, repair/retry, кэширование и контроль качества. Числовая итоговая точность не зафиксирована — метрика не заявляется.

## Tabular ML, recommender systems и временные ряды

### Ozon E-CUP: product matching

Командный мультимодальный pairwise matching: нормализация атрибутов, typed features, NER, OCR, image/text encoders, cross-attention и hard negatives. **Macro PR-AUC 0.769580845** на отдельной локальной Human validation (~73k строк); это не официальный leaderboard результат.

### Ozon E-CUP: LTV/GMV forecasting

Memory-efficient pipeline для ~250k клиентов: Parquet/Polars/PyArrow, rolling и decay aggregates, календарные признаки, memmap и LightGBM. **~1.67 RMSE в log1p(GMV)** при указанном в источнике ориентире лучшего решения ~1.64.

### Data Fest 2026, track 2

Multi-target классификация 41 бинарной цели на ~750k объектах и >2k признаках. Использованы экономная обработка Polars/PyArrow, Logistic Regression, CatBoost, XGBoost, LightGBM, MLP, feature selection и stacking. **Macro ROC-AUC около 0.83 на локальной проверке**; опубликованное решение остаётся в [отдельном репозитории](https://github.com/streetsoulZIP/Hackatons-and-ML-competions).

### Neftehack: технологические временные ряды

Командный проект нефтепереработки: объединение телеметрии, лабораторных и online-измерений через Parquet/as-of join, контроль доступности признаков без lookahead, CatBoost/LightGBM для динамики качества и контур оценки управляющих действий. Итоговая RMSE и экономический эффект не зафиксированы — численный результат не приписывается.

## Другие локальные работы

См. [`projects/`](projects): прогноз спроса, энергоэффективность зданий, трудоустройство студентов, классификация русскоязычных новостей, спортивных изображений, отзывы DNS, fake news, NER, классификация тональности речи, Spotify recommendations и шахматное тестовое задание.
