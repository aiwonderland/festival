# test/test_text.py
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from festival.text import style_text as st

if __name__ == "__main__":
    # 测试列表：逐个验证样式
    test_styles = [
        ("bold", "加粗"),
        ("underline", "下划线"),
        ("reverse", "反显"),
        ("dim", "暗淡")
    ]
    
    for style_name, desc in test_styles:
        print(f"\n=== 测试 {desc}（{style_name}）===")
        # 单独调用：仅前景 yellow + 单个样式
        res = st(f"Hi! {desc}效果", fg_color="magenta", effects=[style_name])
        # 打印调试信息
        print(f"返回值类型: {type(res)}")
        print(f"最终效果: {res}")