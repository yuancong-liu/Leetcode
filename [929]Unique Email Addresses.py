# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        address = set()
        for email in emails:
            add_before, add_after = email.split(sep="@")
            add_before = self.simplify(add_before)
            address.add("".join([add_before, "@", add_after]))
        return len(address)

    def simplify(self, add_before):
        add_before = list(add_before)
        if "+" in add_before:
            add_before = add_before[:add_before.index("+")]
        while "." in add_before:
            add_before.pop(add_before.index("."))
        return "".join(add_before)
# leetcode submit region end(Prohibit modification and deletion)
