#r "nuget: Unquote"
open Swensen.Unquote

let path = $@"{__SOURCE_DIRECTORY__}/input.txt"
let lines = System.IO.File.ReadAllLines path

let input = lines

let solve1 input = 42

let testInput = []
test <@ solve1 testInput = None @>

printfn "Part1: %A" (solve1 input)
