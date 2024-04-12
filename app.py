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
        return result.tolist()  # Convert the result to a list
    else:
        return "No matching course found."

# Function to get URL for a given title
def get_url_for_title(title):
    urls = []
    for item in y:
        if item[0] in title:
            urls.append(item[1])
    return urls

# Main Streamlit app
def main():
    st.title("Course Search")
    keyword = st.text_input("Enter your keyword:", "")
    if st.button("Search"):
        # Search for the course based on the keyword
        result = search_course(keyword)
        if result != "No matching course found.":
            st.write("Matching course(s):")
            for course_title in result:
                st.write(course_title)

                # Get URL(s) for the matching course
                urls = get_url_for_title(course_title)
                st.write("URL(s) for the course:")
                for url in urls:
                    st.write(url)

if __name__ == "__main__":
    main()
