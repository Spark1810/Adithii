import streamlit as st



# 1. Initialize the session state to store votes
# This block only runs once when the app first loads
if 'votes' not in st.session_state:
    st.session_state.votes = {"Python": 0, "JavaScript": 0, "C++": 0}

st.title("🚀 Language Popularity Poll")
st.write("Cast your vote for your favorite programming language!")

# 2. Create the layout with columns
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Vote Python"):
        st.session_state.votes["Python"]= 1
        st.toast("Vote recorded for Python!")

with col2:
    if st.button("Vote JavaScript"):
        st.session_state.votes["JavaScript"] += 1
        st.toast("Vote recorded for JavaScript!") 

with col3:
    if st.button("Vote C++"):
        st.session_state.votes["C++"] += 1
        st.toast("Vote recorded for C++!")

st.divider()
st.divider()

# 3. Display the live results
st.subheader("Live Results")

# Loop through the dictionary to show metrics
res_col1, res_col2, res_col3 = st.columns(3)
res_col1.metric("Python", st.session_state.votes["Python"])
res_col2.metric("JavaScript", st.session_state.votes["JavaScript"])
res_col3.metric("C++", st.session_state.votes["C++"])

# 4. Add a reset button
if st.button("Reset Poll"):
    st.session_state.votes = {"Python": 0, "JavaScript": 0, "C++": 0}
    st.rerun()
