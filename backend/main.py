from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import jieba
import jieba.analyse
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI翻译助手")

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TranslateRequest(BaseModel):
    text: str


class TranslateResponse(BaseModel):
    translation: str
    keywords: list[str]


async def call_qiwen_api(text: str) -> str:
    """调用通义千问API进行翻译"""
    api_key = os.getenv("QIWEN_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="API密钥未配置")

    api_url = os.getenv("QIWEN_API_URL")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "qwen-plus",
        "messages": [
            {
                "role": "system",
                "content": "你是一个专业的翻译助手，请将中文翻译成英文。只返回翻译结果，不要有其他解释。",
            },
            {"role": "user", "content": text},
        ],
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.post(api_url, json=payload, headers=headers)
            response.raise_for_status()
            result = response.json()
            translation = result["choices"][0]["message"]["content"].strip()
            return translation
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"API调用失败: {str(e)}")


def extract_keywords(text: str, top_k: int = 3) -> list[str]:
    """使用jieba提取关键词"""
    keywords = jieba.analyse.extract_tags(text, topK=top_k)
    return keywords


@app.post("/translate", response_model=TranslateResponse)
async def translate(request: TranslateRequest):
    """翻译接口"""
    if not request.text or not request.text.strip():
        raise HTTPException(status_code=400, detail="输入文本不能为空")

    # 调用通义千问API进行翻译
    translation = await call_qiwen_api(request.text)

    # 使用jieba提取关键词
    keywords = extract_keywords(request.text)

    return TranslateResponse(translation=translation, keywords=keywords)


@app.get("/")
async def root():
    """健康检查"""
    return {"message": "AI翻译助手API运行中"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
