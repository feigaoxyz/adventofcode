#r "nuget: Unquote"
open Swensen.Unquote

let path = $@"{__SOURCE_DIRECTORY__}/day01_in.txt"

let input =
    System.IO.File.ReadAllLines path
    |> Seq.map int
    |> Seq.toList

let rec getPairs =
    function
    | [] -> []
    | x :: xs -> (xs |> List.map (fun y -> (x, y))) @ (getPairs xs)

let rec getTriples xs =
    match xs with
    | x :: ys ->
        (ys |> getTriples)
        @ (ys
           |> getPairs
           |> List.map (fun (y, z) -> (x, y, z)))
    | otherwise -> []


let solve1 xs =
    xs
    |> getPairs
    |> List.filter (fun (x, y) -> x + y = 2020)
    |> List.map (fun (x, y) -> x * y)
    |> List.tryHead

let testInput = [ 1721; 979; 366; 299; 675; 1456 ]
test <@ solve1 testInput = Some 514579 @>

printfn "Part1: %A" (solve1 input)


let solve2 xs =
    xs
    |> getTriples
    |> List.filter (fun (x, y, z) -> x + y + z = 2020)
    |> List.map (fun (x, y, z) -> x * y * z)
    |> List.tryHead

test <@ solve2 testInput = Some 241861950 @>

printfn "Part2: %A" (solve2 input)
