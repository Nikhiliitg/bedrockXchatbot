import boto3
import json
import streamlit as st 

# Initialize Bedrock client
bedrock_runtime = boto3.client("bedrock-runtime", region_name="us-east-1")

# Meta Llama 3 Model - Using Inference Profile ARN
model_arn = "arn:aws:bedrock:us-east-1:767398122823:inference-profile/us.meta.llama3-2-11b-instruct-v1:0"

def my_chatbot(language, user_text):
    # Meta Llama 3 expects a simple "prompt" field
    payload = {
        "prompt": f"You are an AI assistant. Respond in {language}.\n\nUser: {user_text}\nAssistant:",
        "temperature": 0.9,
        "max_gen_len": 512
    }

    # Invoke model
    response = bedrock_runtime.invoke_model(
        modelId=model_arn,  # Using your ARN
        body=json.dumps(payload),
        contentType="application/json",
        accept="application/json"
    )

    # Parse response
    response_body = json.loads(response["body"].read())

    # Extract response text
    output_message = response_body.get("generation", "")
    return output_message if output_message else "Error: No response from model."

# Streamlit UI
st.title("LLM Chatbot powered by Bedrock")

language = st.sidebar.selectbox("Language", ["English", "French", "German", "Spanish"])
user_text = st.sidebar.text_area(label="What is your question?", max_chars=1000)

if user_text:
    response = my_chatbot(language, user_text)
    st.write(response)
    
    ## this is using cross region inference
    