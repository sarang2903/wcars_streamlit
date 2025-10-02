import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Load dataset
df = pd.read_csv("CARS.csv")

# App title
st.title("Car Dataset Analysis")

# Show dataset
st.subheader("Dataset Preview")
st.dataframe(df)

# Show unique car brands
brands = df.Make.unique()
st.subheader("Available Brands")
st.write(brands)

# Select brand from dropdown instead of input()
c = st.selectbox("Select a Brand", brands)

# Filter by brand
s = df[df.Make == c]

# Plot 1: Horsepower by Model for selected brand
st.subheader(f"Horsepower of Models for {c}")
fig1, ax1 = plt.subplots(figsize=(10, 6))
sb.barplot(x="Model", y="Horsepower", data=s, ax=ax1)
plt.xticks(rotation=90)
st.pyplot(fig1)

# Plot 2: MSRP by DriveTrain
st.subheader("MSRP by DriveTrain")
fig2, ax2 = plt.subplots(figsize=(8, 6))
sb.barplot(x="DriveTrain", y="MSRP", data=df, ax=ax2)
plt.xticks(rotation=90)
st.pyplot(fig2)

# Plot 3: Invoice by Type (Pointplot)
st.subheader("Invoice Price by Car Type")
fig3, ax3 = plt.subplots(figsize=(8, 6))
sb.pointplot(x="Type", y="Invoice", data=df, ax=ax3)
st.pyplot(fig3)
