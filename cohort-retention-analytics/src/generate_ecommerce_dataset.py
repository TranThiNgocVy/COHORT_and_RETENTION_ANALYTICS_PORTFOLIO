#!/usr/bin/env python3
"""
generate_ecommerce_dataset.py

Sinh dữ liệu e-commerce tổng hợp (synthetic) cho dự án Cohort & Retention Analytics.
Tạo ra 4 file CSV: customers, products, orders, order_items.

Cách chạy:
    cd cohort-retention-analytics
    python src/generate_ecommerce_dataset.py --output data/raw --seed 20260503
"""

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

# ─── Constants ────────────────────────────────────────────────────────────────
N_CUSTOMERS  = 650
N_PRODUCTS   = 12
ORDER_START  = "2025-01-01"   # Thời gian đặt hàng: Jan–Dec 2025
ORDER_END    = "2025-12-31"
SIGNUP_START = "2024-06-01"   # Một số khách signup trước kỳ phân tích


# ─── Generator: customers ─────────────────────────────────────────────────────
def gen_customers(rng: np.random.Generator) -> pd.DataFrame:
    """Sinh bảng customers (1 row = 1 khách hàng)."""
    n = N_CUSTOMERS

    # signup_date ngẫu nhiên trong khoảng Jun 2024 – Dec 2025
    signup_start = pd.Timestamp(SIGNUP_START)
    order_end    = pd.Timestamp(ORDER_END)
    total_days   = (order_end - signup_start).days
    offsets      = rng.integers(0, total_days + 1, size=n)
    signup_dates = [
        (signup_start + pd.Timedelta(days=int(d))).strftime("%Y-%m-%d")
        for d in offsets
    ]

    regions   = ["Hà Nội", "TP.HCM", "Đà Nẵng", "Hải Phòng", "Cần Thơ"]
    region_p  = [0.28, 0.42, 0.12, 0.10, 0.08]

    segments  = ["New", "Regular", "VIP"]
    segment_p = [0.52, 0.34, 0.14]

    channels  = ["organic", "paid_search", "social_media", "email", "referral"]
    channel_p = [0.26, 0.30, 0.20, 0.14, 0.10]

    return pd.DataFrame({
        "customer_id":         [f"CUST_{i+1:04d}" for i in range(n)],
        "signup_date":         signup_dates,
        "region":              rng.choice(regions,   size=n, p=region_p),
        "segment":             rng.choice(segments,  size=n, p=segment_p),
        "acquisition_channel": rng.choice(channels,  size=n, p=channel_p),
    })


# ─── Generator: products ──────────────────────────────────────────────────────
def gen_products() -> pd.DataFrame:
    """Sinh bảng products (1 row = 1 sản phẩm, cố định 12 sản phẩm)."""
    rows = [
        ("PROD_0001", "Electronics",  "TechVN",     2_500_000, 1_750_000),
        ("PROD_0002", "Electronics",  "TechVN",     4_800_000, 3_360_000),
        ("PROD_0003", "Electronics",  "SmartLife",    890_000,   622_000),
        ("PROD_0004", "Fashion",      "StyleVN",      350_000,   175_000),
        ("PROD_0005", "Fashion",      "StyleVN",      520_000,   260_000),
        ("PROD_0006", "Fashion",      "UrbanWear",    280_000,   140_000),
        ("PROD_0007", "Home & Living","HomeComfort",  620_000,   372_000),
        ("PROD_0008", "Home & Living","HomeComfort",1_200_000,   720_000),
        ("PROD_0009", "Beauty",       "GlowVN",       480_000,   240_000),
        ("PROD_0010", "Beauty",       "GlowVN",       320_000,   160_000),
        ("PROD_0011", "Sports",       "ActiveVN",     750_000,   450_000),
        ("PROD_0012", "Sports",       "ActiveVN",   1_100_000,   682_000),
    ]
    return pd.DataFrame(
        rows,
        columns=["product_id", "category", "brand", "list_price", "unit_cost"]
    )


