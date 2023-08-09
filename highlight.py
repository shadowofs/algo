# 题目：
# 输入两个参数s和keys，s是一个字符串，keys是一个字符串列表，包含一系列关键词。
# 函数需要把s中每一处和任一关键词相同的部分用<highlight>和</highlight>包围起来，
# 连续的部分自动合并，比如输入s="你好大家好"，keys=["好大", "大家"]，需要输出"你<highlight>好大家</highlight>好"。
# 注意关键字不会重复，但有可能包含，比如可能是["大", "大家"]，s中无论是"大家"还是单独一个"大"字都需要highlight。

def highlight_keywords(s, keys):
    # 使用临时标记列表来记录需要高亮的部分的起始位置和结束位置
    marks = []

    for key in keys:
        start = 0
        while True:
            # 在字符串中搜索关键词的起始位置
            start = s.find(key, start)
            if start == -1:
                break

            end = start + len(key)
            insert_marks(marks, start, end)

            # 继续搜索下一个匹配的关键词
            start = end + 1

    # 根据标记列表，构建最终的高亮字符串
    highlighted = ""
    prev_end = 0
    for start, end in marks:
        highlighted += s[prev_end:start] + "<highlight>" + s[start:end] + "</highlight>"
        prev_end = end

    # 添加剩余的非高亮部分
    highlighted += s[prev_end:]

    return highlighted


def insert_marks(marks, start, end):
    i = 0
    while i < len(marks):
        if marks[i][0] <= start <= marks[i][1]:
            marks[i][1] = max(marks[i][1], end)
            if i + 1 < len(marks) and marks[i + 1][0] <= marks[i][1]:
                marks[i][1] = marks[i + 1][1]
                marks.pop(i + 1)
            return
        elif marks[i][0] <= end <= marks[i][1]:
            marks[i][0] = min(marks[i][0], start)
            if i >= 1 and marks[i - 1][1] >= marks[i][0]:
                marks[i][0] = marks[i - 1][0]
                marks.pop(i - 1)
            return
        elif start < marks[i][0]:
            marks.insert(i, [start, end])
            return
        i += 1

    marks.append([start, end])


if __name__ == '__main__':
    s = "你好大家好"
    keys = ["好大", "大家"]
    highlighted_string = highlight_keywords(s, keys)
    print(highlighted_string)
