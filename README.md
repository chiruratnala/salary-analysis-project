# 📊 Data Science Salary Analysis (2020–2023)

## 📌 Project Overview
This project analyzes Data Science salaries worldwide to understand how pay varies based on experience level, job role, employment type, company size, remote work, and location. The goal is to uncover real market trends that can help job seekers, companies, and decision-makers understand salary dynamics in the data science field.

## 🎯 Business Objectives
* **Identify factors** that influence salary growth.
* **Compare** job demand vs. pay.
* **Understand** how remote work and company size impact salaries.
* **Analyze** country-wise salary differences.
* **Highlight** high-paying vs. high-demand roles.

## 📂 Dataset
* **Source:** Data Science Salaries dataset (2020–2023)
* **Records:** Multiple countries, roles, and experience levels

### Key Columns:
* `work_year`
* `experience_level`
* `employment_type`
* `job_title`
* `salary_in_usd`
* `remote_ratio`
* `company_location`
* `employee_residence`
* `company_size`

## 🧹 Data Cleaning & Preparation
* Standardized column names.
* Converted salaries to USD.
* Removed duplicate rows.
* Handled low-frequency categories.
* Created salary ranges (e.g., <50K, 50K–100K, 100K–150K).
* Ensured consistent country names.

## 🔍 Exploratory Data Analysis (EDA)

### 1️⃣ Salary Trends Over Time
* Median salary shows steady growth from 2020 to 2023.
* Major jump observed after 2021, indicating market expansion.

### 2️⃣ Experience Level vs. Salary
* Salary increases significantly with experience.
* Executive and senior roles dominate high pay.
* Entry-level salaries remain comparatively lower.

### 3️⃣ Employment Type vs. Salary
* **Full-time** roles pay the highest.
* **Contract** roles follow.
* **Freelance and part-time** roles earn less on average.

### 4️⃣ Remote Ratio vs. Salary
* Remote and on-site roles offer higher median salaries.
* Hybrid roles consistently show lower pay.

### 5️⃣ Company Size vs. Salary
* Medium and large companies pay more than small companies.
* Salary spread is wider in large companies.

### 6️⃣ Job Role Analysis
* **High demand roles:** Data Engineer, Data Scientist, Data Analyst.
* **Highest paying roles:**
    * Data Science Tech Lead
    * Cloud Data Architect
    * Head of Data
* *Note: High-paying roles usually have lower job counts.*

### 7️⃣ Demand vs. Pay Analysis
* Jobs with highest demand do not always offer highest pay.
* Specialized leadership roles offer high salary with limited openings.

### 8️⃣ Country-wise Analysis
* United States dominates job count.
* Some countries offer very high salaries but fewer jobs.
* Salary varies significantly by location and work type.

## 📊 Visualizations Used
* Bar charts
* Box plots
* Line plots
* Scatter plots
* Pie charts
* *All visuals focus on clear storytelling, not just decoration.*

## 💡 Key Insights
* Experience and specialization matter more than location alone.
* High salary ≠ high job availability.
* Remote work is financially competitive.
* Senior roles drive most salary growth.
* The market rewards skills depth over volume.

## 🧠 Final Conclusion
> The data science job market shows strong salary growth, driven primarily by experience, role seniority, and company size. While demand is high for mid-level roles, top compensation is concentrated in senior and specialized positions, especially in medium and large organizations.

## 🛠️ Tools & Technologies
* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

## 📁 Project Structure
```text
├── data/
│   └── cleaned_dataset.csv
├── notebook/
│   └── salary_analysis.ipynb
├── images/
│   └── visualizations.png
├── README.md
```
## 📜 License
> This project is released under the MIT License and is free to use for learning and educational purposes.

## How to Run the Project
1. Clone the repository
2. Install required libraries:
   ```bash
   pip install pandas matplotlib seaborn
3. Open notebook:
   ```bash
   jupyter notebook

---

## Author

Chiru Ratnala

Aspiring Data Analyst

GitHub :https://github.com/chiruratnala
