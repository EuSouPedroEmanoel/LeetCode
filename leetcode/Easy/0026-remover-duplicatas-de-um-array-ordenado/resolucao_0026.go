package main

func removeDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	writer := 0
	for pointer := 1; pointer < len(nums); pointer++ {
		if nums[pointer] != nums[pointer-1] {
			writer++
			nums[writer] = nums[pointer]
		}
	}

	return writer + 1
}

// remova o main ao testar no leetcode
func main() {}
