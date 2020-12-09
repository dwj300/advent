use std::fs;
use std::collections::HashMap;
use std::iter::FromIterator;

fn check(nums: &[i32], target: i32) -> bool {
    let diff: HashMap<i32, usize> = HashMap::from_iter(nums.iter().enumerate().map(|(i,n)| (target-n,i)));
    return nums.iter().enumerate().any(|(j,n)| diff.contains_key(n) && *(diff.get(n).unwrap()) != j);
}

fn part1(nums: &[i32], pre: usize) -> i32 {
    for i in pre..nums.len() {
        if !check(&nums[i-pre..i], nums[i]) {
            return nums[i];
        }
    }
    return -1;
}

fn part2(nums: &[i32], target: i32) -> i32 {
    let (mut i, mut j, mut s) = (0, 0, nums[0]);
    while s != target && j < nums.len() {
        if s < target {
            j += 1;
            s += nums[j]
        }
        else {
            s -= nums[i];
            i += 1;
        }
    }
    return nums[i..j+1].iter().min().unwrap() + nums[i..j+1].iter().max().unwrap();
}

pub fn day9() {
    let sample: Vec<i32> = "35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576".lines().flat_map(|x| x.parse::<i32>()).collect();
    assert_eq!(part1(&sample, 5), 127);

    let contents = fs::read_to_string("day9.txt").unwrap();
    let input: Vec<i32> = contents.lines().flat_map(|x| x.parse::<i32>()).collect();
    println!("len{}", input.len());
    let ans1 = part1(&input, 25);
    println!("{}", ans1);
    assert_eq!(ans1, 27911108);

    assert_eq!(part2(&sample, 127), 62);
    let ans2 = part2(&input, 27911108);
    println!("{}", ans2);
    assert_eq!(ans2, 4023754);
}