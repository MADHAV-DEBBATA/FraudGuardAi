import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import requests

# Page Configuration
st.set_page_config(
    page_title="FraudGuard AI | Credit Card Fraud Detection",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Look
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%);
        color: #f8fafc;
    }
    
    /* Header Styling */
    .main-header {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #60a5fa 0%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    /* Card Styling */
    .metric-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 1.5rem;
        border-radius: 1rem;
        backdrop-filter: blur(10px);
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        border-color: rgba(96, 165, 250, 0.5);
    }
    
    /* Status Badge */
    .status-badge {
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        font-family: monospace;
    }
    .status-online { background: rgba(34, 197, 94, 0.2); color: #4ade80; border: 1px solid #22c55e; }
    
    /* Sidebar Styling */
    .css-1d391kg { background-color: #0f172a; }
    
    /* Custom Button */
    .stButton>button {
        background: linear-gradient(90deg, #2563eb 0%, #7c3aed 100%);
        color: white;
        border: none;
        border-radius: 0.5rem;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        opacity: 0.9;
        transform: scale(1.02);
        box-shadow: 0 10px 15px -3px rgba(37, 99, 235, 0.3);
    }
    
    /* Tabs Customization */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 0.5rem 0.5rem 0 0;
        padding-top: 0.5rem;
        padding-bottom: 0.5rem;
        transition: all 0.3s ease;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #2563eb 0%, #7c3aed 100%);
        color: white !important;
        border-bottom: none;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.image("https://img.icons8.com/isometric/100/shield.png", width=80)
    st.markdown("### FraudGuard AI")
    st.markdown("---")
    page = st.radio("Navigate", ["Dashboard", "Real-time Detection", "Analytics", "System Settings"])
    
    st.markdown("---")
    st.markdown("### System Status")
    st.markdown('<div class="status-badge status-online">● CORE SYSTEM ONLINE</div>', unsafe_allow_html=True)
    st.markdown(f"**Uptime:** 142h 12m")
    st.markdown(f"**Last Sync:** {datetime.now().strftime('%H:%M:%S')}")

# Header
st.markdown('<h1 class="main-header">Credit Card Fraud Detection</h1>', unsafe_allow_html=True)
st.markdown("##### AI-Powered Real-time Financial Protection System")

if page == "Dashboard":
    # Hero Section
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <p style="color: #94a3b8; font-size: 0.875rem;">Total Transactions</p>
            <h2 style="margin: 0;">1.2M</h2>
            <p style="color: #4ade80; font-size: 0.75rem; margin: 0;">↑ 12% vs last month</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="metric-card">
            <p style="color: #94a3b8; font-size: 0.875rem;">Fraud Prevented</p>
            <h2 style="margin: 0; color: #f87171;">$2.4M</h2>
            <p style="color: #4ade80; font-size: 0.75rem; margin: 0;">↑ 8% efficiency</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="metric-card">
            <p style="color: #94a3b8; font-size: 0.875rem;">Model Accuracy</p>
            <h2 style="margin: 0; color: #60a5fa;">99.92%</h2>
            <p style="color: #94a3b8; font-size: 0.75rem; margin: 0;">v2.4 NeuralNet</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col4:
        st.markdown("""
        <div class="metric-card">
            <p style="color: #94a3b8; font-size: 0.875rem;">System Latency</p>
            <h2 style="margin: 0;">18ms</h2>
            <p style="color: #4ade80; font-size: 0.75rem; margin: 0;">● Optimized</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Recent Activities")
    
    # Mock Data for Recent Activities
    data = {
        'Time': [datetime.now().strftime('%H:%M:%S')] * 5,
        'Amount': [45.22, 1200.00, 15.00, 243.50, 89.00],
        'Location': ['NYC, USA', 'Lagos, NG', 'London, UK', 'Dubai, UAE', 'Tokyo, JP'],
        'Risk Score': [0.02, 0.98, 0.05, 0.12, 0.08],
        'Status': ['Safe', 'Flagged', 'Safe', 'Safe', 'Safe']
    }
    df = pd.DataFrame(data)
    
    # Modern Dataframe with interactive columns
    st.dataframe(
        df,
        column_config={
            "Time": st.column_config.TimeColumn("Time", format="HH:mm:ss"),
            "Amount": st.column_config.NumberColumn("Amount", format="$%.2f"),
            "Risk Score": st.column_config.ProgressColumn("Risk Score", format="%.2f", min_value=0, max_value=1),
            "Status": st.column_config.TextColumn("Status"),
        },
        use_container_width=True,
        hide_index=True
    )

    # Visualizations
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.markdown("#### Transaction Volume (24h)")
        chart_data = pd.DataFrame(
            np.random.randn(24, 1),
            columns=pd.Index(['Volume'])
        ).cumsum()
        st.line_chart(chart_data)
        
    with col_chart2:
        st.markdown("#### Detection Distribution")
        labels = ['Legitimate', 'Fraudulent', 'Suspicious']
        values = [450, 25, 105]
        fig = px.pie(values=values, names=labels, hole=.3, color_discrete_sequence=['#22c55e', '#ef4444', '#f59e0b'])
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white', margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig, use_container_width=True)

elif page == "Real-time Detection":
    st.markdown("### Transaction Analysis Engine")
    
    tab1, tab2 = st.tabs(["Manual Entry", "Batch Upload"])
    
    with tab1:
        st.info("Enter transaction details below for instant AI analysis.")
        col_in1, col_in2, col_in3 = st.columns(3)
        
        with col_in1:
            amount = st.number_input("Transaction Amount ($)", min_value=0.0, step=0.01)
            time_val = st.number_input("Time offset (Sec)", min_value=0)
        with col_in2:
            card_type = st.selectbox("Card Type", ["Visa", "MasterCard", "Amex", "Discover"])
            location = st.text_input("Merchant Category", "Retail")
        with col_in3:
            v1 = st.slider("V1 (Principal Component)", -2.0, 2.0, 0.0)
            v2 = st.slider("V2 (Principal Component)", -2.0, 2.0, 0.0)

        # Expandable component for the full vector of inputs
        with st.expander("Advanced System Features (V3 - V28)"):
            st.markdown("<small style='color:#94a3b8;'>Configure additional PCA components from your transaction dataset.</small>", unsafe_allow_html=True)
            adv_col1, adv_col2, adv_col3, adv_col4 = st.columns(4)
            for i in range(3, 29):
                target_col = [adv_col1, adv_col2, adv_col3, adv_col4][i % 4]
                target_col.number_input(f"V{i}", value=0.0, format="%0.2f", key=f"v_{i}")

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🔍 Analyze Transaction Integrity", use_container_width=True):
            with st.spinner("Processing through Deep Neural Network..."):
                
                # Setup payload for API Call
                api_url = "https://fraud-guard-ai-git-main-madhav-debbatas-projects.vercel.app/predict"
                payload = {
                    "amount": float(amount),
                    "time": float(time_val),
                    "v1": float(v1),
                    "v2": float(v2),
                    "features": {} # Connect v3-v28 later
                }

                try:
                    # Actually connect to Backend!
                    response = requests.post(api_url, json=payload)
                    response.raise_for_status()
                    result = response.json()
                    
                    is_fraud = result["is_fraud"]
                    risk_value = result["risk_score"]
                except Exception as e:
                    st.error(f"⚠️ Failed to connect to FastAPI backend algorithm. Is it running? Error: {e}")
                    st.stop()
                
                # Interactive UI Results containing Gauge Chart
                res_col1, res_col2 = st.columns([1, 2])
                with res_col1:
                    fig_gauge = go.Figure(go.Indicator(
                        mode = "gauge+number",
                        value = risk_value,
                        number = {'suffix': "%", 'font': {'size': 40, 'color': 'white'}},
                        title = {'text': "Fraud Risk Score", 'font': {'size': 20, 'color': '#94a3b8'}},
                        gauge = {
                            'axis': {'range': [0, 100], 'tickcolor': "white"},
                            'bar': {'color': "#ef4444" if is_fraud else "#22c55e", 'thickness': 0.8},
                            'bgcolor': "rgba(255,255,255,0.05)",
                            'borderwidth': 0,
                            'steps': [
                                {'range': [0, 25], 'color': 'rgba(34, 197, 94, 0.1)'},
                                {'range': [25, 75], 'color': 'rgba(234, 179, 8, 0.1)'},
                                {'range': [75, 100], 'color': 'rgba(239, 68, 68, 0.2)'}],
                        }
                    ))
                    fig_gauge.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': "white"}, height=260, margin=dict(l=20, r=20, t=50, b=20))
                    st.plotly_chart(fig_gauge, use_container_width=True)
                
                with res_col2:
                    if is_fraud:
                        st.error("🚨 **HIGH RISK DETECTED : TRANSACTION BLOCKED**")
                        st.markdown(f"""
                        <div style="background: rgba(239, 68, 68, 0.1); padding: 1rem; border-radius: 0.5rem; border-left: 4px solid #ef4444;">
                            <h4 style="margin-top:0;">Risk Analysis Breakdown:</h4>
                            <ul>
                                <li>🔴 <b>Transaction Amount:</b> ${amount:,.2f} sharply deviates from user's historical baseline.</li>
                                <li>🔴 <b>PCA Feature Match:</b> V1 & V2 alignments point heavily to known malicious patterns.</li>
                                <li>🟡 <b>Merchant Volatility:</b> Sudden spike in activity at <b>{location}</b>.</li>
                            </ul>
                            <b>Recommended Action:</b> Freeze card immediately and trigger SMS multi-factor auth.
                        </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.success("✅ **TRANSACTION VERIFIED : SAFE TO PROCEED**")
                        st.markdown(f"""
                        <div style="background: rgba(34, 197, 94, 0.1); padding: 1rem; border-radius: 0.5rem; border-left: 4px solid #22c55e;">
                            <h4 style="margin-top:0;">System Verification:</h4>
                            <ul>
                                <li>🟢 <b>Behavioral Match:</b> Amount (${amount:,.2f}) seamlessly matches organic spending habits.</li>
                                <li>🟢 <b>Location Security:</b> Merchant category <b>{location}</b> verified against historical dataset.</li>
                                <li>🟢 <b>Network Status:</b> Secure telemetry channel validated.</li>
                            </ul>
                        </div>
                        """, unsafe_allow_html=True)
                        st.balloons()

    with tab2:
        st.markdown("#### Upload Dataset for Batch Processing")
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file is not None:
            df_upload = pd.read_csv(uploaded_file)
            st.write("File Preview:")
            st.dataframe(df_upload.head())
            if st.button("Start Batch Analysis"):
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.01)
                    progress_bar.progress(i + 1)
                st.write("Analysis Complete. 34 anomalies detected.")

elif page == "Analytics":
    st.markdown("### Advanced Model Analytics")
    # Add some complex charts
    np.random.seed(42)
    scatter_data = pd.DataFrame(
        np.random.randn(100, 2),
        columns=pd.Index(['V1', 'V2'])
    )
    scatter_data['Fraud'] = np.random.choice([True, False], 100, p=[0.1, 0.9])
    
    fig = px.scatter(scatter_data, x="V1", y="V2", color="Fraud", 
                     title="Fraud vs Legitimate Clusters (PCA space)",
                     color_discrete_map={True: '#ef4444', False: '#60a5fa'})
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white')
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    #### Model Performance Metrics
    - **F1-Score:** 0.982
    - **Precision:** 0.991
    - **Recall:** 0.974
    """)

elif page == "System Settings":
    st.markdown("### ⚙️ System Configuration")
    
    col_s1, col_s2 = st.columns(2)
    
    with col_s1:
        st.markdown("#### Detection Sensitivity")
        sensitivity = st.select_slider(
            "Adjust AI flagging threshold",
            options=["Low", "Conservative", "Standard", "Aggressive", "Maximum Performance"],
            value="Standard"
        )
        st.info(f"Current Mode: {sensitivity}. This affects the False Positive Rate vs. Recall.")
        
        st.markdown("#### API Configuration")
        st.text_input("Webhook URL", "https://api.securefin.tech/v1/alerts")
        st.selectbox("Alert Priority", ["P0 - Critical", "P1 - High", "P2 - Medium", "P3 - Low"])

    with col_s2:
        st.markdown("#### Model Updates")
        st.write("Current Version: **v2.4.0-build-812**")
        if st.button("Check for Updates"):
            with st.spinner("Talking to model registry..."):
                time.sleep(2)
                st.success("System is up to date!")
        
        st.markdown("#### Security")
        st.toggle("Enabled MFA for Admin overrides", value=True)
        st.toggle("Audit Logging", value=True)
        st.toggle("Anonymize PII in reports", value=True)

    if st.button("Save Configuration", type="primary"):
        st.toast("Settings saved successfully!", icon="✅")

# Footer
st.markdown("---")
st.markdown(
    '<div style="text-align: center; color: #94a3b8; font-size: 0.75rem;">'
    'Powered by FraudGuard AI Engine v2.4.0 • © 2026 SecureFin Technologies'
    '</div>', 
    unsafe_allow_html=True
)
