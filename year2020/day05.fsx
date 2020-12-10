#r "nuget: Unquote"
open Swensen.Unquote

let path = $@"{__SOURCE_DIRECTORY__}/day05_in.txt"
let inputLines = System.IO.File.ReadAllLines path
let testLines = @"BBFFBBFRLL".Split "\n"

let readLine (text: string) =
    let readBinary s = int ("0b" + s)

    let row =
        text.[0..6]
        |> String.collect (fun c -> if c = 'F' then "0" else "1")
        |> readBinary

    let col =
        text.[7..]
        |> String.collect (fun c -> if c = 'L' then "0" else "1")
        |> readBinary

    row * 8 + col

test <@ readLine "BFFFBBFRRR" = 567 @>
test <@ readLine "FFFBBBFRRR" = 119 @>
test <@ readLine "BBFFBBFRLL" = 820 @>

let preprocessing ss = ss |> Seq.map readLine |> Seq.sort

let testInput = preprocessing testLines
let input = preprocessing inputLines

// part 1

let solve_p1 = Seq.max

test <@ solve_p1 testInput = 820 @>

printfn "Part1: %A" (solve_p1 input) // 901

// part 2
let solve_p2 input =
    input
    |> Seq.pairwise
    |> Seq.pick (fun (f, s) -> if s - f = 1 then None else Some(f + 1))


// test <@ solve_p2 testInput = 42 @>

printfn "Part2: %A" (solve_p2 input) // 661
