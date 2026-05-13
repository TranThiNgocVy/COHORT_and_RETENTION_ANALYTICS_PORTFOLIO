# Business Brief — Cohort & Retention Analytics

**Project:** Cohort & Retention Analytics Portfolio  
**Analyst:** [Tên của bạn]  
**Ngày tạo:** 2026-05  
**Stakeholders:** CEO, Growth Lead, Marketing Lead, Product Lead, CRM Lead  

---

## 1. Context (Bối cảnh)

Growth team đã triển khai nhiều chiến dịch acquisition trong 12 tháng gần nhất
(Jan–Dec 2025). Doanh thu tổng có xu hướng tăng, nhưng leadership chưa rõ
đây là tăng trưởng bền vững hay chỉ phản ánh chi phí marketing tăng.

Analyst được giao nhiệm vụ phân tích chất lượng tăng trưởng thông qua
cohort retention và channel performance để hỗ trợ quyết định ngân sách
và chiến lược giữ chân khách hàng cho Q1/2026.

---

## 2. Business Questions (Câu hỏi cần trả lời)

| # | Câu hỏi | Stakeholder | Output |
|:-:|---------|-------------|--------|
| 1 | Monthly revenue và active customers thay đổi như thế nào qua 12 tháng? | CEO / Growth Lead | Monthly KPI table |
| 2 | Channel nào đóng góp doanh thu và khách hàng nhiều nhất? | Marketing Lead | Channel contribution table |
| 3 | Retention sau tháng đầu của từng cohort ra sao? Cohort nào tốt nhất / tệ nhất? | Product Lead | Cohort retention matrix |
| 4 | Nên ưu tiên hành động gì để cải thiện retention trong Q1/2026? | CRM Lead | 2 recommendations |

---

## 3. Decision Needed (Quyết định cần đưa ra)

Đề xuất **2 hành động cụ thể** cho Growth/CRM team trong tháng tới,
dựa trên bằng chứng từ:
- Cohort retention theo channel và thời gian
- Xu hướng churn trong 30–60 ngày đầu của từng cohort

---

## 4. Scope & Constraints (Phạm vi & Giới hạn)

- **Dữ liệu:** Transactions từ Jan 2025 đến Dec 2025 (12 tháng)
- **Chỉ tính đơn hàng `completed`** — bỏ qua `cancelled`, `returned`
- **Grain phân tích:** Monthly (không phân tích daily/weekly)
- **Metric chính:** Revenue, Active Customers, Retention Rate, AOV
- **Ngoài phạm vi:** Phân tích theo sản phẩm, phân tích cost per channel

---

## 5. Expected Outputs (Kết quả mong đợi)

- [ ] `outputs/tables/monthly_kpi.csv`
- [ ] `outputs/tables/channel_contribution.csv`
- [ ] `outputs/tables/cohort_retention_matrix.csv`
- [ ] `outputs/charts/revenue_trend.png`
- [ ] `outputs/charts/channel_contribution.png`
- [ ] `outputs/charts/retention_heatmap.png`
- [ ] `reports/executive_summary.md`