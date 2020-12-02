use std::collections::HashMap;
use std::fs;

fn part2(input: Vec<i32>) -> i32 {
    let mut partials = HashMap::<i32, i32>::new();
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

fn part1(input: Vec<i32>) -> i32 {
    let mut partials = HashMap::<i32, i32>::new();
    for i in input.iter() {
        partials.insert(2020-i, *i);
    }

    for i in input.iter() {
        match partials.get(i) {
            Some(partial) => return partial * i,
            _ => ()
        }
    }
    return -1;
}

pub fn day1() {
    let sample = [1721,979,366,299,675,1456];
    let ans = part1(sample.to_vec());
    assert_eq!(ans, 514579);
    let ans2 = part2(sample.to_vec());
    assert_eq!(ans2, 241861950);

    let contents = fs::read_to_string("day1.txt")
        .expect("Something went wrong reading the file");

    let input: Vec<&str> = contents.lines().collect();
    let mut nums = Vec::new();
    for line in input.iter() {
        let i: i32 = line.parse().unwrap_or(-1);
        nums.push(i)
    }
    let nums2 = nums.clone();
    let ans3 = part1(nums);
    println!("{}", ans3);
    assert_eq!(ans3, 842016);

    let ans4 = part2(nums2);
    println!("{}", ans4);
    assert_eq!(ans4, 9199664);
}