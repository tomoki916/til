use std::collections::HashMap;

pub fn length_of_longest_substring(s: String) -> i32 {
  if s.len() == 0 {
    return 0
  }
  let mut answer = 1; // 少なくとも1文字以上
  let mut head: usize = 0;
  let mut cache = HashMap::<char, usize>::new();

  // 1文字ずつ見ていく
  for (tail, c) in s.chars().enumerate() {
    // キャッシュにヒット
    if let Some(&cached_index) = cache.get(&c) {
      if cached_index >= head {
        let current_length = tail - head ;
        if current_length > answer {
          answer = current_length
        }
        head = cached_index + 1;
      }
    }
    cache.insert(c, tail);
  }

  // 一度もキャッシュにヒットしなかった時を考慮
  answer = if answer > s.len() - head {
    answer
  } else {
    s.len()-head
  };

  answer as i32
}


#[cfg(test)]
mod test {
  use super::*;

  #[test]
  fn case1() {
    let s =  "abcabcbb";
    let answer = 3;
    assert_eq!(length_of_longest_substring(s.to_string()), answer);
  }

  #[test]
  fn case2() {
    let s =  "bbbbb";
    let answer = 1;
    assert_eq!(length_of_longest_substring(s.to_string()), answer);
  }

  #[test]
  fn case3() {
    let s =  "pwwkew";
    let answer = 3;
    assert_eq!(length_of_longest_substring(s.to_string()), answer);
  }

  #[test]
  fn case4() {
    let s =  "abc";
    let answer = 3;
    assert_eq!(length_of_longest_substring(s.to_string()), answer);
  }

  #[test]
  fn case5() {
    let s =  "dvdf";
    let answer = 3;
    assert_eq!(length_of_longest_substring(s.to_string()), answer);
  }
}