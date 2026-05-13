# Cohort & Retention Analytics Portfolio

> **Data Analyst Portfolio Project** — E-commerce customer retention analysis using Python & pandas.

---

## 📌 Business Question

Một doanh nghiệp e-commerce muốn hiểu:
1. Doanh thu đang tăng trưởng như thế nào theo tháng?
2. Kênh acquisition nào mang lại khách hàng có giá trị cao nhất?
3. Cohort khách hàng nào có retention rate tốt nhất? Sau bao nhiêu tháng thì retention ổn định?

---

## 📁 Project Structure

```
cohort-retention-analytics/
├── data/
│   ├── raw/                    # CSV gốc (customers, products, orders, order_items)
│   └── processed/              # clean_orders.csv sau khi cleaning
├── notebooks/
│   └── project_starter.ipynb  # Notebook phân tích chính (chạy từ đây)
├── outputs/
│   ├── tables/                 # CSV kết quả phân tích
│   └── charts/                 # PNG charts
├── reports/
│   └── executive_summary.md   # Tóm tắt kết quả cho stakeholder
├── src/
│   └── generate_ecommerce_dataset.py   # Script tạo dataset
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run Locally

**Yêu cầu:** Python 3.9+ đã cài sẵn.

```powershell
# 1. Clone repo
git clone https://github.com/TranThiNgocVy/COHORT_and_RETENTION_ANALYTICS_PORTFOLIO.git
cd COHORT_and_RETENTION_ANALYTICS_PORTFOLIO

# 2. Tạo và kích hoạt virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate      # macOS/Linux

# 3. Cài thư viện
pip install -r requirements.txt

# 4. Tạo dataset (nếu chưa có trong data/raw/)
python src/generate_ecommerce_dataset.py --output data/raw

# 5. Chạy notebook phân tích
jupyter notebook notebooks/project_starter.ipynb
# Chọn "Run All" hoặc chạy từng cell theo thứ tự
```

> ⚠️ Chạy các cell **theo đúng thứ tự từ trên xuống** — mỗi bước phụ thuộc vào bước trước.

---

## 📊 Key Outputs

| File | Mô tả |
|------|-------|
| `outputs/tables/monthly_kpi.csv` | Revenue, orders, active customers, AOV theo tháng |
| `outputs/tables/channel_contribution.csv` | Revenue share và AOV theo kênh acquisition |
| `outputs/tables/cohort_retention_matrix.csv` | % khách quay lại theo cohort × tháng |
| `outputs/charts/cohort_retention_heatmap.png` | Visualization retention (xem ngay không cần chạy code) |
| `reports/executive_summary.md` | Tóm tắt findings và recommendations |

---

## 🔑 Key Findings

1. **[Điền sau khi chạy]** — Tháng doanh thu cao nhất là ... với ... VNĐ (+...% so với trung bình).
2. **[Điền sau khi chạy]** — Kênh ... chiếm ...% tổng revenue với AOV cao nhất (...VNĐ/đơn).
3. **[Điền sau khi chạy]** — Cohort ... có retention tháng 2 = ...%, giảm về ...% ở tháng 4.

---

## 🛠️ Tech Stack

- **Python 3.9+** — pandas, numpy, matplotlib, seaborn
- **Jupyter Notebook** — phân tích interactive
- **Matplotlib/Seaborn** — visualization

---

## 📋 Rubric (tự đánh giá)

| Tiêu chí | Trọng số | Trạng thái |
|----------|:--------:|:----------:|
| Data quality & cleaning | 25% | ✅ |
| KPI/cohort tính đúng | 30% | ✅ |
| Insight gắn với business question | 25% | ⬜ Điền sau |
| Notebook/README dễ chạy lại | 10% | ✅ |
| Chart & summary rõ ràng | 10% | ✅ |
