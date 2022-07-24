import streamlit as st

def predictOddEven(number):
    result=""
    if(number%2==0):
        result="EVEN"
    else:
        result="ODD"

    print(result)
    return result

def main():
    st.title("Predict Odd or Even!")
    html_temp="""
        <div class="div"><h1>Even or Odd</h1>
        <p>Input the number to check whether it is even or odd!</p>
        </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    number=st.text_input("Enter the Number",)
    result=""

    if st.button("Submit"):
        result=predictOddEven(int(number))

    st.success("The number is : {}".format(result))

if __name__=="__main__":
    main()