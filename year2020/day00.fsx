#r "nuget: Unquote"
open Swensen.Unquote

// utilities
let split (separator: string) (s: string) =
    s.Split([| separator |], System.StringSplitOptions.RemoveEmptyEntries) |> Seq.toList

let getLines = split "\n"

// inputs
let path = $@"{__SOURCE_DIRECTORY__}/day00_in.txt"
let inputRaw = System.IO.File.ReadAllText path
let testRaw = """"""

let preprocessing ss = ss

let testInput = preprocessing testRaw
let input = preprocessing inputRaw
// part 1
let solve_p1 input = 42

test <@ solve_p1 testInput = 42 @>

printfn "Part1: %A" (solve_p1 input)  //

// part 2
let solve_p2 input = 42

test <@ solve_p2 testInput = 42 @>

printfn "Part2: %A" (solve_p2 input)  //
