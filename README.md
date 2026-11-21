# pairwise-color-range-mismatch

同一段视频在播放器里发灰，黑边处能看到 16 到 235 的台阶，容器没有标记 limited range，解码后直接按 full 解释；YUV 转 RGB 的矩阵按分辨率猜，1080p 用了 BT.601，红色整体偏橙；色度平面按最近邻上采样，彩色边缘出现锯齿；10bit 素材被降到 8bit 后再做范围扩展，暗部出现断层；范围转换在解码器和滤镜链各做一次，黑位被抬了两遍；HDR 素材套用了 SDR 的 limited range 公式，高光直接削平；字幕叠加在范围转换之后，白字变成灰字；缩略图走的是另一条管线，同一帧在列表里和播放时颜色不同；转码输出没有写 range 标记，下游继续猜；gamma 与范围转换顺序反了，中间调整体偏暗。media/color_range_mismatch.py 是核心，tests/test_color_range_mismatch.py 15个红。要修的是：读容器 range；按色彩原色选矩阵；正确色度上采样；保持位深；只转换一次；HDR 单独处理；字幕在转换后；缩略图同链路；输出写标记；先范围后 gamma。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：见平台；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
