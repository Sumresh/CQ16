import streamlit as st
import pandas as pd

# Read the CSV file
df = pd.read_csv("udemy_courses.csv")
x = df['course_title']
y = df.iloc[:, 1:3].values
# Function to search for a course based on keyword
def search_course(keyword):
    result = x[x.str.contains(keyword, case=False)]
    if not result.empty:
        return result.iloc[0]  # Return only the first result
    else:
        return "No matching course found."

# Function to get URL for a given title
def get_url_for_title(title):
    for item in y:
        if item[0] == title:
            return item[1]
    return "URL not found for the given title."

# Main Streamlit app
def main():
    st.title("Course Search")
    keyword = st.text_input("Enter your keyword:", "")
    if st.button("Search"):
        # Search for the course based on the keyword
        result = search_course(keyword)
        st.write("Matching course:", result)

        # Get URL for the matching course
        if result != "No matching course found.":
            url = get_url_for_title(result)
            st.write("URL for the course:", url)

if __name__ == "__main__":
    main()
