#r "nuget: Unquote"
#r "nuget: FSharp.Text.RegexProvider"

open Swensen.Unquote
open FSharp.Text.RegexProvider

let path = $@"{__SOURCE_DIRECTORY__}/day04_in.txt"
let inputLines = System.IO.File.ReadAllLines path

let testLines =
    let s = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

    s.Split '\n'

type KVP = { Key: string; Value: string }

type Passport = KVP list

type KVPRegex = Regex<"(?<key>\S+):(?<value>\S+)">

let parsePassword text: Passport =
    text
    |> KVPRegex().TypedMatches
    |> Seq.map (fun kvp ->
        { Key = kvp.key.Value
          Value = kvp.value.Value })
    |> Seq.toList

let preprocessing ss =
    ss
    |> String.concat "\n"
    |> fun s -> s.Split "\n\n"
    |> Seq.map parsePassword

let testInput = preprocessing testLines
// printfn "%A" (testInput |> Seq.map List.length)
let input = preprocessing inputLines

// part 1

let requiredKeys =
    [ "byr"
      "iyr"
      "eyr"
      "hgt"
      "hcl"
      "ecl"
      "pid" ]

let hasRequiredKeys (pp: Passport): bool =
    requiredKeys
    |> Seq.forall (fun key -> List.exists (fun kvp -> kvp.Key = key) pp)

let solve_p1 input =
    input |> Seq.filter hasRequiredKeys |> Seq.length

test <@ solve_p1 testInput = 2 @>

printfn "Part1: %A" (solve_p1 input)

// part 2

let between low high value = low <= value && value <= high

type YearRegex = Regex<"^(?<year>\d{4})$">

let validYear low hi (ys: string) =
    match YearRegex().TryTypedMatch ys with
    | Some m ->
        let y = int m.year.Value
        m.year.Value.Length = 4 && between low hi y
    | _ -> false

let validBirthYear = validYear 1920 2002
let validIssueYear = validYear 2010 2020
let validExpirationYear = validYear 2020 2030

type HeightRegex = Regex<"^(?<value>\d+)(?<unit>cm|in)$">

let validHeight (hs: string) =
    match HeightRegex().TryTypedMatch hs with
    | Some m ->
        let h = int m.value.Value
        match m.unit.Value with
        | "cm" -> between 150 193 h
        | "in" -> between 59 76 h
        | _ -> false
    | _ -> false

type HairColorRegex = Regex<"^#[0-9a-f]{6}$">
let validHairColor: string -> bool = HairColorRegex().IsMatch

type EyeColorRegex = Regex<"^amb|blu|brn|gry|grn|hzl|oth$">
let validEyeColor: string -> bool = EyeColorRegex().IsMatch

type PIDRegex = Regex<"^[0-9]{9}$">
let validPassportID = PIDRegex().IsMatch

let validPassport (pp: Passport): bool =
    pp
    |> Seq.forall (fun kvp ->
        (match kvp.Key with
         | "byr" -> validBirthYear
         | "iyr" -> validIssueYear
         | "eyr" -> validExpirationYear
         | "hgt" -> validHeight
         | "hcl" -> validHairColor
         | "ecl" -> validEyeColor
         | "pid" -> validPassportID
         | "cid" -> fun _ -> true
         | _ -> fun _ -> false) kvp.Value)

let solve_p2 pps =
    pps |> Seq.filter validPassport |> Seq.filter hasRequiredKeys |> Seq.length

test <@ solve_p2 testInput = 2 @>
printfn "Part2: %A" (solve_p2 input)  // 147
