import streamlit as st

st.title("Ứng dụng thẩm định khoản vay cá nhân")

# Nhập dữ liệu
STV = st.number_input(
    "Nhập số tiền muốn vay (triệu đồng):",
    min_value=0.0
)

TGV = st.number_input(
    "Nhập thời gian vay (số năm):",
    min_value=1.0
)

LSV = st.number_input(
    "Nhập lãi suất vay (số thập phân):",
    min_value=0.0,
    step=0.01,
    format="%.2f"
)

TN = st.number_input(
    "Nhập thu nhập cả 2 vợ chồng (triệu đồng/tháng):",
    min_value=0.0
)

SNTGD = st.number_input(
    "Nhập số người trong gia đình:",
    min_value=1
)

PTMC = st.number_input(
    "Nhập số tiền phải trả cho khoản vay cũ (triệu đồng/tháng):",
    min_value=0.0
)

GTTSDB = st.number_input(
    "Nhập giá trị tài sản đảm bảo (triệu đồng):",
    min_value=0.0
)

Tuoi = st.number_input(
    "Nhập số tuổi của khách hàng:",
    min_value=18,
    max_value=100
)

# Chi phí sinh hoạt cố định
CPSH = 5

# Nút tính toán
if st.button("Thẩm định khoản vay"):

    # Tính các chỉ số
    LTV = STV / GTTSDB if GTTSDB > 0 else 0
    PTMM = (STV / (TGV * 12)) + (STV * (LSV / 12))
    DTI = (PTMC + PTMM) / (TN - CPSH * SNTGD)

    # Hiển thị kết quả
    st.subheader("Kết quả")

    st.write(f"**Khoản vay mới phải trả/tháng (PTMM):** {PTMM:.2f} triệu đồng")
    st.write(f"**DTI:** {DTI:.2%}")
    st.write(f"**LTV:** {LTV:.2%}")

    # Điều kiện phê duyệt
    if DTI <= 0.7 and LTV <= 0.7 and 18 < Tuoi < 70:
        st.success("✅ Khách hàng được vay")
    else:
        st.error("❌ Khách hàng không được vay")
