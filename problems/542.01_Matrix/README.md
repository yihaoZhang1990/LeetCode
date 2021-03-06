## 542. 01 Matrix (Medium)

### **链接**：
题目：https://leetcode.com/problems/01-matrix  
题解：https://github.com/JianghanLi/LeetCode

### **题意**
给一个只包含0和1的矩阵，要求返回一个矩阵，每个格子是此位置到最近的0的距离。
已知矩阵中至少有一个0，0到此身距离为0。


### **分析**  
1. 深度优先搜索(DFS)：时间复杂度O(mn*4^(mn))，空间复杂度O(4^(mn))。
	- 这个思路比较简单，就是遍历矩阵，遇到0就从此格开始用递归法填充结果。
	- 时间复杂度太高，超时。

2. 广度优先搜索(BFS)+队列(Queue)：时间复杂度O(mn)，空间复杂度O(mn)/O(1)。
	- 思路：
		1. Init：在队列中存入所有0的位置
		2. while循环：取队列最上的值，更新相邻值：
			- 若能更新相邻值（未填入/大于新值），更新，并将此位置放入队列。
			- 若不能（超出边界/大于新值），什么也不做。
	- 若直接在输入的matrix上修改，可达到空间复杂度O(1)。

3. 动态规划(DP)：时间复杂度O(mn)，空间复杂度O(mn)/O(1)。
	- 从左上到右下，从右下到左上遍历两次：
		- 若当前矩阵值为0，填入0
		- 若不为0，取相邻的上下左右已填入的最小值+1。
	- 若直接在输入的matrix上修改，可达到空间复杂度O(1)。