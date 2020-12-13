// inline testing
#r "nuget: Unquote"
open Swensen.Unquote

test <@ 1 = 1 @>

// regex
#r "nuget: FSharp.Text.RegexProvider"
open FSharp.Text.RegexProvider

type RxPattern = Regex< @"(?<key>\d+)" >
let regexMatch text = RxPattern().TypedMatch text

// split
let split (sep: string) (text: string) = text.Split sep

// combination
let rec combination xs =
    match xs with
    | y :: ys ->
        (ys |> List.map (fun z -> (y, z)))
        @ (combination ys)
    | [] -> []
