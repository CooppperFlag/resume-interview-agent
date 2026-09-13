import requests
import json

# ====== 配置区 ======
API_KEY = "app-z8DMtmsiKDrXMHDjtoLl4Go0"   # 把引号里的内容换成你真实的Key
API_URL = "http://localhost/v1/workflows/run"

# 工作流输入变量
payload = {
    "inputs": {
        "resume_text": "张三，男，2025届本科，计算机专业，做过学生干部，参与过xx项目，会Java不会Python。",
        "target_position": "AI Agent 开发实习生"
    },
    "response_mode": "blocking",
    "user": "test_user_001"
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 发送请求
response = requests.post(API_URL, headers=headers, data=json.dumps(payload))

if response.status_code == 200:
    result = response.json()
    print("==== 调用成功 ====")
    
    # 1. 提取真正的内容（根据你截图里的结构，它在 data -> outputs -> result 里面）
    output_text = result["data"]["outputs"]["result"]
    
    # 2. 用正则把 <|think|>...</|think|> 以及里面的思考过程全部删掉
    import re
    clean_text = re.sub(r'<\|?think\|?>.*?<\|?/think\|?>', '', output_text, flags=re.DOTALL)
    # 如果有残留的标签，再暴力替换一下（防止格式不完全一样）
    clean_text = clean_text.replace('<|think|>', '').replace('<|/think|>', '')
    
    # 3. 直接打印处理后的文本（Python 会自动把 \n 变成换行）
    print(clean_text)
