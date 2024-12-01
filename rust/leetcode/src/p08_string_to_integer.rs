use std::{collections::HashMap, result};

pub fn my_atoi(s: String) -> i32 {
  let s = s.trim_start();
  let (s, sign) = match s.strip_prefix('-') {
    Some(s) => (s, -1),
    None => (s.strip_prefix('+').unwrap_or(s), 1)
  };

  s.chars()
    .map(|c| c.to_digit(10))
    .take_while(Option::is_some)
    .flatten()
    .fold(0, |acc, digit|  {
      acc.saturating_mul(10).saturating_add(sign * digit as i32)
    })
}

// pub fn my_atoi(s: String) -> i32 {
//   // 変換テーブルを作る
//   let atoi_map = HashMap::<char, i32>::from([
//     ('0', 0),
//     ('1', 1),
//     ('2', 2),
//     ('3', 3),
//     ('4', 4),
//     ('5', 5),
//     ('6', 6),
//     ('7', 7),
//     ('8', 8),
//     ('9', 9),
//   ]);

//   // 先頭の方の数値以外を読んでいる時をステートとして管理する
//   let mut is_leading_chars = true;

//   let mut is_negative = false;

//   // まず文字列として抽出する
//   let mut answer_string: Vec<char> = vec!(); 
//   for c in s.chars() {

//     if is_leading_chars && c == ' ' {
//       // 先頭のスペースは無視する
//       continue;
//     };

//     if is_leading_chars && c == '-' {
//       // 負の数の判定
//       is_negative = true;
//       is_leading_chars = false;
//       continue;
//     }

//     if is_leading_chars && c == '+' {
//       // 正の数の判定
//       is_negative = false;
//       is_leading_chars = false;
//       continue;
//     }

//     if is_leading_chars && c == '0' {
//       // 先頭の0は無視する
//       is_leading_chars = false;
//       continue;
//     }

//     // 数値以外が出てきたら終了
//     if !atoi_map.contains_key(&c) {
//       break;
//     }

//     // 数値が出てきたらそれを回答に入れる
//     answer_string.push(c);
//     is_leading_chars = false;
//   };
//   println!("answer_string: {:#?}", answer_string);

//   // 数の文字が含まれていない場合は0を返す
//   if answer_string.len() == 0 {
//     return 0;
//   };

//   // それを数値に変換する
//   let mut answer: i32 = 0;
//   for (index, c) in answer_string.iter().rev().enumerate() {
//     let order = match 10_i32.checked_pow(index as u32) {
//       Some(result) => result,
//       None => i32::MAX
//     };

//     let current = match atoi_map[&c].checked_mul(order) {
//       Some(result) => result,
//       None => i32::MAX
//     };

//     match answer.checked_add(current) {
//         Some(result) => answer = result,
//         None => if is_negative {
//           return i32::MIN;
//         } else {
//           return i32::MAX;
//         }
//     }
//   };

//   if is_negative {
//     answer * -1
//   } else {
//     answer
//   }
// }


#[cfg(test)]
mod test {
  use super::*;

  #[test]
  fn case1() {
    let s = "42";
    let answer = 42;
    assert_eq!(my_atoi(s.to_string()), answer);
  }

  #[test]
  fn case2() {
    let s =  " -042";
    let answer = -42;
    assert_eq!(my_atoi(s.to_string()), answer);
  }

  #[test]
  fn case3() {
    let s =  "1337c0d3";
    let answer = 1337;
    assert_eq!(my_atoi(s.to_string()), answer);
  }

  #[test]
  fn case4() {
    let s =  "0-1";
    let answer = 0;
    assert_eq!(my_atoi(s.to_string()), answer);
  }

  #[test]
  fn case5() {
    let s = "words and 987";
    let answer = 0;
    assert_eq!(my_atoi(s.to_string()), answer);
  }

  #[test]
  fn case6() {
    let s = "9 8";
    let answer = 9;
    assert_eq!(my_atoi(s.to_string()), answer);
  }

  #[test]
  fn case7() {
    let s = " 0a";
    let answer = 0;
    assert_eq!(my_atoi(s.to_string()), answer);
  }

  #[test]
  fn case8() {
    let s = "asdfghjk";
    let answer = 0;
    assert_eq!(my_atoi(s.to_string()), answer);
  }

  #[test]
  fn case9() {
    let s = "2147483648";
    let answer = 2147483647;
    assert_eq!(my_atoi(s.to_string()), answer);
  }

  #[test]
  fn case10() {
    let s = "-91283472332";
    let answer = -2147483648;
    assert_eq!(my_atoi(s.to_string()), answer);
  }
}