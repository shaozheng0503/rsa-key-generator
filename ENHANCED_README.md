# 增强版 RSA 密钥管理工具

这是一个功能完整的 RSA 密钥管理工具，不仅支持密钥生成，还包含数字签名、加密解密、密钥管理等高级功能。

## 🚀 新功能特性

### 核心功能
- **密钥生成**: 支持 2048/4096 位 RSA 密钥对生成
- **数字签名**: 使用 PSS 填充方案进行安全的数字签名
- **签名验证**: 验证消息的完整性和真实性
- **加密解密**: 使用 OAEP 填充方案进行安全的加密解密
- **密钥管理**: 完整的密钥生命周期管理

### 高级特性
- **密钥指纹**: 生成唯一的密钥指纹用于识别
- **密钥备份**: 自动创建带时间戳的密钥备份
- **信息导出**: 将密钥信息导出为 JSON 格式
- **命令行界面**: 支持命令行参数操作
- **文件操作**: 支持对文件进行签名和验证

## 📦 安装依赖

```bash
pip install cryptography
```

## 🛠️ 使用方法

### 1. 基本密钥生成

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

## 📚 编程接口使用

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

运行完整的功能演示：

```bash
python example_usage.py
```

这将演示所有功能，包括：
- 基本密钥操作
- 数字签名和验证
- 加密解密
- 文件操作
- 密钥管理

## 📁 输出文件说明

### 生成的文件
- `private_key.pem` - RSA 私钥文件
- `public_key.pem` - RSA 公钥文件
- `key_info.json` - 密钥信息文件
- `key_backup/` - 密钥备份目录
- `demo_signature.bin` - 数字签名文件
- `demo_encrypted.txt` - 加密结果文件

### 安全注意事项
- 私钥文件包含敏感信息，请妥善保管
- 不要将私钥文件上传到公共仓库
- 建议定期备份密钥文件
- 使用强密码保护私钥文件

## 🔒 安全特性

### 算法选择
- **签名算法**: RSA-PSS with SHA-256
- **加密算法**: RSA-OAEP with SHA-256
- **密钥长度**: 支持 2048/4096 位
- **填充方案**: 使用安全的填充方案

### 最佳实践
- 使用 2048 位或更长的密钥
- 定期轮换密钥
- 安全存储私钥
- 验证公钥的真实性

## 🧪 测试

运行测试示例：

```bash
# 基本功能测试
python example_usage.py

# 命令行功能测试
python enhanced_rsa_tool.py --action generate
python enhanced_rsa_tool.py --action sign --message "测试消息"
python enhanced_rsa_tool.py --action verify --message "测试消息" --signature-file demo_signature.bin
```

## 📈 性能优化建议

### 密钥长度选择
- **2048 位**: 适合一般用途，性能较好
- **4096 位**: 适合高安全要求，性能稍慢

### 批量操作
- 对于大量文件，建议批量处理
- 使用多线程处理可以提高性能

## 🔮 未来扩展计划

- [ ] 支持 ECC 密钥
- [ ] 添加密钥轮换功能
- [ ] 支持硬件安全模块 (HSM)
- [ ] 添加 Web 界面
- [ ] 支持更多加密算法
- [ ] 添加密钥恢复功能

## 🤝 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目！

## 📄 许可证

本项目采用 MIT 许可证。

## 📞 支持

如果您遇到问题或有建议，请创建 Issue 或联系维护者。 