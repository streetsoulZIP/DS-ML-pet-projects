# ML / DS portfolio

Портфолио самостоятельных ML/DS-проектов, экспериментов и соревнований. Машиночитаемый источник — [`portfolio/catalog.json`](portfolio/catalog.json), человекочитаемый обзор — [`PORTFOLIO.md`](PORTFOLIO.md), происхождение импорта — [`SOURCES.md`](SOURCES.md).

| ID | Проект | Направление | Подтверждённый результат |
| --- | --- | --- | --- |
| `semantic-retrieval-films` | [Семантический поиск фильмов](Семантический%20поиск%20(retrievel)) | NLP, retrieval | Triplet loss 0.23; уменьшение модели на 63% |
| `llm-film-data-generation` | [Генерация данных о фильмах](генерация%20данных) | LLM, синтетические данные | 70k запросов, 6k описаний |
| `student-employment-tabular` | [Прогноз трудоустройства](Классификация%20и%20анализ%20табличных%20данных) | табличный ML | 5 стратегий |
| `russian-news-classification` | [Классификация новостей](Классификация%20текста) | NLP | F1 0.91 |
| `demand-forecasting` | [Прогноз спроса](временные%20ряды) | временные ряды | RMSE 0.0233; MSE 0.0117; R² 0.9995 |
| `sports-image-classification` | [Классификация спорта](Классификация%20изображений) | Computer Vision | F1-score 0.8623 |
| `underwater-semantic-segmentation` | [Сегментация подводных изображений](Семантическая%20сегментация) | Computer Vision | mIoU 0.813; Dice 0.8425 |
| `building-energy-regression` | [Энергоэффективность зданий](Регрессия) | табличный ML | MAE 0.25; R² 0.9984 |
| `dns-review-sentiment`, `fake-news-detection`, `roberta-ner`, `speech-sentiment` | [Импортированные NLP-работы](NLP%20и%20речевые%20технологии) | NLP, speech | результат не зафиксирован |
| `spotify-topic-recommender` | [Рекомендации Spotify](Рекомендательные%20системы) | recommender systems | результат не зафиксирован |
| `chess-move-probabilities` | [Шахматное тестовое задание](Шахматное%20тестовое%20задание) | Deep Learning | результат не зафиксирован |

Метрики восьми исходных работ перенесены из ранее подтверждённого README. Ноутбуки содержат авторский код и Markdown, но очищены от старых outputs и `execution_count`; они не служат доказательством сохранённых экспериментов.

## Пополнение

Добавьте код, запись с устойчивым `id` в `portfolio/catalog.json`, ссылку на ID в `PORTFOLIO.md` и запустите `python tools/validate_portfolio.py`.
