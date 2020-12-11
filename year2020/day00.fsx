#r "nuget: Unquote"
open Swensen.Unquote

// utilities
let split (separator: string) (s: string) =
    s.Split([| separator |], System.StringSplitOptions.RemoveEmptyEntries)

// inputs
let path = $@"{__SOURCE_DIRECTORY__}/day00_in.txt"
let inputLines = System.IO.File.ReadAllLines path
let testLines: string list = []

let preprocessing ss = ss

let testInput = preprocessing testLines
let input = preprocessing inputLines
// part 1
let solve_p1 input = 42

test <@ solve_p1 testInput = 42 @>

printfn "Part1: %A" (solve_p1 input)

// part 2
let solve_p2 input = 42

test <@ solve_p2 testInput = 42 @>

printfn "Part2: %A" (solve_p2 input)
