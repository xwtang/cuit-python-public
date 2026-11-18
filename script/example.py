"""
示例：典型 Python 程序结构示例
"""

# 常量定义（全大写）
DEFAULT_THRESHOLD = 10


# 函数定义：带类型标注与文档字符串
def compute_sum(numbers: list[int]) -> int:
    """返回列表中所有数字的和。"""
    total = 0
    for n in numbers:
        total += n
    return total


# 类定义：展示初始化、方法、属性
class ScoreChecker:
    """一个简单的分数检测类。"""

    def __init__(self, threshold: int = DEFAULT_THRESHOLD):
        self.threshold = threshold

    def is_pass(self, score: int) -> bool:
        """判断分数是否达到阈值。"""
        return score >= self.threshold


# 主程序入口
def main():
    # 创建列表与字典
    data = [3, 5, 12, 8]
    info = {"name": "Alice", "scores": data}

    print(f"学生 {info['name']} 的成绩列表：", info["scores"])

    # 调用函数
    total = compute_sum(info["scores"])
    print("总分 =", total)

    # 使用类
    checker = ScoreChecker()
    for score in info["scores"]:
        # 条件判断
        if checker.is_pass(score):
            print(f"{score} 分：通过")
        else:
            print(f"{score} 分：未通过")


# 规范写法：只在脚本执行时运行
if __name__ == "__main__":
    main()
