use std::collections::HashMap;

fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
  let mut cache = HashMap::<i32, usize>::new(); // numsの値をkey、インデックスをvalueとする

  for (index, &n) in nums.iter().enumerate() {
    if let Some(&prev_index) = cache.get(&n) {
      return vec![prev_index as i32, index as i32];
    } else {
      cache.insert(target - n,  index);
    }
   
  }

  vec![]
}

pub fn solution() {
  let nums = vec![2, 7, 11, 15];
  let target= 9;
  let answer = two_sum(nums, target);

  println!("Answer: {:?}", answer)
}

#[cfg(test)]
mod test {
  use super::*;

  #[test]
  fn case1() {
    let nums = vec![2, 7, 11, 15];
    let target= 9;
    let answer = [0, 1];
    assert_eq!(two_sum(nums, target), answer);
  }

  #[test]
  fn case2() {
    let nums = vec![3, 2, 4];
    let target= 6;
    let answer = [1, 2];
    assert_eq!(two_sum(nums, target), answer);
  }

  #[test]
  fn case3() {
    let nums = vec![3, 3];
    let target= 6;
    let answer = [0, 1];
    assert_eq!(two_sum(nums, target), answer);
  }
}