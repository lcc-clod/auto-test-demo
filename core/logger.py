import os
import logging
import sys

def setup_logger(name="test_logger", level=logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # 控制台输出
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # --- 新增：自动创建 logs 目录 ---
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)   # 创建目录

    # 文件输出
    file_handler = logging.FileHandler(os.path.join(log_dir, 'test.log'), encoding='utf-8')
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

# 创建默认日志实例
logger = setup_logger()