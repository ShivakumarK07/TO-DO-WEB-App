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

# Title of the web app
st.title("TO-DO App")

# Subheading
st.subheader(" we can enter our tasks")

# Looping through each to-do item  and displaying it with checkbox
for index,todo in enumerate(todos):
    # Create a checkbox for each to-do item; `key=to,do` ensures each checkbox is unique
    checkbox = st.checkbox(todo,key = todo)

    if checkbox:   # If the checkbox is ticked
        todos.pop(index)             # Removes to-do from list
        function.write_todos(todos)  # save the updated list
        del st.session_state[todo]    #Removes checkbox from session
        st.rerun()                    # Rerun the app to update UI

st.text_input(label = " ",             # Empty label no text shown
              placeholder = "Add a new todo", # Text inside the inputfield
              on_change = add_todo , # When user presses Enter, call add_todo()
              key = 'new_todo')       #Store the text input value in session state


