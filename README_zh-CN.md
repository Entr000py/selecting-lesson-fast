[English](./README.md)

# selecting-lesson-fast - 快速选课工具

一个经过重构的自动化选课工具，旨在提高代码的可维护性和易用性。

## ✨ 功能

-   **命令行界面:** 通过命令行参数轻松操作。
-   **自动登录:** 使用 OCR 技术识别验证码，实现自动登录。
-   **灵活选课:** 通过课程ID和板块信息精确选择课程。

## 🚀 安装

1.  克隆本仓库:
    ```bash
    git clone https://github.com/your-username/selecting-lesson-fast.git
    cd selecting-lesson-fast
    ```

2.  安装所需依赖:
    ```bash
    pip install -r requirements.txt
    ```
    
3.  您可能还需要为您的浏览器安装对应的 WebDriver。例如，如果您使用 Chrome 浏览器，则需要下载 [ChromeDriver](https://chromedriver.chromium.org/downloads)。

## 📋 使用方法

在终端中运行以下命令:

```bash
python src/main.py --username 你的学号 --password 你的密码 --course-id 课程ID --plate 课程板块
```

**参数说明:**

-   `--username`: 你的学号
-   `--password`: 你的密码
-   `--course-id`: 你想选择的课程ID (例如: `kcmcGrid_xk_4`)
-   `--plate`: 你想选择的课程所在的板块 (例如: `板块（1）`)

### 示例

```bash
python src/main.py --username 123456 --password "mysecretpassword" --course-id "kcmcGrid_xk_4" --plate "板块（1）"
```

## 🤝 贡献

欢迎参与贡献！请阅读 [贡献指南](CONTRIBUTING.md)。

## 📄 许可证

本项目基于 MIT 许可证。详情请见 [LICENSE](LICENSE) 文件。
