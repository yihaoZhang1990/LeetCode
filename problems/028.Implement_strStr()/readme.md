## 028. Implement strStr() (Easy)

### **链接**：
题目：https://leetcode.com/problems/implement-strstr/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
在一个字符串haystack（文本串）里，找另一个字符串needle（模式串）在其中的位置。  

### **分析**：
1. 暴力搜索：时间复杂度O(n2)，空间复杂度O(1)。
	- 这题难度为 Easy 是因为它 O(n^2) 的暴力能过。如果数据强点就得 Medium 以上了。  
	
2. 各种高级算法：
	- [KMP 算法](http://en.wikipedia.org/wiki/Knuth-Morris-Pratt_algorithm): 时间复杂度O(n)，空间复杂度O(k)。
		1. 第一步：[求Partial Match表](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm#.22Partial_match.22_table_.28also_known_as_.22failure_function.22.29)
			- 这个表的意义：T[i]的值表示：needle的前缀子字符串needle[0 : T[i]-1]和needle[i-T[i] : i-1]相同
		2. 第二步：只需一个 for 循环遍历haystack, 当haystack[i] != needle[j]，i保持不变，j回溯到T[j]。
	
	- [Boyer–Moore算法](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string_search_algorithm)
	- [Rolling Hash(Rabin-Karp)算法](https://en.wikipedia.org/wiki/Rolling_hash)  
		- 可以用 hash 去做，叫 rolling hash 算法（见 [Wiki](http://en.wikipedia.org/wiki/Rolling_hash) 和 [StackOverflow](http://stackoverflow.com/questions/711770/fast-implementation-of-rolling-hash)）  
		- 就是把字符串 hash 出来，按匹配串长度窗口去滚动，再去匹配。  
		- hash 字符串有很多种方法，这边的字母好像都是小写，有 26 个，所以就用 29 做基数（本来想像 djb2 算法用 33 做基数，可以直接 `((hash << 5) + hash)` 很快，不过 int 范围只能 hash 6 个字母而且 rolling 的时候还是要 `/33`，还是用 29 算了），超 int 范围的话用 Python 就不用考虑这个问题了。  