import pandas as pd
import streamlit as st
import time
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import xgboost as xgb
from streamlit_extras.stylable_container import stylable_container


def GenderCategory(gender):
    if (gender== "Male"):
        return "1"
    else:
        return "0"


def education_qualification(data):
    if (data == "No Education"):
        return "00"
    elif (data == "Basic Education"):
        return "01"
    elif (data == "Basic Education"):
        return "02"
    elif (data == "Basic Education"):
        return "03"
    elif (data == "Basic Education"):
         return "04"
    elif (data == "Basic Education"):
        return "05"
    elif (data == "Basic Education"):
        return "06"
    else:
       return "07"



def AttendanceCategory(attendance):
    if (attendance== "Daytime"):
        return "1"
    else:
        return "0"

def BinaryFinancial(data):
    if (data == "Yes"):
        return "1"
    else:
        return "0"

def fit_transform_minmax(data, min, max):
    Min_Max_Scaler = MinMaxScaler()
    scaller = Min_Max_Scaler.fit([[min] , [max]])
    scaller_data = scaller.transform(data)
    return scaller_data

def num_scaler(data):
    data[['Application_order']] = fit_transform_minmax(data[['Application_order']], 0., 9.)
    data[['Previous_qualification_grade']] = fit_transform_minmax(data[['Previous_qualification_grade']], 0., 200.)
    data[['Admission_grade']] = fit_transform_minmax(data[['Admission_grade']], 0., 200.)
    data[['Age_at_enrollment']] = fit_transform_minmax(data[['Age_at_enrollment']], 17., 70.)
    data[['Curricular_units_grade']] = fit_transform_minmax(data[['Curricular_units_grade']], 0., 20.)
    data[['Curricular_units_credited']] = fit_transform_minmax(data[['Curricular_units_credited']], 0., 40.)
    data[['Curricular_units_enrolled']] = fit_transform_minmax(data[['Curricular_units_enrolled']], 0., 52.)
    data[['Curricular_units_approved']] = fit_transform_minmax(data[['Curricular_units_approved']], 0., 52.)
    data[['Curricular_units_evaluations']] = fit_transform_minmax(data[['Curricular_units_evaluations']], 0., 72.)
    data[['Curricular_units_without_evaluations']] = fit_transform_minmax(data[['Curricular_units_without_evaluations']], 0., 24.)

    return data



def data_preparation(data_input):
    students_data = pd.read_csv("D:/pythonProject/student_model/students_data.csv")
    students_data = students_data.drop(columns = ["ID", "Status"])
    data_prep = pd.concat([students_data, data_input])
    num = ['Application_order', 'Previous_qualification_grade', 'Admission_grade',
           'Age_at_enrollment', 'Curricular_units_credited',
           'Curricular_units_approved', 'Curricular_units_enrolled',
           'Curricular_units_evaluations', 'Curricular_units_without_evaluations',
           'Curricular_units_grade']
    data_num = num_scaler(data_prep[num])
    for num in num:
        data_prep[num] = data_num[num]
    cat = ['Application_order', 'Previous_qualification_grade',
       'Admission_grade', 'Age_at_enrollment', 'Curricular_units_credited',
       'Curricular_units_approved', 'Curricular_units_enrolled',
       'Curricular_units_evaluations', 'Curricular_units_without_evaluations',
       'Curricular_units_grade', 'Marital_status', 'Application_mode',
       'Course', 'Daytime_evening_attendance', 'Previous_qualification',
       'Mothers_qualification', 'Fathers_qualification', 'Mothers_occupation',
       'Fathers_occupation', 'Debtor', 'Tuition_fees_up_to_date', 'Gender',
       'Scholarship_holder']
    data_cat = data_prep[cat].astype(str)
    encoder = LabelEncoder()
    for cat in cat:
        data_cat[cat]= encoder.fit_transform(data_cat[cat])
        data_prep[cat] = data_cat[cat]
    return data_prep.tail(1)

def example():

    st.button("Normal button")

    with stylable_container(
        key="container_with_border",
        css_styles="""
            {
                border: 1px solid rgba(49, 51, 63, 0.2);
                border-radius: 0.5rem;
                padding: calc(1em - 1px)
            }
            """,
    ):
        st.markdown("This is a container with a border.")

