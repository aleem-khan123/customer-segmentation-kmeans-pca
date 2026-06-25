import streamlit as st
import pandas as pd

# --------------------------------
# PAGE CONFIG
# --------------------------------

st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="📊",
    layout="wide"
)

# --------------------------------
# CUSTOM CSS
# --------------------------------

st.markdown("""
<style>
:root{
    --bg-1: #f6f8fb;
    --primary: #0b3d91; /* deep navy */
    --accent: #1f77b4;  /* blue */
    --teal: #0b9faa;    /* teal */
    --gold: #c6861f;    /* gold accent */
    --heading-start: #bff3d8; /* light green start */
    --heading-end: #7fe1b0;   /* light green end */
    --muted: #6b7280;
    --card: #ffffff;
}


body, .stApp {
    background: linear-gradient(180deg, #ffffff 0%, var(--bg-1) 100%);
    font-family: 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    color: #0f1724;
}

h1{
    text-align:center;
    color:#fff;
    font-size:2.2rem;
    margin:0.6rem auto 0.35rem auto;
    letter-spacing:0.2px;
    display:block;
    width:fit-content;
    padding:0.6rem 1.25rem;
    border-radius:14px;
    background: linear-gradient(90deg, var(--heading-start) 0%, var(--heading-end) 80%);
    box-shadow: 0 14px 30px rgba(34,139,85,0.10);
}

h1:after{
    content: "";
    display:block;
    height:6px;
    width:48%;
    margin:10px auto 0 auto;
    border-radius:6px;
    background: linear-gradient(90deg, var(--gold), var(--teal));
    opacity:0.95;
}

h2, h3 {
    color:var(--primary);
}

p{ color:var(--muted); text-align:center; margin-top:0 }

/* Card-like appearance for blocks and metrics */
.stBlock { background:transparent }
[data-testid="stMetric"] {
    background: linear-gradient(90deg, rgba(11,61,145,0.06), rgba(255,255,255,0));
    border-radius:12px;
    padding:10px 12px;
    box-shadow: 0 8px 20px rgba(15,23,36,0.04);
}

.metric-card{
    background-color:var(--card);
    padding:12px;
    border-radius:10px;
}

/* Dataframe & info boxes */
.stDataFrame, .stDataFrame div{
    border-radius:10px;
    box-shadow:0 12px 30px rgba(2,6,23,0.04);
    overflow:auto;
}

/* Images */
img{
    border-radius:10px;
    box-shadow: 0 12px 30px rgba(2,6,23,0.06);
    max-width:100%;
    height:auto;
    display:block;
    margin:0 auto;
}

/* Section accents: makes each subheader look like a professional section */
h2{
    display:block;
    padding:0.5rem 0.75rem;
    border-left:6px solid var(--gold);
    background: linear-gradient(90deg, rgba(198,134,31,0.06), rgba(255,255,255,0));
    border-radius:8px;
    margin-top:1rem;
}

h3{
    display:block;
    padding:0.35rem 0.5rem;
    border-left:6px solid var(--teal);
    background: linear-gradient(90deg, rgba(11,157,170,0.04), rgba(255,255,255,0));
    border-radius:6px;
    margin-top:0.6rem;
}

/* Styled info/success boxes to match brand */
.stInfo{ background: linear-gradient(90deg, rgba(11,157,170,0.06), rgba(255,255,255,0)); border-left:4px solid var(--teal); }
.stSuccess{ background: linear-gradient(90deg, rgba(31,119,180,0.04), rgba(255,255,255,0)); border-left:4px solid var(--accent); }

/* Small tweaks for Streamlit message boxes */
.stAlert, .stInfo, .stSuccess, .stWarning, .stError{
    border-radius:10px;
    padding:10px 12px;
}

/* Responsive adjustments */
@media (max-width: 900px){
    .block-container{ padding:0.5rem; }
    img{ width:100%!important; height:auto!important; }
    h1{ font-size:1.4rem; padding:0.5rem 0.9rem; width:auto }
    h1:after{ width:60%; height:5px }
}

/* Hero container to center the main banner */
.hero{ display:flex; flex-direction:column; align-items:center; justify-content:center; padding:1rem 0 0.6rem 0 }

</style>
""", unsafe_allow_html=True)

# --------------------------------
# LOAD DATA
# --------------------------------

df = pd.read_csv("Dataset/customer_segments_final.csv")
# st.write(df.columns)
# --------------------------------
# HEADER
# --------------------------------

