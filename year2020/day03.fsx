#r "nuget: Unquote"
open Swensen.Unquote

let path = $@"{__SOURCE_DIRECTORY__}/day03_in.txt"
let inputLines = System.IO.File.ReadAllLines path

let testLines = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""" |> fun s -> s.Split '\n'

type Map = {row: int; col: int; map: char list list }

let preprocessing ss =
    let map = ss |> Seq.toList |> List.map Seq.toList
    let row = map |> Seq.length
    let col = map.[0] |> Seq.length
    { row = row; col = col; map = map }

let testInput = preprocessing testLines
let input = preprocessing inputLines

let queryMap r c map = map.map.[r % map.row].[c % map.col]

let lcm x y =
    let rec gcd x y = if x % y = 0 then y else gcd y (x % y)
    x * y / (gcd x y)

// part 1
let solve_p1 map right down =
    // List.init (lcm map.row down) (fun i -> queryMap (down * i) (right * i) map )
    List.init (1 + map.row / down) (fun i -> queryMap (down * i) (right * i) map )
    |> List.filter (fun c -> c = '#')
    |> List.length

test <@ solve_p1 testInput 3 1 = 7 @>

printfn "Part1: %A" (solve_p1 input 3 1)

// part 2
let solve_p2 input =
    [ (1, 1); (3, 1); (5, 1); (7, 1); (1, 2) ]
    |> Seq.map (fun (r, d) -> solve_p1 input r d)
    |> Seq.reduce (fun x y -> x * y)

test <@ solve_p2 testInput = 336 @>

printfn "Part2: %A" (solve_p2 input)
