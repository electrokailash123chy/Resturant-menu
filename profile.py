import streamlit as st
st.title("😎Welcome to kailash Resturaunt")


st.write("list out your favourite item from this listed table")
col1, col2 = st.columns(2)

with col1:
    st.header("Menu")
    st.image("tea.jpg", width=150)
    st.subheader("Tea — Rs 20")
    num1 = st.checkbox("Tea (Rs 20)", key="tea_cb")
    qty1 = st.number_input("Quantity (Tea)", min_value=0, value=1, step=1, key="tea_qty") if num1 else 0

    st.subheader("Coffee — Rs 30")
    st.image("coffee.jpg", width=150)
    num2 = st.checkbox("Coffee (Rs 30)", key="coffee_cb")
    qty2 = st.number_input("Quantity (Coffee)", min_value=0, value=1, step=1, key="coffee_qty") if num2 else 0

with col2:
    st.subheader("Mix Juice — Rs 40")
    st.image("mix.jpg", width=150)
    num3 = st.checkbox("Mix Juice (Rs 40)", key="juice_cb")
    qty3 = st.number_input("Quantity (Juice)", min_value=0, value=1, step=1, key="juice_qty") if num3 else 0

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
        total_time += 3 
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