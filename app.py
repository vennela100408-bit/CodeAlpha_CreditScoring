import streamlit as st
import pandas as pd
import joblib
import os


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Credit Scoring",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    .main {
        background-color: #f7f9fc;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    .title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        color: #172033;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 17px;
        color: #667085;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 23px;
        font-weight: 700;
        color: #172033;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .info-box {
        background: white;
        padding: 20px;
        border-radius: 14px;
        border: 1px solid #e4e7ec;
        margin-bottom: 20px;
    }

    .result-good {
        background: #ecfdf3;
        border: 2px solid #12b76a;
        border-radius: 18px;
        padding: 30px;
        text-align: center;
        margin-top: 30px;
    }

    .result-poor {
        background: #fff1f3;
        border: 2px solid #f04438;
        border-radius: 18px;
        padding: 30px;
        text-align: center;
        margin-top: 30px;
    }

    .score {
        font-size: 58px;
        font-weight: 800;
        margin: 10px 0;
    }

    .result-title {
        font-size: 30px;
        font-weight: 800;
    }

    .small-text {
        color: #667085;
        font-size: 14px;
    }

    div.stButton > button {
        width: 100%;
        height: 52px;
        border-radius: 10px;
        font-size: 18px;
        font-weight: 700;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# MODEL LOCATION
# =========================================================

MODEL_PATH = "models/credit_scoring_model.pkl"


# =========================================================
# LOAD MODEL
# =========================================================

if not os.path.exists(MODEL_PATH):

    st.error(
        "❌ Model file was not found.\n\n"
        "Expected location:\n"
        "`models/credit_scoring_model.pkl`"
    )

    st.stop()


try:
    model = joblib.load(MODEL_PATH)

except Exception as e:

    st.error("❌ Unable to load the credit scoring model.")

    st.code(str(e))

    st.stop()


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">💳 AI Credit Scoring System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Enter your financial and personal information to estimate your credit risk.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# INFORMATION BOX
# =========================================================

st.markdown("""
<div class="info-box">
<b>How it works</b><br>
Answer the questions below using the available options.
The trained Machine Learning model analyzes the information and
generates an estimated credit score percentage and risk category.
</div>
""", unsafe_allow_html=True)


# =========================================================
# PERSONAL INFORMATION
# =========================================================

st.markdown(
    '<div class="section-title">👤 Personal Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=25,
        step=1
    )

with col2:

    dependents = st.selectbox(
        "Number of Dependents",
        [
            0,
            1,
            2,
            3,
            4
        ]
    )

with col3:

    personal_status = st.selectbox(
        "Personal / Family Status",
        [
            "Male - Single",
            "Male - Married/Widowed",
            "Female - Single",
            "Female - Married/Widowed"
        ]
    )


col1, col2, col3 = st.columns(3)

with col1:

    housing = st.selectbox(
        "Housing",
        [
            "Rent",
            "Own",
            "Free"
        ]
    )

with col2:

    residence_since = st.selectbox(
        "Years at Current Residence",
        [
            "Less than 1 year",
            "1 - 2 years",
            "2 - 3 years",
            "3 - 4 years",
            "4+ years"
        ]
    )

with col3:

    telephone = st.selectbox(
        "Telephone",
        [
            "Yes",
            "No"
        ]
    )


# =========================================================
# EMPLOYMENT & INCOME
# =========================================================

st.markdown(
    '<div class="section-title">💼 Employment & Income</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    employment = st.selectbox(
        "Employment Duration",
        [
            "Unemployed",
            "Less than 1 year",
            "1 - 4 years",
            "4 - 7 years",
            "7+ years"
        ]
    )

with col2:

    income = st.selectbox(
        "Monthly Income",
        [
            "Below ₹15,000",
            "₹15,000 - ₹25,000",
            "₹25,000 - ₹40,000",
            "₹40,000 - ₹60,000",
            "₹60,000 - ₹1,00,000",
            "Above ₹1,00,000"
        ]
    )

with col3:

    job = st.selectbox(
        "Job Type",
        [
            "Unskilled / Unemployed",
            "Unskilled - Resident",
            "Skilled Employee",
            "Highly Skilled / Management"
        ]
    )


# =========================================================
# BANKING & CREDIT INFORMATION
# =========================================================

st.markdown(
    '<div class="section-title">🏦 Banking & Credit Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    checking_account = st.selectbox(
        "Checking Account Balance",
        [
            "No checking account",
            "Below ₹10,000",
            "₹10,000 - ₹50,000",
            "Above ₹50,000"
        ]
    )

with col2:

    savings_account = st.selectbox(
        "Savings Account",
        [
            "No savings account",
            "Below ₹10,000",
            "₹10,000 - ₹50,000",
            "₹50,000 - ₹1,00,000",
            "Above ₹1,00,000"
        ]
    )

with col3:

    credit_history = st.selectbox(
        "Credit History",
        [
            "Good - existing credits paid properly",
            "Existing credits paid properly",
            "Critical / Other existing credits",
            "Delayed payments",
            "No credit history"
        ]
    )


col1, col2, col3 = st.columns(3)

with col1:

    existing_credits = st.selectbox(
        "Number of Existing Credits",
        [
            1,
            2,
            3,
            4
        ]
    )

with col2:

    credit_amount = st.number_input(
        "Requested Credit Amount (₹)",
        min_value=500,
        max_value=5000000,
        value=50000,
        step=500
    )

with col3:

    duration = st.selectbox(
        "Loan Duration",
        [
            "Less than 1 year",
            "1 - 2 years",
            "2 - 3 years",
            "3 - 4 years",
            "4 - 5 years",
            "More than 5 years"
        ]
    )


# =========================================================
# LOAN PURPOSE
# =========================================================

st.markdown(
    '<div class="section-title">🎯 Purpose of Credit</div>',
    unsafe_allow_html=True
)

purpose = st.selectbox(
    "Why do you need the credit?",
    [
        "Car / Vehicle",
        "Furniture / Equipment",
        "Radio / Television",
        "Domestic Appliances",
        "Repairs",
        "Education",
        "Vacation",
        "Business",
        "Personal needs",
        "Other"
    ]
)


# =========================================================
# FINANCIAL COMMITMENTS
# =========================================================

st.markdown(
    '<div class="section-title">💰 Financial Commitments</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    installment_rate = st.selectbox(
        "Installment Level",
        [
            "Low",
            "Moderate",
            "High",
            "Very High"
        ]
    )

with col2:

    other_debtors = st.selectbox(
        "Other Debtors / Guarantor",
        [
            "None",
            "Co-applicant",
            "Guarantor"
        ]
    )

with col3:

    other_installment_plans = st.selectbox(
        "Other Installment Plans",
        [
            "None",
            "Bank",
            "Stores"
        ]
    )


# =========================================================
# PROPERTY
# =========================================================

st.markdown(
    '<div class="section-title">🏠 Assets & Property</div>',
    unsafe_allow_html=True
)

property_type = st.selectbox(
    "Property Ownership",
    [
        "Real estate",
        "Building society / savings agreement",
        "Car or other property",
        "No known property"
    ]
)


# =========================================================
# OTHER INFORMATION
# =========================================================

st.markdown(
    '<div class="section-title">📋 Additional Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    foreign_worker = st.selectbox(
        "Are you currently working in your home country?",
        [
            "Yes",
            "No"
        ]
    )

with col2:

    age_group = st.selectbox(
        "Age Group",
        [
            "18 - 25",
            "26 - 35",
            "36 - 50",
            "51 - 65",
            "Above 65"
        ]
    )

with col3:

    payment_behavior = st.selectbox(
        "Previous Payment Behaviour",
        [
            "Always paid on time",
            "Usually paid on time",
            "Sometimes delayed",
            "Frequently delayed"
        ]
    )


# =========================================================
# CONVERT USER INPUT TO MODEL FORMAT
# =========================================================

def convert_input():

    # -----------------------------------------------------
    # Checking account
    # -----------------------------------------------------

    checking_map = {
        "No checking account": "unknown",
        "Below ₹10,000": "little",
        "₹10,000 - ₹50,000": "moderate",
        "Above ₹50,000": "rich"
    }

    # -----------------------------------------------------
    # Savings
    # -----------------------------------------------------

    savings_map = {
        "No savings account": "unknown",
        "Below ₹10,000": "little",
        "₹10,000 - ₹50,000": "moderate",
        "₹50,000 - ₹1,00,000": "quite rich",
        "Above ₹1,00,000": "rich"
    }

    # -----------------------------------------------------
    # Employment
    # -----------------------------------------------------

    employment_map = {
        "Unemployed": "unemployed",
        "Less than 1 year": "<1",
        "1 - 4 years": "1<=X<4",
        "4 - 7 years": "4<=X<7",
        "7+ years": ">=7"
    }

    # -----------------------------------------------------
    # Credit history
    # -----------------------------------------------------

    credit_history_map = {
        "Good - existing credits paid properly": "existing paid",
        "Existing credits paid properly": "existing paid",
        "Critical / Other existing credits": "critical/other existing credit",
        "Delayed payments": "delayed previously",
        "No credit history": "no credits/all paid"
    }

    # -----------------------------------------------------
    # Purpose
    # -----------------------------------------------------

    purpose_map = {
        "Car / Vehicle": "car",
        "Furniture / Equipment": "furniture/equipment",
        "Radio / Television": "radio/tv",
        "Domestic Appliances": "domestic appliances",
        "Repairs": "repairs",
        "Education": "education",
        "Vacation": "vacation",
        "Business": "business",
        "Personal needs": "other",
        "Other": "other"
    }

    # -----------------------------------------------------
    # Installment rate
    # -----------------------------------------------------

    installment_map = {
        "Low": 1,
        "Moderate": 2,
        "High": 3,
        "Very High": 4
    }

    # -----------------------------------------------------
    # Personal status
    # -----------------------------------------------------

    personal_status_map = {
        "Male - Single": "male single",
        "Male - Married/Widowed": "male married/widowed",
        "Female - Single": "female single",
        "Female - Married/Widowed": "female married/widowed"
    }

    # -----------------------------------------------------
    # Other debtors
    # -----------------------------------------------------

    debtor_map = {
        "None": "none",
        "Co-applicant": "co-applicant",
        "Guarantor": "guarantor"
    }

    # -----------------------------------------------------
    # Residence
    # -----------------------------------------------------

    residence_map = {
        "Less than 1 year": 1,
        "1 - 2 years": 2,
        "2 - 3 years": 3,
        "3 - 4 years": 4,
        "4+ years": 4
    }

    # -----------------------------------------------------
    # Property
    # -----------------------------------------------------

    property_map = {
        "Real estate": "real estate",
        "Building society / savings agreement":
            "building society savings agreement",
        "Car or other property":
            "car or other property",
        "No known property":
            "unknown / no property"
    }

    # -----------------------------------------------------
    # Housing
    # -----------------------------------------------------

    housing_map = {
        "Rent": "rent",
        "Own": "own",
        "Free": "for free"
    }

    # -----------------------------------------------------
    # Other installment plans
    # -----------------------------------------------------

    installment_plan_map = {
        "None": "none",
        "Bank": "bank",
        "Stores": "stores"
    }

    # -----------------------------------------------------
    # Job
    # -----------------------------------------------------

    job_map = {
        "Unskilled / Unemployed":
            "unskilled and non-resident",
        "Unskilled - Resident":
            "unskilled and resident",
        "Skilled Employee":
            "skilled",
        "Highly Skilled / Management":
            "management/self-employed/highly qualified employee/officer"
    }

    # -----------------------------------------------------
    # Build dataframe
    # -----------------------------------------------------

    data = {

        "checking_account":
            checking_map[checking_account],

        "duration":
            {
                "Less than 1 year": 6,
                "1 - 2 years": 18,
                "2 - 3 years": 30,
                "3 - 4 years": 42,
                "4 - 5 years": 54,
                "More than 5 years": 72
            }[duration],

        "credit_history":
            credit_history_map[credit_history],

        "purpose":
            purpose_map[purpose],

        "credit_amount":
            credit_amount,

        "savings_account":
            savings_map[savings_account],

        "employment":
            employment_map[employment],

        "installment_rate":
            installment_map[installment_rate],

        "personal_status":
            personal_status_map[personal_status],

        "other_debtors":
            debtor_map[other_debtors],

        "residence_since":
            residence_map[residence_since],

        "property":
            property_map[property_type],

        "age":
            age,

        "other_installment_plans":
            installment_plan_map[other_installment_plans],

        "housing":
            housing_map[housing],

        "existing_credits":
            existing_credits,

        "job":
            job_map[job],

        "dependents":
            dependents,

        "telephone":
            "yes" if telephone == "Yes" else "none",

        "foreign_worker":
            "yes" if foreign_worker == "Yes" else "no"
    }

    return pd.DataFrame([data])


# =========================================================
# PREDICTION FUNCTION
# =========================================================

def make_prediction(input_data):

    try:

        # -------------------------------------------------
        # Normal pipeline / model
        # -------------------------------------------------

        if hasattr(model, "predict_proba"):

            probabilities = model.predict_proba(input_data)

            # If model has two classes
            if probabilities.shape[1] >= 2:

                # Usually class 1 = Good credit
                score = float(probabilities[0][1])

            else:

                score = float(probabilities[0][0])

        else:

            prediction = model.predict(input_data)

            score = 1.0 if int(prediction[0]) == 1 else 0.0

        return score

    except Exception as first_error:

        # -------------------------------------------------
        # Fallback for models whose training columns differ
        # -------------------------------------------------

        try:

            # Get expected feature names if available
            if hasattr(model, "feature_names_in_"):

                expected_columns = list(model.feature_names_in_)

                fallback_data = input_data.copy()

                for column in expected_columns:

                    if column not in fallback_data.columns:

                        fallback_data[column] = 0

                fallback_data = fallback_data[expected_columns]

                if hasattr(model, "predict_proba"):

                    probabilities = model.predict_proba(
                        fallback_data
                    )

                    if probabilities.shape[1] >= 2:

                        score = float(probabilities[0][1])

                    else:

                        score = float(probabilities[0][0])

                    return score

                prediction = model.predict(fallback_data)

                return 1.0 if int(prediction[0]) == 1 else 0.0

        except Exception:
            pass

        raise first_error


# =========================================================
# PREDICT BUTTON
# =========================================================

st.markdown("---")

st.markdown(
    '<div class="section-title">🔍 Check Credit Risk</div>',
    unsafe_allow_html=True
)

st.write(
    "Review your answers and click the button below to generate "
    "the AI-based credit risk result."
)

predict_button = st.button(
    "💳 Calculate My Credit Score",
    type="primary",
    use_container_width=True
)


# =========================================================
# RESULT
# =========================================================

if predict_button:

    with st.spinner("Analyzing your information..."):

        try:

            input_data = convert_input()

            score = make_prediction(input_data)

            # Keep score between 0 and 1
            score = max(0.0, min(1.0, score))

            percentage = score * 100

            # -------------------------------------------------
            # CREDIT CATEGORY
            # -------------------------------------------------

            if percentage >= 70:

                category = "GOOD CREDIT RISK"

                message = (
                    "Your profile shows a relatively strong credit "
                    "risk according to the trained Machine Learning model."
                )

                st.markdown(
                    f"""
                    <div class="result-good">

                        <div class="result-title">
                            ✅ {category}
                        </div>

                        <div class="score">
                            {percentage:.1f}%
                        </div>

                        <p>
                            {message}
                        </p>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                category = "POOR CREDIT RISK"

                message = (
                    "Your profile indicates a higher credit risk "
                    "according to the trained Machine Learning model."
                )

                st.markdown(
                    f"""
                    <div class="result-poor">

                        <div class="result-title">
                            ⚠️ {category}
                        </div>

                        <div class="score">
                            {percentage:.1f}%
                        </div>

                        <p>
                            {message}
                        </p>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # -------------------------------------------------
            # SCORE PROGRESS
            # -------------------------------------------------

            st.markdown("<br>", unsafe_allow_html=True)

            st.progress(
                int(round(percentage))
            )

            st.caption(
                f"Estimated credit score probability: {percentage:.2f}%"
            )

            # -------------------------------------------------
            # RESULT SUMMARY
            # -------------------------------------------------

            st.markdown(
                '<div class="section-title">📊 Assessment Summary</div>',
                unsafe_allow_html=True
            )

            result_col1, result_col2, result_col3 = st.columns(3)

            with result_col1:

                st.metric(
                    "Estimated Score",
                    f"{percentage:.1f}%"
                )

            with result_col2:

                st.metric(
                    "Risk Category",
                    category
                )

            with result_col3:

                st.metric(
                    "Model",
                    "Random Forest / ML"
                )

            # -------------------------------------------------
            # IMPORTANT NOTICE
            # -------------------------------------------------

            st.info(
                "ℹ️ This result is an AI/ML-based prediction for "
                "your project demonstration. It is not a real "
                "banking or financial approval decision."
            )

        except Exception as e:

            st.error(
                "❌ The model could not process these inputs."
            )

            st.warning(
                "This usually means that the input columns or "
                "category values do not exactly match the way "
                "the model was trained."
            )

            with st.expander("Technical error"):

                st.code(str(e))


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:#667085; font-size:14px;">
        AI Credit Scoring System | Machine Learning Project
    </div>
    """,
    unsafe_allow_html=True
)