import streamlit as st

st.set_page_config(page_title="Expense Tracker", layout="centered")

# ---- load your existing style.css so the look matches your HTML/CSS ----
with open("new.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ---- session state replaces the global lists from expense.py ----
if "income_list" not in st.session_state:
    st.session_state.income_list = []
if "expense_list" not in st.session_state:
    st.session_state.expense_list = []

# ---- your functions from expense.py, unchanged logic, just no input()/print() ----
def cal_income(income):
    st.session_state.income_list.append(income)

def cal_expense(expense):
    st.session_state.expense_list.append(expense)

def cal_balance(income_list, expense_list):
    return sum(income_list) - sum(expense_list)

# ---- markup mirrors your profile.html structure ----
st.markdown("<h1>Expense Tracker</h1>", unsafe_allow_html=True)
st.markdown("<h2>Do you want to add income or expense?</h2>", unsafe_allow_html=True)

st.markdown("<h3>Add income</h3>", unsafe_allow_html=True)
income_val = st.text_input("income", label_visibility="collapsed", placeholder="income", key="income_input")
if st.button("add", key="add_income"):
    if income_val:
        cal_income(float(income_val))
        st.rerun()

st.markdown("<h3>Add expense</h3>", unsafe_allow_html=True)
expense_val = st.text_input("expense", label_visibility="collapsed", placeholder="expense", key="expense_input")
if st.button("add", key="add_expense"):
    if expense_val:
        cal_expense(float(expense_val))
        st.rerun()

st.markdown("<h3>total balance</h3>", unsafe_allow_html=True)
balance = cal_balance(st.session_state.income_list, st.session_state.expense_list)
st.markdown(f"<p id='balance'>${balance:.2f}</p>", unsafe_allow_html=True)

if st.button("Reset", key="reset"):
    st.session_state.income_list = []
    st.session_state.expense_list = []
    st.rerun()
