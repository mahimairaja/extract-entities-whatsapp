from utils import extract_food_order
from utils import FoodOrder
import streamlit as st

st.title("Food Order Assistant 🍕")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def append_message(role: str, content: str):
    st.chat_message(role).markdown(prompt)
    st.session_state.messages.append({"role": role, "content": prompt})

if __name__ == "__main__":
    if prompt := st.chat_input("What would you like to have today?"):
        append_message("user", prompt)

        response = extract_food_order(prompt)
        if type(response) != FoodOrder:
            response = {"msg": "no food order details found"}
            reply = ''
        else:
            response = dict(response)
            reply = f"Sure, I have noted down your order for {response['quantity']} {response['food_name']}"
            if response["when_needed"]:
                reply += f" for {response['when_needed']}."
            else:
                reply += "."

        with st.chat_message("assistant"):
            st.json(response)
            st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})