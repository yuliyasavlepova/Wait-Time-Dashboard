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

## 📌 Personal Note

This project was created as part of my journey learning data analytics.  
The goal was not just to create charts, but to **highlight the value of analytics through a clean and intuitive interface**.

---

## 🚀 Run locally

```bash
git clone https://github.com/your-username/wait-time-dashboard.git
cd wait-time-dashboard
pip install -r requirements.txt
streamlit run app.py
...
---

