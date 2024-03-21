#!/bin/bash

# 定义服务对应的Python脚本路径
API_SERVER_SCRIPT="../main.py"
CORE_DATA_GENERATOR_SCRIPT="../src/com_desmond/main.py"

# 启动函数
start_api_server() {
    echo "Starting API Server..."
    python3 $API_SERVER_SCRIPT &
    echo "API Server is running in the background."
}

start_core_data_generator() {
    echo "Starting Core Data Generator..."
    python3 $CORE_DATA_GENERATOR_SCRIPT &
    echo "Core Data Generator is running in the background."
}

start_all() {
    start_api_server
    start_core_data_generator
    echo "Both services are now running."
}

# 检查参数并启动相应的服务
case "$1" in
    "api")
        start_api_server
        ;;
    "core")
        start_core_data_generator
        ;;
    "all")
        start_all
        ;;
    *)
        echo "Usage: $0 [api|core|all]"
        exit 1
        ;;
esac

echo "Press Ctrl+C to stop the service(s)."
wait # 等待所有后台进程结束

exit 0