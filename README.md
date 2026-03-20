# Auto-ArktsDoc

Auto-ArktsDoc 仓库的初始化说明与日常 Git 命令速查。

- 远程仓库：`origin -> https://github.com/ActiveInsighter/Auto-ArktsDoc.git`
- 常用命令文档：[`docs/common-git-commands.md`](docs/common-git-commands.md)
- ArkTS 文档抓取脚本：[`ArktsDocScript/fetch-html.py`](ArktsDocScript/fetch-html.py)
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
- 运行结果会自动提交到 `arkts-docs` 分支，Markdown 会直接出现在仓库里，并保留分支提交历史，方便回退到旧版本

生成流程是：先抓取 HTML，再转换成 Markdown，最后把 Markdown 提交到专用分支。

本地安装依赖时可以执行：

```bash
pip install -r ArktsDocScript/requirements.txt
python -m playwright install chromium
```
