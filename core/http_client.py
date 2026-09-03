import requests
from core.logger import logger
from core.config_manager import config

class HttpClient:
    def __init__(self, base_url=None, timeout=None):
        self.base_url = base_url or config['base_url']
        self.timeout = timeout or config.get('timeout', 10)
        self.headers = {}
        logger.info(f"初始化 HttpClient，base_url={self.base_url}")

    def set_headers(self, headers):
        self.headers.update(headers)

    def post(self, endpoint, data=None, json=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        req_headers = self.headers.copy()
        if headers:
            req_headers.update(headers)
        
        logger.info(f"POST 请求: {url}")
        logger.debug(f"请求头: {req_headers}")
        logger.debug(f"请求体: {json or data}")
        
        response = requests.post(url, data=data, json=json,
                                  headers=req_headers, timeout=self.timeout)
        
        logger.info(f"响应状态码: {response.status_code}")
        logger.debug(f"响应体: {response.text[:500]}")  # 只记录前500字符
        return response

    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        req_headers = self.headers.copy()
        if headers:
            req_headers.update(headers)
        
        logger.info(f"GET 请求: {url}")
        response = requests.get(url, params=params,
                                headers=req_headers, timeout=self.timeout)
        logger.info(f"响应状态码: {response.status_code}")
        return response