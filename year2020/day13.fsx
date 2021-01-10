#r "nuget: Unquote"
open Swensen.Unquote

// utilities
let split (separator: string) (s: string) =
    s.Split([| separator |], System.StringSplitOptions.RemoveEmptyEntries)
    |> Seq.toList

let getLines = split "\n"

// inputs
let path = $"{__SOURCE_DIRECTORY__}/day13_in.txt"
let inputRaw = System.IO.File.ReadAllText path

type Bus =
    | ID of int64
    | X

let testRaw = """939
7,13,x,x,59,x,31,19"""

let preprocessing ss =
    let tS, busS =
        match getLines ss with
        | [ t; b ] -> t, b
        | _ -> failwith "wrong input format"

    let currentTS = int64 tS

    let buses =
        busS
        |> split ","
        |> List.map (fun x -> if x = "x" then X else ID(int64 x))

    (currentTS, buses)

let testInput = preprocessing testRaw
let input = preprocessing inputRaw

// part 1
let solve_p1 input =
    let current, buses = input

    let minBus, minTime =
        buses
        |> List.filter ((<>) X)
        |> List.map (fun (ID x) -> x)
        |> List.map
            (fun cycle ->
                (cycle,
                 if current % cycle = 0L then
                     current
                 else
                     cycle * (current / cycle + 1L)))
        |> List.minBy snd

    minBus * (minTime - current)

test <@ solve_p1 testInput = 295L @>

printfn "Part1: %A" (solve_p1 input) // 1835

// part 2

let rec sieve cs x N =
    match cs with
    | [] -> Some x
    | (a, n) :: rest ->
        let arrProgress = Seq.unfold (fun x -> Some(x, x + N)) x
        let firstXmodNequalA = Seq.tryFind (fun x -> a = x % n)

        match firstXmodNequalA (Seq.take (int n) arrProgress) with
        | None -> None
        | Some x -> sieve rest x (N * n)

let rem x n = ((x % n) + n) % n

let chineseRemainderTheorem congruences =
    let cs =
        congruences
        |> List.map (fun (a, n) -> (rem a n, n))
        |> List.sortBy (snd >> (~-))

    let an = List.head cs
    sieve (List.tail cs) (fst an) (snd an)


let solve_p2 input =
    let _, buses = input

    let busRem =
        buses
        |> List.mapi
            (fun i b ->
                match b with
                | X -> []
                | ID x -> [ (-(int64 i), x) ])
        |> List.concat

    match chineseRemainderTheorem busRem with
    | Some v -> v
    | _ -> failwith "no answer"


test <@ solve_p2 testInput = 1068781L @>
printfn "Part2: %A" (solve_p2 input) // 247086664214628L
