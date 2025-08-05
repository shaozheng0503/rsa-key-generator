#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RSA 工具测试套件
测试所有功能的正确性和安全性
"""

import unittest
import tempfile
import os
import json
import base64
from enhanced_rsa_tool import EnhancedRSATool

class TestEnhancedRSATool(unittest.TestCase):
    """增强版 RSA 工具测试类"""
    
    def setUp(self):
        """测试前的准备工作"""
        self.temp_dir = tempfile.mkdtemp()
        self.rsa_tool = EnhancedRSATool(2048)
        
    def tearDown(self):
        """测试后的清理工作"""
        # 清理临时文件
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)
    
    def test_key_generation(self):
        """测试密钥生成功能"""
        print("\n测试密钥生成...")
        
        # 生成密钥对
        private_key, public_key = self.rsa_tool.generate_key_pair(save_to_file=False)
        
        # 验证密钥对象
        self.assertIsNotNone(private_key)
        self.assertIsNotNone(public_key)
        self.assertEqual(private_key.key_size, 2048)
        self.assertEqual(public_key.key_size, 2048)
        
        print("✅ 密钥生成测试通过")
    
    def test_key_save_and_load(self):
        """测试密钥保存和加载功能"""
        print("\n测试密钥保存和加载...")
        
        # 生成并保存密钥
        private_file = os.path.join(self.temp_dir, "test_private.pem")
        public_file = os.path.join(self.temp_dir, "test_public.pem")
        
        self.rsa_tool.generate_key_pair(save_to_file=False)
        self.rsa_tool.save_keys(private_file, public_file)
        
        # 验证文件存在
        self.assertTrue(os.path.exists(private_file))
        self.assertTrue(os.path.exists(public_file))
        
        # 创建新实例并加载密钥
        new_tool = EnhancedRSATool()
        success = new_tool.load_keys(private_file, public_file)
        
        self.assertTrue(success)
        self.assertIsNotNone(new_tool.private_key)
        self.assertIsNotNone(new_tool.public_key)
        
        print("✅ 密钥保存和加载测试通过")
    
    def test_digital_signature(self):
        """测试数字签名功能"""
        print("\n测试数字签名...")
        
        # 生成密钥
        self.rsa_tool.generate_key_pair(save_to_file=False)
        
        # 测试消息
        test_message = "这是一个测试消息，用于验证数字签名功能。"
        
        # 生成签名
        signature = self.rsa_tool.sign_message(test_message)
        self.assertIsNotNone(signature)
        self.assertGreater(len(signature), 0)
        
        # 验证签名
        is_valid = self.rsa_tool.verify_signature(test_message, signature)
        self.assertTrue(is_valid)
        
        # 测试被篡改的消息
        tampered_message = "这是一个被篡改的消息，用于验证数字签名功能。"
        is_valid = self.rsa_tool.verify_signature(tampered_message, signature)
        self.assertFalse(is_valid)
        
        print("✅ 数字签名测试通过")
    
    def test_encryption_decryption(self):
        """测试加密解密功能"""
        print("\n测试加密解密...")
        
        # 生成密钥
        self.rsa_tool.generate_key_pair(save_to_file=False)
        
        # 测试消息
        original_message = "这是一个需要加密的敏感信息。"
        
        # 加密消息
        encrypted = self.rsa_tool.encrypt_message(original_message)
        self.assertIsNotNone(encrypted)
        self.assertGreater(len(encrypted), 0)
        
        # 解密消息
        decrypted = self.rsa_tool.decrypt_message(encrypted)
        self.assertEqual(original_message, decrypted)
        
        print("✅ 加密解密测试通过")
    
    def test_key_info(self):
        """测试密钥信息功能"""
        print("\n测试密钥信息...")
        
        # 生成密钥
        self.rsa_tool.generate_key_pair(save_to_file=False)
        
        # 获取密钥信息
        info = self.rsa_tool.get_key_info()
        self.assertIsNotNone(info)
        
        # 验证信息字段
        required_fields = ['key_size', 'public_exponent', 'modulus', 
                          'public_key_base64', 'fingerprint', 'generated_time']
        for field in required_fields:
            self.assertIn(field, info)
        
        # 验证具体值
        self.assertEqual(info['key_size'], 2048)
        self.assertEqual(info['public_exponent'], 65537)
        self.assertIsInstance(info['fingerprint'], str)
        self.assertEqual(len(info['fingerprint']), 64)  # SHA-256 哈希长度
        
        print("✅ 密钥信息测试通过")
    
    def test_key_backup(self):
        """测试密钥备份功能"""
        print("\n测试密钥备份...")
        
        # 生成密钥
        self.rsa_tool.generate_key_pair(save_to_file=False)
        
        # 创建备份
        backup_dir = os.path.join(self.temp_dir, "backup")
        self.rsa_tool.create_key_backup(backup_dir)
        
        # 验证备份目录存在
        self.assertTrue(os.path.exists(backup_dir))
        
        # 验证备份文件存在
        backup_files = os.listdir(backup_dir)
        self.assertGreater(len(backup_files), 0)
        
        # 验证备份文件包含私钥和公钥
        has_private = any('private_key' in f for f in backup_files)
        has_public = any('public_key' in f for f in backup_files)
        self.assertTrue(has_private)
        self.assertTrue(has_public)
        
        print("✅ 密钥备份测试通过")
    
    def test_export_key_info(self):
        """测试密钥信息导出功能"""
        print("\n测试密钥信息导出...")
        
        # 生成密钥
        self.rsa_tool.generate_key_pair(save_to_file=False)
        
        # 导出密钥信息
        info_file = os.path.join(self.temp_dir, "key_info.json")
        self.rsa_tool.export_key_info(info_file)
        
        # 验证文件存在
        self.assertTrue(os.path.exists(info_file))
        
        # 验证 JSON 格式正确
        with open(info_file, 'r', encoding='utf-8') as f:
            info = json.load(f)
        
        self.assertIsInstance(info, dict)
        self.assertIn('key_size', info)
        self.assertEqual(info['key_size'], 2048)
        
        print("✅ 密钥信息导出测试通过")
    
    def test_different_key_sizes(self):
        """测试不同密钥长度"""
        print("\n测试不同密钥长度...")
        
        # 测试 4096 位密钥
        rsa_4096 = EnhancedRSATool(4096)
        private_key, public_key = rsa_4096.generate_key_pair(save_to_file=False)
        
        self.assertEqual(private_key.key_size, 4096)
        self.assertEqual(public_key.key_size, 4096)
        
        # 测试签名和验证
        message = "测试 4096 位密钥的签名功能"
        signature = rsa_4096.sign_message(message)
        is_valid = rsa_4096.verify_signature(message, signature)
        self.assertTrue(is_valid)
        
        print("✅ 不同密钥长度测试通过")
    
    def test_file_operations(self):
        """测试文件操作功能"""
        print("\n测试文件操作...")
        
        # 生成密钥
        self.rsa_tool.generate_key_pair(save_to_file=False)
        
        # 创建测试文件
        test_file = os.path.join(self.temp_dir, "test_file.txt")
        test_content = "这是一个测试文件的内容。\n包含多行文本。\n用于测试文件签名。"
        
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write(test_content)
        
        # 对文件内容进行签名
        signature = self.rsa_tool.sign_message(test_content)
        
        # 验证文件签名
        is_valid = self.rsa_tool.verify_signature(test_content, signature)
        self.assertTrue(is_valid)
        
        # 测试被篡改的文件内容
        tampered_content = test_content + "\n恶意内容"
        is_valid = self.rsa_tool.verify_signature(tampered_content, signature)
        self.assertFalse(is_valid)
        
        print("✅ 文件操作测试通过")
    
    def test_error_handling(self):
        """测试错误处理"""
        print("\n测试错误处理...")
        
        # 测试未加载密钥时的操作
        with self.assertRaises(ValueError):
            self.rsa_tool.sign_message("测试消息")
        
        with self.assertRaises(ValueError):
            self.rsa_tool.encrypt_message("测试消息")
        
        # 测试加载不存在的密钥文件
        success = self.rsa_tool.load_keys("nonexistent_private.pem", "nonexistent_public.pem")
        self.assertFalse(success)
        
        print("✅ 错误处理测试通过")

def run_performance_test():
    """运行性能测试"""
    print("\n" + "="*60)
    print("性能测试")
    print("="*60)
    
    import time
    
    # 测试密钥生成性能
    print("测试密钥生成性能...")
    start_time = time.time()
    rsa_tool = EnhancedRSATool(2048)
    rsa_tool.generate_key_pair(save_to_file=False)
    generation_time = time.time() - start_time
    print(f"2048 位密钥生成时间: {generation_time:.3f} 秒")
    
    # 测试签名性能
    print("测试签名性能...")
    message = "这是一个用于性能测试的消息。" * 100  # 长消息
    start_time = time.time()
    signature = rsa_tool.sign_message(message)
    signing_time = time.time() - start_time
    print(f"签名时间: {signing_time:.3f} 秒")
    
    # 测试验证性能
    print("测试验证性能...")
    start_time = time.time()
    is_valid = rsa_tool.verify_signature(message, signature)
    verification_time = time.time() - start_time
    print(f"验证时间: {verification_time:.3f} 秒")
    
    # 测试加密性能
    print("测试加密性能...")
    short_message = "短消息"
    start_time = time.time()
    encrypted = rsa_tool.encrypt_message(short_message)
    encryption_time = time.time() - start_time
    print(f"加密时间: {encryption_time:.3f} 秒")
    
    # 测试解密性能
    print("测试解密性能...")
    start_time = time.time()
    decrypted = rsa_tool.decrypt_message(encrypted)
    decryption_time = time.time() - start_time
    print(f"解密时间: {decryption_time:.3f} 秒")
    
    print("✅ 性能测试完成")

def main():
    """主测试函数"""
    print("RSA 工具完整测试套件")
    print("="*60)
    
    # 运行单元测试
    print("运行单元测试...")
    unittest.main(argv=[''], exit=False, verbosity=2)
    
    # 运行性能测试
    run_performance_test()
    
    print("\n" + "="*60)
    print("所有测试完成！")
    print("="*60)

if __name__ == "__main__":
    main() 