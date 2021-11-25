import streamlit as st
import pandas as pd

st.write("""# Group 4 Data Science 
""")

st.write('6231302004 Charuwan Phithak')
st.write('6231302006 Thidawan Chaichana')
st.write('6231302011 Pun Kongsomboon')
st.write('6231302024 Peetikorn Preechachot')

st.sidebar.header('User Input')
st.sidebar.subheader('Please enter your data: ')

v_Sex = st.sidebar.radio('Sex' ,['Male' , 'Female'])
v_Faculty = st.sidebar.selectbox('FacultyName' , [
  'School of Management' 
, 'School of Agro-industry' 
, 'School of Cosmetic Science' 
, 'School of Dentistry' 
, 'School of Health Science' 
, 'School of Information Technology'
, 'School of Integrative Medicine' 
, 'School of Law' 
, 'School of Liberal Arts' 
, 'School of Medicine' 
, 'School of Nursing' 
, 'School of Science' 
, 'School of Sinology' 
, 'School of Social Innovation'
] , )

v_Entry = st.sidebar.selectbox('EntryGroupName' , [
  'รับตรงอิสระ'
, 'การรับนักศึกษาหลักสูตรทันตแพทยศาสตรบัณฑิต (17 จังหวัดภาคเหนือ)' 
, 'การรับนักศึกษาหลักสูตรทันตแพทยศาสตรบัณฑิต ประเภทโควตา บุตร/ธิดา ของบุคลากรทางด้านการแพทย์ฯ'
, 'การรับนักศึกษาหลักสูตรทันตแพทยศาสตรบัณฑิต รับตรงอิสระ' 
, 'การรับนักศึกษาหลักสูตรทันตแพทยศาสตรบัณฑิต โควตา 17 จังหวัดภาคเหนือ' 
, 'การรับนักศึกษาหลักสูตรทันตแพทยศาสตรบัณฑิต โควตา 17 จังหวัดภาคเหนือ ประเภทโควตา บุตร ธิดาฯ' 
, 'การรับนักศึกษาหลักสูตรแพทยศาสตรบัณฑิต (17 จังหวัดภาคเหนือ)' 
, 'การรับนักศึกษาหลักสูตรแพทยศาสตรบัณฑิต ประเภทโควตา บุตร/ธิดา ของบุคลากรด้านการแพทย์ฯ' 
, 'การรับนักศึกษาหลักสูตรแพทยศาสตรบัณฑิต รับตรงอิสระ' 
, 'การรับนักศึกษาหลักสูตรแพทยศาสตรบัณฑิต โควตา 17 จังหวัดภาคเหนือ' 
, 'การรับนักศึกษาหลักสูตรแพทยศาสตรบัณฑิต โควตา 17 จังหวัดภาคเหนือ ประเภทโควตา บุตร ธิดาฯ' 
, 'การรับผู้สำเร็จการศึกษาจากโรงเรียนนานาชาติในประเทศไทย และจบจากต่างประเทศหรือเทียบเท่า (รอบพิเศษ)' 
, 'รับตรงพิเศษสำนักวิชา (รอบที่ 5/2)'
, 'โครงการทุนการศึกษาสิงห์ปาร์คเชียงราย'
, 'โครงการทุนอุดมศึกษาเพื่อการพัฒนาจังหวัดชายแดนภาคใต้' 
, 'โครงการผลิตนักวิทยาศาสตร์เคมี'
, 'โครงการผลิตนักวิศวกรรมวัสดุ'
, 'โครงการผลิตบัณฑิตเพื่ออุตสาหกรรมดิจิทัล' 
, 'โครงการพัฒนานักเทคโนโลยีชีวภาพ' 
, 'โครงการพิเศษรับตรงสำนักวิชา' 
, 'โครงการพิเศษเพื่อนักเรียนในเขตพัฒนาพิเศษเฉพาะกิจจังหวัดชายแดนภาคใต้ รอบที่ 2'
, 'โครงการพิเศษเพื่อส่งเสริมเด็กดีมีที่เรียน' 
, 'โครงการพิเศษเพื่อเด็กดีมีที่เรียน'
, 'โครงการรับนักศึกษามหาวิทยาลัยแม่ฟ้าหลวงกลับเข้าศึกษาใหม่ (แบบมีเงื่อนไข)'
, 'โครงการรับนักศึกษามหาวิทยาลัยแม่ฟ้าหลวงกลับเข้าศึกษาใหม่ (แบบมีเงื่อนไข) รอบที่ 2' 
, 'โครงการรับนักเรียนห้องเรียนพิเศษเน้นภาษาอังกฤษ' 
, 'โครงการรับนักเรียนห้องเรียนพิเศษเน้นภาษาอังกฤษ รอบที่ 2' 
, 'โครงการรับนักเรียนในเขตพัฒนาพิเศษเฉพาะกิจจังหวัดชายแดนภาคใต้' 
, 'โครงการรับผู้พิการเข้าศึกษา'
, 'โครงการรับผู้มีความสามารถดีเด่นด้านดนตรี นาฏศิลป์ และกีฬา' 
, 'โครงการรับผู้สำเร็จการศึกษาจากโรงเรียนนานาชาติในประเทศไทย และจบจากต่างประเทศหรือเทียบเท่า' 
, 'โครงการรับผู้สำเร็จการศึกษาจากโรงเรียนนานาชาติในประเทศไทย และจบจากต่างประเทศหรือเทียบเท่า รอบที่ 2' 
, 'โครงการสร้างบัณฑิตรุ่นใหม่ทางด้านโลจิสติกส์เกษตร' 
, 'โครงการหลักสูตรฟู้ดยุคใหม่ โดนใจ Gen Z' 
, 'โครงการเครือข่ายครูแนะแนว' 
, 'โครงการเด็กดีมีที่เรียน' 
, 'โครงการโควตาพิเศษสำนักวิชา' 
, 'โครงการโควตาพิเศษสำหรับครูแนะแนว' 
, 'โควตา 17 จังหวัดภาคเหนือ'
, 'โควตาช่องทางพิเศษ (Fast Tract) เพื่อผลิตนักอนามัยสิ่งแวดล้อม' 
, 'โควตาช่องทางพิเศษเพื่อพัฒนานักสาธารณสุขชุมชนตามมาตรฐานวิชาชีพ' 
, 'โควตาพิเศษทุนการศึกษาเพื่อพัฒนาจังหวัดเชียงราย (สิงห์ปาร์คเชียงราย)' 
, 'โควตาพิเศษสำนักวิชาการจัดการ' 
, 'โควตาพิเศษสำนักวิชานวัตกรรมสังคม' 
, 'โควตาพิเศษสำนักวิชาพยาบาลศาสตร์ (โครงการผลิตพยาบาลเพื่อพัฒนาสุขภาพประชาชนฯ)' 
, 'โควตาพิเศษเพื่อพัฒนานักสาธารณสุขชุมชนตามมาตรฐานวิชาชีพ' 
, 'โควตาพิเศษเพื่อส่งเสริมนักวิทยาศาสตร์การกีฬา ในศตวรรษที่ 21' 
, 'โควตาวิทยาศาสตร์การกีฬายุคใหม่' 
, 'โควตาเยาวชนรุ่นใหม่ใส่ใจอนามัยสิ่งแวดล้อม' 
])

