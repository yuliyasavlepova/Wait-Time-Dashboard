import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Аналіз служби підтримки", layout="wide")
st.title("📊 Аналіз SLA + медіанний wait + handle time")

# 📥 Завантаження CSV
df = pd.read_csv("data.csv", parse_dates=["request_time", "start_time", "finish_time"])

# 🧹 Очищення
df = df.dropna(subset=["request_time", "start_time", "finish_time"])
df = df[df["start_time"] > df["request_time"]]

# ⏱ Обчислення
df["wait_time_min"] = (df["start_time"] - df["request_time"]).dt.total_seconds() / 60
df["handle_time_min"] = (df["finish_time"] - df["start_time"]).dt.total_seconds() / 60
df["request_hour"] = df["request_time"].dt.hour
df["request_weekday"] = df["request_time"].dt.strftime("%A")

# 📍 Фільтр по команді
teams = df["team"].unique()
team = st.selectbox("Оберіть команду:", teams)
filtered = df[df["team"] == team]

# 🎯 Метрики (медіана)
st.markdown("### 🎯 Загальні метрики (медіана)")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Кількість запитів", len(filtered))
col2.metric("Медіана wait (хв)", round(filtered["wait_time_min"].median(), 1))
col3.metric("Медіана handle (хв)", round(filtered["handle_time_min"].median(), 1))
col4.metric("P90 wait (хв)", round(np.percentile(filtered["wait_time_min"], 90), 1))

# 🚦 SLA
st.markdown("### 🚦 SLA (15/45 хв)")
sla_15 = (filtered["wait_time_min"] <= 15).mean() * 100
sla_45 = (filtered["wait_time_min"] <= 45).mean() * 100
col5, col6 = st.columns(2)
col5.metric("✅ <= 15 хв", f"{sla_15:.1f} %")
col6.metric("⚠️ <= 45 хв", f"{sla_45:.1f} %")

# ⏰ Медіана wait по годинам
st.markdown("### ⏰ Медіана wait по годинам")
med_by_hour = filtered.groupby("request_hour")["wait_time_min"].median()
st.bar_chart(med_by_hour)

# 📅 Медіана wait по дням тижня
st.markdown("### 📆 Медіана wait по дням тижня")
med_by_weekday = filtered.groupby("request_weekday")["wait_time_min"].median().reindex(
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
)
st.bar_chart(med_by_weekday)

# 📉 ТОП-5 найгірших годин (медіана найбільша)
st.markdown("### 🔥 ТОП-5 годин з найвищою медіаною wait")
top_hours = med_by_hour.sort_values(ascending=False).head(5)
top_hours_df = top_hours.reset_index()
top_hours_df.columns = ["Година", "Медіана wait (хв)"]
st.table(top_hours_df)

# 🧑‍💼 Аналіз по модераторам — handle time
st.markdown("### 🧑‍💼 Медіана handle time по модераторам")
handle_stats = filtered.groupby("moderator")["handle_time_min"].median().sort_values()
handle_stats_df = handle_stats.reset_index()
handle_stats_df.columns = ["Модератор", "Медіана handle (хв)"]
st.dataframe(handle_stats_df)

# 🌡️ HEATMAP — день × година
st.markdown("### 🌡️ Heatmap: медіана wait по годинам і дням тижня")

# 1. Агрегація
heat_data = filtered.groupby(["request_weekday", "request_hour"])["wait_time_min"].median().unstack()

# 2. Порядок днів
ordered_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
heat_data = heat_data.reindex(ordered_days)

# 3. Форматування значень
def format_value(x):
    if x >= 1000:
        return f"{x/1000:.1f}k"
    else:
        return f"{int(x)}"

heat_display = heat_data.applymap(format_value)

# 4. Візуалізація
fig, ax = plt.subplots(figsize=(15, 8))
sns.heatmap(
    heat_data,
    cmap="YlOrRd",
    annot=heat_display,
    fmt="",
    linewidths=.5,
    annot_kws={"size": 8},
    ax=ax
)
plt.xlabel("Година доби")
plt.ylabel("День тижня")
st.pyplot(fig)

# 📋 Перегляд очищених даних
st.markdown("### 📋 Перші 10 записів очищених даних")
st.dataframe(filtered[[
    "team", "moderator", "request_time", "start_time", "finish_time", "wait_time_min", "handle_time_min"
]].head(10))