st.set_page_config(layout="wide")
st.title("Jaya Jaya Maju Institute Student Status Prediction")

with st.container(border = True):

    st.subheader('Personal and Parents Data', divider='grey')

    col1a, col1b = st.columns(2)

    with col1a:
        gender = st.selectbox("Gender", ("Male", "Female"))
        gender= GenderCategory(gender)

        father_qualification = st.selectbox("Father Qualification", ("No Education",
                                                                     "Basic Education",
                                                                     "Secondary Education",
                                                                     "Degree",
                                                                     "Bachelor Degree",
                                                                     "Master",
                                                                     "Doctor",
                                                                     "Frequently Higher Education"))
        father_qualification = education_qualification(father_qualification)
        father_occupation = st.selectbox("Father Occupation", ('Students',
                                                               'Professionals and Specialists',
                                                               'Intermediate Level Technicians and Professions',
                                                               'Administrative Staff',
                                                               'Service Workers and Sellers',
                                                               "Agricultural and Forestry Workers",
                                                               "Skilled Workers in Industry, Construction, and Craftsmen",
                                                               "Installation and Machine Operators and Assembly Workers",
                                                               "Unskilled Workers",
                                                               'Armed Forces Professions',
                                                               "Other"))

    with col1b:
        marital_status = st.selectbox("Marital Status", ("Single", "In Relationship"))

        mother_qualification = st.selectbox("Mother Qualification", ("No Education",
                                                                     "Basic Education",
                                                                     "Secondary Education",
                                                                     "Degree",
                                                                     "Bachelor Degree",
                                                                     "Master",
                                                                     "Doctor",
                                                                     "Frequently Higher Education"))

        mother_qualification = education_qualification(mother_qualification)

        mother_occupation = st.selectbox("Mother Occupation", ('Students',
                                                               'Professionals and Specialists',
                                                               'Intermediate Level Technicians and Professions',
                                                               'Administrative Staff',
                                                               'Service Workers and Sellers',
                                                               "Agricultural and Forestry Workers",
                                                               "Skilled Workers in Industry, Construction, and Craftsmen",
                                                               "Installation and Machine Operators and Assembly Workers",
                                                               "Unskilled Workers",
                                                               'Armed Forces Professions',
                                                               "Other"))

with st.container(border = True):
    st.subheader('Enrollment Data', divider='grey')
    col2a, col2b = st.columns(2)
    with col2a:
        min_age = 18
        Age_at_enrollment= st.number_input("Age at Enrollment",
                                           min_value = 17,
                                           max_value= 70,
                                           value= min_age,
                                           step = 1)

        Application_mode = st.selectbox("Application Mode", ("General Contingent",
                                                            "Special Contingent",
                                                            "International",
                                                            "Transfer and Change",
                                                            "Specific ordinances",
                                                            "Other"))
        Previous_qualification = st.selectbox("Previous Qualification", ("Basic Education",
                                                                        "Secondary Education",
                                                                        "Degree",
                                                                        "Bachelor Degree",
                                                                        "Master",
                                                                        "Doctor",
                                                                        "Frequently Higher Education"))

        Previous_qualification = education_qualification(Previous_qualification)
    with col2b:
        Admission_grade = st.number_input("Admission Grade",
                                           min_value = 0,
                                           max_value= 200,
                                           value= 0,
                                           step = 1)

        Application_order = st.number_input("Application Order",
                                           min_value = 0,
                                           max_value= 9,
                                           value= 0,
                                           step = 1)

        Previous_qualification_grade = st.number_input("Previous Qualification Grade",
                                                       min_value = 0,
                                                       max_value= 200,
                                                       value= 0,
                                                       step = 1)

