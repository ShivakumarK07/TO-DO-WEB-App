import streamlit as st    # importing a 3rd party library for web application
import function           # importing python functions

# Fetching the current list of todos from the helper module
todos = function.get_todos()

# custom function that adds new to-do to the list
def add_todo():
    # Get the value entered in the text input box from Streamlit's session state
    todo = st.session_state["new_todo"] +"\n"  # New line for formatting
    todos.append(todo)                         # Add new to-do to list
    function.write_todos(todos)                # Updating the list
    st.session_state['new_todo'] = ""          # clears the text field for next todo

# Title of the web app
st.title("TO-DO Web App")

# Subheading
st.subheader(" we can enter our tasks")


# --- At the very top of your Streamlit script (BEFORE any other code) ---
if 'task_finished_message' in st.session_state:
    # Display the stored message
    st.success(st.session_state['task_finished_message'])
    # Remove the message immediately so it only appears once
    del st.session_state['task_finished_message']


# --- Inside your checkbox loop (Modified Deletion Logic) ---
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        # Store the confirmation message in session state
        st.session_state['task_finished_message'] = f"🏆 COMPLETED! 🥳 *{todo}* has been removed 🏆."

        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.rerun() # This restarts the script and displays the message


st.text_input(label = " ",             # Empty label no text shown
              placeholder = "Add a new todo", # Text inside the inputfield
              on_change = add_todo , # When user presses Enter, call add_todo()
              key = 'new_todo')       #Store the text input value in session state


