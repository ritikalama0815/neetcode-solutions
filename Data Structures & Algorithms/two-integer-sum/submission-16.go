func twoSum(nums []int, target int) []int {
    hashmap := make(map[int]int)

	for i, n := range nums{
		hashmap[n] = i
	}
	for i, n := range nums{
		diff := target - n
		if j := hashmap[diff];j!=i{
			return []int{i,j}
		}
	}
	return []int{}
}
