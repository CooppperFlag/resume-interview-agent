# 基于 RAG 的简历优化面试 Agent

基于 Dify + DeepSeek + RAG 构建的 AI Agent 实战项目。输入简历和目标岗位，自动生成优化后的简历和针对性模拟面试题。

## 架构

## 技术栈
- Agent 编排：Dify (本地 Docker 部署)
- LLM：DeepSeek / 通义千问
- Embedding：BAAI/bge-m3 (硅基流动)
- 知识库：92 道 AI Agent 面试题 (Markdown, RAG)
- 后端调用：Python + Requests

## 核心亮点
- **Query Rewriting**：用 LLM 把"岗位名称"改写成"面试题检索句"，解决语义不匹配导致检索为空的问题。
- **RAG 知识库**：接入 92 道 AI Agent 面试题，按 `###` 分段切块，检索 top-5 相关题目。
- **输出清洗**：用 Python 正则表达式去除推理模型的 <think> 思考标签，保证输出干净。
- **事实核查**：加入事实核查节点，防止大模型在优化简历时编造用户未提供的信息。

## 快速开始
1. 本地 Docker 启动 Dify：`cd D:\dify\dify-main\docker && docker compose up -d`
2. 在 Dify 后台导入工作流，配置 DeepSeek 和 bge-m3 模型
3. 安装依赖：`pip install requests`
4. 修改脚本里的 API_KEY
5. 运行：`python3 test_dify.py`

## 效果展示
<img width="721" height="1305" alt="image" src="https://github.com/user-attachments/assets/429944b4-3f41-4fe8-ab8d-f9b4c903ed35" />
<img width="1365" height="1184" alt="image" src="https://github.com/user-attachments/assets/78bc7a27-d054-483e-9eb0-740894d8e5e0" />
<img width="1386" height="1193" alt="image" src="https://github.com/user-attachments/assets/0ce783fe-ba63-410b-900d-b99406e54031" />


