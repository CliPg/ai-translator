# AI翻译助手 - 前端

基于 Flutter 开发的翻译助手移动应用

## 运行步骤

1. 确保已安装 Flutter：
   - 访问 https://flutter.dev/docs/get-started/install
   - 验证安装: `flutter doctor`

2. 安装依赖：
```bash
cd frontend
flutter pub get
```

3. 配置后端地址：

编辑 `lib/main.dart` 中的 `_baseUrl` 变量：
```dart
static const String _baseUrl = 'http://your-backend-url:8000';
```

4. 运行应用：
```bash
# 模拟器/设备
flutter run

# Web
flutter run -d chrome

# 桌面
flutter run -d macos  # macOS
flutter run -d windows  # Windows
flutter run -d linux  # Linux
```

## 功能说明

- 输入中文文本
- 点击翻译按钮
- 显示英文翻译结果
- 显示提取的关键词

## 注意事项

1. 确保后端服务已启动
2. 确认网络连接正常
3. 检查后端地址配置是否正确
