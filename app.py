import streamlit as st

# Define the HTML and CSS code
html_code = """
<style>
.scroll-container {
    display: flex;
}

.left-column {
    width: 50%;
    height: 400px;
    overflow-y: scroll;
}

.right-column {
    width: 50%;
}
</style>

<div class="scroll-container">
    <div class="left-column">
        </div>
    <div class="right-column">
        </div>
</div>
"""

# Display the content using st.markdown
st.markdown(html_code, unsafe_allow_html=True)

# Import necessary libraries
import streamlit as st

# Create two beta columns
left_col, right_col = st.beta_columns(2)

# Add content to both columns
with left_col:
    # Your content for the left column (scrollable)
    for i in range(100):
        st.write(f"This is item {i + 1}")

with right_col:
    # Your content for the right column (static)
    st.write("This is the static right column")
