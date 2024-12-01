pub fn convert(s: String, num_rows: i32) -> String {
  if num_rows == 1 {
    return s;
  }

  // 答えが入る配列の初期か
  let mut answer = vec![Vec::<char>::new(); num_rows as usize];

  // 降っている
  let mut is_going_down = true;
  let mut current_row: i32 = 0;

  // 与えられた文字列を１文字ずつ
  for c in s.chars() {
    answer[current_row as usize].push(c);

    // 最終行まで到達したら上に行く
    if current_row == num_rows -1  {
      is_going_down = false;
    }

    // 一番上の行まで到達したら下に行く
    if current_row == 0 {
      is_going_down = true;
    }

    if is_going_down {
      current_row += 1;
    } else {
      current_row -= 1;
    }
  }

  answer.into_iter().map(|chars| chars.into_iter().collect::<String>()).collect::<Vec<String>>().join("")
}


#[cfg(test)]
mod test {
  use super::*;

  #[test]
  fn case1() {
    let s = "PAYPALISHIRING";
    let num_rows = 3;
    let answer = "PAHNAPLSIIGYIR";
    assert_eq!(convert(s.to_string(), num_rows), answer);
  }

  #[test]
  fn case2() {
    let s = "PAYPALISHIRING";
    let num_rows = 4;
    let answer = "PINALSIGYAHRPI";
    assert_eq!(convert(s.to_string(), num_rows), answer);
  }

  #[test]
  fn case3() {
    let s = "A";
    let num_rows = 1;
    let answer = "A";
    assert_eq!(convert(s.to_string(), num_rows), answer);
  }
}