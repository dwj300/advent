use std::fs;
use regex::Regex;

fn part1(input: &[&str]) -> i32 {
    let mut num = 0;
    let p = Regex::new(r"(?P<min>[0-9]+)-(?P<max>[0-9]+) (?P<letter>[a-z]): (?P<pw>[a-z]+)").unwrap();
    for line in input.iter() {
        let caps = p.captures(line).unwrap();
        let min: usize = caps.name("min").unwrap().as_str().parse().unwrap();
        let max: usize = caps.name("max").unwrap().as_str().parse().unwrap();
        let letter: char = caps.name("letter").unwrap().as_str().chars().next().unwrap();
        let pw: &str = caps.name("pw").unwrap().as_str();
        let count = pw.matches(|c| c == letter).count();
        if count >= min && count <= max {
            num += 1;
        }
    }
    num
}

fn part2(input: &[&str]) -> i32 {
    let mut num = 0;
    let p = Regex::new(r"(?P<min>[0-9]+)-(?P<max>[0-9]+) (?P<letter>[a-z]): (?P<pw>[a-z]+)").unwrap();
    for line in input.iter() {
        let caps = p.captures(line).unwrap();
        let min: usize = caps.name("min").unwrap().as_str().parse::<usize>().unwrap()-1;
        let max: usize = caps.name("max").unwrap().as_str().parse::<usize>().unwrap()-1;
        let letter: char = caps.name("letter").unwrap().as_str().chars().next().unwrap();
        let pw: Vec<char> = caps.name("pw").unwrap().as_str().chars().collect();
        if (pw[min] == letter && pw[max] != letter) || (pw[min] != letter && pw[max] == letter) {
            num += 1;
        }
    }
    num
}

fn runner(func: &dyn Fn(&[&str]) -> i32, sample: &[&str], expected: i32, input: &[&str], answer: Option<i32>) {
    assert_eq!(func(sample), expected);
    let ans = func(input);
    println!("{}", ans);
    if let Some(x) = answer {
        assert_eq!(ans, x);
    }
}

pub fn day2() {
    let sample = ["1-3 a: abcde", "1-3 b: cdefgn", "2-9 c: ccccccccc"];
    let contents = fs::read_to_string("day2.txt").unwrap();
    let input: Vec<&str> = contents.lines().collect();
    runner(&part1, &sample, 2, &input, Some(550));
    runner(&part2, &sample, 1, &input, Some(634));
}