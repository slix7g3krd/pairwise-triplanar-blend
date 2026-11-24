# pairwise-triplanar-blend

## 领域

游戏、图形与多媒体

## 主题

三平面贴图混合

## 说明

权重归一、连续过渡与按实例采样器。

初始状态下 `graphics/triplanar_blend.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
