use std::fs;
use std::collections::{HashMap, HashSet};

fn part1(lines: &[&str]) -> i32 {
    let mut groups: Vec<i32> = Vec::new();
    let mut group = HashSet::new();
    for line in lines {
        if *line == "" {
            groups.push(group.len() as i32);
            group = HashSet::new();
        }
        else {
            for c in line.chars() {
                group.insert(c);
            }
        }
    }
    return groups.iter().sum();
}

fn part2(lines: &[&str]) -> i32 {
    let mut groups: Vec<i32> = Vec::new();
    let mut group = HashMap::new();
    let mut count = 0;
    for line in lines {
        if *line == "" {
            let mut n = 0;
            for (_k,v) in group {
                if v == count {
                    n += 1;
                }
            }
            groups.push(n);
            group = HashMap::new();
            count = 0
        }
        else {
            for c in line.chars() {
                let x = group.entry(c).or_insert(0);
                *x += 1;
            }
            count += 1;
        }
    }
    return groups.iter().sum();
}

pub fn day6() {
    let contents = fs::read_to_string("day6.txt").unwrap();
    let input: Vec<&str> = contents.lines().collect();
    let mut out = part1(&input);
    println!("{}", out);
    assert_eq!(out, 6714);
    out = part2(&input);
    println!("{}", out);
    assert_eq!(out, 3435);
}