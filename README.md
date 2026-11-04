# NX12 LiveForge

面向 Siemens NX 12 的开源自动化建模 Skill，采用 Codex 式 **"生成-执行-判决-重试"** 闭环。

## 设计理念
- **Agent 不凭直觉建模**：生成 NXOpen Journal，通过可验证的执行结果迭代
- **GUI 前台执行**：在打开的 NX 窗口内逐阶段运行，看得见、可取消
- **判决器不轻信退出码**：NX12 对吞掉异常的 Journal 仍返回 0，必须解析日志 + 几何度量

## 场景
用户给正视图 + 侧视图，Agent 生成并迭代 Journal，在 NX12 GUI 里逐步拉伸出完整三维实体。主测试用例为派大星低模。

## 约束
- NX 12，内嵌 Python **3.6.1**
- NXOpen 不向后兼容：所有 Journal 必须限定 NX12 API 表面
