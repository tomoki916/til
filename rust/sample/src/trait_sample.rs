use std::fmt::{ Display, Formatter};

struct ImaginaryNumber {
  real: f64,
  img: f64
}

impl Display for ImaginaryNumber {
  fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
      write!(f, "{} + {}i", self.real, self.img)
  }
}

pub fn trait_display_sample() {
  let n = ImaginaryNumber {real: 3.0, img: 4.0};
  println!("{n}");
}

#[derive(Debug, Clone)]
enum List<T> {
    Node {data: T, next: Box<List<T>>},
    Nil
}

impl<T> List<T> {
  fn new() -> List<T> {
    List::Nil
  }

  fn cons(self, data: T) -> List<T> {
    List::Node {
      data, 
      next: Box::new(self)
    }
  }

  fn iter<'a>(&'a self) -> ListIter<'a, T> {
    ListIter {elm: self}
  }
}