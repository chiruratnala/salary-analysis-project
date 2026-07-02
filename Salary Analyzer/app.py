import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("model.pkl")

def load_encoder(name):
    return joblib.load(f"{name}_encoder.pkl")

experience_level_encoder = load_encoder("experience_level")
employment_type_encoder = load_encoder("employment_type")
job_title_encoder = load_encoder("job_title")
employee_residence_encoder = load_encoder("employee_residence")
company_location_encoder = load_encoder("company_location")
company_size_encoder = load_encoder("company_size")
remote_ratio_encoder = load_encoder("remote_ratio")
# Streamlit App
st.set_page_config(page_title="Employee Salary Classification", page_icon="💼", layout="centered")
st.title("Salary Analyzer")
st.markdown("Predict an employee's salary class based on input features.")

# Sidebar Inputs
st.sidebar.header("Input Employee Details")

work_year = st.sidebar.number_input(
    "Work Year",
    min_value=2025,
    max_value=2050,
    value=2026,
    step=1,
    format="%d"
)

experience_level = st.sidebar.selectbox("Experience Level", experience_level_encoder.classes_.tolist())
employment_type = st.sidebar.selectbox("Employment Type", employment_type_encoder.classes_.tolist())
job_title = st.sidebar.selectbox("Job Title", job_title_encoder.classes_.tolist())
employee_residence = st.sidebar.selectbox("Employee Residence", employee_residence_encoder.classes_.tolist())
remote_ratio = st.sidebar.selectbox("Remote Ratio", remote_ratio_encoder.classes_.tolist())
company_location = st.sidebar.selectbox("Company Location", company_location_encoder.classes_.tolist())
company_size = st.sidebar.selectbox("Company Size", company_size_encoder.classes_.tolist())

# Display Data
display_df = pd.DataFrame({
    "Work Year": [work_year],
    "Experience Level": [experience_level],
    "Employment Type": [employment_type],
    "Job Title": [job_title],
    "Employee Residence": [employee_residence],
    "Remote Ratio": [remote_ratio],
    "Company Location": [company_location],
    "Company Size": [company_size],
})
st.write("###Input Data")
st.dataframe(display_df)

# Encode Inputs
# Create prediction DataFrame (encoded values)
input_df = pd.DataFrame({
        "work_year": [work_year],
        "experience_level": [experience_level_encoder.transform([experience_level])[0]],
        "employment_type": [employment_type_encoder.transform([employment_type])[0]],
        "job_title": [job_title_encoder.transform([job_title])[0]],
        "employee_residence": [employee_residence_encoder.transform([employee_residence])[0]],
        "remote_ratio": [remote_ratio_encoder.transform([remote_ratio])[0]],
        "company_location": [company_location_encoder.transform([company_location])[0]],
        "company_size": [company_size_encoder.transform([company_size])[0]],
    })

# Prediction
if st.button("Predict Salary Class"):
        prediction = model.predict(input_df)
        st.success(f"Prediction: {prediction[0]}")


# Batch Prediction
st.markdown("---")
st.markdown("#### 📂 Batch Prediction")
st.info(
    "📋 CSV must contain these 8 columns: work_year (numeric year, e.g. 2023), "
    "experience_level, employment_type, job_title, employee_residence, remote_ratio "
    "(On-site / Hybrid / Remote), company_location, company_size — no extra symbols in "
    "numeric fields, and values should match the categories used in training."
)
st.caption("Example row: `2023, Senior-level, Full-time, Data Scientist, United States, Remote, United States, Large`")
uploaded_file = st.file_uploader("Upload a CSV file for batch prediction", type="csv")

required_columns = [
    "work_year", "experience_level", "employment_type", "job_title",
    "employee_residence", "remote_ratio", "company_location", "company_size"
]

if uploaded_file is not None:
    batch_data = pd.read_csv(uploaded_file)
    st.write("Uploaded data preview:", batch_data.head())

    if all(col in batch_data.columns for col in required_columns):
        display_batch = batch_data.copy()

        def safe_transform(col, encoder):
            return col.apply(lambda x: encoder.transform([x])[0] if x in encoder.classes_ else -1)

        batch_data["experience_level"] = safe_transform(batch_data["experience_level"], experience_level_encoder)
        batch_data["employment_type"] = safe_transform(batch_data["employment_type"], employment_type_encoder)
        batch_data["job_title"] = safe_transform(batch_data["job_title"], job_title_encoder)
        batch_data["employee_residence"] = safe_transform(batch_data["employee_residence"], employee_residence_encoder)
        batch_data["company_location"] = safe_transform(batch_data["company_location"], company_location_encoder)
        batch_data["company_size"] = safe_transform(batch_data["company_size"], company_size_encoder)
        batch_data["remote_ratio"] = safe_transform(batch_data["remote_ratio"], remote_ratio_encoder)

        try:
            preds = model.predict(batch_data[required_columns])
            display_batch["PredictedClass"] = preds
            st.dataframe(display_batch)

            csv = display_batch.to_csv(index=False).encode("utf-8")
            st.download_button("Download Predictions CSV", csv, file_name="predicted_classes.csv", mime="text/csv")
        except Exception as e:
            st.error(f"Batch prediction failed: {e}")
    else:
        st.error("Missing required columns in uploaded file.")
