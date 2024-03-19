class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cooling = {task:0 for task in tasks}
        task_num = {}
        for task in tasks:
            if task not in cooling:
                cooling[task] = 0
            
            if task not in task_num:
                task_num[task] = 1
            else:
                task_num[task] += 1

        ans = []
        while sum(task_num.values()) != 0:
            max_num = 0
            task = 'idle'
            for k, v in task_num.items():
                if v != 0 and cooling[k] <= 0:
                    if v > max_num:
                        max_num = v
                        task = k

            for i in cooling:
                cooling[i] -= 1
            
            ans.append(task)
            if task != 'idle':
                task_num[task] -= 1
                cooling[task] = n

        return len(ans)