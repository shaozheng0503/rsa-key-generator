#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RSA 密钥生成器
生成 RSA 密钥对并保存公钥到文件
"""

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
import os
import base64

def generate_rsa_key_pair(key_size=2048):
    """
    生成 RSA 密钥对
    
    Args:
        key_size (int): 密钥长度，默认 2048 位
    
    Returns:
        tuple: (private_key, public_key)
    """
    print(f"正在生成 {key_size} 位的 RSA 密钥对...")
    
    # 生成私钥
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
        backend=default_backend()
    )
    
    # 获取公钥
    public_key = private_key.public_key()
    
    print("RSA 密钥对生成成功！")
    return private_key, public_key

def save_private_key(private_key, filename="private_key.pem"):
    """
    保存私钥到文件
    
    Args:
        private_key: RSA 私钥对象
        filename (str): 私钥文件名
    """
    # 将私钥序列化为 PEM 格式
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    
    # 保存到文件
    with open(filename, 'wb') as f:
        f.write(pem)
    
    print(f"私钥已保存到: {filename}")

def save_public_key(public_key, filename="public_key.pem"):
    """
    保存公钥到文件
    
    Args:
        public_key: RSA 公钥对象
        filename (str): 公钥文件名
    """
    # 将公钥序列化为 PEM 格式
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    # 保存到文件
    with open(filename, 'wb') as f:
        f.write(pem)
    
    print(f"公钥已保存到: {filename}")

def get_public_key_base64(public_key):
    """
    获取 Base64 编码的公钥
    
    Args:
        public_key: RSA 公钥对象
    
    Returns:
        str: Base64 编码的公钥
    """
    # 获取公钥的原始字节
    public_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    # 转换为 Base64
    return base64.b64encode(public_bytes).decode('utf-8')

def display_key_info(private_key, public_key):
    """
    显示密钥信息
    
    Args:
        private_key: RSA 私钥对象
        public_key: RSA 公钥对象
    """
    print("\n" + "="*50)
    print("RSA 密钥信息")
    print("="*50)
    
    # 获取密钥大小
    key_size = private_key.key_size
    print(f"密钥长度: {key_size} 位")
    
    # 获取公钥的 Base64 编码
    public_key_b64 = get_public_key_base64(public_key)
    print(f"公钥 (Base64):")
    print(public_key_b64)
    
    # 获取公钥的十六进制表示
    public_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.DER,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    public_hex = public_bytes.hex()
    print(f"\n公钥 (十六进制):")
    print(public_hex)
    
    print("="*50)

def main():
    """主函数"""
    print("RSA 密钥生成器")
    print("="*30)
    
    try:
        # 生成密钥对
        private_key, public_key = generate_rsa_key_pair()
        
        # 保存密钥到文件
        save_private_key(private_key)
        save_public_key(public_key)
        
        # 显示密钥信息
        display_key_info(private_key, public_key)
        
        print("\n密钥生成完成！")
        print("请妥善保管私钥文件，不要泄露给他人。")
        print("公钥可以安全地分享给需要验证您签名的用户。")
        
    except Exception as e:
        print(f"生成密钥时发生错误: {e}")

if __name__ == "__main__":
    main() 