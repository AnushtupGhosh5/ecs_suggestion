import streamlit as st
import mysql.connector

mydb = mysql.connector.connect(

    host='localhost',
    user='root',
    password='@Nu$#tup12345',
    port='3306',
    database='extracurriculars_db'
)

st.title('Extracurricular Suggestion App')

# Create a cursor to execute SQL queries
cursor = mydb.cursor()

# Query to get unique majors from your database
unique_majors_query = 'SELECT DISTINCT major FROM extracurriculars'
cursor.execute(unique_majors_query)
unique_majors = [row[0] for row in cursor.fetchall()]

selected_major = st.selectbox('Select your major:', unique_majors)

if st.button('Get Extracurricular Suggestions'):
    # Query to get suggestions based on the selected major
    suggestions_query = f"SELECT suggestion FROM extracurriculars WHERE major = '{selected_major}'"
    cursor.execute(suggestions_query)
    suggestions = [row[0] for row in cursor.fetchall()]

    st.header(f'Suggested Extracurricular Activities for {selected_major}:')
    for suggestion in suggestions:
        st.write(suggestion)

# Close the cursor and database connection when done
cursor.close()
mydb.close()
