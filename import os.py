import os
import streamlit as st
import openai

# 获取API密钥
api_key = os.environ.get("OPENAI_API_KEY")

# 设置API密钥
openai.api_key = api_key

# 定义OpenAI GPT模型调用函数
def generate_text(industry, category, style):
    prompt = (f"在{industry}行业中的{category}领域，以{style}的方式，我想要一个创业点子。")

    # 设置请求参数
    completions = openai.Completion.create(
        engine="davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # 获取文本
    message = completions.choices[0].text.strip()

    return message

# 定义Streamlit应用程序
def app():
    st.title("创业点子生成器")

    # 设置行业选择列表
    industries = [
        "科技",
        "金融",
        "教育",
        "医疗",
        "零售",
        "制造",
        "娱乐",
        "餐饮",
        "旅游",
        "房地产",
        "能源",
        "体育",
        "农业",
        "艺术",
        "公益",
        "其他",
    ]

    # 设置类别选择列表
    categories = [
        "供应链",
        "物流",
        "销售",
        "营销",
        "人力资源",
        "财务",
        "法律",
        "IT",
        "产品",
        "设计",
        "客户服务",
        "研发",
        "其他",
    ]

    # 设置风格选择列表
    styles = [
        "幽默",
        "正式",
        "专业",
        "潮流",
        "时尚",
        "艺术",
        "创新",
        "实用",
        "科技感",
        "清新",
        "其他",
    ]

    # 显示选择列表
    industry = st.selectbox("请选择行业", industries)
    category = st.selectbox("请选择类别", categories)
    style = st.selectbox("请选择风格", styles)

    # 生成文本
    message = generate_text(industry, category, style)

    # 显示生成的文本
    st.write("以下是您的创业点子：")
    st.write(message)

if __name__ == "__main__":
    app()
