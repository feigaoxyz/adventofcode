#r "nuget: Unquote"
#r "nuget: FSharp.Text.RegexProvider"

open Swensen.Unquote
open System.Text.RegularExpressions
open FSharp.Text.RegexProvider

let path = $@"{__SOURCE_DIRECTORY__}/day02_in.txt"
let lines = System.IO.File.ReadAllLines path

let testInput =
    [ "1-3 a: abcde"
      "1-3 b: cdefg"
      "2-9 c: ccccccccc" ]


type Password =
    { min: int
      max: int
      character: char
      password: string }

let isPasswordValid1 password =
    password.password
    |> Seq.filter (fun y -> y = password.character)
    |> Seq.length
    |> fun x -> x >= password.min && x <= password.max

type PasswordRegex = Regex< @"(?<min>\d+)-(?<max>\d+) (?<char>\w): (?<pass>\w+)" >

let tryReadPassword line =
    match PasswordRegex().TryTypedMatch(line) with
    | Some m ->
        Some
            { min = int m.min.Value
              max = int m.max.Value
              character = char m.char.Value
              password = m.pass.Value }
    | None -> None

printfn "test password reading: %A" (tryReadPassword "2-9 c: ccccccccc")

let solve1 input =
    input |> Seq.map (tryReadPassword >> Option.toList) |> Seq.concat |> Seq.filter (isPasswordValid1) |> Seq.length

test <@ solve1 testInput = 2 @>

printfn "Part1: %A" (solve1 lines)

let isPasswordValid2 password =
    [ password.password.[password.min - 1] = password.character
      password.password.[password.max - 1] = password.character ]
    |> Seq.filter (fun x -> x)
    |> Seq.length
    |> fun x -> x = 1

let solve2 input =
    input |> Seq.map (tryReadPassword >> Option.toList) |> Seq.concat |> Seq.filter (isPasswordValid2) |> Seq.length


test <@ solve2 testInput = 1 @>

printfn "Part2: %A" (solve2 lines)
