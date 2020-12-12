use std::fs;

fn occupied(seats: &[Vec<char>], r: usize, c:usize, search: bool) -> usize {
    let mut count = 0;
    for ii in 0..3 {
        for jj in 0..3 {
            let i:isize = ii - 1;
            let j:isize = jj - 1;
            if i == j && j == 0 {
                continue;
            }
            let mut rr: isize = r as isize + i;
            let mut cc: isize = c as isize + j;
            if search {
                while 0 <= rr && rr < seats.len() as isize && cc < seats[0].len() as isize && cc >= 0 && seats[rr as usize][cc as usize] == '.' {
                    rr += i;
                    cc += j;
                }
            }
            if rr >= 0 && cc >= 0 && rr < (seats.len() as isize) && cc < (seats[0].len() as isize) && seats[rr as usize][cc as usize] == '#' {
                count += 1;
            }
        }
    }
    count
}

fn part1(seats: &[Vec<char>], search: bool, num: usize) -> usize {
    let mut old: Vec<Vec<char>> = vec![vec!['_'; seats[0].len()]; seats.len()];
    let mut new: Vec<Vec<char>> = seats.iter().map(|x| x.to_vec()).collect();
    while new != old {
        old = new.iter().map(|x| x.to_vec()).collect();
        for (r, row) in old.iter().enumerate() {
            for (c, seat) in row.iter().enumerate() {
                let mut new_seat = *seat;
                if *seat == 'L' && occupied(&old, r, c, search) == 0 {
                    new_seat = '#';
                }
                if *seat == '#' && occupied(&old, r, c, search) >= num {
                    new_seat = 'L';
                }
                new[r][c] = new_seat;
            }
        }
    }
    return new.iter().map(|r| r.iter().filter(|s| **s == '#').count()).sum();
}

pub fn day11() {
    let sample: Vec<&str> = "L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL".lines().collect();
    let sample_vec: Vec<Vec<char>> = sample.iter().map(|x| (*x).chars().collect::<Vec<char>>()).collect();
    let contents = fs::read_to_string("day11.txt").unwrap();
    let input_vec: Vec<Vec<char>> = contents.lines().collect::<Vec<&str>>().iter().map(|x| x.chars().collect::<Vec<char>>()).collect();

    assert_eq!(part1(&sample_vec, false, 4), 37);
    let ans1 = part1(&input_vec, false, 4);
    println!("{}", ans1);
    assert_eq!(ans1, 2406);

    assert_eq!(part1(&sample_vec, true, 5), 26);
    let ans1 = part1(&input_vec, true, 5);
    println!("{}", ans1);
    assert_eq!(ans1, 2149);
}