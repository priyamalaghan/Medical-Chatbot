from setuptools import setup, find_packages

setup(
    name="medical_chatbot", 
    version="0.1.0",
    author="Priya Malaghan",
    description="A Medical Chatbot using LLMs, LangChain, Pinecone, Flask and AWS",
    author_email="priyankamalaghan191@gmail.com",
    packages=find_packages(), #find __init__.py files and install the folder as local package
    install_requires=[]
)