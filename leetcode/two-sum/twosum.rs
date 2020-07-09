/*

coding reference:
    -  https://www.tutorialspoint.com/rust/rust_input_output.htm
    -  https://stackoverflow.com/a/40315112/8654623
    -  https://stackoverflow.com/a/30186553/8654623
    -  https://doc.rust-lang.org/std/io/trait.BufRead.html#method.lines
*/

use std::io;


pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    use std::collections::HashMap;

    let mut h = HashMap::new();

    for (i, n) in nums.iter().enumerate() {
        match h.get(&(target - n)) {
            None => {
                h.insert(n, i);
            }
            Some(idx) => {
                return vec![*idx as i32, i as i32];
            }
        }
    }
    vec![]
}


fn string_to_integer_vector(numbers: String) -> Vec<i32>{
    let ret: Vec<i32> = numbers.trim_end()
                               .split(",")
                               .filter_map(|s| s.parse().ok())
                               .collect();
    return ret;
}



fn main() {
    let mut input = String::new();
    while io::stdin().read_line(&mut input).unwrap() > 0 {

        // read the array
        let nums: Vec<i32> = string_to_integer_vector(input);
        input = String::new();

        // read target
        io::stdin().read_line(&mut input).unwrap();
        let target: i32 = input.trim_end().parse().expect("expecting integer");
        input = String::new();

        // do it
        let res = two_sum(nums, target);
        println!("{:?}", res);

    }
}
