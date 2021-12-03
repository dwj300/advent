use std::collections::HashMap;
use std::collections::HashSet;
use std::fs;
use regex::Regex;

fn part1(lines: &[&str]) -> i32 {
    let keys: HashSet<&str> = ["byr","iyr","eyr","hgt","hcl","ecl", "pid"].iter().cloned().collect();
    let mut count = 0;
    let mut current = HashSet::new();
    for line in lines {
        if line.is_empty() {
            if current.is_superset(&keys) {
                count += 1;
            }
            current = HashSet::new();
        }
        else {
            for pair in line.split(' ') {
                current.insert(pair.split(':').next().unwrap());
            }
        }
    }
    count
}

fn part2(lines: &[&str]) -> i32 {
    let hcl_p = Regex::new(r"^#[0-9a-f]{6}$").unwrap();
    let pid_p = Regex::new(r"^[0-9]{9}$").unwrap();
    let mut count = 0;
    let mut current: HashMap<&str, &str> = HashMap::new();
    for line in lines {
        if line.is_empty() {
            let mut n = 0;
            for (k, v) in current {
                match k {
                    "byr" => if v.len() == 4 && v.parse::<usize>().unwrap() >= 1920 && v.parse::<usize>().unwrap() <= 2002 { n += 1; },
                    "iyr" => if v.len() == 4 && v.parse::<usize>().unwrap() >= 2010 && v.parse::<usize>().unwrap() <= 2020 { n += 1; },
                    "eyr" => if v.len() == 4 && v.parse::<usize>().unwrap() >= 2020 && v.parse::<usize>().unwrap() <= 2030 { n += 1; },
                    "ecl" => if "amb blu brn gry grn hzl oth".split(' ').any(|x| x == v) { n += 1; },
                    "hcl" => if hcl_p.is_match(v) { n += 1 },
                    "pid" => if pid_p.is_match(v) { n += 1 },
                    "hgt" => if v.len() >= 3 && (
                        (&v[v.len() - 2..v.len()] == "cm" &&
                            v[0..v.len() - 2].parse::<usize>().unwrap() >= 150 &&
                            v[0..v.len() - 2].parse::<usize>().unwrap() <= 193) ||
                        (&v[v.len() - 2..v.len()] == "in" &&
                            v[0..v.len() - 2].parse::<usize>().unwrap() >= 59 &&
                            v[0..v.len() - 2].parse::<usize>().unwrap() <= 76)) { n += 1; },
                    _ => ()
                }
            }
            if n == 7 {
                count += 1;
            }

            current = HashMap::new();
        }
        else {
            for pair in line.split(' ') {
                let k = pair.split(':').next().unwrap();
                let v = pair.split(':').nth(1).unwrap();
                current.insert(k, v);
            }
        }
    }
    count
}

fn runner(func: &dyn Fn(&[&str]) -> i32, sample: &[&str], expected: i32, input: &[&str], answer: Option<i32>) {
    assert_eq!(func(sample), expected);
    let ans = func(input);
    println!("{}", ans);

    if let Some(x) = answer {
        assert_eq!(ans, x);
    }
}

pub fn day4() {
    let contents = fs::read_to_string("day4.txt").unwrap();
    let input: Vec<&str> = contents.lines().collect();

    let sample_contents = fs::read_to_string("4s.txt").unwrap();
    let sample: Vec<&str> = sample_contents.lines().collect();

    let sample_contentsi = fs::read_to_string("42i.txt").unwrap();
    let samplei: Vec<&str> = sample_contentsi.lines().collect();

    let sample_contentsv = fs::read_to_string("42v.txt").unwrap();
    let samplev: Vec<&str> = sample_contentsv.lines().collect();

    runner(&part1, &sample, 2, &input, Some(235));
    runner(&part2, &samplei, 0, &input, Some(194));
    runner(&part2, &samplev, 4, &input, Some(194));
}