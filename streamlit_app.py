import streamlit as st
import gettext


#i18n
t = gettext.translation("i18n", "locale", fallback=True)
_ = t.gettext


#Sidebar
st.sidebar.image("static/datarobot.png")

#Body
st.write("My app")
st.write(_("Hello friends"))
# st.balloons()
st.write("A new update..")
st.caption("Not sure about this either . . ")
st.text("This is some text . . . . ")


st.markdown(
    """
    <style>
    .element-container:has(style){
        display: none;
    }
    #button-after {
        display: none;
    }
    .element-container:has(#button-two){
    display: none;
    }
    .element-container:has(#button-after) {
        display: none;
    }
    .element-container:has(#button-two) + div button{
        background-color: green;
        width:  200px;
        height: 200px;
    }
    .element-container:has(#button-after) + div button {
        background-color: orange;
        width:  200px;
        height: 200px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

col1, col2 = st.columns([1,1])
with col1:
    st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)
    st.button("My Button")
with col2:
    st.markdown('<span id="button-two"></span>', unsafe_allow_html=True)
    st.button("Some other button")


# st.write(st.experimental_user)