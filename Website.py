import streamlit as s
from backend import chat

s.title("Hi, how can I help You today? ")
s.write("Calvin is the best programmer")
with s.sidebar:
    s.write("Settings")
    Current_Chat = s.radio("pick the type", ["Genius", "Average", "Stupid"])
s.audio_input(label = "Insert message below", sample_rate=16000, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible", width="stretch")
with s.chat_message(name = "Bot", avatar="🤖", width="stretch"):
    s.write("How can I help You today")
input = s.chat_input("Type your message")

if Current_Chat not in s.session_state:
    if Current_Chat == "Tutor":
        s.session_state[Current_Chat] = [{"role": "system", "content": "You understand all the proper materials provided by the user and will explain everything properly step by step."}]

    if Current_Chat == "ETU":
        s.session_state[Current_Chat] = [{"role": "system", "content": "You make everything easy to understand and will put it in simple to understand anologies. like placing it in different scenarios."}]
    
    if Current_Chat == "Quiz":
        s.session_state[Current_Chat] = [{"role": "system", "content": " you will make the appropiate messages into quiz forms and ask then then give them results quiz and provide answers for mistakes."}]
    
# Display chat messages from history on app rerun
for message in s.session_state[Current_Chat]:
    with s.chat_message(message["role"]):
        s.markdown(message["content"])

if input:
    with s.chat_message(name = "user", width="stretch"):
        s.write(input)
    s.session_state[Current_Chat].append({"role": "user", "content": input})

    with s.chat_message(name = "assistant", width ="stretch"):
        chatt = s.write_stream(chat(s.session_state[Current_Chat])) 
    s.session_state[Current_Chat].append({"role": "assistant", "content": chatt})