v_GPAX = st.sidebar.slider('GPAX' , min_value = 0.0, max_value = 4.0)
v_GPA_Eng = st.sidebar.slider('GPA_Eng' , min_value = 0.0, max_value = 4.0)
v_GPA_Math = st.sidebar.slider('GPA_Math' , min_value = 0.0, max_value = 4.0)
v_GPA_Sci = st.sidebar.slider('GPA_Sci' , min_value = 0.0, max_value = 4.0)
v_GPA_Sco = st.sidebar.slider('GPA_Sco' , min_value = 0.0, max_value = 4.0)
v_Q1 = st.sidebar.radio('Expectation for studying in MFU: beautiful scenary and atmosphere' , ['Agree' , 'Not Agree'])
v_Q2 = st.sidebar.radio('Expectation for studying in MFU: quality of life' , ['Agree' , 'Not Agree'])
v_Q3 = st.sidebar.radio('Expectation for studying in MFU: campus and facilities' , ['Agree' , 'Not Agree'])
v_Q4 = st.sidebar.radio('Expectation for studying in MFU: modern and ready-to-use learning support and facilities' , ['Agree' , 'Not Agree'])
v_Q5 = st.sidebar.radio('Expectation for studying in MFU: sources of student scholarship' , ['Agree' , 'Not Agree'])
v_Q6 = st.sidebar.radio('Expectation for studying in MFU: demand by workforce market' , ['Agree' , 'Not Agree'])
v_Q7 = st.sidebar.radio('Source of information for this application: email' , ['Agree' , 'Not Agree'])
v_Q8 = st.sidebar.radio('Source of information for this application: Facebook Admission@MFU' , ['Agree' , 'Not Agree'])
v_Q9 = st.sidebar.radio('Source of information for this application: Facebook MFU' , ['Agree' , 'Not Agree'])
v_Q10 = st.sidebar.radio('Source of information for this application: Facebook school or major' , ['Agree' , 'Not Agree'])
v_Q11 = st.sidebar.radio('Source of information for this application: Road show' , ['Agree' , 'Not Agree'])
v_Q12 = st.sidebar.radio('Source of information for this application: Family/friend/relative' , ['Agree' , 'Not Agree'])
v_Q13 = st.sidebar.radio('Source of information for this application: school teachers' , ['Agree' , 'Not Agree'])
v_Q14 = st.sidebar.radio('Source of information for this application: education exhibitions' , ['Agree' , 'Not Agree'])
v_Q15 = st.sidebar.radio('Source of information for this application: tutor schools' , ['Agree' , 'Not Agree'])
v_Q16 = st.sidebar.radio('Source of information for this application: television/Youtube channel' , ['Agree' , 'Not Agree'])
v_Q17 = st.sidebar.radio('Source of information for this application: advertisement in radio/newspaper/other publications' , ['Agree' , 'Not Agree'])
v_Q18 = st.sidebar.radio('Source of information for this application: other sources' , ['Agree' , 'Not Agree'])
v_Q19 = st.sidebar.radio('Source of information for this application: https://admission.mfu.ac.th' , ['Agree' , 'Not Agree'])
v_Q20 = st.sidebar.radio('Source of information for this application: https://www.mfu.ac.th' , ['Agree' , 'Not Agree'])
v_Q21 = st.sidebar.radio('Source of information for this application: other educational websites' , ['Agree' , 'Not Agree'])
v_Q22 = st.sidebar.radio('Source of information for this application: telephone/personal contact' , ['Agree' , 'Not Agree'])
v_Q23 = st.sidebar.radio('Factor to apply for MFU: easy/convenient transportation' , ['Agree' , 'Not Agree'])
v_Q24 = st.sidebar.radio('Factor to apply for MFU: suitable cost' , ['Agree' , 'Not Agree'])
v_Q25 = st.sidebar.radio('Factor to apply for MFU: graduates with higher language/academic competency than other universities' , ['Agree' , 'Not Agree'])
v_Q26 = st.sidebar.radio('Factor to apply for MFU: learning in English' , ['Agree' , 'Not Agree'])
v_Q27 = st.sidebar.radio('Factor to apply for MFU: quality/reputation of university' , ['Agree' , 'Not Agree'])
v_Q28 = st.sidebar.radio('Factor to apply for MFU: excellence in learning support and facilities' , ['Agree' , 'Not Agree'])
v_Q29 = st.sidebar.radio('Factor to apply for MFU: provision of preferred major' , ['Agree' , 'Not Agree'])
v_Q30 = st.sidebar.radio('Factor to apply for MFU: environment and setting motivate learning' , ['Agree' , 'Not Agree'])
v_Q31 = st.sidebar.radio('Factor to apply for MFU: experienced and high-quality instructors' , ['Agree' , 'Not Agree'])
v_Q32 = st.sidebar.radio('Factor to apply for MFU: suggestion by school teacher/friend/relative' , ['Agree' , 'Not Agree'])
v_Q33 = st.sidebar.radio('Factor to apply for MFU: suggestion by family' , ['Agree' , 'Not Agree'])
v_Q34 = st.sidebar.radio('If your application fails, will you try again? : try the same major' , ['Agree' , 'Not Agree'])
v_Q35 = st.sidebar.radio('If your application fails, will you try again? : try a different major' , ['Agree' , 'Not Agree'])
v_Q36 = st.sidebar.radio('If your application fails, will you try again? : will not try again' , ['Agree' , 'Not Agree'])
v_Q37 = st.sidebar.radio('Reason for apply for the major: suggestion by school teacher' , ['Agree' , 'Not Agree'])
v_Q38 = st.sidebar.radio('Reason for apply for the major: suggestion by family' , ['Agree' , 'Not Agree'])
v_Q39 = st.sidebar.radio('Reason for apply for the major: personal preference' , ['Agree' , 'Not Agree'])
v_Q40 = st.sidebar.radio('Reason for apply for the major: chance of getting a job after graduation' , ['Agree' , 'Not Agree'])
v_Q41 = st.sidebar.radio('Reason for apply for the major: less competitive than other universities' , ['Agree' , 'Not Agree'])
v_Q42 = st.sidebar.radio('Reason for apply for the major: suggestion by friend/relative/others' , ['Agree' , 'Not Agree'])


