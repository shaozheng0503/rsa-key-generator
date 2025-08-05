#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RSA 密钥生成器项目配置文件
"""

from setuptools import setup, find_packages
import os

# 读取 README 文件
def read_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()

# 读取 requirements.txt
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="rsa-key-generator",
    version="2.0.0",
    author="shaozheng0503",
    author_email="",  # 可以添加您的邮箱
    description="一个功能完整的 RSA 密钥管理工具，支持密钥生成、数字签名、加密解密等功能",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/shaozheng0503/rsa-key-generator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Security :: Cryptography",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration",
    ],
    python_requires=">=3.6",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    entry_points={
        "console_scripts": [
            "rsa-keygen=enhanced_rsa_tool:main",
        ],
    },
    keywords="rsa cryptography key-generation digital-signature encryption security",
    project_urls={
        "Bug Reports": "https://github.com/shaozheng0503/rsa-key-generator/issues",
        "Source": "https://github.com/shaozheng0503/rsa-key-generator",
        "Documentation": "https://github.com/shaozheng0503/rsa-key-generator#readme",
    },
) 