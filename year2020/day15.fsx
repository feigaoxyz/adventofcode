#r "nuget: Unquote"
open Swensen.Unquote

// utilities
let split (separator: string) (s: string) =
    s.Split([| separator |], System.StringSplitOptions.RemoveEmptyEntries)
    |> Seq.toList

let getLines = split "\n"

// inputs
let path = $"{__SOURCE_DIRECTORY__}/day15_in.txt"
let inputRaw = "20,0,1,11,6,3"
let testRaw = """0,3,6"""

let preprocessing ss =
    ss |> split "," |> List.map int |> List.rev

let testInput = preprocessing testRaw
let input = preprocessing inputRaw

// part 1
let solve_p1 (input: int list) len =
    let folder xs _ =
        match xs with
        | [] -> []
        | h :: rest ->
            match List.tryFindIndex ((=) h) rest with
            | Some p -> p + 1 :: xs
            | None -> 0 :: xs

    List.fold folder input [ 1 .. (len - List.length input) ]
    |> List.head

// test <@ solve_p1 testInput 2020 = 436 @>

printfn "Part1: %A" (solve_p1 input 2020) // 421

// part 2

let mkSt xs =
    let xis = xs |> List.indexed
    let (lastP, lastV) = xis |> List.last

    let seen =
        xis
        |> List.rev
        |> List.tail
        |> List.map (fun (a, b) -> (b, a))
        |> Map.ofList

    (lastV, lastP, seen)

let solve_p2 input len =
    let folder (last, lastPos, seen) _ =
        match Map.tryFind last seen with
        | Some p -> (lastPos - p, lastPos + 1, Map.add last lastPos seen)
        | None -> (0, lastPos + 1, Map.add last lastPos seen)

    let initSt = mkSt (input |> List.rev)

    List.fold folder initSt [ (List.length input) .. (len - 1) ]
    |> fun (last, _, _) -> last

// test <@ solve_p2 testInput 30000000 = 175594 @>

printfn "Part2: %A" (solve_p2 input 30000000) // 436
