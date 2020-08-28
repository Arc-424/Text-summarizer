import streamlit as st
from gensim.summarization import summarize
import spacy
import spacy_streamlit
nlp = spacy.load('en_core_web_sm')

#custom funtion 
def summary(text):
    return summarize(text)

def main():
    st.title("Text Summarizer App")
    activites = ["Summary","Tokenizer","About"]
    choice = st.sidebar.selectbox("Select Activity",activites)
    if choice == "Summary":
        text = st.text_area("Input Text For Summary",height=300)
        if st.button("summarize"):
            st.success(summary(text))
        text_range= st.sidebar.slider("Summarize words Range",25,500)
        text = st.text_area("Input Text For Summary",height=250)
        if st.button("summarize1"):
            st.warning(summarize(text,word_count=text_range))
    # Tokenizer 
    elif choice == "Tokenizer":
        row_data = st.text_area("write Text For Tokenizer")
        docx= nlp(row_data)
        if st.button("Tokenizer"):
            spacy_streamlit.visualize_tokens(docx,attrs=['text','pos_','dep_','ent_type_'])
        if st.button("NER"):
            spacy_streamlit.visualize_ner(docx,labels=nlp.get_pipe('ner').labels)
        if st.button("Text Relationship"):
            spacy_streamlit.visualize_parser(docx)
        
    
            
        
        
            
        
    
    
    
    
    
if __name__ == '__main__':
    main()

