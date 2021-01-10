#r "nuget: Unquote"
open Swensen.Unquote

// utilities
let split (separator: string) (s: string) =
    s.Split([| separator |], System.StringSplitOptions.RemoveEmptyEntries)
    |> Seq.toList

let getLines = split "\n"

// inputs
let path = $"{__SOURCE_DIRECTORY__}/day14_in.txt"
let inputRaw = System.IO.File.ReadAllText path

let testRaw = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

#r "nuget: FSharp.Text.RegexProvider"
open FSharp.Text.RegexProvider

type CmdRegex = Regex< @"(?<cmd>[0-9X]+)" >

type Cmd =
    | Mask of string
    | Mem of (int64 * int64)

let parseLine (text: string) =
    match text.[1] with
    | 'a' ->
        let m = CmdRegex().TypedMatch text
        Mask m.cmd.Value
    | _ ->
        let ms =
            CmdRegex().TypedMatches text |> Seq.toList

        Mem(int64 ms.[0].cmd.Value, int64 ms.[1].cmd.Value)

let preprocessing ss = ss |> getLines |> List.map parseLine

let testInput = preprocessing testRaw
let input = preprocessing inputRaw

let set1 value pos = value ||| (1L <<< pos)
let set0 value pos = value &&& (~~~(1L <<< pos))

let findIndices p xs =
    xs
    |> List.indexed
    |> List.filter (snd >> p)
    |> List.map fst

type Program =
    { Mask: string
      Mems: Map<int64, int64> }

// part 1
let mask1 (m: string) (v: int64) =
    let mr = m |> List.ofSeq |> List.rev
    let d0 = mr |> findIndices ((=) '0')
    let d1 = mr |> findIndices ((=) '1')
    List.fold set1 (List.fold set0 v d0) d1

let stepFun1 p cmd =
    match cmd with
    | Mask m -> { Mask = m; Mems = p.Mems }
    | Mem (k, v) ->
        { Mask = p.Mask
          Mems = Map.add k (mask1 p.Mask v) p.Mems }

let solve_p1 input =
    let p = { Mask = ""; Mems = Map.empty }
    let pEnd = List.fold stepFun1 p input
    pEnd.Mems |> Map.fold (fun acc _ v -> acc + v) 0L

test <@ solve_p1 testInput = 165L @>
printfn "Part1: %A" (solve_p1 input) // 13476250121721

// part 2
let mask2 (m: string) (v: int64) =
    let mr = m |> List.ofSeq |> List.rev
    let d1 = mr |> findIndices ((=) '1')
    let dx = mr |> findIndices ((=) 'X')
    let v1 = List.fold set1 v d1
    List.fold (fun st p -> List.collect (fun v -> [ set0 v p; set1 v p ]) st) [ v1 ] dx


let stepFun2 p cmd =
    match cmd with
    | Mask m -> { Mask = m; Mems = p.Mems }
    | Mem (k, v) ->
        { Mask = p.Mask
          Mems =
              mask2 p.Mask k
              |> List.fold (fun m kk -> Map.add kk v m) p.Mems }


let solve_p2 input =
    let p = { Mask = ""; Mems = Map.empty }
    let pEnd = List.fold stepFun2 p input
    pEnd.Mems |> Map.fold (fun acc _ v -> acc + v) 0L

let testInput2 =
    """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
    |> getLines
    |> List.map parseLine

test <@ solve_p2 testInput2 = 208L @>
printfn "Part2: %A" (solve_p2 input) // 4463708436768
