import openai
import streamlit as st

# 在OpenAI平台上设置您的API密钥
openai.api_key = "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"

# 定义您要使用的GPT模型的引擎ID
engine_id = "davinci-003"


# 定义可供选择的选项列表
industries = [
    "Healthcare",
    "Technology",
    "Retail",
    "Finance",
    "Education",
    "Entertainment",
    "Real Estate",
    "Food and Beverage",
    "Travel and Tourism",
    "Fashion",
    "Automotive",
    "Energy",
    "Sports",
    "Marketing",
    "Media",
    "Construction",
    "Agriculture",
    "Telecommunications",
    "Government",
    "Nonprofit",
]

parts = [
    "Supply Chain",
    "Storefront",
    "Marketing",
    "Product Development",
    "Customer Service",
    "Operations",
    "Finance",
    "Human Resources",
    "Sales",
    "Distribution",
    "Research and Development",
    "Logistics",
    "Legal",
    "Information Technology",
    "Quality Control",
    "Public Relations",
    "Administration",
    "Purchasing",
    "Training and Development",
    "Facilities Management",
]

styles = [
    "Humorous",
    "Professional",
    "Trendy",
    "Classic",
    "Modern",
    "Elegant",
    "Casual",
    "Playful",
    "Sophisticated",
    "Edgy",
    "Bold",
    "Minimalist",
    "Luxurious",
    "Rustic",
    "Vintage",
    "Futuristic",
    "Whimsical",
    "Gothic",
    "Ethnic",
    "Nautical",
]

# 创建Streamlit应用程序的界面
st.title("Startup Idea Generator")

# 添加下拉列表作为选项
industry = st.selectbox("Select an industry", industries)
part = st.selectbox("Select a part of the industry", parts)
style = st.selectbox("Select a style", styles)

# 添加按钮以生成创业点子
if st.button("Generate Idea"):
    # 根据用户的选择生成创业点子
    prompt = f"As a {style} {part} in the {industry} industry, I want to create a startup that..."
    response = openai.Completion.create(
        engine=engine_id,
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # 获取OpenAI的响应并在屏幕上显示它
    idea = response.choices[0].text.strip()
    existing_ideas = st.session_state.get("generated_ideas", [])
    while idea in existing_ideas:
        response = openai.Completion.create(
            engine=engine_id,
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.5,
        )
        idea = response.choices[0].text.strip()
    existing_ideas.append(idea)
    st.session_state["generated_ideas"] = existing_ideas
    st.write("Your startup idea is:", idea)
