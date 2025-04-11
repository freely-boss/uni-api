import logging
import os

# 获取DEBUG环境变量，默认为False
DEBUG = os.environ.get('DEBUG', 'False').lower() in ('true', '1', 't')

# 根据DEBUG环境变量设置日志级别
LOG_LEVEL = logging.DEBUG if DEBUG else logging.INFO

# 设置日志格式
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"

# 配置根日志记录器
logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)

# 获取应用程序日志记录器
logger = logging.getLogger("uni-api")
logger.setLevel(LOG_LEVEL)

# 如果DEBUG设置为True，更详细记录日志
if DEBUG:
    # 将httpx和watchfiles的日志级别设置为WARNING
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("watchfiles.main").setLevel(logging.WARNING)
    
    # 记录当前环境变量信息
    for key, value in os.environ.items():
        if key.startswith('CONFIG_') or key in ('DEBUG', 'DISABLE_DATABASE', 'IS_VERCEL'):
            logger.debug(f"环境变量 {key}={value}")
else:
    # 非调试模式下，降低这些库的日志级别
    logging.getLogger("httpx").setLevel(logging.CRITICAL)
    logging.getLogger("watchfiles.main").setLevel(logging.CRITICAL)

logger.info(f"日志记录器初始化完成，级别: {'DEBUG' if DEBUG else 'INFO'}")