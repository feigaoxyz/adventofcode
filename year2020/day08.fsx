#r "nuget: Unquote"
open Swensen.Unquote

#r "nuget: FSharp.Text.RegexProvider"
open FSharp.Text.RegexProvider

// utilities
let split (separator: string) (s: string) =
    s.Split([| separator |], System.StringSplitOptions.RemoveEmptyEntries)

// inputs
let path = $@"{__SOURCE_DIRECTORY__}/day08_in.txt"
let inputLines = System.IO.File.ReadAllLines path

let testLines =
    split "\n" """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

type Operation =
    | Acc of int
    | Jmp of int
    | Nop of int

type InstructionRegex = Regex< @"(?<op>acc|jmp|nop) (?<arg>[+-]\d+)" >

let readInstruction line =
    let m = line |> InstructionRegex().TypedMatch
    let arg = int m.arg.Value
    match m.op.Value with
    | "acc" -> Acc arg
    | "jmp" -> Jmp arg
    | _ -> Nop arg

type Program = Operation list

type Runtime =
    { acc: int
      curPos: int
      posHist: int list
      prog: Program }

let step (runtime: Runtime): Runtime =
    match runtime.prog.[runtime.curPos] with
    | Acc arg ->
        { acc = runtime.acc + arg
          curPos = runtime.curPos + 1
          posHist = runtime.curPos :: runtime.posHist
          prog = runtime.prog }
    | Jmp arg ->
        { acc = runtime.acc
          curPos = runtime.curPos + arg
          posHist = runtime.curPos :: runtime.posHist
          prog = runtime.prog }
    | Nop _ ->
        { acc = runtime.acc
          curPos = runtime.curPos + 1
          posHist = runtime.curPos :: runtime.posHist
          prog = runtime.prog }

type ProgReturn =
    | Loop
    | Exit
    | Exception
    | Normal

let checkStatus (rt: Runtime): ProgReturn =
    if (List.contains rt.curPos rt.posHist) then Loop
    elif rt.curPos = rt.prog.Length then Exit
    elif rt.curPos > rt.prog.Length || rt.curPos < 0 then Exception
    else Normal

let runProg (prog: Program): ProgReturn * Runtime =
    let rec helper rt =
        match checkStatus rt with
        | Normal -> helper (step rt)
        | st -> (st, rt)

    let initRt =
        { acc = 0
          curPos = 0
          posHist = List.empty
          prog = prog }

    helper initRt

let preprocessing ss =
    ss |> Seq.map readInstruction |> Seq.toList

let testInput = preprocessing testLines
let input = preprocessing inputLines

// part 1
let solve_p1 input =
    let (st, rt) = runProg input
    rt.acc

test <@ solve_p1 testInput = 5 @>

printfn "Part1: %A" (solve_p1 input) // 1709

// part 2

let alterProg prog idx =
    let p1 = prog |> List.take idx
    let p2 = prog |> List.skip (idx + 1)

    let p =
        match prog.[idx] with
        | Nop arg -> Jmp arg
        | Jmp arg -> Nop arg
        | Acc arg -> Acc arg

    p1 @ (p :: p2)

let solve_p2 (prog: Program) =
    prog
    |> List.indexed
    |> List.choose (function
        | (_, Acc _) -> None
        | (idx, _) -> Some idx)
    |> List.map (alterProg prog)
    |> List.skipWhile (fun prog ->
        match runProg prog with
        | (Exit, rt) -> false
        | _ -> true)
    |> List.head
    |> runProg
    |> snd
    |> fun rt -> rt.acc

test <@ solve_p2 testInput = 8 @>

printfn "Part2: %A" (solve_p2 input) // 1976
