# AI翻译助手

基于 FastAPI + 通义千问 + Flutter 的智能翻译应用

## 项目结构

```
translator-helper/
├── backend/                # 后端服务
│   ├── main.py            # FastAPI 应用入口
│   ├── requirements.txt   # Python 依赖
│   ├── .env.example       # 环境变量示例
│   └── README.md          # 后端文档
└── frontend/              # 前端应用
    ├── lib/
    │   └── main.dart      # Flutter 应用入口
    ├── pubspec.yaml       # Flutter 依赖
    └── README.md          # 前端文档
```

## 快速开始

### 1. 后端配置

```bash
cd backend

# 安装依赖
pip install -r requirements.txt

# 配置 API 密钥
cp .env.example .env
# 编辑 .env 文件，填入通义千问 API Key

# 启动服务
python main.py
```

后端将运行在 `http://localhost:8000`

### 2. 前端运行

```bash
cd frontend

# 安装依赖
flutter pub get

# 运行应用
flutter run -d chrome
```

## 功能特性

- **智能翻译**: 使用通义千问大模型进行高质量中英翻译
- **关键词提取**: 基于 jieba 分词提取文本关键词
- **简洁界面**: Flutter 实现的现代化移动端界面
- **RESTful API**: 标准的 HTTP 接口设计

## API 接口

### POST /translate

请求示例：
```bash
curl -X POST http://localhost:8000/translate \
  -H "Content-Type: application/json" \
  -d '{"text": "你好，世界"}'
```

响应示例：
```json
{
  "translation": "Hello, world",
  "keywords": ["你好", "世界"]
}
```

## 技术栈

### 后端
- FastAPI - 现代 Python Web 框架
- 通义千问 API - 阿里云大语言模型
- jieba - 中文分词工具
- httpx - 异步 HTTP 客户端

### 前端
- Flutter - 跨平台 UI 框架
- http - HTTP 请求库

## 注意事项

1. 需要申请通义千问 API 密钥：https://dashscope.aliyuncs.com/
2. 确保后端服务运行在前端访问的地址上
3. Flutter 可运行在 iOS/Android/Web/Desktop 多平台
