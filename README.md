# tripPlanner

基于 FastAPI、HelloAgents 与高德地图 MCP 的智能旅行规划后端。通过 API 接收旅行需求，并提供行程规划、地点搜索、路线规划、天气查询及景点图片接口。

> 当前仓库包含后端服务。部分地图数据解析仍处于 TODO 阶段，具体接口能力以当前实现为准。

## 功能

- 使用 HelloAgents 多智能体能力生成旅行计划
- 集成高德地图 MCP，支持 POI、路线和天气相关服务
- 提供 FastAPI / Swagger / ReDoc 接口
- 支持 Unsplash 景点图片查询
- 提供健康检查接口

## 技术栈

Python 3.10+ · FastAPI · Pydantic · HelloAgents · 高德地图 MCP

## 快速开始

### 1. 准备环境

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
source .venv/bin/activate
```

安装依赖：

```bash
pip install -r requirements.txt
```

高德地图 MCP 服务通过 `uvx` 启动，请确保已安装 `uv` 并可在 PATH 中使用。

### 2. 配置密钥

将 `.env.example` 复制为 `.env`，填入有效密钥：

```bash
cp .env.example .env
```

Windows PowerShell 可运行：

```powershell
Copy-Item .env.example .env
```

至少需要 `AMAP_API_KEY` 和 `LLM_API_KEY`（或 `OPENAI_API_KEY`）。不要提交 `.env` 或真实密钥。

### 3. 启动服务

```bash
python run.py
```

默认地址为 `http://localhost:8000`。接口文档：`/docs`，ReDoc：`/redoc`。

## API 概览

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| GET | `/` | 服务信息 |
| GET | `/health` | 服务健康状态 |
| POST | `/api/trip/plan` | 生成旅行计划 |
| GET | `/api/trip/health` | 行程规划服务状态 |
| GET | `/api/map/poi` | 搜索地点 |
| GET | `/api/map/weather` | 查询天气 |
| POST | `/api/map/route` | 路线规划 |
| GET | `/api/poi/search` | 搜索地点 |
| GET | `/api/poi/detail/{poi_id}` | 地点详情 |
| GET | `/api/poi/photo` | 景点图片 |

请求和响应字段可在启动后通过 Swagger 文档查看。

## 环境变量

| 变量 | 必填 | 说明 |
| --- | --- | --- |
| `AMAP_API_KEY` | 是 | 高德地图 Web 服务 API Key |
| `LLM_API_KEY` | 是* | HelloAgents 使用的模型 API 密钥 |
| `LLM_BASE_URL` | 否 | 模型服务地址 |
| `LLM_MODEL_ID` | 否 | 模型名称 |
| `HOST` / `PORT` | 否 | 服务监听地址和端口 |
| `CORS_ORIGINS` | 否 | 允许跨域访问的来源，以逗号分隔 |
| `UNSPLASH_ACCESS_KEY` | 否 | Unsplash Access Key |
| `UNSPLASH_SECRET_KEY` | 否 | Unsplash Secret Key |

`LLM_API_KEY` 可用 `OPENAI_API_KEY` 替代，取决于 HelloAgents 配置。地图服务调用需要有效的高德 Key。

## GitHub 发布建议

- Repository name：`tripPlanner`
- Description：`基于 FastAPI、HelloAgents 和高德地图 MCP 的智能旅行规划后端，支持行程生成、地点搜索与路线规划。`
- Topics：`trip-planner`、`travel-planner`、`fastapi`、`python`、`helloagents`、`amap`、`mcp`

## 当前限制

地图服务中的 POI、天气、路线和地理编码结果解析仍有 TODO，部分函数目前返回空结果或原始数据。项目建议在补齐解析与验证后用于生产环境。

## License

尚未指定许可证。发布前请添加适合项目的 LICENSE 文件；没有许可证时，默认版权仍归作者所有。