if v_Q1 == 'Agree': v_Q1 = 1
else : v_Q1 = 0

if v_Q2 == 'Agree': v_Q2 = 1
else : v_Q2 = 0

if v_Q3 == 'Agree': v_Q3 = 1
else : v_Q3 = 0

if v_Q4 == 'Agree': v_Q4 = 1
else : v_Q4 = 0

if v_Q5 == 'Agree': v_Q5 = 1
else : v_Q5 = 0

if v_Q6 == 'Agree': v_Q6 = 1
else : v_Q6 = 0

if v_Q7 == 'Agree': v_Q7 = 1
else : v_Q7 = 0

if v_Q8 == 'Agree': v_Q8 = 1
else : v_Q8 = 0

if v_Q9 == 'Agree': v_Q9 = 1
else : v_Q9 = 0

if v_Q10 == 'Agree': v_Q10 = 1
else : v_Q10 = 0

if v_Q11 == 'Agree': v_Q11 = 1
else : v_Q11 = 0

if v_Q12 == 'Agree': v_Q12 = 1
else : v_Q12 = 0

if v_Q13 == 'Agree': v_Q13 = 1
else : v_Q13 = 0

if v_Q14 == 'Agree': v_Q14 = 1
else : v_Q14 = 0

if v_Q15 == 'Agree': v_Q15 = 1
else : v_Q15 = 0

