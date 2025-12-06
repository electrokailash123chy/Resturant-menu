import streamlit as st
st.title("😎Welcome to kailash Resturaunt")

st.write("list out your favourite item from this listed table")
num1 = st.checkbox("tea Rs 20")
num2 = st.checkbox("coffee Rs 30")
num3 = st.checkbox("Mix juice Rs 40")

# Number inputs for quantity
qty1 = st.number_input("Quantity of tea", min_value=0, value=0, step=1) if num1 else 0
qty2 = st.number_input("Quantity of coffee", min_value=0, value=0, step=1) if num2 else 0
qty3 = st.number_input("Quantity of Mix juice", min_value=0, value=0, step=1) if num3 else 0

enter = st.button("submit")

if enter:
    selected_items = []
    total = 0
    total_time = 0

    if num1 and qty1 > 0:
        selected_items.append(f"tea quantity={qty1}")
        total += 20 * qty1
        total_time += 2  
    if num2 and qty2 > 0:
        selected_items.append(f"coffee quantity={qty2}")
        total += 30 * qty2
        total_time += 5 
    if num3 and qty3 > 0:
        selected_items.append(f"Mix juice quantity={qty3}")
        total += 40 * qty3
        total_time += 3 

    if selected_items:
        st.write(f"Your favourite items are: {', '.join(selected_items)}")
        st.write(f"Total cost: Rs {total}")
        st.write(f"Total preparation time: {total_time} minutes")
    else:
        st.write("No items selected.")