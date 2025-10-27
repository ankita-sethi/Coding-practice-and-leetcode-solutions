class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        container=set()
        for val in nums:
            if val in container:
                return True
            container.add(val)
        return False