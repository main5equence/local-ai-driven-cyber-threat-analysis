import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(
    page_title="Local AI-driven Cyber-Threat Analysis",
    layout="wide"
)

st.title("Local AI-driven Cyber-Threat Analysis")

engine = create_engine("sqlite:///data/threats.db")

query = "SELECT * FROM threats ORDER BY id DESC"

df = pd.read_sql(query, engine)

# =========================
# METRICS
# =========================

if not df.empty:

    total_threats = len(df)

    high_severity = len(df[df["severity"] == "HIGH"])

    unique_ips = df["source_ip"].nunique()

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Threats", total_threats)

    col2.metric("High Severity", high_severity)

    col3.metric("Unique IPs", unique_ips)

# =========================
# TABLE
# =========================

st.subheader("Threat Events")

st.dataframe(
    df[[
        "timestamp",
        "event_type",
        "source_ip",
        "severity"
    ]],
    use_container_width=True
)

# =========================
# CHARTS
# =========================

if not df.empty:

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Threat Severity")

        severity_counts = df["severity"].value_counts()

        st.bar_chart(severity_counts)

    with col2:

        st.subheader("Threat Types")

        event_counts = df["event_type"].value_counts()

        st.bar_chart(event_counts)

# =========================
# AI ANALYSIS
# =========================

st.subheader("AI Threat Analysis")

if not df.empty:

    for index, row in df.iterrows():

        with st.expander(
            f"{row['event_type']} | {row['source_ip']} | {row['severity']}"
        ):

            st.markdown("### AI Analysis")

            st.write(row["ai_analysis"])

            st.markdown("### Incident Details")

            st.write(f"Timestamp: {row['timestamp']}")
            st.write(f"Source IP: {row['source_ip']}")
            st.write(f"Severity: {row['severity']}")
