class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        def backtrack(start_index,combination_sum,current_sum):
            if current_sum==target:
                result.append(combination_sum[:])
                return
            if current_sum>target:
                return
            for i in range(start_index,len(candidates)):
                if i>start_index and candidates[i]==candidates[i-1]:
                    continue
                combination_sum.append(candidates[i])
                backtrack(i+1,combination_sum,current_sum+candidates[i])
                combination_sum.pop()
        backtrack(0,[],0)
        return result
        
        