# ─── Generator: orders + order_items ──────────────────────────────────────────
def gen_orders_and_items(
    rng: np.random.Generator,
    customers: pd.DataFrame,
    products: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Sinh bảng orders và order_items (có seasonality + segment behavior)."""

    # Số đơn trung bình theo segment (phân phối Poisson)
    avg_orders = {"New": 1.8, "Regular": 3.8, "VIP": 6.5}

    # Seasonality: tháng 7 (summer sale), tháng 11–12 (Black Friday + Tết)
    month_weights = {
         1: 0.070,  2: 0.060,  3: 0.070,
         4: 0.070,  5: 0.070,  6: 0.080,
         7: 0.105,  8: 0.080,  9: 0.070,
        10: 0.085, 11: 0.115, 12: 0.125,
    }
    months  = list(month_weights.keys())
    month_p = [month_weights[m] for m in months]

    # ~82% completed, ~10% cancelled, ~8% returned
    status_pool = ["completed"] * 82 + ["cancelled"] * 10 + ["returned"] * 8

    order_end    = pd.Timestamp(ORDER_END)
    orders_rows: list[dict] = []
    items_rows:  list[dict] = []
    oid_counter  = 1

    for _, cust in customers.iterrows():
        cid       = cust["customer_id"]
        seg       = cust["segment"]
        signup_ts = pd.Timestamp(cust["signup_date"])
        n_orders  = max(1, int(rng.poisson(avg_orders[seg])))

        for _ in range(n_orders):
            # Chọn tháng theo seasonality
            m       = rng.choice(months, p=month_p)
            m_start = pd.Timestamp(f"2025-{m:02d}-01")
            m_end   = m_start + pd.offsets.MonthEnd(0)
            days    = (m_end - m_start).days + 1
            order_date = m_start + pd.Timedelta(days=int(rng.integers(0, days)))

            # Đảm bảo order_date >= signup_date (không thể đặt hàng trước khi đăng ký)
            if order_date < signup_ts:
                order_date = signup_ts + pd.Timedelta(days=int(rng.integers(1, 15)))
            order_date = min(order_date, order_end)

            status = rng.choice(status_pool)
            oid    = f"ORD_{oid_counter:05d}"
            oid_counter += 1

            # Sinh order_items: mỗi đơn có 1–6 sản phẩm khác nhau
            n_items  = int(rng.choice([1, 2, 3, 4, 5, 6], p=[0.30, 0.28, 0.20, 0.12, 0.06, 0.04]))
            prod_idx = rng.choice(len(products), size=n_items, replace=False)
            gross    = 0.0

            for pi in prod_idx:
                prod = products.iloc[pi]
                # Phân phối quantity thực tế: long-tail 1–100
                # ~70% đơn lẻ (1–5), ~20% mua nhiều (6–20), ~10% mua sỉ (21–100)
                tier = rng.random()
                if tier < 0.70:
                    qty = int(rng.integers(1, 6))       # 1–5
                elif tier < 0.90:
                    qty = int(rng.integers(6, 21))      # 6–20
                else:
                    qty = int(rng.integers(21, 101))    # 21–100
                # unit_price = list_price ± 5%, làm tròn đến 1,000 VNĐ
                up = float(prod["list_price"]) * rng.uniform(0.95, 1.05)
                up = round(up / 1000) * 1000
                items_rows.append({
                    "order_id":   oid,
                    "product_id": prod["product_id"],
                    "quantity":   qty,
                    "unit_price": int(up),
                })
                gross += up * qty

            # net_revenue: completed=gross, returned=10% (phí xử lý), cancelled=0
            if status == "completed":
                net = gross
            elif status == "returned":
                net = round(gross * 0.10, 2)
            else:  # cancelled
                net = 0.0

            orders_rows.append({
                "order_id":      oid,
                "customer_id":   cid,
                "order_date":    order_date.strftime("%Y-%m-%d"),
                "status":        status,
                "gross_revenue": round(gross, 2),
                "net_revenue":   round(net, 2),
            })

    return pd.DataFrame(orders_rows), pd.DataFrame(items_rows)


# ─── Main ─────────────────────────────────────────────────────────────────────
def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sinh e-commerce dataset tổng hợp cho Cohort & Retention Analytics"
    )
    parser.add_argument(
        "--output", default="data/raw",
        help="Thư mục lưu file CSV (default: data/raw)"
    )
    parser.add_argument(
        "--seed", type=int, default=20260503,
        help="Random seed để đảm bảo reproducibility (default: 20260503)"
    )
    args = parser.parse_args()

    out_dir = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(args.seed)

    print(f"🌱 Random seed  : {args.seed}")
    print(f"📁 Output folder: {out_dir.resolve()}")
    print("⏳ Generating dataset...\n")

    customers              = gen_customers(rng)
    products               = gen_products()
    orders, order_items    = gen_orders_and_items(rng, customers, products)

    customers.to_csv(   out_dir / "customers.csv",   index=False, encoding="utf-8-sig")
    products.to_csv(    out_dir / "products.csv",    index=False, encoding="utf-8-sig")
    orders.to_csv(      out_dir / "orders.csv",      index=False, encoding="utf-8-sig")
    order_items.to_csv( out_dir / "order_items.csv", index=False, encoding="utf-8-sig")

    print(f"✅ customers.csv     → {len(customers):>6,} rows")
    print(f"✅ products.csv      → {len(products):>6,} rows")
    print(f"✅ orders.csv        → {len(orders):>6,} rows")
    print(f"✅ order_items.csv   → {len(order_items):>6,} rows")
    print("\n🎉 Dataset generated successfully!")


if __name__ == "__main__":
    main()