use std::collections::HashMap;
use std::fs;

fn part1(input: &[i32]) -> i32 {
    let mut partials = HashMap::<i32, i32>::new();
    for i in input.iter() {
        partials.insert(2020-i, *i);
    }

    for i in input {
        match partials.get(i) {
            Some(partial) => return partial * i,
            _ => ()
        }
    }
    return -1;
}

fn part2(input: &[i32]) -> i32 {
    let mut partials = HashMap::new();
    for i in input.iter() {
        partials.insert(2020-i, *i);
    }

    for i in 0..input.len() {
        for j in 1..input.len() {
            if i == j {
                continue;
            }
            match partials.get(&(input[i] + input[j])) {
                Some(partial) => return partial * input[i] * input[j],
                _ => ()
            }
        }
    }
    return -1;
}

fn runner(func: &dyn Fn(&[i32]) -> i32, sample: &[i32], expected: i32, input: &[i32], answer: Option<i32>) {
    assert_eq!(func(sample), expected);
    let ans = func(input);
    println!("{}", ans);
    match answer {
        Some(x) => {
            assert_eq!(ans, x);
        },
        None => ()
    }
}

pub fn day1() {
    let sample = [1721,979,366,299,675,1456];
    let nums: Vec<i32> = fs::read_to_string("day1.txt").unwrap().lines().map(|line| line.parse::<i32>().unwrap()).collect();
    runner(&part1, &sample, 514579, &nums, Some(842016));
    runner(&part2, &sample, 241861950, &nums, Some(9199664));
}