# 🔐 RSA 密钥生成器

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/shaozheng0503/rsa-key-generator.svg)](https://github.com/shaozheng0503/rsa-key-generator/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/shaozheng0503/rsa-key-generator.svg)](https://github.com/shaozheng0503/rsa-key-generator/network)

一个功能完整的 RSA 密钥管理工具，支持密钥生成、数字签名、加密解密等高级功能。从简单的密钥生成器发展成为了一个专业的密码学工具箱。

## ✨ 功能特性

### 🔑 核心功能
- **RSA 密钥生成** - 支持 2048/4096 位密钥对生成
- **数字签名** - 使用 RSA-PSS 算法进行安全签名
- **签名验证** - 验证消息完整性和真实性
- **加密解密** - 使用 RSA-OAEP 算法进行安全加密
- **密钥管理** - 完整的密钥生命周期管理

### 🛡️ 高级特性
- **密钥指纹** - 生成唯一密钥标识
- **自动备份** - 带时间戳的密钥备份
- **信息导出** - JSON 格式的密钥信息
- **命令行界面** - 支持多种操作模式
- **文件操作** - 支持文件签名和验证
- **错误处理** - 完善的异常管理机制

## 🚀 快速开始

### 安装依赖

```bash
pip install cryptography
```

### 基本使用

```bash
# 生成 RSA 密钥对
python generate_rsa_key.py

# 使用增强版工具
python enhanced_rsa_tool.py --action generate
```

## 📦 安装

### 方法一：直接下载

```bash
git clone https://github.com/shaozheng0503/rsa-key-generator.git
cd rsa-key-generator
pip install -r requirements.txt
```

### 方法二：从源码安装

```bash
git clone https://github.com/shaozheng0503/rsa-key-generator.git
cd rsa-key-generator
pip install -e .
```

## 🛠️ 使用方法

### 1. 基础密钥生成

```bash
# 生成 2048 位 RSA 密钥对
python enhanced_rsa_tool.py --action generate

# 生成 4096 位 RSA 密钥对
python enhanced_rsa_tool.py --action generate --key-size 4096
```

### 2. 数字签名

```bash
# 对消息进行签名
python enhanced_rsa_tool.py --action sign --message "要签名的消息"

# 对消息进行签名并保存到文件
python enhanced_rsa_tool.py --action sign --message "要签名的消息" --signature-file signature.bin
```

### 3. 签名验证

```bash
# 验证签名
python enhanced_rsa_tool.py --action verify --message "原始消息" --signature-file signature.bin
```

### 4. 加密解密

```bash
# 加密消息
python enhanced_rsa_tool.py --action encrypt --message "要加密的消息" --output encrypted.txt

# 解密消息
python enhanced_rsa_tool.py --action decrypt --message "Base64编码的加密消息" --output decrypted.txt
```

### 5. 密钥信息

```bash
# 显示密钥信息
python enhanced_rsa_tool.py --action info
```

## 📚 编程接口

### 基本使用

```python
from enhanced_rsa_tool import EnhancedRSATool

# 创建工具实例
rsa_tool = EnhancedRSATool(2048)

# 生成密钥对
rsa_tool.generate_key_pair()

# 获取密钥信息
info = rsa_tool.get_key_info()
print(f"密钥长度: {info['key_size']} 位")
print(f"密钥指纹: {info['fingerprint']}")
```

### 数字签名

```python
# 对消息进行签名
message = "重要的消息内容"
signature = rsa_tool.sign_message(message, "signature.bin")

# 验证签名
is_valid = rsa_tool.verify_signature(message, signature)
print("签名验证:", "成功" if is_valid else "失败")
```

### 加密解密

```python
# 加密消息
message = "敏感信息"
encrypted = rsa_tool.encrypt_message(message)

# 解密消息
decrypted = rsa_tool.decrypt_message(encrypted)
print(f"解密结果: {decrypted}")
```

### 密钥管理

```python
# 导出密钥信息
rsa_tool.export_key_info("key_info.json")

# 创建密钥备份
rsa_tool.create_key_backup("backup_dir")

# 加载现有密钥
rsa_tool.load_keys("my_private.pem", "my_public.pem")
```

## 🔧 运行示例

### 完整功能演示

```bash
python example_usage.py
```

这将演示所有功能，包括：
- 基本密钥操作
- 数字签名和验证
- 加密解密
- 文件操作
- 密钥管理

### 运行测试

```bash
python test_rsa_tool.py
```

## 📁 项目结构

```
rsa-key-generator/
├── generate_rsa_key.py          # 基础 RSA 密钥生成器
├── enhanced_rsa_tool.py         # 增强版 RSA 工具
├── example_usage.py             # 使用示例
├── test_rsa_tool.py             # 测试套件
├── setup.py                     # 项目配置文件
├── requirements.txt             # 依赖包列表
├── README.md                    # 项目说明文档
├── ENHANCED_README.md           # 增强版功能说明
├── .github/workflows/           # GitHub Actions 工作流
│   └── test.yml
└── .gitignore                   # Git 忽略文件
```

## 📊 性能基准

根据测试结果：

| 操作 | 2048 位密钥 | 4096 位密钥 |
|------|-------------|-------------|
| 密钥生成 | ~0.12 秒 | ~0.45 秒 |
| 数字签名 | ~0.001 秒 | ~0.003 秒 |
| 签名验证 | ~0.000 秒 | ~0.001 秒 |
| 加密 | ~0.000 秒 | ~0.001 秒 |
| 解密 | ~0.001 秒 | ~0.002 秒 |

## 🔒 安全特性

### 算法选择
- **签名算法**: RSA-PSS with SHA-256
- **加密算法**: RSA-OAEP with SHA-256
- **密钥长度**: 支持 2048/4096 位
- **填充方案**: 使用安全的填充方案

### 安全最佳实践
- 使用 2048 位或更长的密钥
- 定期轮换密钥
- 安全存储私钥
- 验证公钥的真实性
- 使用强密码保护私钥

## 🧪 测试

### 运行所有测试

```bash
python test_rsa_tool.py
```

### 测试覆盖范围

- ✅ 密钥生成测试
- ✅ 密钥保存和加载测试
- ✅ 数字签名测试
- ✅ 加密解密测试
- ✅ 密钥信息测试
- ✅ 密钥备份测试
- ✅ 文件操作测试
- ✅ 错误处理测试
- ✅ 性能测试

## 📈 使用场景

### 软件开发
- API 安全认证
- 软件包签名验证
- 代码完整性检查

### 系统管理
- 服务器密钥管理
- 配置文件加密
- 日志文件签名

### 安全通信
- 消息加密传输
- 数字证书管理
- 安全协议实现

## 🤝 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目！

### 贡献指南

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

### 开发环境设置

```bash
# 克隆仓库
git clone https://github.com/shaozheng0503/rsa-key-generator.git
cd rsa-key-generator

# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
python test_rsa_tool.py
```

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- [cryptography](https://cryptography.io/) - 强大的密码学库
- [Python](https://www.python.org/) - 优秀的编程语言
- [GitHub](https://github.com/) - 代码托管平台

## 📞 支持

如果您遇到问题或有建议，请：

1. 查看 [Issues](https://github.com/shaozheng0503/rsa-key-generator/issues)
2. 创建新的 Issue
3. 联系维护者

## 🔮 路线图

- [ ] 支持 ECC 密钥
- [ ] 添加密钥轮换功能
- [ ] 支持硬件安全模块 (HSM)
- [ ] 添加 Web 界面
- [ ] 支持更多加密算法
- [ ] 添加密钥恢复功能
- [ ] 支持分布式密钥管理
- [ ] 添加审计日志功能

---

⭐ 如果这个项目对您有帮助，请给它一个星标！ 