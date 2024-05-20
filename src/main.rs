use std::collections::HashMap;

fn main() {

    let large_string = "Hello World Hello World Cheese";
    let words = large_string.split(" ");
    let mut word_counter = HashMap::new();
    for w in words {
        *word_counter.entry(w).or_insert(0) += 1
    }
    for (word, count) in word_counter.iter() {
        print!("{} -> {}\n", word, count)
    }


}


