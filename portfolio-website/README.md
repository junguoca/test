# 作品集网站

一个现代化的个人作品集网站项目，展示个人技能、项目和联系方式。

## 项目结构

```
portfolio-website/
├── index.html          # 主页面文件
├── styles.css          # 样式文件
├── main.js             # JavaScript 交互文件
├── images/             # 图片资源文件夹
└── README.md           # 项目说明文档
```

## 功能特性

- ✅ 响应式设计，支持移动端和桌面端
- ✅ 平滑滚动导航
- ✅ 移动端汉堡菜单
- ✅ 项目展示区域
- ✅ 联系表单
- ✅ 页面滚动动画效果
- ✅ 现代化的 UI 设计

## 技术栈

- HTML5
- CSS3 (包含 CSS 重置样式)
- Vanilla JavaScript (原生 JavaScript，无依赖)

## 运行说明

### 方法一：直接打开

1. 下载或克隆项目到本地
2. 双击 `index.html` 文件在浏览器中打开

### 方法二：使用本地服务器（推荐）

#### 使用 Python（如果已安装）

```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

然后在浏览器中访问：`http://localhost:8000`

#### 使用 Node.js（如果已安装）

```bash
# 安装 http-server（全局安装）
npm install -g http-server

# 在项目目录下运行
cd portfolio-website
http-server
```

然后在浏览器中访问：`http://localhost:8080`

#### 使用 VS Code Live Server

1. 在 VS Code 中安装 "Live Server" 扩展
2. 右键点击 `index.html` 文件
3. 选择 "Open with Live Server"

## 自定义说明

### 修改内容

1. **个人信息**：编辑 `index.html` 中的文本内容
2. **样式**：修改 `styles.css` 中的颜色、字体、间距等
3. **功能**：在 `main.js` 中添加或修改交互功能
4. **图片**：将图片文件放入 `images/` 文件夹，并在 HTML 中引用

### 添加项目

在 `index.html` 的 `.project-grid` 中添加新的 `.project-card`：

```html
<div class="project-card">
    <h3>项目名称</h3>
    <p>项目描述...</p>
</div>
```

### 修改颜色主题

在 `styles.css` 中修改以下颜色变量：

- 主色调：`#667eea` 和 `#764ba2`（渐变背景）
- 背景色：`#2c3e50`（导航栏和页脚）
- 文字颜色：`#333`（主要内容）

## 浏览器支持

- Chrome（最新版本）
- Firefox（最新版本）
- Safari（最新版本）
- Edge（最新版本）

## 许可证

本项目采用 MIT 许可证。

## 贡献

欢迎提交 Issue 和 Pull Request！

## 联系方式

如有问题或建议，请通过以下方式联系：

- 邮箱：[your-email@example.com]
- GitHub：[your-github-username]

