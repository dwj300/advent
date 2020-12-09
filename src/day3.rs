use std::fs;

fn helper(lines: &[&str], dx: usize, dy: usize) -> i32 {
    let mut x = 0;
    let mut y = 0;
    let mut count = 0;
    while y < lines.len()-1 {
        x += dx;
        y += dy;
        if lines[y].chars().nth(x % lines[0].len()).unwrap() == '#' {
            count += 1
        }
    }
    count
}

fn part1(input: &[&str]) -> i32 {
    helper(input, 3, 1)
}

fn part2(input: &[&str]) -> i32 {
    let slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]];
    let mut product = 1;
    for slope in slopes.iter() {
        product *= helper(input, slope[0], slope[1]);
    }
    product
}

fn runner(func: &dyn Fn(&[&str]) -> i32, sample: &[&str], expected: i32, input: &[&str], answer: Option<i32>) {
    assert_eq!(func(sample), expected);
    let ans = func(input);
    println!("{}", ans);
    if let Some(x) = answer {
        assert_eq!(ans, x);
    }
}

pub fn day3() {
    let sample = ["..##.......",
                  "#...#...#..",
                  ".#....#..#.",
                  "..#.#...#.#",
                  ".#...##..#.",
                  "..#.##.....",
                  ".#.#.#....#",
                  ".#........#",
                  "#.##...#...",
                  "#...##....#",
                  ".#..#...#.#"].to_vec();
    let contents = fs::read_to_string("day3.txt").unwrap();
    let input: Vec<&str> = contents.lines().collect();
    runner(&part1, &sample, 7, &input, Some(181));
    runner(&part2, &sample, 336, &input, Some(1260601650));
}