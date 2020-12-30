#r "nuget: Unquote"
open Swensen.Unquote

// utilities
let split (separator: string) (s: string) =
    s.Split([| separator |], System.StringSplitOptions.RemoveEmptyEntries)

let getLines = split "\n"

// inputs
let path = $@"{__SOURCE_DIRECTORY__}/day11_in.txt"
let inputRaw = System.IO.File.ReadAllText path

let testRaw = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

type Seat =
    | Floor
    | Empty
    | Occupied

let preprocessing ss =
    ss
    |> getLines
    |> Seq.map
        (Seq.map (fun x -> if x = 'L' then Empty else Floor)
         >> Seq.toList)
    |> Seq.toList

let testInput = preprocessing testRaw
let input = preprocessing inputRaw

let dxy8 =
    let s = [ -1; 0; 1 ]
    List.allPairs s s |> List.filter ((<>) (0, 0))


let inRange (mr, mc) (r, c) = (0 <= r && r < mr) && (0 <= c && c < mc)

let getAdjacent1 seats (r, c) =
    let (mr, mc) =
        (List.length seats, List.length seats.[0])

    dxy8
    |> List.map (fun (dr, dc) -> (r + dr, c + dc))
    |> List.filter (inRange (mr, mc))
    |> List.map (fun (nr, nc) -> seats.[nr].[nc])

let getAdjacent2 seats (r, c) =
    let (mr, mc) =
        (List.length seats, List.length seats.[0])

    dxy8
    |> List.map (fun (dr, dc) ->
        List.unfold (fun (nr, nc) ->
            let (nnr, nnc) = (nr + dr, nc + dc)
            if inRange (mr, mc) (nnr, nnc) then Some(seats.[nnr].[nnc], (nnr, nnc)) else None) (r, c)
        |> List.skipWhile ((=) Floor)
        |> List.tryHead)
    |> List.map Option.toList
    |> List.concat


let transformPos (seats: Seat list list) getAdjFun crowded (r, c) =
    let seat = seats.[r].[c]
    let neighbors = getAdjFun seats (r, c)
    if seat = Empty
       && (List.contains Occupied neighbors |> not) then
        Occupied
    elif seat = Occupied
         && (List.sumBy (fun x -> if x = Occupied then 1 else 0) neighbors
             >= crowded) then
        Empty
    else
        seat

let rec moveUntil adjFun crowded seats =
    let oneRound (seats: Seat list list) =
        seats
        |> List.mapi (fun r -> List.mapi (fun c _ -> transformPos seats adjFun crowded (r, c)))

    let newSeats = oneRound seats
    if newSeats = seats then seats else moveUntil adjFun crowded newSeats

let countOccupied = List.sumBy (fun row -> List.sumBy (fun s -> if s = Occupied then 1 else 0) row)

// part 1
let solve_p1 = moveUntil getAdjacent1 4 >> countOccupied


test <@ solve_p1 testInput = 37 @>

printfn "Part1: %A" (solve_p1 input) // 2254

// part 2
let solve_p2 = moveUntil getAdjacent2 5 >> countOccupied


test <@ solve_p2 testInput = 26 @>

printfn "Part2: %A" (solve_p2 input) // 2004