st.markdown("""
<div class="hero">
    <h1>Customer Segmentation Analysis Dashboard</h1>
    <p style='text-align:center'>
        Unsupervised Learning using PCA and K-Means Clustering
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# --------------------------------
# EXECUTIVE SUMMARY
# --------------------------------

st.subheader("Executive Summary")

c1,c2,c3,c4 = st.columns(4)

c1.metric(
    "Total Customers",
    len(df)
)

c2.metric(
    "Average Age",
    round(df["Age"].mean(),1)
)

c3.metric(
    "Average Income",
    round(df["Annual Income"].mean(),1)
)

c4.metric(
    "Average Spending",
    round(df["Spending Score"].mean(),1)
)

st.divider()

# --------------------------------
# DATASET OVERVIEW
# --------------------------------

st.subheader("Dataset Overview")

left,right = st.columns([2,1])

with left:
    st.dataframe(df.head())

with right:
    st.info(f"""
Rows : {df.shape[0]}

Columns : {df.shape[1]}

Missing Values : 0

Duplicate Records : 0
""")

st.divider()

# --------------------------------
# BASIC VISUALIZATIONS
# --------------------------------

st.subheader("Customer Demographics")

c1,c2 = st.columns(2)

with c1:
    st.image(
        "Charts/Gender distribution chart.png",
        use_container_width=True
    )

with c2:
    st.image(
        "Charts/Age distribution chart.png",
        use_container_width=True
    )

c3,c4 = st.columns(2)

with c3:
    st.image(
        "Charts/Income Histogram chart.png",
        use_container_width=True
    )

with c4:
    st.image(
        "Charts/Spending Score Histogram chart.png",
        use_container_width=True
    )

# CORRELATION
st.divider()

st.subheader("Correlation Analysis")

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image(
        "Charts/Coreleation Heatmap.png",
        width=500
    )

st.divider()

# --------------------------------
# PCA
# --------------------------------
st.divider()
st.subheader("Principal Component Analysis")
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image(
    "Charts/Customer Segments using K-Means.png",
    use_container_width=500
)
st.divider()
st.info("""
PCA reduced four original features into two principal components while retaining approximately 60% of the dataset variance.
""")

st.divider()

# --------------------------------
# ELBOW & SILHOUETTE
# --------------------------------

st.subheader("Optimal Cluster Selection")

c1,c2 = st.columns(2)

with c1:
    st.image(
        "Charts/Elbow Method.png",
        use_container_width=True
    )

with c2:
    st.image(
        "Charts/Silhouette Score.png",
        use_container_width=True
    )

st.success("""
Both methods indicated that K = 4 provides a strong balance between cluster separation and compactness.
""")

st.divider()

# --------------------------------
# GENDER BY CLUSTER
# --------------------------------

st.subheader("Gender Distribution by Cluster")

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image(
        "Charts/Gender Distribution by Cluster.png",
        width=550
    )

st.divider()

# --------------------------------
# CUSTOMER PERSONAS
# --------------------------------

st.subheader("Customer Personas")

persona_df = pd.DataFrame({

"Cluster":[0,1,2,3],

"Persona":[
"High-Value Customers",
"Conservative Customers",
"Budget-Conscious Customers",
"Young Spenders"
],

"Average Age":[
29.91,
47.65,
49.22,
27.30
],

"Average Income":[
81.50,
74.63,
46.22,
49.82
],

"Average Spending":[
73.88,
30.86,
34.00,
67.51
]
})

st.dataframe(
    persona_df,
    use_container_width=True
)

st.divider()

# --------------------------------
# BUSINESS INSIGHTS
# --------------------------------

st.subheader("Key Business Insights")

st.markdown("""
### Cluster 0 – High-Value Customers
- High income
- High spending behavior
- Best target for premium products

### Cluster 1 – Conservative Customers
- Good income
- Lower spending habits
- Focus on retention strategies

### Cluster 2 – Budget-Conscious Customers
- Price-sensitive segment
- Discounts and promotions work well

### Cluster 3 – Young Spenders
- Younger audience
- Strong spending behavior
- Suitable for social media marketing
""")

st.divider()

# --------------------------------
# CONCLUSION
# --------------------------------

st.subheader("Final Conclusion")

st.success("""
K-Means clustering successfully segmented customers into four meaningful groups.

These segments can help businesses design personalized marketing strategies, improve customer engagement, and increase revenue through data-driven decision making.
""")