package math

func Fib(n int, m map[int]int) int {
    if n < 2 { return n }
    if v, ok := m[n]; ok { return v }
    m[n] = Fib(n-1, m) + Fib(n-2, m); return m[n]
}
