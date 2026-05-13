# Executive Summary: Cohort & Retention Analytics

**Ngày:** 13/05/2026  
**Dataset:** Synthetic e-commerce — 650 khách hàng, 12 sản phẩm, ~2,057 đơn hàng (2025)

---

## 📌 Context

Dự án phân tích dữ liệu e-commerce tổng hợp nhằm đánh giá hiệu quả doanh thu, đóng góp theo kênh và chất lượng giữ chân khách hàng (retention) theo cohort.

**Business Question:** Kênh nào mang lại khách hàng chất lượng nhất? Cohort nào có retention tốt nhất và vì sao?

---

## 📊 Key Findings

1. **Revenue tổng:** 50,390,620,000 VNĐ trong 12 tháng — trung bình 4,199,218,333 VNĐ/tháng. Tháng đỉnh là **2025-11** với 7,897,053,000 VNĐ.

2. **Channel dominant:** Kênh **paid_search** chiếm 29.3% tổng revenue với AOV 26,912,470 VNĐ/đơn — [thêm nhận xét so sánh với các kênh còn lại].

3. **Cohort retention:** Cohort 2025-01 có retention rate tháng 2 = 8%, tháng 4 = 21% — [thêm đánh giá: tốt/thấp so với benchmark industry ~25–30%].

---

## 💼 Business Implications

- **Growth:** [Nhận xét về xu hướng doanh thu — tăng trưởng đều hay phụ thuộc vào promotion?]
- **CRM:** Retention drop mạnh nhất xảy ra ở tháng thứ 2 (index 0→1) → đây là thời điểm vàng để re-engage khách hàng.
- **Marketing:** Nếu 1 kênh chiếm >40% revenue → concentration risk — cần đa dạng hoá nguồn traffic.

---

## ✅ Recommendations

1. **Triển khai re-engagement campaign trong 30 ngày sau mua đầu** vì retention drop lớn nhất ở index 0→1 (8%).
2. **Tăng ngân sách cho kênh paid_search** vì kênh này có AOV cao nhất (26,912,470 VNĐ/đơn) — mỗi đồng acquisition mang về nhiều revenue hơn.
3. **[Recommendation 3]** vì [evidence từ data].

---

## ⚠️ Data Quality Caveat

- Dataset là dữ liệu **tổng hợp (synthetic)** — các pattern được thiết kế để có ý nghĩa phân tích nhưng không phản ánh thị trường thực.
- Đơn `cancelled` và `returned` được loại khỏi KPI và cohort analysis — chỉ tính đơn `completed`.
- Cohort 2–3 tháng cuối chưa đủ thời gian quan sát → không nên so sánh với cohort tháng đầu.

---

## 📁 Outputs

| File | Mô tả |
|------|-------|
| `outputs/tables/monthly_kpi.csv` | KPI theo tháng |
| `outputs/tables/channel_contribution.csv` | Revenue share theo kênh |
| `outputs/tables/cohort_retention_matrix.csv` | Retention matrix |
| `outputs/charts/monthly_revenue_trend.png` | Line chart doanh thu |
| `outputs/charts/revenue_by_channel.png` | Bar chart theo kênh |
| `outputs/charts/cohort_retention_heatmap.png` | Heatmap cohort |
