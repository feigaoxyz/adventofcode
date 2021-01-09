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

type Ship = { Pos: int * int; Waypoint: int * int }

let rec rotateClockwise heading degree =
    match (heading, degree) with
    | (h, 0) -> h
    | ((dx, dy), 90) -> (dy, -dx)
    | (h, d) -> rotateClockwise (rotateClockwise h 90) (d - 90)

let move (ship: Ship) (cmd, value): Ship =
    let x, y = ship.Pos
    let dx, dy = ship.Waypoint

    match (cmd, value) with
    | ("E", v) ->
        { Pos = ship.Pos
          Waypoint = (dx + v, dy) }
    | ("W", v) ->
        { Pos = ship.Pos
          Waypoint = (dx - v, dy) }
    | ("N", v) ->
        { Pos = ship.Pos
          Waypoint = (dx, dy + v) }
    | ("S", v) ->
        { Pos = ship.Pos
          Waypoint = (dx, dy - v) }
    | ("F", v) ->
        { Pos = (x + dx * v, y + dy * v)
          Waypoint = ship.Waypoint }
    | ("R", v) ->
        { Pos = ship.Pos
          Waypoint = rotateClockwise ship.Waypoint v }
    | ("L", v) ->
        { Pos = ship.Pos
          Waypoint = rotateClockwise ship.Waypoint (360 - v) }
    | _ -> failwith "error input"

let manDist ship =
    let x, y = ship.Pos
    abs x + abs y

// part 2
let solve_p2 input =
    input
    |> List.fold move { Pos = (0, 0); Waypoint = (10, 1) }
    |> manDist


test <@ solve_p2 testInput = 286 @>

printfn "Part2: %A" (solve_p2 input) // 42495
