use std::fs;

struct Elf {
    number: u64,
    calories: u64,
}

fn main() {
    println!("Hello, world!");
    let contents = fs::read_to_string("../input.txt").expect("Couldn't read input file");
    let mut elf = Elf{ number: 0, calories: 0};
    let mut elves = Vec::new();
    for mut line in contents.lines() {
        line = line.trim();
        if !line.is_empty() {
            elf.calories += line.parse::<u64>().unwrap();
        } else {
            elves.push(elf);
            elf = Elf{ number: elves.len() as u64, calories: 0}
        }
    }

    elves.sort_by(|a, b| b.calories.cmp(&a.calories));

    println!("Top three elves:");
    let mut sum : u64 = 0;
    for n in 0..3 {
        sum += elves[n].calories;
        println!("    Elf #{} has {} calories", elves[n].number, elves[n].calories);
    }
    println!("Together they are carrying {} calories", sum);
}
