import streamlit as st
import openai

# Set up OpenAI credentials
openai.api_key = "YOUR_OPENAI_API_KEY"

# Initialize context
context = ""

# Main Streamlit app
def main():
    st.title("Question Answering with LangChain")

    # Input question
    question = st.text_input("Enter your question")

    # Display previous context
    st.subheader("Context:")
    st.write(context)

    # Button to add context
    if st.button("Add Context"):
        new_context = st.text_area("Enter additional context")
        update_context(new_context)

    # Button to clear context
    if st.button("Clear Context"):
        clear_context()

    # Button to get answer
    if st.button("Get Answer"):
        if not context:
            st.warning("Please provide some context.")
        elif not question:
            st.warning("Please enter a question.")
        else:
            answer = generate_answer(question)
            st.subheader("Answer:")
            st.write(answer)

# Function to update context
def update_context(new_context):
    global context
    context += new_context + "\n"

# Function to clear context
def clear_context():
    global context
    context = ""

# Function to generate answer using OpenAI API
def generate_answer(question):
    prompt = context + "Question: " + question + "\nAnswer:"
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
        temperature=0.7
    )
    answer = response.choices[0].text.strip().replace("Answer:", "")
    return answer

if __name__ == "__main__":
    main()

# This code sets up a Streamlit application with input fields for the question and context. The user can add or clear context, and upon clicking the "Get Answer" button, the application sends the question and context to the OpenAI Language API to generate an answer. The generated answer is then displayed on the Streamlit app.

# Note that this is a basic example, and you may need to modify and customize it further based on your specific requirements. Additionally, please be mindful of the OpenAI API usage and billing policies when implementing such applications.
