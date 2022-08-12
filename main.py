
import streamlit as st
import numbersystem as ns

with open ("style.css") as f :
    st.markdown( f'<style>{f.read()}</style>',unsafe_allow_html=True)

global info_num,info,data_source,info_source
info_num=0

st.header("Number System Converter")
col1,col2=st.columns(2)

data_source=col1.selectbox("From",["Binary","Octal","Decimal","Hexa"])
info_source=col2.selectbox("To",["Decimal","Octal","Binary","Hexa"])

data=col1.text_input("Number")


def convert(data):
    global data_source,info_source
    info=col1.header(info_num)
    
    info.empty()
    atri=ns.binaryToDecimal
    if data_source=="Decimal":
        if info_source=="Binary":
            atri=ns.decimalToBinary
            originalFormat="Binary"

        elif info_source=="Octal" :
            atri=ns.decimalToOctal  
            originalFormat="Octal" 

        elif info_source=="Hexa" :   
            atri=ns.decimalToHexa
            orinalFormat="Hexa"

    elif data_source=="Binary":
        if info_source=="Decimal":
            atri=ns.binaryToDecimal
            originalFormat="Decimal"

        elif info_source=="Octal" :
            originalFormat="Octal" 
            atri=ns.binaryToOctal  

        elif info_source=="Hexa" :   
            atri=ns.binaryToHexa
            originalFormat="Hexa"

    elif data_source=="Octal":
        if info_source=="Binary":
            atri=ns.octalToBinary
            originalFormat="Binary"

        elif info_source=="Decimal" :
            atri=ns.octalToDecimal  
            originalFormat="Decimal" 

        elif info_source=="Hexa" :   
            atri=ns.octalToHexa
            originalFormat="Hexa"

    elif data_source=="Hexa":
        if info_source=="Binary":
            atri=ns.hexaToBinary
            originalFormat="Binary"

        elif info_source=="Octal" :
            atri=ns.hexaToOctal  
            originalFormat="Octal"  

        elif info_source=="Decimal" :   
            atri=ns.hexaToDecimal
            originalFormat="Decimal"
    try:
        answer=atri(data)
        info=col1.header("{} - {}".format(originalFormat,answer))
        
    except:
        info=col1.header("Enter a number")
convert_btn=st.button(label='Convert',on_click=convert(data))