with st.container(border = True):
    st.subheader('While Studying Data', divider='grey')

    Course = st.selectbox("Course", ("Basic Education","Technology and Engineering",
                                     "Design and Creativity",
                                     "Health and Care",
                                     "Social Services and Management",
                                     "Agriculture and Environment"))

    Daytime_evening_attendance = st.selectbox("Daytime/Evening Attendance", ("Daytime", "Evening"))
    Daytime_evening_attendance = AttendanceCategory(Daytime_evening_attendance)

    col3b, col3c = st.columns(2)
    with col3b:
        Curricular_units_credited = st.number_input("Curricular Units Credited",
                                                   min_value = 0,
                                                   max_value= 40,
                                                   value= 0,
                                                   step = 1)

        Curricular_units_enrolled = st.number_input("Curricular Units Enrolled",
                                                       min_value = 0,
                                                       max_value= 52,
                                                       value= 0,
                                                       step = 1)

        Curricular_units_approved = st.number_input("Curricular Units Approved",
                                                       min_value = 0,
                                                       max_value= Curricular_units_enrolled,
                                                       value= 0,
                                                       step = 1)

    with col3c:
        Curricular_units_evaluation = st.number_input("Curricular Units with Evaluation",
                                                       min_value = 0,
                                                       max_value= 72,
                                                       value= 0,
                                                       step = 1)
        Curricular_units_without_evaluation = st.number_input("Curricular Units without Evaluation",
                                                       min_value = 0,
                                                       max_value= 24,
                                                       value= 0,
                                                       step = 1)
        Curricular_units_grade = st.number_input("Curricular Units Grade",
                                                       min_value = 0.0,
                                                       max_value= 20.0,
                                                       value= 0.0,
                                                       step = 0.5)

with st.container(border = True):
        st.subheader('Financial Data', divider='grey')

        col4a, col4b, col4c = st.columns(3)
        with col4a:
            Scholarship_holder = st.selectbox("Scholarship Holder", ("Yes", "No"))
            scholarship = BinaryFinancial(Scholarship_holder)

        with col4b:
            Tuition_fees_up_to_date = st.selectbox("Tuition Fees Up to Date", ("Yes", "No"))
            tuition_fees_up = BinaryFinancial(Tuition_fees_up_to_date)

        with col4c:
            Debtor = st.selectbox("Debtor", ("Yes", "No"))
            debtor_status = BinaryFinancial(Debtor)



data = [[Application_order, Previous_qualification_grade,
             Admission_grade, Age_at_enrollment,
             Curricular_units_credited,Curricular_units_approved,
             Curricular_units_enrolled,Curricular_units_evaluation,
             Curricular_units_without_evaluation, Curricular_units_grade,
             marital_status, Application_mode, Course, int(Daytime_evening_attendance),
             int(Previous_qualification), int(mother_qualification), int(father_qualification),
             mother_occupation, father_occupation, int(debtor_status), int(tuition_fees_up),
             int(gender), int(scholarship)]]
data_df = pd.DataFrame(data, columns=[ 'Application_order', 'Previous_qualification_grade',
                                        'Admission_grade', 'Age_at_enrollment',
                                        'Curricular_units_credited','Curricular_units_approved',
                                        'Curricular_units_enrolled','Curricular_units_evaluations',
                                        'Curricular_units_without_evaluations','Curricular_units_grade',
                                        'Marital_status', 'Application_mode', 'Course',
                                        'Daytime_evening_attendance', 'Previous_qualification',
                                        'Mothers_qualification', 'Fathers_qualification',
                                        'Mothers_occupation','Fathers_occupation',
                                        'Debtor', 'Tuition_fees_up_to_date', 'Gender',
                                        'Scholarship_holder'])

# Load Model Machine Learning
model = xgb.XGBClassifier()
model.load_model("D:/pythonProject/student_model/model.json")
with stylable_container(
    key="PREDICT",
    css_styles="""
        button {
            background-color: blue;
            color: white;
            border-radius: 20px;
        }
        """,
):

    if st.button("PREDICT", use_container_width=True):
        container = st.container(border = True)
        with container:
            input = data_preparation(data_df)
            prediction = model.predict(input)
            with st.spinner('Predict data...'):
                time.sleep(5)
            if (prediction == 0):
                st.subheader("Student Status: Dropout",  divider="red")
            elif (prediction == 1):

                st.subheader("Student Status: Enrolled",  divider="yellow")
            else:

                st.subheader("Student Status: Graduate",  divider="green")
            with stylable_container(key="Reset",css_styles="""
                                                                button {
                                                                    background-color: white;
                                                                    color: black;
                                                                    border-radius: 20px;
                                                                }
                                                                """,):
                if st.button("Reset"):
                    st.rerun()





















