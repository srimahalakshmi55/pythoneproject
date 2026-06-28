import streamlit as st

if "expenses" not in st.session_state:
    st.session_state.expenses = []

st.title("Expense Tracker")

date = st.text_input("Date")

category = st.selectbox(
    "Category",
    ["Food", "Travel", "Shopping", "Education",
     "Entertainment", "Health", "Bills", "Other"]
)

amount = st.number_input("Amount", min_value=0.0)

description = st.text_input("Description")

if st.button("Add Expense"):
    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    st.session_state.expenses.append(expense)
    st.success("Expense Added Successfully!")

st.subheader("Expenses")

if st.button("View Expenses"):
    if len(st.session_state.expenses) == 0:
        st.warning("No expenses found.")
    else:
        for e in st.session_state.expenses:
            st.write("Date:", e["date"])
            st.write("Category:", e["category"])
            st.write("Amount:", e["amount"])
            st.write("Description:", e["description"])
            st.write("--------------------")

if st.button("Show Total Expense"):
    total = 0

    for e in st.session_state.expenses:
        total = total + e["amount"]

    st.success(f"Total Expense = ₹{total}")+