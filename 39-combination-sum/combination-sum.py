class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def backtrack(start_index,combination_sum,current_sum):
            if current_sum==target:
                result.append(combination_sum[:])
                return
            if current_sum>target:
                return

            for i in range(start_index,len(candidates)):
                combination_sum.append(candidates[i])
                backtrack(i,combination_sum,current_sum+candidates[i])
                combination_sum.pop()
        
        backtrack(0,[],0)
        return result
        