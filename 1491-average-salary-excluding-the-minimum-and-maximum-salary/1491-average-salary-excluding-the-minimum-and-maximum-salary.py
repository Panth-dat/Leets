class Solution:
    def average(self, salary: List[int]) -> float:
        salary=sorted(salary)
        salary=salary[1:-1]
        ans=sum(salary)/len(salary)
        return round(ans, 5)