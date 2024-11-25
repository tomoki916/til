#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }

  pub fn from_vec(values: Vec<i32>) -> Option<Box<ListNode>> {
    let mut current = None;

    // ベクタの末尾から逆順にノードを作成してリンク
    for &value in values.iter().rev() {
        let mut new_node = ListNode::new(value);
        new_node.next = current;
        current = Some(Box::new(new_node));
    }

    current
}
}

fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    let mut l1 = l1;
    let mut l2 = l2;
    let mut  carry = 0 ; //繰り上がり
    let mut answer = Some(Box::new(ListNode::new(0)));
    let mut current = &mut answer;

    // ノードがどちらかある限り繰り返す
    while l1.is_some() || l2.is_some() || carry != 0  {
      // 値を取り出す
      let val1 = l1.as_ref().map_or(0, |node| node.val);
      let val2 = l2.as_ref().map_or(0, |node| node.val);

      // 足し算をする
      let sum = val1 + val2 + carry;
      carry = sum / 10;
      let new_val = sum % 10;

      // 新しいノードを作ってリンクする
      if let Some(ref mut current_node) = current {
        current_node.next = Some(Box::new(ListNode::new(new_val)));
        current = &mut current_node.next;
      }


      // 次のノードへ移動
      l1 = l1.and_then(|node| node.next);
      l2 = l2.and_then(|node| node.next);
    }

    answer.unwrap().next
}


#[cfg(test)]
mod test {
  use super::*;

  #[test]
  fn case1() {
    let l1 = vec![2, 4, 3];
    let l2 = vec![5, 6, 4];
    let answer = vec![7, 0, 8];
    assert_eq!(add_two_numbers(ListNode::from_vec(l1), ListNode::from_vec(l2)), ListNode::from_vec(answer));
  }

  #[test]
  fn case2() {
    let l1 = vec![0];
    let l2 = vec![0];
    let answer = vec![0];
    assert_eq!(add_two_numbers(ListNode::from_vec(l1), ListNode::from_vec(l2)), ListNode::from_vec(answer));
  }

  #[test]
  fn case3() {
    let l1 = vec![9,9,9,9,9,9,9];
    let l2 = vec![9,9,9,9];
    let answer = vec![8,9,9,9,0,0,0,1];
    assert_eq!(add_two_numbers(ListNode::from_vec(l1), ListNode::from_vec(l2)), ListNode::from_vec(answer));
  }
}