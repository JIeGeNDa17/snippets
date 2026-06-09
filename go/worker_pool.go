package pool

func Run(jobs <-chan int, n int, f func(int)) {
    for i := 0; i < n; i++ { go func() { for j := range jobs { f(j) } }() }
}
