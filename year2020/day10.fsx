#r "nuget: Unquote"
open Swensen.Unquote

let path = $@"{__SOURCE_DIRECTORY__}/day10_in.txt"
let inputLines = System.IO.File.ReadAllLines path
let testLines =
    let s = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
    s.Split "\n"

let preprocessing = Seq.toList >> List.map int >> List.append [0] >> List.sort

let testInput = preprocessing testLines
let input = preprocessing inputLines

// part 1
let solve_p1 input =
    let diffs = 
        input
        |> List.pairwise
        |> List.map (fun (fst, snd) -> snd - fst)
        |> List.groupBy (fun x -> x)
    let findDiff df xs = 
        match List.tryFind (fun (d, _) -> d = df) xs with
        | None -> 0
        | Some (_, ds) -> List.length ds
    let one = findDiff 1 diffs
    let three = findDiff 3 diffs + 1
    one * three

test <@ solve_p1 testInput = 220 @>

printfn "Part1: %A" (solve_p1 input)  // 2040

// part 2
let solve_p2 input =
    let acc = (0, 1L) :: (input |> List.tail |> List.map (fun v -> (v, 0L)))
    printfn "Acc %A" acc
    let rec helper xys =
        match xys with
        | [] -> 0L
        | [(x, y)] -> y
        | (x,y) :: tail -> 
            let low = tail |> List.takeWhile (fun (k, v) -> k <= x + 3) |> List.map (fun (k, v) -> (k, v + y))
            let high = tail |> List.skip (low |> List.length)
            helper (List.append low high)
    helper acc

test <@ solve_p2 testInput = 19208L @>

printfn "Part2: %A" (solve_p2 input)  // 28346956187648L
