import streamlit as st
import pandas as pd

# Title of the web app
st.title('Simple Data Dashboard')

# File uploader
upload_file = st.file_uploader("Upload a file", type=["csv"])

if upload_file is not None:
    try:
        # Read file
        df = pd.read_csv(upload_file)
        
        # Clean column names
        df.columns = (
            df.columns
            .str.strip()
            .str.replace('"', '', regex=False)
            .str.replace(',', '', regex=False)
            .str.replace(';', '', regex=False)
        )
    
        st.header('Data')
        st.write(df)

        # Filter data
        st.subheader("Filter Data")
        columns = df.columns.tolist()
        selected_column = st.selectbox("Select Column", columns)
        unique_values = sorted(df[selected_column].unique(), key=lambda x: (float(x) if str(x).replace('.', '', 1).isdigit() else float('inf')))
        selected_value = st.selectbox("Select Value", unique_values)

        filtered_df = df[df[selected_column] == selected_value]
        st.write(filtered_df)

        # Plot data
        x_column = st.selectbox("Select X Axis", df.columns)
        y_column = st.selectbox("Select Y Axis", df.columns)

        if st.button("Generate Plot"):
            st.line_chart(filtered_df[[x_column, y_column]])
    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")
else:
    st.write("Waiting for data")
    # Display a loading animation
    st.markdown(
        """
        <div style="display: flex; justify-content: center; align-items: center; height: 200px;">
            <div style="width: 40px; height: 40px; border: 4px solid rgba(0, 0, 0, 0.1); border-top: 4px solid #4CAF50; border-radius: 50%; animation: spin 1s linear infinite;"></div>
        </div>
        <style>
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
