#r "nuget: Unquote"
open Swensen.Unquote

let path = $@"{__SOURCE_DIRECTORY__}/day09_in.txt"
let inputLines = System.IO.File.ReadAllLines path

let testLines =
    """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".Split "\n"

let preprocessing ss = ss |> Seq.map int64 |> Seq.toList

let testInput = preprocessing testLines
let input = preprocessing inputLines

// part 1

let rec combination xs =
    match xs with
    | y :: ys ->
        (ys |> List.map (fun z -> (y, z)))
        @ (combination ys)
    | _ -> []

let checkPreamble preamble value =
    preamble
    |> combination
    |> List.map (fun (x, y) -> x + y)
    |> List.contains value

let rec solve_p1 preLength input =
    let (pre, (x :: _)) = List.splitAt preLength input
    if checkPreamble pre x then solve_p1 preLength (List.tail input) else x

test <@ solve_p1 5 testInput = 127L @>

printfn "Part1: %A" (solve_p1 25 input) // 1309761972

// part 2
let findRange y xs =
    let rec helper st en acc =
        if acc = y then (st, en)
        elif acc < y then helper st (en + 1) (acc + List.item en xs)
        else helper (st + 1) en (acc - List.item st xs)
    helper 0 0 0L

test <@ findRange 127L testInput = (2, 6) @>

let solve_p2 target input =
    let (st, en) = findRange target input
    let xs = input |> List.skip st |> List.take (en - st)
    (List.min xs) + (List.max xs)

test <@ solve_p2 127L testInput = 62L @>

printfn "Part2: %A" (solve_p2 1309761972L input)  // 177989832
