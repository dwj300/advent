use std::fs;
use std::collections::HashSet;

fn split(line: &str, mut r: [i32; 2], target: char, i: usize, j: usize) -> i32 {
    for l in line[i..j].chars() {
        if l == target {
            r[1] = ((r[1] - r[0]) / 2) + r[0];
        }
        else {
            r[0] = ((r[1] as f32 - r[0] as f32) / 2.0).round() as i32 + r[0];
        }
    }
    return if line.chars().nth(j).unwrap() == target { r[0] } else { r[1] };
}

fn seat(line: &str) -> i32 {
    let row = split(line, [0, 127], 'F', 0, 7);
    let col = split(line, [0, 7], 'L', 7, 9);
    return row * 8 + col
}

fn part1(lines: &[&str]) -> i32 {
    return lines.iter().map(|line| seat(line)).max().unwrap();
}

fn part2(lines: &[&str]) -> i32 {
    let seats: Vec<i32> = lines.into_iter().map(|line| seat(line)).collect();
    let seats_set: HashSet<i32> = seats.clone().into_iter().collect();
    let min = seats.clone().into_iter().min().unwrap();
    let max = seats.clone().into_iter().max().unwrap();
    let nums: HashSet<i32> = (min..=max).into_iter().collect();
    return *nums.difference(&seats_set).nth(0).unwrap();
}

pub fn day5() {
    let contents = fs::read_to_string("day5.txt").unwrap();
    let input: Vec<&str> = contents.lines().collect();
    assert_eq!(seat("FBFBBFFRLR"), 357);
    let mut out = part1(&input);
    println!("{}", out);
    assert_eq!(out, 838);
    out = part2(&input);
    println!("{}", out);
    assert_eq!(out, 714);
}