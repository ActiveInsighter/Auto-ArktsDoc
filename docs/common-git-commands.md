# 常用 Git 命令

本文档整理了日常开发中最常用的一组 Git 命令，适合新仓库初始化、多人协作和本地分支管理。

## 1. 仓库初始化与远程仓库

```bash
git init
```

初始化当前目录为一个新的 Git 仓库。

```bash
git remote add origin https://github.com/ActiveInsighter/Auto-ArktsDoc.git
```

将远程仓库命名为 `origin` 并绑定地址。

```bash
git remote -v
```

查看当前配置的远程仓库地址。

```bash
git branch -M main
```

将当前分支重命名为 `main`，适合作为默认主分支。

## 2. 查看状态与历史

```bash
git status
```

查看工作区、暂存区和分支状态。

```bash
git log --oneline --graph --decorate --all
```

以简洁图形方式查看提交历史。

```bash
git diff
```

查看工作区未暂存的修改。

```bash
git diff --cached
```

查看已暂存但尚未提交的修改。

## 3. 提交代码

```bash
git add .
```

将当前目录下的所有变更加入暂存区。

```bash
git add <file>
```

只暂存指定文件。

```bash
git commit -m "message"
```

提交暂存区内容并添加提交说明。

建议提交信息简短明确，例如：

- `feat: add login page`
- `fix: handle null response`
- `docs: update git commands`

## 4. 拉取与推送

```bash
git fetch origin
```

只从远程获取更新，不自动合并。

```bash
git pull origin main
```

从远程 `main` 拉取并合并到本地。

```bash
git push origin main
```

将本地 `main` 分支推送到远程仓库。

```bash
git push -u origin main
```

首次推送时建立本地分支与远程分支的跟踪关系。

## 5. 分支管理

```bash
git branch
```

查看本地分支列表。

```bash
git branch <name>
```

创建新分支。

```bash
git switch <name>
```

切换到指定分支。

```bash
git switch -c <name>
```

创建并切换到新分支。

```bash
git branch -d <name>
```

删除已合并的本地分支。

## 6. 撤销与回退

```bash
git restore <file>
```

撤销工作区中对指定文件的修改。

```bash
git restore --staged <file>
```

取消暂存，但保留工作区修改。

```bash
git reset HEAD~1
```

取消最近一次提交对应的暂存状态，常用于修正提交前的操作。

```bash
git revert <commit>
```

通过新提交撤销指定历史提交，适合已推送到远程的改动。

## 7. 常见协作流程

1. `git pull origin main`
2. 修改代码
3. `git status`
4. `git add .`
5. `git commit -m "feat: ..."`
6. `git push origin main`

## 8. 实用建议

- 提交前先看 `git status`，确认改动范围。
- 团队协作优先使用清晰的提交信息。
- 如果改动已经推送到远程，优先使用 `git revert`，避免直接改写历史。
- 大功能拆分成小提交，便于回滚和排查问题。
