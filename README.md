[![CI - 自动化测试](https://github.com/lcc-clod/auto-test-demo/actions/workflows/ci.yml/badge.svg)](https://github.com/lcc-clod/auto-test-demo/actions/workflows/ci.yml)

# 接口自动化测试框架（Python + Pytest）

## 项目简介

这是一个基于 Python + Pytest + Requests 的接口自动化测试框架，包含：
- 注册/登录接口的自动化测试用例（正向 + 异常场景）
- 数据驱动测试（测试数据与代码分离）
- 完整的日志记录系统
- Allure 测试报告
- GitHub Actions 持续集成（每次推送自动运行测试）

## 技术栈

- Python 3.11+
- Pytest 9.0+（测试框架）
- Requests 2.31+（HTTP 客户端）
- PyYAML 6.0+（配置文件解析）
- Allure 报告（可视化测试报告）
- GitHub Actions（持续集成）

## 项目结构
auto-test-demo/
├── .github/workflows/ # CI 配置
├── core/ # 核心封装
│ ├── http_client.py # HTTP 客户端
│ ├── logger.py # 日志模块
│ └── config_manager.py # 配置管理
├── tests/ # 测试用例
│ └── test_login.py # 登录/注册接口测试
├── config/ # 配置文件
│ └── config.yaml # 环境配置
├── data/ # 测试数据
│ └── test_data.yaml # 数据驱动用例
├── reports/ # 测试报告
├── logs/ # 日志文件
├── requirements.txt # 项目依赖
└── README.md