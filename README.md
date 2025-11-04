# ⏱ Request Wait Time Analysis (Wait Time Dashboard)

An interactive Streamlit app for analyzing support request wait times based on a CSV dataset.  
The goal of the project is to visualize key wait time metrics, identify bottlenecks, and evaluate SLA compliance.

🔗 [Try it online →](https://slaskelar-d6j6twzgbkzskiyte3m9ma.streamlit.app/)

---

## 📊 Features

- General metrics:
  - Total number of requests
  - Average, median, and 90th percentile wait time
  - SLA 15/45 min breakdown

- Hourly dynamics:
  - Median wait time by hour of day
  - Heatmap of wait times by day and hour

- Top 5 peak hours with highest median wait

- Moderator analysis:
  - Median **handle time** (actual processing duration)

---

## 🛠 Technologies

- `Python`, `pandas`, `numpy`
- `Streamlit` for interface and app logic
- `matplotlib` & `seaborn` for data visualization
- Hosted on **Streamlit Cloud**

---

## 📁 Files

- `app.py` — main Streamlit app file
- `data.csv` — example input dataset
- `requirements.txt` — dependencies to run the project

---

## 🚀 Run locally

```bash
git clone https://github.com/your-username/wait-time-dashboard.git
cd wait-time-dashboard
pip install -r requirements.txt
streamlit run app.py
...
---

## 📌 Personal Note

This project was created as part of my journey learning data analytics.  
The goal was not just to create charts, but to **highlight the value of analytics through a clean and intuitive interface**.



# ⏱ Аналіз часу очікування запитів (Wait Time Dashboard)

Інтерактивна апка, створена в Streamlit для аналізу даних очікування запитів на основі CSV-файлу.  
Мета проєкту — візуалізувати основні метрики очікування, виявити вузькі місця та оцінити відповідність SLA.

🔗 [Спробувати онлайн →](https://slaskelar-d6j6twzgbkzskiyte3m9ma.streamlit.app/)

---

## 📊 Основні функції

- Загальні метрики:
  - Кількість запитів
  - Середній, медіанний та 90-й перцентиль часу очікування
  - SLA 15/45 хв

- Динаміка по годинам:
  - Середній/медіанний wait по годинам доби
  - Heatmap очікування за днями та годинами

- Топ-5 годин з найвищим очікуванням

- Аналіз по модераторам:
  - Медіанний **handle time** (реальний час обробки)

---

## 🛠 Технології

- `Python`, `pandas`, `numpy`
- `Streamlit` для візуалізації
- `matplotlib` та `seaborn` для графіків
- Хостинг на **Streamlit Cloud**

---

## 📁 Файли

- `app.py` — основний код Streamlit-додатку
- `data.csv` — приклад вхідних даних
- `requirements.txt` — залежності для запуску

---

## 🚀 Запуск локально

```bash
git clone https://github.com/your-username/wait-time-dashboard.git
cd wait-time-dashboard
pip install -r requirements.txt
streamlit run app.py
...

---

## 📌 Коментар

Цей проєкт я створила як частину власного навчання аналітики даних.  
Метою було не просто побудувати графіки, а **передати цінність аналітики через простий і зручний інтерфейс**.
