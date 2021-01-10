package main
// for loop version
import (
    "fmt"
    "os"
)

func sumSq(arr []int) int {
    var ret = 0
    for _, v:= range arr {
        if v > 0{
            ret += v * v
        }
    }
    return ret
}

func main() {
    // scanner := bufio.NewScanner(os.Stdin)
    var nCases int
    fmt.Fscan(os.Stdin, &nCases)
    // nCases, err := strconv.Atoi(scanner.Text())
    for i:=0; i < nCases; i++{
        var nNum int
        fmt.Fscan(os.Stdin, &nNum)
        var arr []int

        for j:=0; j < nNum; j++ {
            var t int
            fmt.Fscan(os.Stdin, &t)
            arr = append(arr, t)
        }
        fmt.Println(arr)
        fmt.Println(sumSq(arr))
    }
}
