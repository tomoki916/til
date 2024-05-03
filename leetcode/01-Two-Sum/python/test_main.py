from main import Solution 

def test__case1():
  solution = Solution()
  assert solution.twoSums([2,7,11,15], 9) == [0,1]

def test__case2():
  solution = Solution()
  assert solution.twoSums([3,2,4], 6) == [1,2]

def test__case3():
  solution = Solution()
  assert solution.twoSums([3, 3], 6) == [0,1]
