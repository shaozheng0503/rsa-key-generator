#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
增强版 RSA 工具使用示例
演示各种功能的使用方法
"""

from enhanced_rsa_tool import EnhancedRSATool
import base64
import json

def demo_basic_operations():
    """演示基本操作"""
    print("="*60)
    print("RSA 工具基本操作演示")
    print("="*60)
    
    # 创建工具实例
    rsa_tool = EnhancedRSATool(2048)
    
    # 生成密钥对
    print("\n1. 生成 RSA 密钥对")
    rsa_tool.generate_key_pair()
    
    # 显示密钥信息
    print("\n2. 显示密钥信息")
    info = rsa_tool.get_key_info()
    print(f"密钥长度: {info['key_size']} 位")
    print(f"密钥指纹: {info['fingerprint']}")
    print(f"生成时间: {info['generated_time']}")
    
    # 导出密钥信息
    print("\n3. 导出密钥信息")
    rsa_tool.export_key_info("demo_key_info.json")
    
    # 创建备份
    print("\n4. 创建密钥备份")
    rsa_tool.create_key_backup("demo_backup")

def demo_digital_signature():
    """演示数字签名功能"""
    print("\n" + "="*60)
    print("数字签名功能演示")
    print("="*60)
    
    # 创建工具实例并加载密钥
    rsa_tool = EnhancedRSATool()
    if not rsa_tool.load_keys():
        print("请先生成密钥对")
        return
    
    # 要签名的消息
    message = "这是一个重要的消息，需要数字签名验证其完整性。"
    print(f"原始消息: {message}")
    
    # 生成签名
    print("\n1. 生成数字签名")
    signature = rsa_tool.sign_message(message, "demo_signature.bin")
    signature_b64 = base64.b64encode(signature).decode('utf-8')
    print(f"签名 (Base64): {signature_b64}")
    
    # 验证签名
    print("\n2. 验证数字签名")
    rsa_tool.verify_signature(message, signature)
    
    # 验证被篡改的消息
    print("\n3. 验证被篡改的消息")
    tampered_message = "这是一个被篡改的消息，需要数字签名验证其完整性。"
    rsa_tool.verify_signature(tampered_message, signature)

def demo_encryption_decryption():
    """演示加密解密功能"""
    print("\n" + "="*60)
    print("加密解密功能演示")
    print("="*60)
    
    # 创建工具实例并加载密钥
    rsa_tool = EnhancedRSATool()
    if not rsa_tool.load_keys():
        print("请先生成密钥对")
        return
    
    # 要加密的消息
    message = "这是一个需要加密的敏感信息。"
    print(f"原始消息: {message}")
    
    # 加密消息
    print("\n1. 使用公钥加密消息")
    encrypted = rsa_tool.encrypt_message(message)
    encrypted_b64 = base64.b64encode(encrypted).decode('utf-8')
    print(f"加密结果 (Base64): {encrypted_b64}")
    
    # 保存加密结果
    with open("demo_encrypted.txt", "w") as f:
        f.write(encrypted_b64)
    print("加密结果已保存到: demo_encrypted.txt")
    
    # 解密消息
    print("\n2. 使用私钥解密消息")
    decrypted = rsa_tool.decrypt_message(encrypted)
    print(f"解密结果: {decrypted}")
    
    # 验证解密结果
    if decrypted == message:
        print("✅ 加密解密成功！")
    else:
        print("❌ 加密解密失败！")

def demo_file_operations():
    """演示文件操作"""
    print("\n" + "="*60)
    print("文件操作演示")
    print("="*60)
    
    # 创建工具实例并加载密钥
    rsa_tool = EnhancedRSATool()
    if not rsa_tool.load_keys():
        print("请先生成密钥对")
        return
    
    # 创建测试文件
    test_content = """这是一个测试文件的内容。
包含多行文本信息。
用于演示文件签名和验证功能。
"""
    
    with open("test_file.txt", "w", encoding="utf-8") as f:
        f.write(test_content)
    
    print("1. 创建测试文件: test_file.txt")
    
    # 对文件进行签名
    print("\n2. 对文件进行数字签名")
    signature = rsa_tool.sign_message(test_content, "file_signature.bin")
    print("文件签名已保存到: file_signature.bin")
    
    # 验证文件签名
    print("\n3. 验证文件签名")
    rsa_tool.verify_signature(test_content, signature)
    
    # 模拟文件被篡改
    print("\n4. 模拟文件被篡改")
    tampered_content = test_content + "\n这是被添加的恶意内容。"
    rsa_tool.verify_signature(tampered_content, signature)

def demo_key_management():
    """演示密钥管理功能"""
    print("\n" + "="*60)
    print("密钥管理功能演示")
    print("="*60)
    
    # 创建工具实例
    rsa_tool = EnhancedRSATool(4096)  # 使用 4096 位密钥
    
    # 生成新密钥对
    print("1. 生成 4096 位 RSA 密钥对")
    rsa_tool.generate_key_pair("new_private.pem", "new_public.pem")
    
    # 显示密钥信息
    print("\n2. 显示新密钥信息")
    info = rsa_tool.get_key_info()
    print(json.dumps(info, indent=2, ensure_ascii=False))
    
    # 导出密钥信息
    print("\n3. 导出密钥信息")
    rsa_tool.export_key_info("new_key_info.json")
    
    # 创建备份
    print("\n4. 创建密钥备份")
    rsa_tool.create_key_backup("new_key_backup")

def main():
    """主演示函数"""
    print("增强版 RSA 工具功能演示")
    print("="*60)
    
    try:
        # 基本操作演示
        demo_basic_operations()
        
        # 数字签名演示
        demo_digital_signature()
        
        # 加密解密演示
        demo_encryption_decryption()
        
        # 文件操作演示
        demo_file_operations()
        
        # 密钥管理演示
        demo_key_management()
        
        print("\n" + "="*60)
        print("所有演示完成！")
        print("="*60)
        
    except Exception as e:
        print(f"演示过程中发生错误: {e}")

if __name__ == "__main__":
    main() 