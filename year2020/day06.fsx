#r "nuget: Unquote"
open Swensen.Unquote

#r "nuget: FSharp.Text.RegexProvider"
open FSharp.Text.RegexProvider

let path = $@"{__SOURCE_DIRECTORY__}/day06_in.txt"
let inputLines = System.IO.File.ReadAllText path

let testLines = """abc

a
b
c

ab
ac

a
a
a
a

b"""

let split (separator: string) (s: string) =
    s.Split([| separator |], System.StringSplitOptions.RemoveEmptyEntries)

let preprocessing = split "\n\n"

let testInput = preprocessing testLines
let input = preprocessing inputLines

// part 1
let solve_p1 input =
    input
    |> Seq.map (String.collect (fun c -> if c = '\n' then "" else (string c)))
    |> Seq.map Seq.distinct
    |> Seq.sumBy Seq.length

test <@ solve_p1 testInput = 11 @>

printfn "Part1: %A" (solve_p1 input) // 6534

// part 2
let solve_p2 (input: seq<string>) =
    input
    |> Seq.map
        (split "\n"
         >> Seq.map Set.ofSeq
         >> Set.intersectMany)
    |> Seq.sumBy Set.count


test <@ solve_p2 testInput = 6 @>

printfn "Part2: %A" (solve_p2 input) // 3402
