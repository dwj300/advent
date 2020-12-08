use std::fs;
use std::collections::HashSet;

fn part1(lines: &[&str]) -> i32 {
    let mut a = 0;
    let mut seen = HashSet::new();
    let mut i = 0;
    while !seen.contains(&i) {
        seen.insert(i);
        let parts: Vec<&str> = lines[i as usize].split(" ").collect();
        let delta = parts[1].parse::<i32>().unwrap();
        if parts[0] == "acc" {
            a += delta;
        }
        else if parts[0] == "jmp" {
            i += delta - 1;
        }
        i += 1;
    }
    return a;
}

fn part2(lines: &[&str]) -> i32 {
    for j in 0..lines.len() {
        for inst in &["nop", "jmp"] {
            let mut a: i32 = 0;
            let mut seen = HashSet::new();
            let mut i: i32 = 0;
            while !seen.contains(&i) && i != lines.len() as i32 {
                seen.insert(i);
                let mut parts: Vec<&str> = lines[i as usize].split(" ").collect();
                if i == j as i32 && *inst == parts[0] {
                    parts[0] = if *inst == "nop" {"jmp"} else {"nop"};
                }
                if parts[0] == "acc" {
                    a += parts[1].parse::<i32>().unwrap();
                }
                else if parts[0] == "jmp" {
                    i = i + parts[1].parse::<i32>().unwrap() - 1;
                }
                i += 1;
            }
            if i == lines.len() as i32 {
                return a;
            }
        }
    }
    return 0;
}

pub fn day8() {
    let sample: Vec<&str> = "nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
".lines().collect();
    assert_eq!(part1(&sample), 5);

    let contents = fs::read_to_string("day8.txt").unwrap();
    let input: Vec<&str> = contents.lines().collect();
    let ans1 = part1(&input);
    println!("{}", ans1);
    assert_eq!(ans1, 1179);

    assert_eq!(part2(&sample), 8);
    let ans2 = part2(&input);
    println!("{}", ans2);
    assert_eq!(ans2, 1089);
}