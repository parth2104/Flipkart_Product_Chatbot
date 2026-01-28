from setuptools import setup,find_packages   

with open("requirements.txt","r") as f:
    requirements=f.read().splitlines()

setup(
    name="Flipkart Chatbot",
    version="0.1",
    author="flipkart",
    packages=find_packages(),
    install_requires=requirements
)