if v_Q16 == 'Agree': v_Q16 = 1
else : v_Q16 = 0

if v_Q17 == 'Agree': v_Q17 = 1
else : v_Q17 = 0

if v_Q18 == 'Agree': v_Q18 = 1
else : v_Q18 = 0

if v_Q19 == 'Agree': v_Q19 = 1
else : v_Q19 = 0

if v_Q20 == 'Agree': v_Q20 = 1
else : v_Q20 = 0

if v_Q21 == 'Agree': v_Q21 = 1
else : v_Q21 = 0

if v_Q22 == 'Agree': v_Q22 = 1
else : v_Q22 = 0

if v_Q23 == 'Agree': v_Q23 = 1
else : v_Q23 = 0

if v_Q24 == 'Agree': v_Q24 = 1
else : v_Q24 = 0

if v_Q25 == 'Agree': v_Q25 = 1
else : v_Q25 = 0

if v_Q26 == 'Agree': v_Q26 = 1
else : v_Q26 = 0

if v_Q27 == 'Agree': v_Q27 = 1
else : v_Q27 = 0

if v_Q28 == 'Agree': v_Q28 = 1
else : v_Q28 = 0

if v_Q29 == 'Agree': v_Q29 = 1
else : v_Q29 = 0

if v_Q30 == 'Agree': v_Q30 = 1
else: v_Q30 = 0

