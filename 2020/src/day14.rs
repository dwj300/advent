use std::fs;
use std::collections::HashMap;

fn set_bit(value: u64, bit: u8) -> u64 {
    return value | (1<<35-bit);
}

fn clear_bit(value: u64, bit: u8) -> u64 {
    return value & !(1<<35-bit);
}

fn part1(lines: &[&str]) -> u64 {
    let mut memory: HashMap<usize, u64> = HashMap::new();
    let mut mask = "";
    for line in lines {
        let parts: Vec<&str> = line.split(" = ").collect();
        if parts[0].contains("mask") {
            mask = parts[1];
        } else {
            let address: usize = parts[0][4..parts[0].len()-1].parse().unwrap();
            let mut value: u64 = parts[1].parse().unwrap();
            for (i, x) in mask.chars().enumerate() {
                if x == '1' {
                    value = set_bit(value, i as u8);
                } else if x == '0' {
                    value = clear_bit(value, i as u8);
                }
            }

            memory.insert(address, value);
        }

    }
    return memory.values().sum();
}

fn addresses(addr: u64, floats: &[u8], i: usize) -> Vec<u64> {
    if i == floats.len()-1 {
        let zero = clear_bit(addr, floats[i]);
        let one = set_bit(addr, floats[i]);
        return [zero, one].to_vec();
    }
    let mut ans: Vec<u64> = Vec::new();
    ans.append(&mut addresses(clear_bit(addr, floats[i]), floats, i+1));
    ans.append(& mut addresses(set_bit(addr, floats[i]), floats, i+1));

    return ans;
}

fn part2(lines: &[&str]) -> u64 {
    let mut memory: HashMap<u64, u64> = HashMap::new();
    let mut mask = "";
    for line in lines {
        let parts: Vec<&str> = line.split(" = ").collect();
        if parts[0].contains("mask") {
            mask = parts[1];
        } else {
            let mut address: u64 = parts[0][4..parts[0].len()-1].parse().unwrap();
            let value: u64 = parts[1].parse().unwrap();
            let mut floats: Vec<u8> = Vec::new();
            for (i, x) in mask.chars().enumerate() {
                if x == '1' {
                    address = set_bit(address, i as u8);
                } else if x == 'X' {
                    floats.push(i as u8);
                }
            }
            for addr in addresses(address, &floats, 0) {
                memory.insert(addr, value);
            }
        }

    }
    return memory.values().sum();
}

pub fn day14() {
    let sample: Vec<&str> = "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0".lines().collect();

    let sample2: Vec<&str> = "mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1".lines().collect();

    let contents = fs::read_to_string("day14.txt").unwrap();
    let problem: Vec<&str> = contents.lines().collect();
    assert_eq!(part1(&sample), 165);
    let ans1 = part1(&problem);
    println!("{}", ans1);
    assert_eq!(ans1, 18630548206046);

    assert_eq!(part2(&sample2), 208);
    let ans2 = part2(&problem);
    println!("{}", ans2);
    assert_eq!(ans2, 4254673508445);
}