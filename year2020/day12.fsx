#r "nuget: Unquote"
open Swensen.Unquote

// utilities
let split (separator: string) (s: string) =
    s.Split([| separator |], System.StringSplitOptions.RemoveEmptyEntries)
    |> Seq.toList

let getLines = split "\n"

// inputs
let path = $"{__SOURCE_DIRECTORY__}/day12_in.txt"
let inputRaw = System.IO.File.ReadAllText path

let testRaw = """F10
N3
F7
R90
F11"""

// regex
#r "nuget: FSharp.Text.RegexProvider"
open FSharp.Text.RegexProvider

type RxPattern = Regex< @"(?<cmd>N|S|E|W|L|R|F)(?<value>\d+)" >

let regexMatch text =
    let m = RxPattern().TypedMatch text
    (m.cmd.Value, m.value.Value |> int)

let preprocessing (ss: string) = ss |> getLines |> List.map regexMatch

let testInput = preprocessing testRaw
let input = preprocessing inputRaw

type Direction =
    | North
    | East
    | South
    | West

type Ship =
    { Heading: Direction
      XPos: int
      YPos: int }

let rec rotateClockwise heading degree =
    match (heading, degree) with
    | (h, 0) -> h
    | (h, 90) ->
        match h with
        | North -> East
        | East -> South
        | South -> West
        | West -> North
    | (h, d) -> rotateClockwise (rotateClockwise h 90) (d - 90)

let move { Heading = h; XPos = x; YPos = y } (cmd, value): Ship =
    match (cmd, value) with
    | ("E", v) -> { Heading = h; XPos = x + v; YPos = y }
    | ("W", v) -> { Heading = h; XPos = x - v; YPos = y }
    | ("N", v) -> { Heading = h; XPos = x; YPos = y + v }
    | ("S", v) -> { Heading = h; XPos = x; YPos = y - v }
    | ("F", v) ->
        let dx, dy =
            match h with
            | East -> (1, 0)
            | West -> (-1, 0)
            | North -> (0, 1)
            | South -> (0, -1)

        { Heading = h
          XPos = x + dx * v
          YPos = y + dy * v }
    | ("R", v) ->
        { Heading = rotateClockwise h v
          XPos = x
          YPos = y }
    | ("L", v) ->
        { Heading = rotateClockwise h (360 - v)
          XPos = x
          YPos = y }
    | _ -> failwith "error input"

let manDist ship = abs ship.XPos + abs ship.YPos

// part 1
let solve_p1 input =
    input
    |> List.fold move { Heading = East; XPos = 0; YPos = 0 }
    |> manDist

test <@ solve_p1 testInput = 25 @>

printfn "Part1: %A" (solve_p1 input) // 445
