use std::fs;
use regex::Regex;

fn part2(input: Vec<&str>) -> i32 {
    let mut num = 0;
    let p = Regex::new(r"(?P<min>[0-9]+)-(?P<max>[0-9]+) (?P<letter>[a-z]): (?P<pw>[a-z]+)").unwrap();
    for line in input.iter() {
        let caps = p.captures(line).unwrap();
        let min: usize = caps.name("min").unwrap().as_str().parse().unwrap_or(0)-1;
        let max: usize = caps.name("max").unwrap().as_str().parse().unwrap_or(0)-1;
        let letter: char = caps.name("letter").unwrap().as_str().chars().next().unwrap();
        let pw: Vec<char> = caps.name("pw").unwrap().as_str().chars().collect();
        if (pw[min] == letter && pw[max] != letter) || (pw[min] != letter && pw[max] == letter) {
            num += 1;
        }
    }
    return num;
}

fn part1(input: Vec<&str>) -> i32 {
    let mut num = 0;
    let p = Regex::new(r"(?P<min>[0-9]+)-(?P<max>[0-9]+) (?P<letter>[a-z]): (?P<pw>[a-z]+)").unwrap();
    for line in input.iter() {
        let caps = p.captures(line).unwrap();
        let min: usize = caps.name("min").unwrap().as_str().parse().unwrap_or(0);
        let max: usize = caps.name("max").unwrap().as_str().parse().unwrap_or(0);
        let letter: char = caps.name("letter").unwrap().as_str().chars().next().unwrap();
        let pw: &str = caps.name("pw").unwrap().as_str();
        let count = pw.matches(|c| c == letter).count();
        if count >= min && count <= max {
            num += 1;
        }
    }
    return num;
}

pub fn day2() {
    let sample = ["1-3 a: abcde", "1-3 b: cdefgn", "2-9 c: ccccccccc"];
    let ans = part1(sample.to_vec());
    assert_eq!(ans, 2);
    let ans2 = part2(sample.to_vec());
    assert_eq!(ans2, 1);

    let contents = fs::read_to_string("day2.txt")
        .expect("Something went wrong reading the file");

    let input: Vec<&str> = contents.lines().collect();
    let input2: Vec<&str> = contents.lines().collect();
    
    let ans3 = part1(input);
    println!("{}", ans3);
    assert_eq!(ans3, 550);

    let ans4 = part2(input2);
    println!("{}", ans4);
    assert_eq!(ans4, 634);
}