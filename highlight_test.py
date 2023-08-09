import unittest

import highlight


class TestHighlight(unittest.TestCase):
    cases = [["你好大家好", ["大家", "你好", "好"], "<highlight>你好大家好</highlight>"],
             ["Kubernetes 是一个可移植、可扩展的开源平台，用于管理容器化的工作负载和服务，可促进声明式配置和自动化。", ["Kube", "Kubernetes", "容器化", "管理", "自动化"], "<highlight>Kubernetes</highlight> 是一个可移植、可扩展的开源平台，用于<highlight>管理容器化</highlight>的工作负载和服务，可促进声明式配置和<highlight>自动化</highlight>。"],
             ["Abcdefg", ["efg", "abc", "def"], "Abc<highlight>defg</highlight>"]]

    def test(self):
        for c in self.cases:
            self.assertEqual(highlight.highlight_keywords(c[0], c[1]), c[2])
