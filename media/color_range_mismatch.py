import math

def read_range(tag):
    """读容器 range。"""
    raise NotImplementedError("TODO: read_range")

def matrix_for(height, primaries):
    """按原色选矩阵。"""
    raise NotImplementedError("TODO: matrix_for")

def upsample(mode):
    """色度上采样。"""
    raise NotImplementedError("TODO: upsample")

def bitdepth(bits):
    """保持位深。"""
    raise NotImplementedError("TODO: bitdepth")

def once(count):
    """只转换一次。"""
    raise NotImplementedError("TODO: once")

def hdr_range(tag):
    """HDR 单独处理。"""
    raise NotImplementedError("TODO: hdr_range")

def subtitle_after(enabled):
    """字幕后置。"""
    raise NotImplementedError("TODO: subtitle_after")

def thumbnail(same):
    """缩略图同链路。"""
    raise NotImplementedError("TODO: thumbnail")

def write_tag(range_value):
    """输出写标记。"""
    raise NotImplementedError("TODO: write_tag")

def order(range_first):
    """先范围后 gamma。"""
    raise NotImplementedError("TODO: order")

def clamp_code(value, low, high):
    """编码值钳制。"""
    raise NotImplementedError("TODO: clamp_code")

def matrix_name(primaries):
    """矩阵名。"""
    raise NotImplementedError("TODO: matrix_name")

def span(limited):
    """范围区间。"""
    raise NotImplementedError("TODO: span")

def is_full(tag):
    """全范围判定。"""
    raise NotImplementedError("TODO: is_full")

def gamma_for(tag):
    """gamma 值。"""
    raise NotImplementedError("TODO: gamma_for")
