# chatbot_deepseek.py
# 简单 DeepSeek Chatbot 示例
# 功能：发送问题 → 调用 API → 打印回复

from openai import OpenAI

def deepseek_chatbot(question: str) -> str:
    # 兼容 OpenAI 接口的 DeepSeek 配置
    client = OpenAI(
        api_key="your-deepseek-api-key",  # 替换成你自己的 API Key
        base_url="https://api.deepseek.com"
    )

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": question}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    # 示例调用
    user_question = "请简单介绍 Transformer 模型"
    answer = deepseek_chatbot(user_question)

    print("用户问题：", user_question)
    print("模型回答：", answer)
