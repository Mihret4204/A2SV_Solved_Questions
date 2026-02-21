class Solution:
    def customSortString(self, order: str, s: str) -> str:
        custom_order={c:i for i,c in enumerate(order)}
        ordered=sorted(s, key=lambda c: custom_order.get(c,27))
        return "".join(ordered)
        