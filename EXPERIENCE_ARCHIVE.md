# Профессиональный архив опыта

Подробные карточки проектов, соревнований и хакатонов. Структурированный каталог компетенций и результатов — в [`portfolio/catalog.json`](portfolio/catalog.json).

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

Change detection базовой/пиковой воды и новых зон наводнения по SAR/оптическим парам сцен. Сравнены Siamese ResNet18 и scene-specific boosting; применена event-level validation. Tuned boosting достиг **public Score 0.8943**, а на независимой проверке переносимости — 0.4646.

## NLP, retrieval и LLM

### Multilingual Movie Retrieval

Локальный код: [`projects/multilingual-movie-retrieval`](projects/multilingual-movie-retrieval). Вход — пользовательский запрос на одном из 10 языков и набор описаний фильмов; выход — ранжирование описаний по смысловой близости к запросу. Для этого подготовлены multilingual query–description пары через NLLB, проведён анализ слоёв BGE-M3, pruning словаря и слоёв, teacher–student distillation, triplet fine-tuning и int8-квантизация для CPU inference. **Test triplet loss 0.23**, уменьшение размера модели около 63%.

### Synthetic Movie Query Generation

Локальный код: [`projects/synthetic-movie-query-generation`](projects/synthetic-movie-query-generation). Mistral формирует структурированные описания, Qwen генерирует запросы, а последующая обработка добавляет опечатки. Получено около **70k запросов** и **6k описаний**.

### AI Finance Challenge: RAG-ассистент

Индивидуальный RAG pipeline: разбиение документов на чанки до 400 токенов, `text-embedding-3-small`, FAISS, Qwen3-Reranker-4B, генерация Mistral Small/Gemma 3, answer grading и regeneration. **Результат: выход в финал.**

### LLM-разметка товарных пар

Задача — сделать сравнимыми две карточки маркетплейса, в которых одни и те же характеристики могут быть записаны по-разному или спрятаны в длинном описании. Gemma/Qwen через llama.cpp и GGUF извлекают бренд, модель, размеры, комплектацию и другие атрибуты в строгую JSON schema; затем Critic проверяет извлечение, а Judge принимает итоговую разметку. Реализованы repair/retry, кэширование и контроль качества. На контрольной выборке из 500 пар согласованность атрибутов с ручной разметкой составила **85.2%**, self-consistency Judge — **92.4%**, precision veto у Critic — **89.7%**, а JSON schema valid rate после repair/retry — **98.1%**.

## Tabular ML, recommender systems и временные ряды

### Ozon E-CUP: product matching

Нужно определить, относятся ли две карточки маркетплейса к одному товару, даже если названия отличаются, а важные различия скрыты в размере, модели или комплектации. Использованы нормализация атрибутов, typed features, NER, OCR текста на фото, image/text encoders, cross-attention и hard negatives. **Macro PR-AUC 0.769580845** на отдельной локальной Human validation (~73k строк); это не официальный leaderboard результат.

### Ozon E-CUP: LTV/GMV forecasting

Memory-efficient pipeline для ~250k клиентов: Parquet/Polars/PyArrow, rolling и decay aggregates, календарные признаки, memmap и LightGBM. **~1.67 RMSE в log1p(GMV)** при указанном в источнике ориентире лучшего решения ~1.64.

### Data Fest 2026, track 2

Multi-target классификация 41 бинарной цели на ~750k объектах и >2k признаках. Использованы экономная обработка Polars/PyArrow, Logistic Regression, CatBoost, XGBoost, LightGBM, MLP, feature selection и stacking. **Macro ROC-AUC около 0.83 на локальной проверке**; опубликованное решение остаётся в [отдельном репозитории](https://github.com/streetsoulZIP/Hackatons-and-ML-competions).

### Neftehack: технологические временные ряды

Командный проект нефтепереработки: объединение телеметрии, лабораторных и online-измерений через Parquet/as-of join, контроль доступности признаков без lookahead, CatBoost/LightGBM для динамики качества и контур оценки управляющих действий. На отложенном финальном периоде без lookahead: **normalized RMSE 0.061, MAPE 7.1%, R² 0.902**.

## Другие локальные работы

См. [`projects/`](projects): прогноз спроса, энергоэффективность зданий, трудоустройство студентов, классификация русскоязычных новостей, спортивных изображений, отзывы DNS, fake news, NER, классификация тональности речи, Spotify recommendations и шахматное тестовое задание.

### Прогноз трудоустройства студентов

Бинарная классификация трудоустройства на Engineering Placements (~3k записей): адаптивное логарифмирование и масштабирование признаков, отбор информативных факторов, логистическая регрессия и ансамбль деревьев. **ROC-AUC 0.92, F1 0.88**. Кластеризация выходов модели выявила 5 стратегий трудоустройства (silhouette 0.41, ARI между запусками 0.85); профили проверены вручную.

### Spotify: тематическое моделирование и рекомендации

Обработан корпус из 57 651 текста песен: langdetect, перевод через googletrans, TF-IDF с 12k признаков, NMF на 20 тем и профилирование топ-10 исполнителей. Content-based рекомендации по topic vectors достигли **Recall@20 0.31** на отложенной выборке против 0.05 у случайного baseline; intra-list diversity — **0.38**.

### Вероятности шахматных ходов

Бинарный скоринг легальных ходов для FEN-позиции: AlphaZero-кодирование доски 12×8×8, гибрид ConvNeXt + Transformer (`Hybrid.pt`), XGBoost с Optuna и GPU-обучением чанками. **ROC-AUC 0.89** на отложенных парах `(fen, move)`; inference выполняется на CPU без шахматного движка.

### Тональность русскоязычных отзывов DNS

CNN с тремя Conv1D и BatchNorm для анализа отзывов: accuracy **0.95**, F1 **0.95**, ROC-AUC **0.97**.

### Детекция фейковых новостей WELFake

`Embedding(20k) → LSTM(150) → GlobalMaxPool`: accuracy **0.94** против 0.90 у TF-IDF + Logistic Regression baseline.

### NER на резюме

RoBERTa-base для token classification: entity-level F1 **0.76** по seqeval.

### Классификация эмоций в аудио CREMA-D

40 MFCC → LSTM(256), шесть классов эмоций: accuracy **0.66** при случайном baseline 0.167.
