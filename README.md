# Auto-ArktsDoc

Auto-ArktsDoc 仓库的初始化说明与日常 Git 命令速查。

- 远程仓库：`origin -> https://github.com/ActiveInsighter/Auto-ArktsDoc.git`
- 常用命令文档：[`docs/common-git-commands.md`](docs/common-git-commands.md)
- ArkTS 文档抓取脚本：[`ArktsDocScript/1.py`](ArktsDocScript/1.py)
- HTML 转 Markdown 脚本：[`ArktsDocScript/html_to_md.py`](ArktsDocScript/html_to_md.py)
- 自动化工作流：[`.github/workflows/arkts-doc-sync.yml`](.github/workflows/arkts-doc-sync.yml)

## 目录建议

- `docs/`：常用命令、规范说明
- `ArktsDocScript/`：文档抓取与转换脚本
- `src/`：后续业务代码
- `tests/`：测试代码

## 自动化说明

仓库已经配置 GitHub Actions 用于自动抓取 ArkTS 文档并转换为 Markdown。

- 每天 00:00 UTC 自动运行一次，换算成北京时间是早上 8 点
- 你也可以在 GitHub 页面手动点 `Run workflow` 触发
- 运行结果会上传为 Actions 产物，便于下载和交给 AI 使用

本地安装依赖时可以执行：

```bash
pip install -r ArktsDocScript/requirements.txt
python -m playwright install chromium
```
