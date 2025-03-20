# BedrockXChatbot: AI Chatbot Powered by Amazon Bedrock & Meta Llama 3

## 🚀 Overview
BedrockXChatbot is a **small but impactful** AI-powered chatbot that utilizes **Amazon Bedrock** and **Meta Llama 3 (11B)** to provide intelligent, real-time responses. This project demonstrates how to efficiently deploy LLMs using Bedrock's inference capabilities while addressing cross-region inference challenges.

## 🎯 Features
- **Amazon Bedrock-powered LLM**: Uses Meta Llama 3 (11B) for AI-driven conversations.
- **Streamlit UI**: Simple and interactive frontend for user interaction.
- **Multi-language support**: English, French, German, and Spanish.
- **Optimized inference**: Efficient API calls with correct payload formatting.
- **Cross-region inference guide**: Step-by-step instructions for deploying models across AWS regions.

---

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Nikhiliitg/bedrockXchatbot.git
cd bedrockXchatbot
```

### 2️⃣ Set Up a Virtual Environment (Optional but Recommended)
```sh
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Configure AWS Credentials
Ensure you have the necessary permissions for Amazon Bedrock and that AWS credentials are configured:
```sh
aws configure
```
Or set them as environment variables:
```sh
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_REGION=us-east-1
```

### 5️⃣ Run the Chatbot
```sh
streamlit run app.py
```

---

## 🚀 Cross-Region Inference Setup
Many users face **cross-region inference issues** when using Amazon Bedrock. Follow these steps to ensure smooth execution:

1️⃣ **Go to AWS Bedrock Console** → **Inference and Assessment**
2️⃣ **Enable Cross-Region Inference**
3️⃣ **Copy the ARN** of your required model
4️⃣ **Replace the model ARN in `app.py`**

```python
model_arn = "arn:aws:bedrock:us-east-1:767398122823:inference-profile/us.meta.llama3-2-11b-instruct-v1:0"
```

That’s it! You are now ready to use Meta Llama 3 efficiently across regions. 🚀

---

## 📌 Future Enhancements
- **Add memory to maintain conversation history**
- **Improve UI/UX with a more dynamic frontend**
- **Enable RAG (Retrieval-Augmented Generation) for better responses**
- **Deploy using AWS Lambda & API Gateway for serverless execution**

---

## 🤝 Contributing
Contributions are welcome! Feel free to fork this repo and submit a PR. If you find issues or have feature suggestions, open a GitHub Issue.

---

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).

---

## 🔗 Connect
- **LinkedIn**: [https://www.linkedin.com/in/nikhildeka/](#)
- **GitHub**: [Nikhiliitg](https://github.com/Nikhiliitg)

🔥 Hope you find this project useful! If you do, consider **starring ⭐ the repo** and sharing it with others! 🚀

