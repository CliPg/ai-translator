# AI翻译助手 - 后端

基于 FastAPI + 通义千问的翻译服务

## 配置步骤

1. 安装依赖：
```bash
cd backend
pip install -r requirements.txt
```

2. 配置 API 密钥：
```bash
cp .env.example .env
```

编辑 `.env` 文件，填入你的通义千问 API 密钥：
```
QIWEN_API_KEY=your_actual_api_key_here
```

3. 启动服务：
```bash
python main.py
```

或使用 uvicorn：
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## API 接口

### POST /translate

**请求：**
```json
{
  "text": "要翻译的中文内容"
}
```

**响应：**
```json
{
  "translation": "英文翻译结果",
  "keywords": ["关键词1", "关键词2", "关键词3"]
}
```

## 获取通义千问 API 密钥

访问 https://dashscope.aliyuncs.com/ 注册并获取 API Key
