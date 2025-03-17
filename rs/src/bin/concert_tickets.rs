use std::io;
pub type Result<T> = std::result::Result<T, Box<dyn std::error::Error>>;

fn solve(mut prices: Vec<i32>, maxes: Vec<i32>) -> Result<Vec<i32>> {
    let mut res = vec![];

    prices.sort();

    for max in maxes {
        let mut idx = prices.partition_point(|&x| x <= max);

        if idx == 0 {
            res.push(-1);
            continue;
        }

        idx -= 1;
        res.push(prices[idx]);
        prices.remove(idx);
    }

    Ok(res)
}

fn main() -> Result<()> {
    let mut l1 = String::new();
    io::stdin().read_line(&mut l1)?;

    let mut l2 = String::new();
    io::stdin().read_line(&mut l2)?;
    let prices = l2.split_whitespace().map(|w| w.parse::<i32>().unwrap()).collect();

    let mut l3 = String::new();
    io::stdin().read_line(&mut l3)?;
    let maxes = l3.split_whitespace().map(|w| w.parse::<i32>().unwrap()).collect();

    let res = solve(prices, maxes)?;

    for r in res {
        println!("{}", r);
    }

    Ok(())
}
