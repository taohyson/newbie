// var slice1 []type = make([]type, len)
// slice1 := make([]type, len)
// slice1 := make([]type, len, capacity)
// s :=[] int {1,2,3 } 
// s := arr[:] 
// s :=make([]int,len,cap) 

package main

import "fmt"

func main() {
   var numbers = make([]int,3,5)

   printSlice(numbers)
}

func printSlice(x []int){
   fmt.Printf("len=%d cap=%d slice=%v\n",len(x),cap(x),x)
}