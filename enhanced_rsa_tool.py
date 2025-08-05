#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
增强版 RSA 密钥管理工具
包含密钥生成、签名、验证、加密、解密等功能
"""

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
import os
import base64
import json
import argparse
from datetime import datetime
import hashlib

class EnhancedRSATool:
    """增强版 RSA 工具类"""
    
    def __init__(self, key_size=2048):
        self.key_size = key_size
        self.private_key = None
        self.public_key = None
    
    def generate_key_pair(self, save_to_file=True):
        """生成 RSA 密钥对"""
        print(f"正在生成 {self.key_size} 位的 RSA 密钥对...")
        
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=self.key_size,
            backend=default_backend()
        )
        
        self.public_key = self.private_key.public_key()
        
        if save_to_file:
            self.save_keys()
        
        print("RSA 密钥对生成成功！")
        return self.private_key, self.public_key
    
    def save_keys(self, private_filename="private_key.pem", public_filename="public_key.pem"):
        """保存密钥到文件"""
        # 保存私钥
        private_pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        
        with open(private_filename, 'wb') as f:
            f.write(private_pem)
        
        # 保存公钥
        public_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        
        with open(public_filename, 'wb') as f:
            f.write(public_pem)
        
        print(f"私钥已保存到: {private_filename}")
        print(f"公钥已保存到: {public_filename}")
    
    def load_keys(self, private_filename="private_key.pem", public_filename="public_key.pem"):
        """从文件加载密钥"""
        try:
            # 加载私钥
            with open(private_filename, 'rb') as f:
                private_data = f.read()
                self.private_key = serialization.load_pem_private_key(
                    private_data, password=None, backend=default_backend()
                )
            
            # 加载公钥
            with open(public_filename, 'rb') as f:
                public_data = f.read()
                self.public_key = serialization.load_pem_public_key(
                    public_data, backend=default_backend()
                )
            
            print("密钥加载成功！")
            return True
        except Exception as e:
            print(f"加载密钥失败: {e}")
            return False
    
    def sign_message(self, message, signature_filename=None):
        """对消息进行数字签名"""
        if not self.private_key:
            raise ValueError("请先加载私钥")
        
        # 计算消息的哈希值
        message_hash = hashlib.sha256(message.encode('utf-8')).digest()
        
        # 使用私钥签名
        signature = self.private_key.sign(
            message_hash,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        
        # 保存签名到文件
        if signature_filename:
            with open(signature_filename, 'wb') as f:
                f.write(signature)
            print(f"签名已保存到: {signature_filename}")
        
        return signature
    
    def verify_signature(self, message, signature, public_key=None):
        """验证数字签名"""
        if not public_key:
            public_key = self.public_key
        
        if not public_key:
            raise ValueError("请先加载公钥")
        
        try:
            # 计算消息的哈希值
            message_hash = hashlib.sha256(message.encode('utf-8')).digest()
            
            # 验证签名
            public_key.verify(
                signature,
                message_hash,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            
            print("✅ 签名验证成功！")
            return True
        except Exception as e:
            print(f"❌ 签名验证失败: {e}")
            return False
    
    def encrypt_message(self, message, public_key=None):
        """使用公钥加密消息"""
        if not public_key:
            public_key = self.public_key
        
        if not public_key:
            raise ValueError("请先加载公钥")
        
        # 加密消息
        encrypted = public_key.encrypt(
            message.encode('utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        return encrypted
    
    def decrypt_message(self, encrypted_message):
        """使用私钥解密消息"""
        if not self.private_key:
            raise ValueError("请先加载私钥")
        
        # 解密消息
        decrypted = self.private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
        return decrypted.decode('utf-8')
    
    def get_key_info(self):
        """获取密钥信息"""
        if not self.private_key:
            return None
        
        info = {
            "key_size": self.private_key.key_size,
            "public_exponent": self.private_key.public_key().public_numbers().e,
            "modulus": str(self.private_key.public_key().public_numbers().n),
            "public_key_base64": self.get_public_key_base64(),
            "fingerprint": self.get_key_fingerprint(),
            "generated_time": datetime.now().isoformat()
        }
        
        return info
    
    def get_public_key_base64(self):
        """获取 Base64 编码的公钥"""
        public_bytes = self.public_key.public_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return base64.b64encode(public_bytes).decode('utf-8')
    
    def get_key_fingerprint(self):
        """获取密钥指纹"""
        public_bytes = self.public_key.public_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return hashlib.sha256(public_bytes).hexdigest()
    
    def export_key_info(self, filename="key_info.json"):
        """导出密钥信息到 JSON 文件"""
        info = self.get_key_info()
        if info:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(info, f, indent=2, ensure_ascii=False)
            print(f"密钥信息已导出到: {filename}")
    
    def create_key_backup(self, backup_dir="key_backup"):
        """创建密钥备份"""
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # 备份私钥
        private_backup = os.path.join(backup_dir, f"private_key_{timestamp}.pem")
        private_pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        with open(private_backup, 'wb') as f:
            f.write(private_pem)
        
        # 备份公钥
        public_backup = os.path.join(backup_dir, f"public_key_{timestamp}.pem")
        public_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open(public_backup, 'wb') as f:
            f.write(public_pem)
        
        print(f"密钥备份已创建: {backup_dir}")

def main():
    """主函数 - 命令行界面"""
    parser = argparse.ArgumentParser(description="增强版 RSA 密钥管理工具")
    parser.add_argument("--action", choices=["generate", "sign", "verify", "encrypt", "decrypt", "info"], 
                       default="generate", help="执行的操作")
    parser.add_argument("--key-size", type=int, default=2048, help="密钥长度")
    parser.add_argument("--message", help="要签名/验证/加密/解密的消息")
    parser.add_argument("--signature-file", help="签名文件路径")
    parser.add_argument("--output", help="输出文件路径")
    
    args = parser.parse_args()
    
    rsa_tool = EnhancedRSATool(args.key_size)
    
    if args.action == "generate":
        rsa_tool.generate_key_pair()
        rsa_tool.export_key_info()
        rsa_tool.create_key_backup()
        
        # 显示密钥信息
        info = rsa_tool.get_key_info()
        print("\n" + "="*60)
        print("RSA 密钥信息")
        print("="*60)
        print(f"密钥长度: {info['key_size']} 位")
        print(f"密钥指纹: {info['fingerprint']}")
        print(f"生成时间: {info['generated_time']}")
        print(f"公钥 (Base64):")
        print(info['public_key_base64'])
        print("="*60)
    
    elif args.action == "sign":
        if not args.message:
            print("请提供要签名的消息")
            return
        
        if not rsa_tool.load_keys():
            return
        
        signature = rsa_tool.sign_message(args.message, args.signature_file)
        print(f"签名 (Base64): {base64.b64encode(signature).decode('utf-8')}")
    
    elif args.action == "verify":
        if not args.message or not args.signature_file:
            print("请提供消息和签名文件")
            return
        
        if not rsa_tool.load_keys():
            return
        
        with open(args.signature_file, 'rb') as f:
            signature = f.read()
        
        rsa_tool.verify_signature(args.message, signature)
    
    elif args.action == "encrypt":
        if not args.message:
            print("请提供要加密的消息")
            return
        
        if not rsa_tool.load_keys():
            return
        
        encrypted = rsa_tool.encrypt_message(args.message)
        encrypted_b64 = base64.b64encode(encrypted).decode('utf-8')
        
        if args.output:
            with open(args.output, 'w') as f:
                f.write(encrypted_b64)
            print(f"加密结果已保存到: {args.output}")
        else:
            print(f"加密结果 (Base64): {encrypted_b64}")
    
    elif args.action == "decrypt":
        if not args.message:
            print("请提供要解密的消息 (Base64 格式)")
            return
        
        if not rsa_tool.load_keys():
            return
        
        try:
            encrypted = base64.b64decode(args.message)
            decrypted = rsa_tool.decrypt_message(encrypted)
            
            if args.output:
                with open(args.output, 'w', encoding='utf-8') as f:
                    f.write(decrypted)
                print(f"解密结果已保存到: {args.output}")
            else:
                print(f"解密结果: {decrypted}")
        except Exception as e:
            print(f"解密失败: {e}")
    
    elif args.action == "info":
        if not rsa_tool.load_keys():
            return
        
        info = rsa_tool.get_key_info()
        print(json.dumps(info, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main() 