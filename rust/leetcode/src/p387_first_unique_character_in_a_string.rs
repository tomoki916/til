use std::collections::HashMap;

// pub fn first_uniq_char(s: String) -> i32 {
//   let mut cache = HashMap::<char, (usize, i32)>::new();

//   // 文字を辿る。キャッシュにヒットに登場回数とインデックスを記録する。
//   for (index, c) in s.chars().enumerate() {
//     let current_count = if let Some(value) = cache.get(&c) {
//       value.1
//     } else {
//       0
//     };
//     cache.insert(c, (index, current_count + 1));
//   }

//   // 登場回数が１回のものを抽出する
//   let mut filtered: Vec<_> = cache.iter().filter(|&(_, &(_, count))| count == 1).map(|(&key, &value)| (key, value)).collect();

//   // indexでsort
//   filtered.sort_by_key(|&(_, (index, _))| index);

//   if let Some(value) = filtered.first() {
//     value.1.0 as i32
//   } else {
//     // filteredの要素が1つもなければ-1を返す
//     -1
//   }
// }

pub fn first_uniq_char(s: String) -> i32 {
  let mut count: HashMap<char, i32> = HashMap::new();
        
  for c in s.chars() {
      *count.entry(c).or_insert(0) += 1;
  }

  for (i, c) in s.chars().enumerate() {
    if count[&c] == 1 {
      return i as i32;
    }
  }
  -1
}


#[cfg(test)]
mod test {
  use super::*;

  #[test]
  fn case1() {
    let s = "leetcode";
    let answer = 0;
    assert_eq!(first_uniq_char(s.to_string()), answer);
  }

  #[test]
  fn case2() {
    let s =  "loveleetcode";
    let answer = 2;
    assert_eq!(first_uniq_char(s.to_string()), answer);
  }

  #[test]
  fn case3() {
    let s =  "aabb";
    let answer = -1;
    assert_eq!(first_uniq_char(s.to_string()), answer);
  }

  #[test]
  fn case4() {
    let s =  "dddccdbba";
    let answer = 8;
    assert_eq!(first_uniq_char(s.to_string()), answer);
  }
}