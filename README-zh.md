# YAML MOTD 处理工具

用于处理YAML格式MOTD配置的Python工具，一键导入随机服务器描述。

![GitHub](https://img.shields.io/badge/版本-1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)

## 功能特性
- 两种MOTD格式模式
- 可自定义行前缀
- 保留YAML注释和格式
- 自动文本换行
- 支持UTF-8编码

## 安装步骤
1. 确保已安装Python 3.8+
2. 安装依赖：
   ```bash
   pip install ruamel.yaml
   ```

## 使用说明
1. 准备 ```config.yml``` 和 ```motd.txt``` 文件
2. 运行脚本：
    ```bash
   python motd_processor.py
    ```
3. 根据提示操作：
   - 选择MOTD格式（1/2）
   - 输入两行的前缀
   - 指定YAML键路径（如 ```description.text```）

结果将保存到 ```config_done.yml```

## 文件配置
### motd.txt (一行一条消息)
```
第一条MOTD消息
第二条MOTD消息
...
```