if v_Q31 == 'Agree': v_Q31 = 1
else : v_Q31 = 0

if v_Q32 == 'Agree': v_Q32 = 1
else : v_Q32 = 0

if v_Q33 == 'Agree': v_Q33 = 1
else : v_Q33 = 0

if v_Q34 == 'Agree': v_Q34 = 1
else: v_Q34 = 0

if v_Q35 == 'Agree': v_Q35 = 1
else : v_Q35 = 0

if v_Q36 == 'Agree': v_Q36 = 1
else : v_Q36 = 0

if v_Q37 == 'Agree': v_Q37 = 1
else : v_Q37 = 0

if v_Q38 == 'Agree': v_Q38 = 1
else : v_Q38 = 0

if v_Q39 == 'Agree': v_Q39 = 1
else : v_Q39 = 0

if v_Q40 == 'Agree': v_Q40 = 1
else : v_Q40 = 0

if v_Q41 == 'Agree': v_Q41 = 1
else : v_Q41 = 0

if v_Q42 == 'Agree': v_Q42 = 1
else : v_Q42 = 0


data = {
  'Sex' : v_Sex 
, 'FacultyName' : v_Faculty 
, 'EntryGroupName' : v_Entry
, 'GPAX': v_GPAX
, 'GPA_Eng': v_GPA_Eng
, 'GPA_Math' : v_GPA_Math
, 'GPA_Sci' : v_GPA_Sci
, 'GPA_Sco' : v_GPA_Sco
, 'Q1': v_Q1
, 'Q2': v_Q2
, 'Q3': v_Q3
, 'Q4': v_Q4
, 'Q5': v_Q5
, 'Q6': v_Q6
, 'Q7': v_Q7
, 'Q8': v_Q8
, 'Q9': v_Q9
, 'Q10': v_Q10
, 'Q11': v_Q11
, 'Q12': v_Q12
, 'Q13': v_Q13
, 'Q14': v_Q14
, 'Q15': v_Q15
, 'Q16': v_Q16
, 'Q17': v_Q17
, 'Q18': v_Q18
, 'Q19': v_Q19
, 'Q20': v_Q20
, 'Q21': v_Q21
, 'Q22': v_Q22
, 'Q23': v_Q23
, 'Q24': v_Q24
, 'Q25': v_Q25
, 'Q26': v_Q26
, 'Q27': v_Q27
, 'Q28': v_Q28
, 'Q29': v_Q29
, 'Q30': v_Q30
, 'Q31': v_Q31
, 'Q32': v_Q32
, 'Q33': v_Q33
, 'Q34': v_Q34
, 'Q35': v_Q35
, 'Q36': v_Q36
, 'Q37': v_Q37
, 'Q38': v_Q38
, 'Q39': v_Q39
, 'Q40': v_Q40
, 'Q41': v_Q41
, 'Q42': v_Q42
,
}

df = pd.DataFrame(data , index=[0])

st.header('Application of Student MFU Predection: ')
st.subheader('User Input: ')

st.write(df)


data_sample = pd.read_csv('Result.csv')
df = pd.concat([df ,data_sample] , axis=0)
# st.write(df)


cat_data = pd.get_dummies(df[['Sex','FacultyName','EntryGroupName']])

X_new = pd.concat([cat_data , df] , axis=1)

X_new = X_new[:1]

X_new = X_new.drop(columns=['Sex','FacultyName','EntryGroupName' ])

st.subheader('Pre-Processed Input: ')
st.write(X_new)

import pickle
# -- Reads the saved normalization model
load_nor = pickle.load(open('normalization.pkl', 'rb'))
#Apply the normalization model to new data
X_new = load_nor.transform(X_new)
#Show the X_new data frame on the screen
st.subheader('Normalized Input:')
st.write(X_new)

# -- Reads the saved classification model
load_knn = pickle.load(open('best_knn.pkl', 'rb'))
# Apply model for prediction
prediction = load_knn.predict(X_new)
#Show the prediction result on the screen
st.subheader('Prediction:')
st.write(prediction)