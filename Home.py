import streamlit as st
from jinja2.sandbox import unsafe
from streamlit import session_state

import funtions
todos=funtions.get_todos()
def add_todo():
    todo =st.session_state['new_todo'] +"\n"

    todos.append(todo)
    funtions.write_todos(todos)

#st.title("my web-app to increase <b> productivity </b>",
#         unsafe_allow_url=True)

st.markdown("my web-app to increase <b>productivity</b>", unsafe_allow_html=True)

st.text_input(label="", placeholder="Enter the todo ",
              on_change=add_todo, key='new_todo')


todos=funtions.get_todos()

st.set_page_config(layout="wide")

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        funtions.write_todos(todos)
        del session_state[todo]
        st.rerun()




