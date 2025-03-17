pub type Result<T> = std::result::Result<T, Box<dyn std::error::Error>>;

pub fn bisect_left<T>(arr: &[T], x: T) -> usize 
where 
    T: Ord,
{
    let mut left = 0;
    let mut right = arr.len();

    while left < right { 
        let mid = left + (right - left) / 2;
        if arr[mid] < x {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    
    left
}

pub fn bisect_right<T>(arr: &[T], x: T) -> usize 
where 
    T: Ord,
{
    let mut left = 0;
    let mut right = arr.len();

    while left < right {
        let mid = left + (right - left) / 2;
        if arr[mid] <= x {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    left
}
