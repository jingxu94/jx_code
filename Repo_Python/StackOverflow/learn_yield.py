#__author:  "Jing Xu"
#date:  2018/2/1

# def _get_child_candidates(self, distance, min_dist, max_dist):
# 	if self._leftchild and distance - max_dist < self._median:
# 		yield self._leftchild
# 	if self._rightchild and distance + max_dist >= self._median:
# 		yield self._rightchild
#
# result, candidates = [], [self]
# while candidates:
#     node = candidates.pop()
#     distance = node._get_dist(obj)
#     if distance <= max_dist and distance >= min_dist:
#         result.extend(node._values)
#     candidates.extend(node._get_child_candidates(distance, min_dist, max_dist))
# return result


from collections import deque

class Task:

    next_id = 0

    def __init__(self, routine):
       self.id = Task.next_id
       Task.next_id += 1
       self.routine = routine


class Eventloop:

    def __init__(self):
        self.runnable_task = deque()
        self.computed_task_results = {}
        self.failed_task_errors = {}

    def add(self, routine):
        task = Task(routine)
        self.runnable_task.append(task)
        return task.id

    def run_until_completed(self):
        while len(self.runnable_task) != 0:
            task = self.runnable_task.popleft()
            print("RUNNING TASK: {}".format(task.id))

            try:
                yielded = next(task.routine)
            except StopIteration as stop:
                print("Completed task {} , result {}".format(task.id,stop.value))
                self.computed_task_results[task.id] = stop.value
            except Exception as e:
                print("Task {} Error, Exception {}".format(task.id, e))
                self.failed_task_errors[task.id] = e
            else:
                assert yielded is None
                print("Not finish")
                self.runnable_task.append(task)

def async_sum(f_id, n):
    res = 0
    for i in range(n):
        res = i+res
        print("Functino id : {} , step: {}".format(f_id, i))
        yield
    return res


a = async_sum(1, 3)
b = async_sum(2, 4)
obj = Eventloop()
obj.add(a)
obj.add(b)
obj.run_until_completed()