import streamlit as st
from arxiv import Client, Search, SortCriterion
import requests

st.title("Arxiv Paper Downloader")

client = Client()

choice = st.radio("Choose one method", ["Download 10 most recent papers from a topic", "Download paper using reference id"], index=None)

if choice == "Download 10 most recent papers from a topic":
    topic = st.text_input("Enter topic name:")
    search = Search(query=topic, max_results=5, sort_by=SortCriterion.SubmittedDate)
    results = client.results(search)
    for r in results:
        st.write(r.title)
    download_choice = st.radio("Do you want to download paper:", ["Yes", "No"], index=None)
    # TODO: Download not working
    if download_choice == "Yes":
        for r in results:
            st.write(r.title)
            r.download_pdf(filename=f"{r.title}.pdf")
    
elif choice == "Download paper using reference id":
    reference_id = st.text_input("Enter reference id:")
    st.info("Url: https://arxiv.org/pdf/1804.07612. Only give 1804.07612 as reference id")
    download_choice = st.radio("Do you want to download paper:", ["Yes", "No"], index=None)
    if reference_id == "":
        st.warning("Enter reference id to proceed")
    else:
        search_by_id = Search(id_list=[reference_id])
    result = next(client.results(search_by_id))
    st.text(f"Topic: {result.title}")
    if download_choice == "Yes":
        result.download_pdf(filename=f"{result.title}.pdf")
    