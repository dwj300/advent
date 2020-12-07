use std::fs;
use std::collections::{HashMap, HashSet};
use regex::Regex;

fn parse<'a>(lines: &[&'a str]) -> HashMap<&'a str, Vec<(i32, &'a str)>> {
    let p = Regex::new(r"([0-9]+) ([a-z ]+)").unwrap();
    let mut rules:HashMap<&str, Vec<(i32, &str)>> = HashMap::new();
    for line in lines {
        if line.trim().len() == 0 {
            continue;
        }
        let parts: Vec<&str> = line.split("bags contain ").collect();
        let src: &str = parts.get(0).unwrap().trim();
        let mut targets: Vec<(i32, &str)> = Vec::new();
        if !line.contains("contain no other bags") {
            let second = parts.get(1).unwrap();
            for part in second.split(',') {
                let combo = part.trim().split(" bag").nth(0).unwrap();
                let g = p.captures(combo).unwrap();
                let num = g.get(1).unwrap().as_str().parse::<i32>().unwrap();
                let name = g.get(2).unwrap().as_str();
                targets.push((num, name));
            }
        }
        rules.insert(src, targets);
    }
    return rules;
}

fn search<'a>(start: &'a str, rules: &HashMap<&str, Vec<(i32, &str)>>, seen: HashSet<&'a str>) -> bool {
    if start == "shiny gold"{
        return true;
    }
    if seen.contains(start) || !rules.contains_key(start) || (rules.contains_key(start) && rules.get(start).unwrap().len() == 0) {
        return false;
    }
    let mut seen2 = seen.clone();
    seen2.insert(start);
    for s in rules.get(start).unwrap() {
        let t = s.1;
        if search(t, rules, seen2.clone()) {
            return true;
        }
    }
    return false;
}

fn recurse(k: &str, rules: &HashMap<&str, Vec<(i32, &str)>>) -> i32 {
    if rules.contains_key(k) && rules.get(k).unwrap().len() == 0 {
        return 0;
    }
    let mut sum = 0;
    for rule in rules.get(k).unwrap() {
        sum += rule.0 + rule.0 * recurse(rule.1, rules);
    }
    return sum;
}

fn part1(lines: &[&str]) -> i32 {
    let rules = parse(lines);
    let mut count = 0;
    for key in rules.keys() {
        if *key != "shiny gold" && search(key, &rules, HashSet::new()) {
            count += 1;
        }
    }
    return count;
}

fn part2(lines: &[&str]) -> i32 {
    let rules = parse(lines);
    return recurse("shiny gold", &rules);
}

pub fn day7() {
    let sample1: Vec<&str> = "
    light red bags contain 1 bright white bag, 2 muted yellow bags.
    dark orange bags contain 3 bright white bags, 4 muted yellow bags.
    bright white bags contain 1 shiny gold bag.
    muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
    shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    faded blue bags contain no other bags.
    dotted black bags contain no other bags.
    ".lines().collect();
    let sample2: Vec<&str> = "faded blue bags contain no other bags.
    dotted black bags contain no other bags.
    vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
    dark olive bags contain 3 faded blue bags, 4 dotted black bags.
    shiny gold bags contain 1 dark olive bags, 2 vibrant plum bags.".lines().collect();
    let sample3: Vec<&str> = "shiny gold bags contain 2 dark red bags.
    dark red bags contain 2 dark orange bags.
    dark orange bags contain 2 dark yellow bags.
    dark yellow bags contain 2 dark green bags.
    dark green bags contain 2 dark blue bags.
    dark blue bags contain 2 dark violet bags.
    dark violet bags contain no other bags.".lines().collect();

    assert_eq!(part1(&sample1), 4);

    let contents = fs::read_to_string("day7.txt").unwrap();
    let input: Vec<&str> = contents.lines().collect();
    let ans1 = part1(&input);
    println!("{}", ans1);
    assert_eq!(ans1, 332);

    assert_eq!(part2(&sample2), 32);
    assert_eq!(part2(&sample3), 126);
    let ans2 = part2(&input);
    println!("{}", ans2);
    assert_eq!(ans2, 10875);
}