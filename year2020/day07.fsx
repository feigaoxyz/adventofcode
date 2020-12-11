#r "nuget: Unquote"
open Swensen.Unquote

#r "nuget: FSharp.Text.RegexProvider"
open FSharp.Text.RegexProvider

// utilities
let split (separator: string) (s: string) =
    s.Split([| separator |], System.StringSplitOptions.RemoveEmptyEntries)

// raw inputs
let path = $@"{__SOURCE_DIRECTORY__}/day07_in.txt"
let inputLines = System.IO.File.ReadAllLines path

let testLines =
    """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
    |> split "\n"

// input processing

type Rule =
    { source: string
      targets: (int * string) seq }

type BagRules = Rule list

type RuleRegex = Regex< @"^(?<bag>\S+ \S+) bags contain (?<rule>.*)\." >
type TargetRegex = Regex< @"(?<count>\d+) (?<target>\S+ \S+) bags?" >

let readRule text =
    let m = text |> RuleRegex().TypedMatch
    let bag = m.bag.Value
    let ruleString = m.rule.Value

    let targets =
        ruleString
        |> TargetRegex().TypedMatches
        |> Seq.map (fun m -> (int m.count.Value, m.target.Value))

    { source = bag; targets = targets }


let preprocessing ss: BagRules = ss |> Seq.map readRule |> Seq.toList

// processed inputs
let testInput = preprocessing testLines
let input = preprocessing inputLines

// part 1
let inTarget bag rule =
    Seq.contains bag (Seq.map snd rule.targets)

let gold = "shiny gold"

let solve_p1 input =
    let rec helper rules seen unseen =
        // printfn "in helper: \n\tseen %A \n\tunseen %A" seen unseen
        if Set.isEmpty unseen then
            seen
        else
            let allContainer =
                unseen
                |> Set.map (fun bag ->
                    rules
                    |> List.filter (inTarget bag)
                    |> List.map (fun r -> r.source)
                    |> Set.ofList)
                |> Set.unionMany
            let newSeen = Set.union seen unseen
            let newUnseen = Set.difference allContainer newSeen
            helper rules newSeen newUnseen

    (helper input Set.empty (Set.singleton gold) |> Set.count) - 1


test <@ solve_p1 testInput = 4 @>

printfn "Part1: %A" (solve_p1 input)  // 151

// part 2
let solve_p2 input =
    let rec helper rules bag =
        rules
        |> List.find (fun rule -> rule.source = bag)
        |> fun rule -> rule.targets
        |> Seq.sumBy (fun (count, b) -> count + count * (helper rules b))
    helper input gold


test <@ solve_p2 testInput = 32 @>

printfn "Part2: %A" (solve_p2 input)  // 41559
