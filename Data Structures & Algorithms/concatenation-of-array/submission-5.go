func getConcatenation(nums []int) []int {
    n := len(nums)
    ans := make([]int, n*2)

    copy(ans, nums)
    copy(ans[n:], nums)

    return ans
}
