package main
// recursive version of sum and read
import (
    "fmt"
    "os"
)


// sum the array recusively
func sumSq(arr []int, n int) int {
    if (n < 0) {
        return 0;
    }

    var toSum int
    if (arr[n] < 0) {
        toSum = 0
    } else {
        toSum = arr[n]
        toSum *= toSum
    }

    return (toSum + sumSq(arr, n-1))
}

func readArr(curIdx int, a *[]int) {
    if curIdx == 0 {
        return
    }
    var t int
    fmt.Fscan(os.Stdin, &t)
    *a = append(*a, t)
    readArr(curIdx - 1, a)
}

func readCases(caseIdx int){
    if (caseIdx == 0) {
        return
    }
    var nNum int
    fmt.Fscan(os.Stdin, &nNum)
    var arr []int
    readArr(nNum, &arr)
    fmt.Println(sumSq(arr, nNum-1)) // sum from the end of the array
    readCases(caseIdx-1)
}

func main() {
    var nCases int
    fmt.Fscan(os.Stdin, &nCases)
    readCases(nCases)
}
