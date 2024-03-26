#!/bin/bash

# 获取脚本所在的绝对路径
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# 获取项目的根目录（这里假设bin目录直接位于项目根目录下）
PROJECT_ROOT="${SCRIPT_DIR}/.."

# 设置 PYTHONPATH 环境变量，将项目根目录添加到其中
export PYTHONPATH="${PROJECT_ROOT}:${PYTHONPATH}"

# 定义服务对应的Python脚本路径
API_SERVER_SCRIPT="main.py"
CORE_DATA_GENERATOR_SCRIPT="src/com_desmond/main.py"

# 定义服务对应的进程PID文件路径
API_SERVER_PID_FILE="api_server.pid"
CORE_DATA_GENERATOR_PID_FILE="core_data_generator.pid"

# Python3环境的目录，默认项目目录下
PYTHON_ENV_DIR="venv"

# 启动函数
start_api_server() {
    echo "Starting API Server..."
    nohup $PYTHON_ENV_DIR/bin/python3 $API_SERVER_SCRIPT > /dev/null 2>&1 &
    echo $! > $API_SERVER_PID_FILE
    echo "API Server is running in the background."
}

start_core_data_generator() {
    echo "Starting Core Data Generator..."
    nohup $PYTHON_ENV_DIR/bin/python3 $CORE_DATA_GENERATOR_SCRIPT /dev/null 2>&1 &
    echo $! > $CORE_DATA_GENERATOR_PID_FILE
    echo "Core Data Generator is running in the background."
}

start_all() {
    start_api_server
    start_core_data_generator
    echo "Both services are now running."
}

# 停止函数
stop_api_server() {
    if [ -f "$API_SERVER_PID_FILE" ]; then
        api_pid=$(cat $API_SERVER_PID_FILE)
        echo "Stopping API Server (PID: $api_pid)..."
        kill $api_pid && rm $API_SERVER_PID_FILE
        echo "API Server has been stopped."
    else
        echo "API Server is not currently running."
    fi
    rm $API_SERVER_PID_FILE
}

stop_core_data_generator() {
    if [ -f "$CORE_DATA_GENERATOR_PID_FILE" ]; then
        core_pid=$(cat $CORE_DATA_GENERATOR_PID_FILE)
        echo "Stopping Core Data Generator (PID: $core_pid)..."
        kill $core_pid && rm $CORE_DATA_GENERATOR_PID_FILE
        echo "Core Data Generator has been stopped."
    else
        echo "Core Data Generator is not currently running."
    fi
    rm $CORE_DATA_GENERATOR_PID_FILE
}

stop_all() {
    stop_api_server
    stop_core_data_generator
    echo "All services have been stopped."
}


# 检查参数并启动相应的服务
case "$1" in
    "start-api")
        start_api_server
        ;;
    "start-core")
        start_core_data_generator
        ;;
    "start-all")
        start_all
        ;;
    "stop-api")
        stop_api_server
        ;;
    "stop-core")
        stop_core_data_generator
        ;;
    "stop-all")
        stop_all
        ;;
    *)
        echo "Usage: $0 [start-api|start-core|start-all|stop-api|stop-core|stop-all]"
        exit 1
        ;;
esac

echo "Press Ctrl+C to stop the service(s)."
# wait # 等待所有后台进程结束

exit 0